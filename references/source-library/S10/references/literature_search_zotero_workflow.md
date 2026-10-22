# Literature Search To Zotero Workflow

Use this reference when the user asks to search Chinese/English literature, import records into Zotero, generate structured paper notes, and then write or revise a social science literature review.

This workflow extends the literature review rules. It does not replace source discipline or citation safety rules.

## Required Preconditions

- The user provides at least one of: paper topic, research question, tentative title, keywords, core concepts, population/case, method, period, or target discipline.
- If the user asks to import into Zotero, use available citation/Zotero skills or tools rather than inventing records.
- If online search, CNKI, Google Scholar, Zotero connector, or Zotero Desktop is unavailable, state the blocker and continue with a search strategy or review matrix template.

## Tool Route

Use the available tools/skills in this order when the user asks for actual search or import:

1. CNKI route for Chinese literature.
   - Use `cnki-search` for ordinary keyword search.
   - Use `cnki-advanced-search` for title/author/journal/date/source-category filters.
   - Use `cnki-parse-results` and `cnki-navigate-pages` to collect more result metadata when needed.
   - Use `cnki-paper-detail` to inspect abstracts, keywords, authors, affiliations, source, fund, and classification.
   - Use `cnki-journal-index` when journal level/indexing matters for source screening.
   - Use `cnki-export` to export records to Zotero or RIS/BibTeX when the user asks to collect sources.
   - Use `cnki-download` only when the user explicitly asks to download a specific paper and access/login allows it.
2. Google Scholar route for English and cross-language literature.
   - Use `gs-search` for ordinary keyword search.
   - Use `gs-advanced-search` for exact phrase, author, title-only, journal, and date filters.
   - Use `gs-cited-by` to identify citing literature and later debate development.
   - Use `gs-fulltext` only when the user asks to locate full text or PDFs.
   - Use `gs-export` to export selected records to Zotero or BibTeX when the user asks to collect sources.
3. Citation-management route for metadata.
   - Use `citation-management` when DOI, BibTeX, PubMed, CrossRef, arXiv, or metadata validation is needed.
   - Use it to clean incomplete records, verify DOI metadata, or generate consistent BibTeX.
4. Zotero route for library management.
   - Use Zotero tools/skills to check readiness, search the local library, create or select collections, import records, export BibTeX, and retrieve item keys.
   - Treat Zotero writes as write actions: import only when the user explicitly requested it or confirmed the import.

## Search And Import Workflow

1. Clarify search scope.
   - Extract Chinese keywords, English keywords, synonyms, core concepts, case/region, method terms, and exclusion terms.
   - Separate broad background terms from terms that directly serve the research question.
   - Mark uncertain translations as `[needs user verification]`.
   - Decide whether CNKI, Google Scholar, both, or Zotero-only lookup is appropriate for the task.
2. Build search batches.
   - Batch A: core concept + object.
   - Batch B: mechanism/relationship + object.
   - Batch C: method/case-specific search.
   - Batch D: classic/foundational and recent literature checks.
   - For Chinese literature, prefer CNKI tools or other user-authorized Chinese academic search tools when available.
   - For English literature, prefer Google Scholar tools, discipline databases, CrossRef/DOI metadata, or user-authorized search tools when available.
3. Screen search results.
   - Keep sources that are relevant, direct, important, authoritative/recent/first-hand, and useful for the research question.
   - Exclude weakly related background sources unless needed for concept definition or field context.
   - Do not cite or summarize a source as read if only metadata are available.
4. Import or organize in Zotero.
   - If the user explicitly asked to import, import only verified records with enough metadata.
   - If import requires confirmation under the active Zotero tool rules, ask for confirmation unless the user's request already clearly authorizes import.
   - Put imported records into a named collection when possible, using a collection name tied to the paper topic.
   - Preserve DOI, URL, database source, abstract, tags, and notes when available.
5. Generate structured reading notes.
   - For each source, record metadata, source status, research question, theory/concepts, method/data, main finding, contribution, limitation, usable claim, relation to the user's paper, and citation risk.
   - If full text is unavailable, mark the note as `metadata/abstract only`.
   - If the source is only a search result and not imported/read, mark it as `candidate source`.
