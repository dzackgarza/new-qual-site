---
schema: qual/card@1
id: E-Y75ZB
kind: problem
title: A countable rational rectangle basis for the plane
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Bases
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

Show that the countable collection

$$
\ts{(a, b) \times (c, d) \mid a < b \text{ and } c < d, \text{ and } a, b, c, d \text{ rational}}
$$

is a basis for $\mathbb{R}^2$.
:::

::: {.solution}
The collection is countable because it is indexed by a subset of $\mathbb Q^4$.

Let $U\subseteq\mathbb R^2$ be open and $(x,y)\in U$. Choose an ordinary open rectangle
\[
(x-\varepsilon,x+\varepsilon)\times(y-\delta,y+\delta)\subseteq U.
\]
By density of $\mathbb Q$, choose rationals
\[
a<x<b,\qquad c<y<d
\]
with
\[
(a,b)\subseteq(x-\varepsilon,x+\varepsilon),\qquad
(c,d)\subseteq(y-\delta,y+\delta).
\]
Then
\[
(x,y)\in(a,b)\times(c,d)\subseteq U.
\]
By the basis criterion, the stated countable collection is a basis for the standard topology on $\mathbb R^2$.
:::
