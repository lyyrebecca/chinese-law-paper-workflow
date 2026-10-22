# Citation Safety Rules

Use this for citation, reference, quotation, data-source, and evidence-risk checking.

## Non-Negotiable Rules

- Do not fabricate authors, titles, years, journals, publishers, DOIs, page numbers, archive names, laws, datasets, or URLs.
- Do not attach a real citation to a claim unless the user has provided enough evidence that the source supports it.
- Do not pretend to have read a source when only a title, citation, or second-hand summary is available.
- Do not silently normalize incomplete references. Mark missing fields.
- Do not create exact quotations unless the user provided exact wording.
- Do not supply page numbers, archival locations, survey details, or interview details from memory or plausibility.
- If a user asks to "fix" a reference with missing metadata, preserve known fields and mark unknown fields as `[missing metadata]`.
- A Zotero item proves that a record exists in the user's library; it does not prove the source has been read or that it supports a specific claim.
- Search results and metadata can support source discovery and rough relevance only; detailed claims require abstracts, structured notes, full text, or user-provided excerpts.

## Risk Labels

- `Citation Risk`: Missing citation, incomplete metadata, suspicious reference, second-hand citation, citation does not match claim, or citation not supplied by user.
- `Zotero Import Risk`: Zotero record is incomplete, duplicated, imported to the wrong collection, lacks enough metadata, or is treated as read without source text/notes.
- `Evidence Gap`: Claim requires evidence, but no source/data has been provided.
- `Quotation Risk`: Exact wording or page number is missing for a direct quote.
- `Data Provenance Gap`: Statistic, dataset, interview, fieldwork, archive, or document source is unclear.
- `Causal Overclaim`: Citation or data may show association, description, or interpretation but the prose claims causality.

## Pass / Partial / Fail Criteria

| Criterion | Pass | Partial | Fail |
|---|---|---|---|
| Source traceability | Full enough metadata to locate source | Some fields missing | Source cannot be identified |
| Claim-source fit | Source support is visible from provided text/notes | Fit is plausible but not verified | Source does not support claim or no source provided |
| Quotations | Exact text, quotation marks, page if available | Exact text but page missing | Quote invented or not provided |
| Data claims | Data source and context clear | Source named but method/context missing | Statistic/data unsupported |
| Reference integrity | Entries complete and consistent with required style | Minor style/metadata gaps | Fabricated-looking or incomplete |

## Safe Output Pattern

```markdown
| Claim | Current citation/evidence | Risk | What is needed | Safe wording until verified |
|---|---|---|---|---|
```

For each risk row, include:

- The exact claim or phrase under review.
- The current support visible in the user's material.
- The missing evidence or metadata.
- A safe wording that does not overstate what is known.
- Whether the item blocks submission or can be fixed later.

## Safe Wording Examples

- Instead of "X proves Y", use "The provided material suggests Y, but the source support needs verification."
- Instead of inventing a citation, write "[citation needed: source showing X]".
- Instead of an exact quote, write "[quote needed from source, with page number]".
- Instead of completing an incomplete reference, write "Author, [missing year], [missing title details]."
