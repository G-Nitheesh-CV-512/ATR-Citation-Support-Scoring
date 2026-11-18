"""Independent reconstruction of eligibility, duplicate rules and occurrence bridges.
No imports from project parser, cohort or scorer; assertions compare raw data to outputs.
"""
import argparse,json,csv,hashlib
from collections import defaultdict,Counter
from fractions import Fraction
from pathlib import Path
SYSTEMS=('bing_chat','neeva','perplexity','you')
LABELS={'Citation Completely Supports Statement','Citation Partially Supports Statement','Citation Provides No Support for Statement','Citation Inaccessible','Citation Completely Supports but Also Refutes Statement',"Statement is Unclear, Can't Make Judgment"}
def audit(data,out):
 raw={i:json.loads(s) for i,s in enumerate(Path(data).read_text().splitlines(),1)}
 out=Path(out);groups=defaultdict(list);bridges={};valid={}
 for line,r in raw.items():
  groups[r['id']].append(line)
  ok=True;used=[];bridge=[]
  for j,c in enumerate(r['citations']):
   if r['response'][c['start_index']:c['end_index']]!=c['text']:ok=False
  for si,(st,markers) in enumerate(r['statements_to_citation_texts'].items()):
   a=r['annotation']['statement_to_annotation'][st];jj=a['citation_annotations'] or []
   if Counter(markers)!=Counter(j['citation_text'] for j in jj):ok=False
   if not markers:continue
   start=r['response'].find(st)
   unique=start>=0 and r['response'].find(st,start+1)==-1
   ok=ok and unique and len(set(markers))==len(markers) and a['statement_is_verification_worthy'] is True
   ok=ok and a['statement_supported'] in ('Yes','No','Citations Contradict Each Other')
   for ji,j in enumerate(jj):
    ok=ok and j['citation_supports'] in LABELS
    hits=[k for k,c in enumerate(r['citations']) if c['text']==j['citation_text'] and unique and start<=c['start_index']<c['end_index']<=start+len(st)]
    if len(hits)!=1:ok=False
    used.extend(hits)
    if len(hits)==1:bridge.append((si,ji,hits[0]))
  valid[line]=ok and bool(r['citations']) and Counter(used)==Counter(range(len(r['citations'])))
  bridges[line]=bridge
 report={'status':'PASS','variants':{},'identity_sha256':hashlib.sha256(Path(data).read_bytes()).hexdigest()}
 for variant,dirname in [('primary',''),('collapse_identical','collapse_identical'),('distinct_record_mean','distinct_record_mean')]:
  chosen=[]
  for rid,lines in groups.items():
   distinct={}
   for line in lines:distinct.setdefault(json.dumps(raw[line],sort_keys=True),line)
   if len({raw[line]['response'] for line in lines})!=1:continue
   if variant=='primary':
    if len(lines)==1:chosen.extend(lines)
   elif variant=='collapse_identical':
    if len(distinct)==1:chosen.extend(distinct.values())
   else:chosen.extend(distinct.values())
  cells=defaultdict(list)
  for line in chosen:cells[raw[line]['query'],raw[line]['system_name']].append(line)
  eligible={}
  for k,ls in cells.items():
   if all(valid[x] for x in ls) and len({raw[x]['id'] for x in ls})==1 and (variant=='distinct_record_mean' or len(ls)==1):eligible[k]=ls
  qs={q for q,s in eligible if all((q,sys) in eligible for sys in SYSTEMS)}
  expected={x for q in qs for s in SYSTEMS for x in eligible[q,s]}
  base=out/dirname
  scores=list(csv.DictReader((base/'tables/response_scores.csv').open()))
  assert Counter(int(r['line']) for r in scores)==Counter(expected),(variant,'cohort mismatch')
  units=list(csv.DictReader((base/'tables/citation_credit.csv').open()))
  observed=Counter((int(x['line']),int(x['statement_index']),int(x['judgment_index']),int(x['occurrence_index'])) for x in units)
  intended=Counter((line,*triplet) for line in expected for triplet in bridges[line]);assert observed==intended
  manifest=list(csv.DictReader((base/'tables/cohort_manifest.csv').open()))
  for m in manifest:
   line=int(m['line']);r=raw[line]
   assert Fraction(m['query_weight'])==Fraction(1,len(qs))
   assert Fraction(m['record_weight'])==Fraction(1,len(eligible[r['query'],r['system_name']]))
  report['variants'][variant]={'queries':len(qs),'records':len(expected),'occurrence_links':len(units),'duplicate_policy_verified':True,'equal_query_weights_verified':True}
  if variant=='primary':
   micro={}
   for s in SYSTEMS:
    rr=[r for r in scores if r['system']==s];n=sum(int(r['denominator']) for r in rr)
    micro[s]=(Fraction(sum(int(r['full'])+int(r['conditional_partial']) for r in rr),n),Fraction(sum(int(r['full']) for r in rr),n))
   for row in csv.DictReader((base/'tables/micro_pairwise_gaps.csv').open()):
    a,b=micro[row['system_a']],micro[row['system_b']]
    assert Fraction(row['gap_C0_exact'])==a[0]-b[0]
    assert Fraction(row['gap_C1_exact'])==a[1]-b[1]
    assert Fraction(row['gap_change_exact'])==(a[1]-b[1])-(a[0]-b[0])
 report['micro_pairs_verified']=6
 (out/'logs/independent_cohort_audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--out',required=True);a=p.parse_args();audit(a.data,a.out)
