---
schema: qual/card@1
id: P-CASP04E
kind: problem
title: "Points connected to infinity outside a compact set are not in its polynomial hull"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $K$ be a compact subset of $\mathbb{C}$ and $\hat{K}$ its polynomial hull, i.e. $$\hat{K} := \{z \in \mathbb{C} : |p(z)| \leq \sup_{w \in K} |p(w)|, \text{ for every polynomial } p\}.$$ Show that if $z \in \mathbb{C} \setminus K$ and there is a curve $\gamma \subset \mathbb{C}_\infty \setminus K$ connecting $z$ to $\infty$, then $z \notin \hat{K}$.
:::

::: solution
The curve $\gamma$ says precisely that $z$ lies in the unbounded component of
$\mathbb C_\infty\setminus K$. Apply the pole-moving form of Runge's theorem
to the function
\[
h(w)=\frac1{w-z},
\]
which is holomorphic in a neighborhood of $K$: because its only pole $z$ can
be moved to $\infty$ along $\gamma$ without crossing $K$, $h$ can be
approximated uniformly on $K$ by polynomials. Hence for any
$\varepsilon>0$ there is a polynomial $q$ such that
\[
\sup_{w\in K}\left|q(w)-\frac1{w-z}\right|<\varepsilon.
\]
Define
\[
p(w)=1-(w-z)q(w).
\]
Then $p(z)=1$, while on $K$,
\[
|p(w)|
=|w-z|\left|\frac1{w-z}-q(w)\right|
\le M\varepsilon,
\qquad
M=\max_{w\in K}|w-z|.
\]
Choose $\varepsilon<1/M$. Then
\[
|p(z)|=1>\sup_K|p|,
\]
so $z\notin\widehat K$.
:::
