---
schema: qual/card@1
id: P-WESCA05-I2
kind: problem
title: "Define a cycle in complex analysis"
classification:
  areas: [complex-analysis]
  topics:
  - Contour Integration
  - Winding Number
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 2 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 25: the Complex Analysis Section of
    the Analysis Qualifier, Wesleyan University, Summer 2005, Section 1 item 2. The page had cited
    only the extraction; it now names the examination, its item and the page of the
    scan. The statement is unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had
    answered the question, which STYLE-08 forbids; it is dropped, and the step that
    carries the result is now the QED step. No argument or statement changes.

---

::: {.problem}
Give the definition of a cycle.
:::

::: {.solution}
The item is Section 1 item 2 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan
University, Summer 2005 (definition of a cycle), in the retained scan `assets/attachments/analysis_2003-2007.pdf`.


::: pf

::: {.pf-step #s1-1}

In the contour-integration setting, a cycle in an open set $U\subseteq\CC$ is a finite formal integer linear combination
$$
\boxed{\Gamma=\sum_{j=1}^N n_j\gamma_j}
$$
where $n_j\in\ZZ$ and each $\gamma_j:[a_j,b_j]\to U$ is a closed piecewise $C^1$ curve:
$$
\gamma_j(a_j)=\gamma_j(b_j).
$$


::: pf-proof

This is the definition. The adjective “formal” means that the cycle records the oriented curves together with their integer multiplicities; integration is extended linearly by
$$
\int_\Gamma f(z)\,dz
=
\sum_{j=1}^N n_j\int_{\gamma_j}f(z)\,dz.
$$
Equivalently, a cycle is an integral $1$-chain whose boundary is zero.

:::

:::


:::

:::
