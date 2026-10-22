---
name: social-science-paper-writing
description: Use for social science academic paper drafting, outlining, diagnosis, review, and revision. Trigger for topic diagnosis, research question refinement, literature review planning, CNKI/Google Scholar literature search-to-Zotero workflows, structured paper reading notes, theoretical framework design, research design critique, draft review, section or paragraph revision, citation and evidence risk checking, causal-claim checking, and pre-submission review. Do not use for purely creative writing or non-academic editing.
---

# Social Science Paper Writing

This skill helps write, diagnose, and revise social science academic papers. It is built around course-derived norms in `references/key_principles.md` plus clearly marked general academic writing suggestions.

## First Move

1. Identify the user's task and choose one operating mode below.
2. Load `references/key_principles.md` when the user asks for course-supported norms, source attribution, a full paper/section diagnosis, or any output that labels a rule as `[course norm]`.
3. Load the relevant reference only when needed:
   - `references/literature_review_rubric.md` for literature review planning or diagnosis.
   - `references/literature_search_zotero_workflow.md` for searching Chinese/English literature with available CNKI/Google Scholar/citation tools, importing records into Zotero, making structured paper notes, and drafting a literature review from verified sources.
   - `references/research_design_rubric.md` for methods, data, variables, sampling, causal inference, or research design.
   - `references/data_collection_rules.md` for sampling, sample size, units of analysis, reliability, validity, conceptualization, operationalization, and measurement scales.
   - `references/data_analysis_rules.md` for data cleaning, coding, missing values, descriptive statistics, inferential statistics, test selection, regression strategy, and diagnostic checks.
   - `references/citation_safety_rules.md` for citations, references, quotations, data claims, and evidence risks.
   - `assets/revision_report_template.md` for structured review reports.
   - `assets/literature_review_matrix_template.md` for search logs, structured paper notes, and synthesis matrices.
4. If information is missing, apply the Missing Information Rule before drafting or judging.

## Operating Modes

- `topic_diagnosis`: Evaluate whether a topic is researchable, useful, feasible, focused, field-relevant, and legal.
- `research_question_refinement`: Convert a topic into a problem-oriented research question and 2-4 sharper alternatives.
- `outline_building`: Build or repair a title-to-conclusion structure around the research problem.
- `literature_review_planning`: Plan search scope, source clusters, synthesis logic, gap statement, and review structure.
- `literature_search_to_review`: Search Chinese/English literature through available CNKI, Google Scholar, citation-management, and Zotero tools; import verified records into Zotero when requested; create structured source notes; cluster the literature; and draft a course-compliant literature review.
- `draft_review`: Diagnose a whole draft for argument, structure, literature, theory, method, evidence, citation, and causal claims.
- `section_revision`: Rewrite or revise one section while preserving the user's claims and marking gaps.
- `citation_and_evidence_check`: Check citation support, missing sources, risky quotations, data provenance, and unsupported claims.
- `pre_submission_check`: Final readiness review for research question, structure, methods, evidence, references, style, and overclaiming.

If the user does not specify a mode, infer the mode from the request and state it briefly.

## Mode Execution Protocols

Use the matching protocol after selecting a mode:

- `topic_diagnosis`
  1. Extract topic, object, field, scope, available materials, and intended paper type.
  2. Rate usefulness, feasibility, focus, field relevance, legality, and evidence availability.
  3. Assign problem labels such as `Topic Summary` or `Research Question Too Broad`.
  4. Output 2-4 revised topic directions and list missing information.
- `research_question_refinement`
  1. Convert the topic into a problem statement.
  2. Separate phenomenon-level problem from theory-level problem.
  3. Produce candidate research questions with scope, evidence needed, and tradeoffs.
  4. Mark questions that require unavailable data or unsupported causal inference.
- `outline_building`
  1. Identify title keywords, research question, tentative answer, method/material, and contribution.
  2. Build sections from introduction through conclusion, giving each section one job.
  3. Check whether literature, theory, method, analysis, and conclusion all return to the question.
  4. Mark drift as `Structure Drift`.