6. Build a literature review matrix.
   - Cluster sources by debate, concept, variable/mechanism, method, school, case, or period.
   - For each cluster, identify consensus, disagreement, limits, and the user's possible entry point.
7. Draft the literature review.
   - Write by analytic clusters, not by one-author-one-sentence listing.
   - End with a gap statement that leads to the user's research question, hypothesis, or design.
   - Use only verified sources for concrete citation claims.

## Overall Work Path

```text
paper topic / research question
  -> topic and question clarification
  -> Chinese + English keyword map
  -> CNKI search route for Chinese literature
  -> Google Scholar search route for English/cross-language literature
  -> metadata validation through citation-management when needed
  -> Zotero import / collection organization when requested
  -> source screening log
  -> structured paper notes
  -> literature review matrix
  -> cluster-based literature review draft
  -> citation/evidence risk report
```

## Expected Outputs And Files

When the user asks for a full search-to-review run, produce as many of these outputs as the available tools and permissions allow:

- Search strategy: Chinese/English keywords, databases/tools, filters, date range, inclusion/exclusion criteria.
- Search log: source, database/tool, query, result count when available, screening status, reason for inclusion/exclusion.
- Zotero collection report: collection name, imported items, skipped items, duplicates, item keys, citation keys when available.
- Structured paper notes: one note per source using the schema below.
- Literature review matrix: clusters, sources, shared claims, disagreements/limits, relation to the paper, risks.
- Draft literature review: analytic-cluster version that connects prior studies to the research gap and research question.
- Citation/evidence risk report: unverified records, abstract-only sources, metadata gaps, missing full text, unsupported claims.

Recommended local files when writing to the project is appropriate:

- `drafts/literature_search_strategy.md`
- `drafts/source_screening_log.md`
- `drafts/structured_paper_notes.md`
- `drafts/literature_review_matrix.md`
- `drafts/literature_review_draft.md`
- `drafts/citation_evidence_risks.md`
- `drafts/references.bib` or another user-requested bibliography file

## Structured Paper Note Schema

```markdown
## [Author Year Short Title]

- Source status: `imported to Zotero` / `in Zotero` / `metadata only` / `abstract only` / `full text read` / `candidate source`
- Metadata: author, year, title, journal/book/publisher, DOI/URL/database, Zotero item key if available
- Research question:
- Theory / concepts:
- Method / data:
- Main finding:
- Contribution:
- Limitation:
- Usable claim for this paper:
- Relation to the user's research question:
- Cluster:
- Citation risk:
- Evidence gap:
```

## Literature Review Matrix

| Cluster | Sources | Shared claim | Disagreement / limit | Relation to this paper | Risk |
|---|---|---|---|---|---|

## Pass / Partial / Fail Criteria

| Criterion | Pass | Partial | Fail |
|---|---|---|---|
| Search scope | Search terms cover topic, concepts, relationship, case, method, and language variants | Some key terms or language variants missing | Search is based only on the title or one vague keyword |
| Source verification | Sources have traceable metadata and Zotero item keys or supplied records | Metadata exists but import/full text is incomplete | Sources are invented, untraceable, or not actually searched |
| Screening logic | Inclusion/exclusion reasons are tied to the research question | Relevance is plausible but not explained | Sources are collected randomly or only by availability |
| Structured notes | Each source has method, finding, contribution, limitation, and relation to this paper | Notes summarize findings but miss method/limits/relation | Notes are bibliographic lists or copied abstracts |
| Synthesis | Sources are clustered into debates, concepts, mechanisms, methods, cases, or periods | Clusters exist but the gap is weak | Draft remains author-by-author listing |
| Citation safety | Claims use only verified sources and mark risks | Some claims need verification | Draft attaches unverified or fabricated citations |

## Safety Rules

- Never invent a source to fill a literature gap.
- Never import a fabricated or incomplete record as if verified.
- Never claim that a paper says something unless the claim is supported by the user's supplied text, abstract, notes, or retrieved full text.
- Metadata alone can support only bibliographic existence and rough relevance, not detailed claims about findings.
- Abstract-only reading can support cautious summaries of the abstract, marked as `abstract only`.
- Full-text claims, quotations, page numbers, and detailed methods require full text or user-provided excerpts.
- When source access is incomplete, write the review with placeholders such as `[source needed on X]` or safe wording such as "available abstracts suggest..."
