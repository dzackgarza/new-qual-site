---
schema: qual/card@1
id: P-WESRA04-P1
kind: problem
title: The sum of measurable real-valued functions is measurable
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f,g:X\to\mathbb R$ be measurable functions on a measurable space $(X,\mathcal B)$.
Prove that $f+g$ is measurable.
:::

::: {.solution}
The map
\[
F:X\to\mathbb R^2,
\qquad
F(x)=(f(x),g(x)),
\]
is measurable with respect to the product Borel sigma-algebra: for every Borel rectangle $A\times B$,
\[
F^{-1}(A\times B)=f^{-1}(A)\cap g^{-1}(B)\in\mathcal B,
\]
and such rectangles generate $\mathcal B(\mathbb R^2)$.

The addition map
\[
S:\mathbb R^2\to\mathbb R,
\qquad
S(u,v)=u+v,
\]
is continuous, hence Borel measurable.
Therefore
\[
f+g=S\circ F
\]
is measurable.
:::
