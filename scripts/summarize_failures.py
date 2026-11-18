"""Rebuild reason summaries and deterministic first-three examples from saved audits."""
import argparse,csv
from pathlib import Path
from collections import Counter
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--results',default='results/clean_run');p.add_argument('--out',default='results/tables');a=p.parse_args()
 rows=list(csv.DictReader((Path(a.results)/'tables/record_audit.csv').open()))
 counts=Counter(reason for r in rows for reason in r['reasons'].split(';') if reason)
 dest=Path(a.out);dest.mkdir(parents=True,exist_ok=True)
 with (dest/'failure_summary.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['reason','rows','overlapping_categories']);w.writerows((k,v,True) for k,v in counts.items())
 with (dest/'failure_cases.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader()
  for reason in counts:w.writerows([r for r in rows if reason in r['reasons'].split(';')][:3])
 print('Wrote failure summary and deterministic examples; reason categories overlap.')
