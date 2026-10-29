---
schema: qual/card@1
id: E-WWROF
kind: problem
title: Closed sets via the closed-set formulation of continuity
classification:
  areas:
  - topology
  topics:
  - Closed Sets
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Using the closed set formulation of continuity (Theorem 18.1), show that the following are closed subsets of $\RR^2$:

$$
A = \theset{x \times y \mid xy = 1},
$$

$$
S^1 = \theset{x \times y \mid x^2 + y^2 = 1},
$$

$$
B^2 = \theset{x \times y \mid x^2 + y^2 \leq 1}.
$$

The set $B^2$ is called the (closed) unit ball in $\RR^2$.
:::

::: {.solution}
The coordinate projections $p_1,p_2:\RR^2\to\RR$ are continuous. Hence so are
\[
F(x,y)=xy=p_1p_2,
\qquad
G(x,y)=x^2+y^2=p_1^2+p_2^2.
\]
Since singletons are closed in $\RR$,
\[
A=F^{-1}(\{1\})
\]
is closed. Likewise
\[
S^1=G^{-1}(\{1\})
\]
is closed. Finally $(-\infty,1]$ is closed in $\RR$, so
\[
B^2=G^{-1}(( -\infty,1])
\]
is closed. This proves all three claims directly from the closed-set formulation of continuity.
:::
