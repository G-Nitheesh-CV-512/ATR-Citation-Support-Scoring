import argparse
from pathlib import Path
from run_experiment import run
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--out',default='results');a=p.parse_args()
 for v in ['collapse_identical','distinct_record_mean']:
  s=run(a.data,Path(a.out)/v,v);print(v,s['queries'])
