---
schema: qual/card@1
id: P-WESCA10-I5
kind: problem
title: 'State Morera’s theorem'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Theorems and Definitions, item 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State Morera's theorem.
:::

::: {.solution}
<1>1. Morera's theorem states the following.

::: {.proof}
Let $D\subseteq\mathbb C$ be a domain and let
$$
f:D\to\mathbb C
$$
be continuous. Suppose that for every triangle $T$ whose closure is contained in $D$,
$$
\int_{\partial T}f(z)\,dz=0.
$$
Then $f$ is holomorphic on $D$.

Equivalently, it is enough to assume that the integral of $f$ around every closed triangular path lying with its interior in $D$ vanishes.
:::

<1>2. Q.E.D.

::: {.proof}
Step <1>1 gives the requested precise statement, including the continuity hypothesis and the triangular-contour condition.
:::
:::