- `literature_review_planning`
  1. Load `references/literature_review_rubric.md`.
  2. Define literature clusters, inclusion logic, important source types, and synthesis questions.
  3. Draft a gap statement and show how it leads to the research question.
  4. Mark missing source clusters as `Evidence Gap` or `Citation Risk`.
- `literature_search_to_review`
  1. Load `references/literature_review_rubric.md`, `references/literature_search_zotero_workflow.md`, and `references/citation_safety_rules.md`.
  2. Extract the paper topic, research question, Chinese/English keywords, synonyms, case/region, method terms, time range, and exclusion terms.
  3. Route Chinese literature discovery through available CNKI skills such as `cnki-search`, `cnki-advanced-search`, `cnki-paper-detail`, `cnki-export`, and related CNKI navigation/detail tools when available.
  4. Route English and cross-language discovery through available Google Scholar skills such as `gs-search`, `gs-advanced-search`, `gs-cited-by`, `gs-fulltext`, and `gs-export` when available.
  5. Use `citation-management` for metadata validation, DOI/BibTeX cleanup, and reference accuracy when needed.
  6. Use Zotero tools/skills for collection lookup, import, export, duplicate checks, and citation-key management when the user asks for library organization.
  7. If CNKI, Google Scholar, citation-management, Zotero, network access, or login-dependent access is unavailable, state the blocker and produce a search plan plus matrix template.
  8. Screen real search results for relevance, directness, importance, authority/recency, and first-hand status.
  9. Import only verified records into Zotero when the user has explicitly asked for import or has confirmed it; preserve metadata and collection/tag organization when possible.
  10. Produce structured notes for each source, marking `metadata only`, `abstract only`, `full text read`, `imported to Zotero`, or `candidate source`.
  11. Build a synthesis matrix by debate, concept, variable/mechanism, method, school, case, or period.
  12. Draft the literature review from verified notes and matrix entries, ending with a gap-to-question transition.
- `draft_review`
  1. Identify the paper's research question, thesis/answer, structure, method, data/materials, sampling/measurement status, analysis procedure, evidence, and citation status.
  2. Apply the Pass / Partial / Fail scale to each relevant checklist area.
  3. Assign diagnosis labels with evidence from the draft.
  4. Output priority fixes before optional improvements.
- `section_revision`
  1. Identify the section's job in the whole paper.
  2. Diagnose the section using the relevant checklist.
  3. Rewrite only claims supported by provided information.
  4. Mark placeholders for missing evidence, citations, data, or concept definitions.
- `citation_and_evidence_check`
  1. Load `references/citation_safety_rules.md`.
  2. Extract claims, current support, source metadata, quotations, data claims, and causal verbs.
  3. Assign risk labels and safe wording.
  4. Do not complete or normalize references unless metadata are supplied.
- `pre_submission_check`
  1. Run final checklist across research question, structure, literature, theory, design, sampling, measurement, data analysis, evidence, citation/reference, causal claims, and conclusion.
  2. Separate blockers from polish.
  3. Identify any unverified source, data, page, quote, or method claim.
  4. Output a submit / revise-before-submit judgment.

## Source Discipline

Always distinguish four source-status labels:

- `[course norm]`: Directly supported by `references/key_principles.md`; cite the source pointer when useful.
- `[general academic writing suggestion]`: Common scholarly writing advice not explicitly established as a course rule.
- `[assistant inference]`: A reasoned judgment drawn from the user's draft or materials.
- `[needs user verification]`: A factual, bibliographic, empirical, or course-specific point that needs user-provided evidence.

Rules:

- Do not present general advice as course original text.
- Do not quote or paraphrase course rules as exact wording unless verified in `references/key_principles.md`.
- If `references/course_extracted_rules.md` exists, use it as additional course-derived support; if it is absent, do not invent it.
- When a user asks "what does the course require?", answer only from course-derived references.
- When a rule is not in the course references, say so and mark any advice as `[general academic writing suggestion]`.
- When using Zotero or online literature search results, distinguish source access status: `candidate source`, `metadata only`, `abstract only`, `full text read`, `in Zotero`, or `imported to Zotero`.
- Do not treat Zotero library presence as proof that the source supports a claim; Zotero verifies that a record exists, not that the cited claim is correct.

