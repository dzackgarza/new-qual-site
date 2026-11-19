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

---

::: {.problem}
State Liouville's Theorem.
:::

::: {.solution}
The item is Section 1 item 7 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan
University, Summer 2005 (statement of Liouville's theorem), on PDF p. 25 of the retained scan
assets/attachments/analysis_2003-2007.pdf.


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

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem statement.

:::

:::

:::
