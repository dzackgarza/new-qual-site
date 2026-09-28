---
schema: qual/card@1
id: E-HAT-3.E-1
kind: problem
title: "Cohomology of $K(\\mathbb{Z}_m, 1)$ with $\\mathbb{Z}_k$ coefficients"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $H^*(K(\mathbb{Z}_m, 1); \mathbb{Z}_k)$ is isomorphic as a ring to $H^*(K(\mathbb{Z}_m, 1); \mathbb{Z}_m) \otimes \mathbb{Z}_k$ if $k$ divides $m$.
In particular, if $m/k$ is even, this is $\Lambda_{\mathbb{Z}_k}[x] \otimes \mathbb{Z}_k[y]$.
:::

::: {.solution}
Let
\[
X=K(\mathbb Z_m,1),
\qquad k\mid m.
\]
The standard infinite lens-space CW model for $X$ has one cell in every dimension. With coefficients in a ring $R$ on which $m$ acts as zero, its cellular cochain differential is zero, since the integral cellular boundary maps alternate between $0$ and multiplication by $m$. Hence
\[
H^q(X;\mathbb Z_m)\cong\mathbb Z_m,
\qquad
H^q(X;\mathbb Z_k)\cong\mathbb Z_k
\]
for every $q\ge0$.

The coefficient reduction
\[
\mathbb Z_m\longrightarrow\mathbb Z_k
\]
induces a ring homomorphism
\[
H^*(X;\mathbb Z_m)\otimes_{\mathbb Z_m}\mathbb Z_k
\longrightarrow H^*(X;\mathbb Z_k).
\]
In each degree the source and target are both free rank-one $\mathbb Z_k$-modules, and the cellular generator reduces to the cellular generator. Thus the map is an isomorphism degreewise, hence a ring isomorphism:
\[
\boxed{H^*(X;\mathbb Z_k)
\cong H^*(X;\mathbb Z_m)\otimes_{\mathbb Z_m}\mathbb Z_k.}
\]

Hatcher's calculation of the $\mathbb Z_m$ ring gives generators
\[
x\in H^1(X;\mathbb Z_m),
\qquad y=\beta(x)\in H^2(X;\mathbb Z_m),
\]
with $y$ polynomial and, when $m$ is even,
\[
x^2=\frac m2\,y,
\]
the unique element of order $2$ in $H^2(X;\mathbb Z_m)$. If $m/k$ is even, write $m=2rk$. After reduction to $\mathbb Z_k$,
\[
\frac m2=rk=0\in\mathbb Z_k,
\]
so $x^2=0$. Therefore in this case
\[
\boxed{H^*(K(\mathbb Z_m,1);\mathbb Z_k)
\cong\Lambda_{\mathbb Z_k}[x]\otimes\mathbb Z_k[y],
\quad |x|=1,\ |y|=2.}
\]
:::