## Evidence Safety Rules

- Never fabricate authors, titles, years, journals, publishers, page numbers, DOIs, archives, datasets, laws, or reference entries.
- Never fabricate data, interviews, fieldwork, observations, survey responses, sample sizes, coding results, statistical findings, or cases.
- If the user has not provided a source's text, metadata, or excerpt, do not pretend to have read it.
- Mark unsupported empirical or theoretical assertions as `Evidence Gap`.
- Mark missing, unverifiable, second-hand, mismatched, or possibly fabricated citations as `Citation Risk`.
- Mark causal language unsupported by design as `Causal Overclaim`.
- Replace invented-looking specifics with placeholders or requests for verification.
- When searching and importing literature, do not use a source for detailed findings, methods, quotations, or page-specific claims unless the abstract, full text, or user-provided excerpts support those details.
- Metadata-only records can support only bibliographic traceability and rough relevance, not substantive claims about findings.

## Global Writing Principles

- [course norm] Anchor the paper in a real research problem rather than a topic summary.
- [course norm] The paper should answer: what is the problem, why it matters, what method/material answers it, why the answer is credible, what the answer is, and what sources readers should consult.
- [course norm] Keep the paper complete, reasonable, and tied to the title keywords.
- [course norm] Literature review must serve the research question and lead to a gap, hypothesis, or research plan.
- [course norm] Define core concepts before using them in theory, measurement, or analysis.
- [course norm] Match method, data, variables, and evidence to the question.
- [course norm] Do not overstate causality, especially with cross-sectional or descriptive designs.
- [general academic writing suggestion] Prefer direct, explicit section claims over ornate prose.

## Pass / Partial / Fail Scale

Use this scale for all checklists:

- `Pass`: The item is explicit, specific, supported, and integrated into the paper.
- `Partial`: The item is present but vague, late, under-supported, inconsistent, or not yet integrated.
- `Fail`: The item is absent, contradicted, unsupported, fabricated, or impossible to assess from provided materials.

When reviewing, output `Pass / Partial / Fail` plus one sentence of evidence from the user's material.

Checklist use rule:

- Rate every checklist item that is relevant to the user's request.
- For each `Partial` or `Fail`, give an actionable fix with: target location, operation, and expected improvement.
- If the user's material does not include enough text to rate an item, mark `Fail` or `Partial` with `[needs user verification]` rather than guessing.
- Do not write vague fixes such as "strengthen the argument" unless followed by a concrete operation, e.g. "add one sentence after paragraph 2 stating the research problem and name the evidence that will answer it."

## Section Workflows

### Title

Workflow:

1. Extract object, scope, relationship/puzzle, case/material, and method if relevant.
2. Test whether the title names a researchable problem rather than a broad topic.
3. Check whether title keywords recur in question, literature review, framework, design, and conclusion.

Checklist:

- Research object is clear.
- Scope is focused enough for the paper length and evidence.
- Relationship, puzzle, method, or case is visible when needed.
- Title can expand into a three-level outline.
- Title keywords match the paper body.

### Abstract

Workflow:

1. Identify problem, method/material, finding, and conclusion/contribution.
2. Cut generic background that displaces the research substance.
3. Flag claims not supported in the paper.

Checklist:

- Research problem is stated.
- Method/material is named.
- Main finding is stated.
- Conclusion or contribution is stated.
- Background does not dominate.
- No unsupported claims are introduced.

### Introduction

Workflow:

1. Move from important theme to key unresolved issue to specific research problem.
2. State research question, argument or expected answer, method/material, contribution, and roadmap.
3. Remove textbook-style background that does not create the problem.

Checklist:

- The problem appears early.
- The introduction explains why the problem matters.
- It shows what remains unresolved in existing understanding.
- It states the paper's answer or analytic direction.
- It previews method/material and structure.

