---
schema: qual/card@1
id: E-H7BO5
kind: problem
title: A sequentially compact space is totally bounded
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
---

::: exercise
Show that a sequentially compact space is totally bounded.

#### Exercise
:::

::: {.solution}
<1>1. Let $(X,d)$ be sequentially compact. Suppose, toward a contradiction, that $X$ is not totally bounded.
::: {.proof}
Then there exists $\varepsilon>0$ such that no finite family of open $\varepsilon$-balls covers $X$.
:::

<1>2. Choose inductively $x_1,x_2,\dots$ so that
$$d(x_m,x_n)\ge\varepsilon\qquad(m\ne n).$$
::: {.proof}
After choosing $x_1,\dots,x_n$, their $\varepsilon$-balls do not cover $X$, so choose $x_{n+1}$ outside their union.
:::

<1>3. This sequence has no convergent subsequence.
::: {.proof}
Every convergent sequence in a metric space is Cauchy, but any two distinct terms of any subsequence remain at distance at least $\varepsilon$.
:::

<1>4. This contradicts sequential compactness. Therefore $X$ is totally bounded.
::: {.proof}
Sequential compactness requires every sequence to have a convergent subsequence.
:::
:::
