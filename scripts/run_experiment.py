import sys,argparse,hashlib
from pathlib import Path
from fractions import Fraction
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.data_loader import *
from src.validation import validate
from src.cohort import resolve,common_cohort,SYSTEMS
from src.scoring import credits,conditional_precision,strict_precision
from src.metrics import mean,pairwise
from src.sensitivity import VARIANTS

def run(data,out,variant='primary'):
    out=Path(out);records=load(data);counts,labels,audit,parsed=validate(records)
    mode=VARIANTS[variant];selected,resolution=resolve(records,mode)
    queries,cohort=common_cohort(selected,parsed,mode)
    if not queries:raise ValueError('No valid common cohort')
    responses=[];unit_rows=[];query_scores={};system_scores={};systems=[];manifest=[]
    for q in queries:
        qid=hashlib.sha256(q.encode()).hexdigest()
        for s in SYSTEMS:
            values=[]
            for line,r in cohort[q,s]:
                units,errors=parsed[line];assert not errors
                n=len(r['citations']);p0=conditional_precision(units,n);p1=strict_precision(units,n)
                assert 0<=p1<=p0<=1
                cs=credits(units);fs=sum(u['full_credit'] for u in cs);ps=sum(u['conditional_partial_credit'] for u in cs)
                values.append((p0,p1))
                responses.append(dict(line=line,response_id=r['id'],query_key=qid,system=s,split=r['split'],denominator=n,full=fs,conditional_partial=ps,C0=float(p0),C1=float(p1),loss=float(p0-p1),C0_exact=str(p0),C1_exact=str(p1)))
                manifest.append(dict(query_key=qid,system=s,line=line,response_id=r['id'],split=r['split'],query_weight=str(Fraction(1,len(queries))),record_weight=str(Fraction(1,len(cohort[q,s])))))
                for u in cs:
                    unit_rows.append(dict(line=line,response_id=r['id'],statement_index=u['statement_index'],judgment_index=u['judgment_index'],occurrence_index=u['occurrence_indices'][0],marker=u['marker'],raw_label=u['raw_label'],collective=u['collective'],full_credit=u['full_credit'],partial_credit=u['conditional_partial_credit']))
            query_scores[q,s]=(mean(v[0] for v in values),mean(v[1] for v in values))
    for s in SYSTEMS:
        p0=mean(query_scores[q,s][0] for q in queries);p1=mean(query_scores[q,s][1] for q in queries);system_scores[s]=(p0,p1)
        losses=sorted(query_scores[q,s][0]-query_scores[q,s][1] for q in queries)
        n=len(losses);median=(losses[(n-1)//2]+losses[n//2])/2
        systems.append(dict(system=s,queries=n,C0_percent=float(p0*100),C1_percent=float(p1*100),loss_pp=float((p0-p1)*100),C0_exact=str(p0),C1_exact=str(p1),affected_queries=sum(x>0 for x in losses),affected_fraction=sum(x>0 for x in losses)/n,median_loss_pp=float(median*100),max_loss_pp=float(max(losses)*100),citation_units=sum(x['denominator'] for x in responses if x['system']==s)))
    write_csv(out/'tables/response_scores.csv',responses);write_csv(out/'tables/citation_credit.csv',unit_rows)
    write_csv(out/'tables/cohort_manifest.csv',manifest);write_csv(out/'tables/record_resolution.csv',resolution)
    write_csv(out/'tables/system_scores.csv',systems);write_csv(out/'tables/pairwise_gaps.csv',pairwise(system_scores))
    selected_lines={x['line'] for x in responses}
    write_csv(out/'tables/eligibility.csv',[{**x,'in_common_cohort':x['line'] in selected_lines} for x in audit])
    cats=Counter(r['split'] for _,r in records);retained=Counter(cohort[q,SYSTEMS[0]][0][1]['split'] for q in queries)
    write_csv(out/'tables/source_coverage.csv',[dict(source=k,raw_rows=v,retained_queries=retained[k]) for k,v in sorted(cats.items())])
    summary=dict(variant=variant,queries=len(queries),systems=systems,pairs=pairwise(system_scores),baseline_status='ADAPTED C0/C1; original B0 NOT REPRODUCED',sha256=digest(data))
    if variant=='primary':
        micro={}
        for s in SYSTEMS:
            rr=[r for r in responses if r['system']==s];den=sum(r['denominator'] for r in rr)
            micro[s]=(Fraction(sum(r['full']+r['conditional_partial'] for r in rr),den),Fraction(sum(r['full'] for r in rr),den))
        write_csv(out/'tables/micro_pairwise_gaps.csv',pairwise(micro))
        write_csv(out/'tables/micro_system_scores.csv',[dict(system=s,C0_percent=float(v[0]*100),C1_percent=float(v[1]*100),loss_pp=float((v[0]-v[1])*100)) for s,v in micro.items()])
    write_json(out/'summary.json',summary);return summary
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--out',default='results');p.add_argument('--variant',choices=VARIANTS,default='primary');a=p.parse_args();r=run(a.data,a.out,a.variant);print('Executed',a.variant,'queries',r['queries'])