### Research Question

Workflow:

1. Convert topic into a problem that needs solving.
2. Separate phenomenon-level problem from theory-level problem.
3. Test usefulness, feasibility, scope, field relevance, legality, and evidence availability.
4. Offer refined alternatives with tradeoffs.

Checklist:

- It is a problem, not just a topic or information question.
- It is real and evidence-checkable.
- It has theoretical or practical value.
- It is small enough to answer.
- It fits the field and available method/data.
- It does not require forbidden or unavailable materials.

### Literature Review

Workflow:

1. Define the scholarly conversation.
2. Cluster sources by debate, concept, variable, mechanism, method, school, case, or period.
3. Summarize consensus, disagreement, weaknesses, and gaps.
4. Connect the gap to the user's research question, hypothesis, or design.
5. Flag source gaps and second-hand citation risks.

Optional search-to-review workflow when the user asks for literature search, Zotero import, or source collection:

1. Run `literature_search_to_review` before drafting.
2. Convert the paper topic/research question into Chinese and English search terms, including synonyms, concept terms, case terms, method terms, and exclusion terms.
3. Search Chinese literature through available CNKI tools and English/cross-language literature through available Google Scholar tools; use citation-management for metadata validation and Zotero for import/export.
4. Do not invent sources to fill a cluster.
5. Import verified records to Zotero only when requested or confirmed, preferably into a topic-specific collection.
6. For each source, create a structured note covering: metadata, source status, research question, theory/concepts, method/data, main finding, contribution, limitation, relation to this paper, cluster, citation risk, and evidence gap.
7. Build a review matrix from the structured notes.
8. Draft the review by clusters and cite only claims supported by verified source notes or supplied text.

Checklist:

- Review is organized by analytic logic, not author-by-author listing.
- Sources are relevant, direct, important, and preferably first-hand.
- Classic, authoritative, recent, and field-relevant works are considered when available.
- The review includes evaluation, not only summary.
- The research gap is explicit.
- The review justifies the paper's question or hypothesis.
- Search terms and inclusion/exclusion logic are explicit when literature search is part of the task.
- CNKI/Google Scholar/citation-management/Zotero route and blockers are explicit when search/import is requested.
- Zotero imports or source records are traceable when the task asks for collection management.
- Each source used in the review has a structured note or user-provided evidence.
- Metadata-only or abstract-only sources are not overstated as fully read.

### Theoretical Framework

Workflow:

1. List core concepts that must be defined.
2. Identify whether each definition is accepted, modified, or newly proposed.
3. Link theory to variables, mechanisms, categories, cases, or expected relationships.
4. Remove theory that only decorates the paper.

Checklist:

- Core concepts are defined before use.
- Concept intension/extension or dimensions are clear where needed.
- Definitions have literature support or explicit justification.
- Theory explains the research problem.
- Variable or mechanism relationships have support.
- Framework is concise enough to guide analysis.

### Research Design

Workflow:

1. Restate the question/hypothesis the design must answer.
2. Choose method by problem fit.
3. Specify population, sample, sampling method, unit of analysis, data/materials, generation process, case/corpus boundary, period, and scope.
4. Define concepts, working definitions, variables, indicators, coding categories, measurement scales, reliability/validity checks, or interpretive procedures.
5. Explain how analysis connects evidence to claims.
6. State sampling limits, measurement limits, validity threats, and ethical risks.

Checklist:

- Method fits the question.
- Data/materials are described and traceable.
- Population, sample, sampling process, and unit of analysis are explicit when empirical claims require them.
- Sample, case, field, period, or corpus boundary is clear.
- Operationalization matches concepts.
- Reliability and validity are considered when using scales, indicators, or multiple items.
- Measurement scale fits the planned analysis.
- Analysis procedure is explicit.
- Design supports the level of claim being made.
- Limits and ethics are acknowledged.

### Analysis Chapters

Workflow:

