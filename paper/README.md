# ACM-formatted implementation paper

## Files
- `main.tex` — ACM `acmsmall` manuscript source.
- `references.bib` — the existing bibliography; retained unchanged.
- `main.bbl` — generated ACM Reference Format bibliography output.
- `system_rows.tex`, `gap_rows.tex`, `robustness_rows.tex` — table row fragments.
- `figures/` — original figure PDF assets, retained byte-for-byte.
- `main.pdf` — compiled ACM-style review manuscript.

## Compile
The ACM `acmart` class and `ACM-Reference-Format.bst` must be installed (they are included in current Overleaf ACM projects and standard TeX Live ACM installations).

```bash
latexmk -pdf main.tex
```

Or compile manually:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Format choices
This manuscript uses `acmsmall`, matching the uploaded ACM Small Standard sample. The `review` option enables reviewer line numbering. The `nonacm` option and `printacmref=false` suppress unassigned ACM publication identifiers, rights statements, journal issue metadata, and placeholder DOI values. No ACM venue, volume, issue, article number, ISBN, rights selection, or DOI was supplied, so none has been invented. If the paper is accepted by an ACM publication, replace the draft metadata/options with the exact instructions and rights information supplied by that publication. For a double-anonymous review, use the venue's required anonymous option and author-suppression procedure.

## Preservation and verification
- The manuscript body, experimental claims, numerical results, equations, table data, citation keys, and citation-to-claim placements were retained from the original project source.
- The original `references.bib` was not edited.
- All 22 bibliography records are cited; there are no duplicate BibTeX keys, undefined citation keys, uncited bibliography records, or unresolved `\\ref` labels.
- 21 scholarly records were compared against the official BibTeX export files retained in the project; DOI/URL fields showed no mismatches. The remaining record is the pinned companion GitHub repository.
- All four original figure PDF files were retained byte-for-byte. The three figures used by the manuscript now have ACM accessibility descriptions.
- The Python implementation, scripts, tests, protocol configuration, and experiment evidence were not changed in the full-project archive.

The ACM-styled PDF is a formatting draft, not evidence of acceptance or compliance with an as-yet-unspecified ACM venue's special requirements.
