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

Using the closed set formulation of continuity (Theorem 18.1), show that the following are closed subsets of $\mathbb{R}^2$:

$$
A = \ts{x \times y \mid xy = 1},
$$

$$
S^1 = \ts{x \times y \mid x^2 + y^2 = 1},
$$

$$
B^2 = \ts{x \times y \mid x^2 + y^2 \leq 1}.
$$

The set $B^2$ is called the (closed) unit ball in $\mathbb{R}^2$.
:::

::: {.solution}
The coordinate projections $p_1,p_2:\mathbb R^2\to\mathbb R$ are continuous. Hence so are
\[
F(x,y)=xy=p_1p_2,
\qquad
G(x,y)=x^2+y^2=p_1^2+p_2^2.
\]
Since singletons are closed in $\mathbb R$,
\[
A=F^{-1}(\{1\})
\]
is closed. Likewise
\[
S^1=G^{-1}(\{1\})
\]
is closed. Finally $(-\infty,1]$ is closed in $\mathbb R$, so
\[
B^2=G^{-1}(( -\infty,1])
\]
is closed. This proves all three claims directly from the closed-set formulation of continuity.
:::
