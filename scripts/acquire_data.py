"""Optional explicit download from pinned authors' URL. Never overwrite a file.
Live network acquisition has NOT been tested in the delivered environment.
Access does not establish reuse/redistribution rights; see data/README.md.
"""
import argparse,sys,urllib.request,hashlib,os
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.data_loader import URL,SIZE,SHA256,write_json
from datetime import datetime,timezone
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--destination',required=True);a=p.parse_args()
 dest=Path(a.destination).expanduser().resolve();dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():p.error('Destination exists: validate it; do not overwrite')
 part=dest.with_name(dest.name+'.download')
 with part.open('xb') as f:
  with urllib.request.urlopen(URL,timeout=90) as response:
   while chunk:=response.read(1024*1024):f.write(chunk)
 size=part.stat().st_size;sha=hashlib.sha256(part.read_bytes()).hexdigest()
 if size!=SIZE or sha!=SHA256:raise ValueError('STOP: downloaded identity mismatch; preserved .download for investigation')
 os.link(part,dest);part.unlink() # link fails if another process created destination
 write_json(str(dest)+'.provenance.json',dict(source=URL,sha256=sha,size_bytes=size,acquired_utc=datetime.now(timezone.utc).isoformat(),rights='Dataset-specific scope unresolved; do not redistribute raw data'))
 print(dest)
