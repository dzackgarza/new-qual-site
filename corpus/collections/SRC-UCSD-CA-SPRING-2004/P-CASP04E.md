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

::: {.problem}
Let $K$ be a compact subset of $\CC$ and $\hat{K}$ its polynomial hull, i.e. $$\hat{K} := \{z \in \CC : \abs{p(z)} \leq \sup_{w \in K} \abs{p(w)}, \text{ for every polynomial } p\}.$$ Show that if $z \in \CC \setminus K$ and there is a curve $\gamma \subset \CC_\infty \setminus K$ connecting $z$ to $\infty$, then $z \notin \hat{K}$.
:::

::: {.solution}
The curve $\gamma$ says precisely that $z$ lies in the unbounded component of
$\CC_\infty\setminus K$. Apply the pole-moving form of Runge's theorem
to the function
$$
h(w)=\frac1{w-z},
$$
which is holomorphic in a neighborhood of $K$: because its only pole $z$ can
be moved to $\infty$ along $\gamma$ without crossing $K$, $h$ can be
approximated uniformly on $K$ by polynomials. Hence for any
$\varepsilon>0$ there is a polynomial $q$ such that
$$
\sup_{w\in K}\abs{q(w)-\frac1{w-z}}<\varepsilon.
$$
Define
$$
p(w)=1-(w-z)q(w).
$$
Then $p(z)=1$, while on $K$,
$$
\abs{p(w)}
=\abs{w-z}\abs{\frac1{w-z}-q(w)}
\le M\varepsilon,
\qquad
M=\max_{w\in K}\abs{w-z}.
$$
Choose $\varepsilon<1/M$. Then
$$
\abs{p(z)}=1>\sup_K\abs{p},
$$
so $z\notin\widehat K$.
:::
