# Self Test For social-science-paper-writing

Use these tests to check whether the skill behaves as a reusable social science paper writing, diagnosis, and revision workflow. A passing run should select or respect the operating mode, apply diagnosis labels, use Pass / Partial / Fail when reviewing, and avoid inventing sources, data, page numbers, or course rules.

## Test 1: Topic Diagnosis

Input: A broad social science topic.

Expected behavior:

- Identify topic vs research question.
- Mark `Topic Summary` or `Research Question Too Broad` if appropriate.
- Propose researchable alternatives.
- Suggest suitable materials and methods when possible.
- Do not invent sources.

## Test 2: Literature Review

Input: A literature review that lists authors one by one.

Expected behavior:

- Mark `Literature Listing`.
- Identify missing debate structure.
- Identify missing research gap with `Missing Research Gap` if appropriate.
- Mark `Review-Question Mismatch` if the review does not serve the stated question.
- Suggest organization by debate, approach, concept, variable, case, period, or method.
- Do not invent specific literature.

## Test 3: Theory Framework

Input: A section that only names theories.

Expected behavior:

- Mark `Theory Decoration`.
- Mark `Conceptual Ambiguity` if core concepts are undefined.
- Ask how concepts connect to the research question.
- Suggest operational analytical dimensions.
- Do not add unsupported theory claims or fake citations.

## Test 4: Research Design

Input: A method section with unclear data source.

Expected behavior:

- Mark `Method Mismatch`, `Data Provenance Gap`, `Sampling Gap`, or `Operationalization Gap` as appropriate.
- Ask what material, sample, case, corpus, field site, period, or method is available.
- Explain what can still be revised without the missing information.
- Do not invent data.

## Test 5: Citation Risk

Input: Claims with missing citations or suspicious references.

Expected behavior:

- Mark `Citation Risk` or `Evidence Gap`.
- Mark `Quotation Risk` if exact wording or page number is missing for a direct quotation.
- Do not fabricate bibliographic information.
- Separate verifiable claims from claims needing user verification.
- Provide safe wording until evidence is supplied.

## Test 6: Data Analysis Fit

Input: A quantitative analysis section that reports tests or models without explaining variable levels, missing-value treatment, or model diagnostics.

Expected behavior:

- Mark `Data Cleaning Gap` if cleaning, coding, missing values, or variable transformation are not reported.
- Mark `Statistical Test Mismatch` if the test does not fit the variable measurement level or comparison structure.
- Mark `Regression Strategy Gap` if model choice, predictor selection, regression strategy, or diagnostics are missing.
- Mark `Causal Overclaim` if statistical association is written as a causal mechanism without supporting design.
- Use `references/data_analysis_rules.md` and course source labels for course-supported analysis rules.
- Do not force quantitative statistical criteria onto qualitative interviews, ethnography, historical materials, or interpretive text analysis.

## Test 7: Literature Search To Zotero Review

Input: A paper title or research question plus a request to search Chinese/English literature, import records into Zotero, generate structured notes, and draft a literature review.

Expected behavior:

- Select or respect `literature_search_to_review` mode.
- Build Chinese and English search terms from topic, concepts, relationship, case, method, and time scope.
- Use CNKI skills for Chinese literature search/detail/export when available.
- Use Google Scholar skills for English or cross-language search, cited-by exploration, full-text lookup, and export when available.
- Use `citation-management` for metadata validation and BibTeX/DOI cleanup when needed.
- Use Zotero tools for collection lookup, import, export, duplicate/citation-key reporting, and local library organization.
- Import only verified records into Zotero when requested or confirmed.
- Generate structured notes for each source with source status, metadata, research question, method/data, finding, contribution, limitation, relation to the user's paper, and risk labels.
- Build a synthesis matrix before drafting.
- Draft by analytic clusters rather than author-by-author listing.
- Mark `Search Scope Gap`, `Source Screening Gap`, `Structured Reading Gap`, `Zotero Import Risk`, `Citation Risk`, or `Evidence Gap` when appropriate.
- Do not invent sources, Zotero item keys, citations, abstracts, findings, page numbers, or full-text claims.
- Report final outputs/files such as search strategy, screening log, Zotero collection report, structured notes, review matrix, draft literature review, citation/evidence risks, and bibliography file when created.

## Failure Signals

The skill needs revision if Codex:

- Gives generic advice such as "strengthen the argument" without explaining how.
- Rewrites text without diagnosing the problem.
- Invents literature, page numbers, data, interviews, or findings.
- Treats general advice as a course norm.
- Ignores the operating mode.
- Fails to identify missing information and why it matters.
- Marks `Pass`, `Partial`, or `Fail` without evidence from the user's material.
- Treats significance, correlation, or regression coefficients as sufficient proof of causality.
- Recommends statistical tests without checking variable measurement levels and sample/comparison structure.
- Writes a literature review from fabricated or unverified search results.
- Treats Zotero import as equivalent to having read and verified the source.
