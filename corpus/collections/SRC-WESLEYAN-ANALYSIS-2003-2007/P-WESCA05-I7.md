---
schema: qual/card@1
id: P-WESCA05-I7
kind: problem
title: "State Liouville's Theorem"
classification:
  areas: [complex-analysis]
  topics:
  - 'Liouville''s Theorem'
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 7 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 25: the Complex Analysis Section of
    the Analysis Qualifier, Wesleyan University, Summer 2005, Section 1 item 7. The page had cited
    only the extraction; it now names the examination, its item and the page of the
    scan. The statement is unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had
    answered the question, which STYLE-08 forbids; it is dropped, and the step that
    carries the result is now the QED step. No argument or statement changes.

- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the PDF-page locator in the card's text is removed; the item is cited by its
    examination, section and item number only, which the retained scan prints as its heading.
    The earlier events keep their text (QUAL-11). No statement or step changes.

---

::: {.problem}
State Liouville's Theorem.
:::

::: {.solution}
The item is Section 1 item 7 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan
University, Summer 2005 (statement of Liouville's theorem).


::: pf

::: {.pf-step #s1-1}

Liouville's theorem states:
$$
\boxed{\text{Every bounded entire function }f:\CC\to\CC\text{ is constant}.}
$$


::: pf-proof

Equivalently, if $f$ is analytic on all of $\CC$ and there is $M<\infty$ such that
$$
\abs{f(z)}\le M
\qquad
\text{for every }z\in\CC,
$$
then there is $c\in\CC$ with $f(z)=c$ for every $z\in\CC$. This is the statement of Liouville's theorem.

:::

:::


:::

:::
