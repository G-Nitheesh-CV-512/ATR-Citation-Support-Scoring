"""Independent arithmetic recomputation from raw labels; does not import scorer."""
import argparse,csv,json,hashlib
from pathlib import Path
from fractions import Fraction
from collections import defaultdict

def audit(data,out):
 raw=[json.loads(x) for x in Path(data).read_text().splitlines()]
 out=Path(out); checked=0
 for folder in [out,out/'collapse_identical',out/'distinct_record_mean']:
  rows=list(csv.DictReader((folder/'tables/response_scores.csv').open()))
  by_query=defaultdict(list)
  for row in rows:
   r=raw[int(row['line'])-1];assert r['id']==row['response_id']
   full=partial=0
   for a in r['annotation']['statement_to_annotation'].values():
    jj=a['citation_annotations'] or []
    fs=sum(j['citation_supports']=='Citation Completely Supports Statement' for j in jj)
    full+=fs
    if fs==0 and a['statement_supported']=='Yes':
     partial+=sum(j['citation_supports']=='Citation Partially Supports Statement' for j in jj)
   n=len(r['citations']);assert n==int(row['denominator'])
   assert full==int(row['full']) and partial==int(row['conditional_partial'])
   x,y=Fraction(full+partial,n),Fraction(full,n)
   assert x==Fraction(row['C0_exact']) and y==Fraction(row['C1_exact'])
   q=hashlib.sha256(r['query'].encode()).hexdigest();assert q==row['query_key']
   by_query[q,row['system']].append((x,y));checked+=1
  by_system=defaultdict(list)
  for (q,s),vs in by_query.items():
   by_system[s].append(tuple(sum((v[k] for v in vs),Fraction(0))/len(vs) for k in (0,1)))
  scores={s:tuple(sum((v[k] for v in vs),Fraction(0))/len(vs) for k in (0,1)) for s,vs in by_system.items()}
  for row in csv.DictReader((folder/'tables/system_scores.csv').open()):
   assert scores[row['system']]==(Fraction(row['C0_exact']),Fraction(row['C1_exact']))
  for row in csv.DictReader((folder/'tables/pairwise_gaps.csv').open()):
   a,b=scores[row['system_a']],scores[row['system_b']]
   assert a[0]-b[0]==Fraction(row['gap_C0_exact'])
   assert a[1]-b[1]==Fraction(row['gap_C1_exact'])
   assert (a[1]-b[1])-(a[0]-b[0])==Fraction(row['gap_change_exact'])
 report={'status':'PASS','response_record_checks':checked,'variants':3,'method':'separate raw-label arithmetic; no scorer imports','scope':'implementation arithmetic, not independent human annotation or published B0 fidelity'}
 (out/'logs/independent_audit.json').write_text(json.dumps(report,indent=2)+'\n');print(report)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--out',default='results');a=p.parse_args();audit(a.data,a.out)