1. Assign each section one role in answering the research question.
2. Verify data cleaning, coding, missing-value treatment, variable transformation, and analysis procedure before interpreting results when quantitative data are used.
3. Match descriptive statistics, tests, correlations, or regression models to the variable levels and research question.
4. Start with analytic claims, then evidence, then interpretation.
5. Connect findings back to concepts/theory and the central problem.
6. Flag unsupported claims, model/test mismatch, missing diagnostics, and causal overreach.

Checklist:

- Each chapter/section advances the answer.
- Claims are supported by evidence.
- Data cleaning, coding, missing-value handling, and variable transformation are reported when relevant.
- Statistical test or model matches variable measurement level and comparison structure.
- Regression strategy and independent variables have theoretical justification when regression is used.
- Necessary diagnostic checks are reported or limitations are acknowledged.
- Evidence is interpreted rather than merely displayed.
- Concepts stay consistent.
- Alternative explanations are considered when relevant.
- Claim strength matches evidence strength.

### Conclusion

Workflow:

1. Answer the research question directly.
2. Summarize the reasoning, not the whole paper.
3. State theoretical/practical contribution.
4. Name limitations from data, method, scope, or causal inference.
5. Remove new unsupported claims.

Checklist:

- Direct answer is present.
- Contribution follows from literature and analysis.
- Limitations are specific.
- Claims do not exceed design/evidence.
- No new evidence-dependent claim appears for the first time.

### Notes And References

Workflow:

1. Mark borrowed ideas, paraphrases, quotations, data, laws, official documents, statistics, and factual claims needing support.
2. Check whether each citation actually supports the claim.
3. Require quotation marks and page numbers for direct quotations when available.
4. Prefer original sources over copied review claims.
5. Apply the user's required citation style; otherwise mark style-dependent.

Checklist:

- Borrowed ideas are cited.
- Direct quotations are marked and paginated.
- Important data have source provenance.
- References are complete and traceable.
- Citations support the exact claims attached to them.
- Unverified references are marked instead of normalized.

## Common Problem Diagnosis Labels

- `Topic Summary`: The draft reports a topic without solving a research problem.
- `Weak Problem Consciousness`: The problem is vague, late, unimportant, or not tied to a scholarly/practical puzzle.
- `Research Question Missing`: No explicit research question can be identified.
- `Research Question Too Broad`: The question cannot be answered with the available scope, data, method, or paper length.
- `Literature Listing`: The review lists sources one by one without synthesis.
- `Search Scope Gap`: Literature search terms, databases, language scope, period, or inclusion/exclusion criteria are missing or too narrow.
- `Source Screening Gap`: Search results are collected without explaining why sources are included, excluded, or limited.
- `Structured Reading Gap`: Sources are imported or listed without notes on question, concepts, method/data, finding, contribution, limitation, and relation to this paper.
- `Missing Research Gap`: The review does not show what remains unresolved or why this study is needed.
- `Review-Question Mismatch`: Literature review covers background or adjacent topics rather than the paper's actual question.
- `Theory Decoration`: Theory is used as packaging, not as an explanatory framework.
- `Conceptual Ambiguity`: Core terms are undefined, overlapping, or shifting.
- `Method Mismatch`: Method does not fit the question or claim.
- `Method-Paper Split`: Method is named but not operationalized in the actual study.
- `Operationalization Gap`: Indicators, variables, codes, or categories do not match the concept being claimed.
- `Sampling Gap`: Sample size, sampling process, case boundary, field site, corpus, or period is missing or unjustified.
- `Data Provenance Gap`: Dataset, statistic, archive, interview, fieldwork, survey, or document source is unclear.
- `Measurement Reliability Gap`: Scale, coding, or instrument consistency is not addressed when measurement depends on repeated items or coding.
- `Measurement Validity Gap`: Indicators do not clearly measure the intended concept or do not cover its meaning range.
- `Data Cleaning Gap`: Data receipt, screening, coding, entry checking, missing-value treatment, or outlier review is absent or unclear.
- `Statistical Test Mismatch`: Statistical test does not fit variable levels, group structure, or assumptions.
- `Regression Strategy Gap`: Regression model, predictor selection, diagnostic checks, or strategy lacks justification.
- `Evidence Gap`: A claim lacks evidence or source support.
- `Causal Overclaim`: Causal language exceeds what the design can support.
- `Citation Risk`: Citation is missing, unverifiable, second-hand, fabricated-looking, or mismatched.
- `Zotero Import Risk`: A record is incomplete, unverified, duplicated, imported to the wrong collection, or treated as read merely because it is in Zotero.
- `Quotation Risk`: Direct quotation lacks exact wording, quotation marks, or page/location information.
- `Structure Drift`: Sections drift away from title keywords, research question, or argument sequence.
- `Conclusion Overreach`: Conclusion adds claims or implications beyond evidence and design.

