"""Conservative occurrence bridge. No raw text, judgments or offsets repaired."""
from collections import Counter
FULL='Citation Completely Supports Statement'
PARTIAL='Citation Partially Supports Statement'
NO_SUPPORT={'Citation Provides No Support for Statement','Citation Inaccessible',
 'Citation Completely Supports but Also Refutes Statement',"Statement is Unclear, Can't Make Judgment"}
LABELS={FULL:'full',PARTIAL:'partial',**{x:'none' for x in NO_SUPPORT}}
COLLECTIVE={'Yes','No','Citations Contradict Each Other'}
REQUIRED={'id':str,'query':str,'response':str,'split':str,'system_name':str,
 'citations':list,'statements_to_citation_texts':dict,'annotation':dict}

def parse(record):
    errors=[];units=[]
    for k,t in REQUIRED.items():
        if not isinstance(record.get(k),t): errors.append('schema_'+k)
    if errors:return units,sorted(set(errors))
    r=record; mapping=r['statements_to_citation_texts']; annotations=r['annotation'].get('statement_to_annotation')
    if not isinstance(annotations,dict):return [],['schema_statement_annotations']
    if set(mapping)!=set(annotations):errors.append('statement_key_mismatch')
    occurrences=r['citations'];used=[]
    for i,c in enumerate(occurrences):
        if not isinstance(c,dict) or not all(k in c for k in ['text','start_index','end_index','link_target']):
            errors.append('citation_schema');continue
        a,b=c['start_index'],c['end_index']
        if not isinstance(a,int) or not isinstance(b,int) or not 0<=a<b<=len(r['response']) or r['response'][a:b]!=c['text']:
            errors.append('invalid_offset')
    for si,(statement,markers) in enumerate(mapping.items()):
        ann=annotations.get(statement)
        if not isinstance(statement,str) or not isinstance(markers,list) or not all(isinstance(x,str) for x in markers) or not isinstance(ann,dict):
            errors.append('statement_schema');continue
        collective=ann.get('statement_supported');judgments=ann.get('citation_annotations')
        if judgments is None:judgments=[]
        if not isinstance(judgments,list) or any(not isinstance(j,dict) for j in judgments):
            errors.append('judgment_schema');continue
        if Counter(markers)!=Counter(j.get('citation_text') for j in judgments):errors.append('marker_judgment_mismatch')
        if not markers:continue
        if collective not in COLLECTIVE:errors.append('missing_or_unknown_collective')
        if len(markers)!=len(set(markers)):errors.append('duplicate_statement_marker')
        if ann.get('statement_is_verification_worthy') is not True:errors.append('cited_not_verification_worthy')
        start=r['response'].find(statement)
        unique=start>=0 and r['response'].find(statement,start+1)<0
        if not unique:errors.append('nonunique_statement_span')
        end=start+len(statement)
        for ji,j in enumerate(judgments):
            marker=j.get('citation_text');raw=j.get('citation_supports')
            if raw not in LABELS:errors.append('unknown_individual_label')
            candidates=[i for i,c in enumerate(occurrences) if isinstance(c,dict) and c.get('text')==marker
              and isinstance(c.get('start_index'),int) and isinstance(c.get('end_index'),int)
              and unique and start<=c['start_index']<c['end_index']<=end]
            if len(candidates)!=1:errors.append('nonbijective_marker_occurrence')
            used.extend(candidates)
            units.append(dict(statement_index=si,judgment_index=ji,marker=marker,raw_label=raw,
                 label=LABELS.get(raw),collective=collective,occurrence_indices=candidates))
    if Counter(used)!=Counter(range(len(occurrences))):errors.append('occurrence_coverage_mismatch')
    if len(units)!=len(occurrences):errors.append('denominator_mismatch')
    if not occurrences:errors.append('zero_citations')
    return units,sorted(set(errors))
