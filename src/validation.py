"""Structural validation independent of score calculation."""
from collections import Counter,defaultdict
from .data_loader import canonical
from .annotation_parser import parse

def validate(records):
    ids=defaultdict(list);counts=Counter();labels=Counter();audit=[];parsed={}
    for line,r in records:
        ids[r['id']].append(r)
        units,errors=parse(r);parsed[line]=(units,errors)
        n=len(r['citations']);m=sum(map(len,r['statements_to_citation_texts'].values()))
        counts['rows']+=1;counts['citation_objects']+=n;counts['mapping_entries']+=m
        counts['count_mismatch_rows']+=int(n!=m);counts['zero_citation_rows']+=int(n==0)
        for st,a in r['annotation']['statement_to_annotation'].items():
            if a['statement_supported'] is None:
                counts['null_collective']+=1
                if r['statements_to_citation_texts'].get(st):counts['null_with_mapped_citations']+=1
            labels.update(j['citation_supports'] for j in a['citation_annotations'] or [])
        audit.append(dict(line=line,id=r['id'],system=r['system_name'],split=r['split'],
             citation_objects=n,mapping_entries=m,association_units=len(units),
             mapping_eligible=not errors,reasons=';'.join(errors)))
    counts['distinct_response_ids']=len(ids);counts['queries']=len({r['query'] for _,r in records})
    counts['repeated_id_groups']=sum(len(g)>1 for g in ids.values())
    counts['excess_identical_records']=sum(len(g)-len({canonical(r) for r in g}) for g in ids.values())
    counts['conflicting_repeated_groups']=sum(len({canonical(r) for r in g})>1 for g in ids.values())
    counts['null_with_mapped_citations']+=0
    return dict(counts),labels,audit,parsed
