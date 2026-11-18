"""Clean deterministic reproduction; refuses an existing output directory."""
import argparse,sys,subprocess,time,json,hashlib,platform,os,resource
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
def main():
 p=argparse.ArgumentParser();p.add_argument('--data',required=True);p.add_argument('--out',required=True);p.add_argument('--figures',action='store_true');a=p.parse_args()
 data=Path(a.data).resolve();out=Path(a.out).resolve()
 if out.exists():p.error('Output already exists; choose a new run directory to preserve evidence')
 out.mkdir(parents=True);(out/'logs').mkdir()
 commands=[['-m','unittest','discover','-s','tests','-v'],['scripts/validate_dataset.py','--data',str(data),'--out',str(out)],['scripts/run_experiment.py','--data',str(data),'--out',str(out)],['scripts/run_sensitivity.py','--data',str(data),'--out',str(out)],['scripts/audit_results.py','--data',str(data),'--out',str(out)],['scripts/audit_cohort.py','--data',str(data),'--out',str(out)]]
 if a.figures:commands.append(['scripts/generate_figures.py','--out',str(out)])
 manifest={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'environment':'assistant execution workspace; NOT user WSL','python':sys.version,'platform':platform.platform(),'logical_cpus':os.cpu_count(),'data_sha256':hashlib.sha256(data.read_bytes()).hexdigest(),'data_path':str(data),'config_sha256':hashlib.sha256((ROOT/'configs/protocol.json').read_bytes()).hexdigest(),'code_hashes':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for d in ('src','scripts','tests') for f in sorted((ROOT/d).glob('*.py'))},'seed':None,'commands':[]}
 start=time.perf_counter()
 for i,cmd in enumerate(commands,1):
  t=time.perf_counter();r=subprocess.run([sys.executable]+cmd,cwd=ROOT,text=True,capture_output=True)
  (out/'logs'/f'{i:02d}_execution.txt').write_text(r.stdout+r.stderr)
  manifest['commands'].append({'argv':[sys.executable]+cmd,'exit_code':r.returncode,'elapsed_seconds':time.perf_counter()-t})
  if r.returncode:manifest['status']='FAIL';break
 else:manifest['status']='PASS'
 manifest['elapsed_seconds']=time.perf_counter()-start;manifest['max_child_rss_kib']=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
 (out/'logs/run_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 print(json.dumps({k:manifest[k] for k in ['status','elapsed_seconds','max_child_rss_kib']},indent=2))
 return 0 if manifest['status']=='PASS' else 1
if __name__=='__main__':raise SystemExit(main())