## Revision Output Formats

Output rules for all formats:

- Every diagnosis must include a label, evidence from the provided material, and a fix.
- Every rewrite must preserve the user's verifiable claims and mark unsupported additions as placeholders.
- Every citation/evidence review must include safe wording when support is missing.
- Avoid empty comments such as "improve academic quality"; name the exact criterion that failed and the edit required.

### Whole-paper Diagnosis

```markdown
## Mode
draft_review

## Overall Diagnosis
[One paragraph.]

## Problem Labels
- Label:
  - Severity: High/Medium/Low
  - Evidence from draft:
  - Fix:

## Pass / Partial / Fail Checklist
| Area | Rating | Evidence | Next action |
|---|---|---|---|

## Missing Information
| Missing item | Why it matters | What user should provide | What can still be done |
|---|---|---|---|
```

### Section Revision

```markdown
## Mode
section_revision

## Revision Goal
[What is being fixed.]

## Revised Section
[Text.]

## Change Log
- Claim clarified:
- Structure changed:
- Evidence gap marked:
- Citation risk marked:
```

### Paragraph-level Revision

```markdown
## Original Problem
[Diagnosis label + short explanation.]

## Revised Paragraph
[Text.]

## Why This Revision Works
- [Pass/Partial/Fail improvement.]

## Remaining Gaps
- [Missing source/data/concept.]
```

### Checklist Review

```markdown
| Criterion | Pass/Partial/Fail | Evidence | Fix |
|---|---|---|---|
```

### Citation / Evidence Risk

```markdown
| Claim | Current support | Risk label | Needed evidence | Safe wording now |
|---|---|---|---|---|
```

### Literature Search To Review

```markdown
## Mode
literature_search_to_review

## Search Scope
- Topic / research question:
- Chinese keywords:
- English keywords:
- Databases / tools used:
- Inclusion / exclusion logic:
- Zotero collection:

## Search And Import Log
| Source | Status | Zotero item key | Why included | Risk / next action |
|---|---|---|---|---|

## Structured Notes
### [Author Year Short Title]
- Source status:
- Metadata:
- Research question:
- Theory / concepts:
- Method / data:
- Main finding:
- Contribution:
- Limitation:
- Relation to this paper:
- Cluster:
- Citation risk:

## Synthesis Matrix
| Cluster | Sources | Shared claim | Disagreement / limit | Relation to this paper | Risk |
|---|---|---|---|---|---|

## Draft Literature Review
[Cluster-based review text.]

## Remaining Gaps
- [Sources, full texts, metadata, or user decisions still needed.]
```

## Missing Information Rule

When information is missing, state:

- What is missing.
- Why it matters for the writing or judgment.
- What the user should provide.
- What limited work can still be done without it.

Do this instead of silently inventing research questions, sources, data, methods, findings, page numbers, or course rules.

## Examples

Use `examples/good_outline.md` as a compact model of an outline where question, thesis, method, analysis, and conclusion align.
Use `examples/weak_outline.md` to diagnose broad topic summary and missing method/evidence.
Use `examples/sample_review.md` as a compact review tone model.
Use `assets/literature_review_matrix_template.md` when building a search log, structured reading notes, and synthesis matrix before drafting the literature review.
