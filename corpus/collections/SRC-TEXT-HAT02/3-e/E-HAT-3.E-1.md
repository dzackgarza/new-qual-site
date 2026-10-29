---
schema: qual/card@1
id: E-HAT-3.E-1
kind: problem
title: "Cohomology of $K(\\ZZ_m, 1)$ with $\\ZZ_k$ coefficients"
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
Show that $H^*(K(\ZZ_m, 1); \ZZ_k)$ is isomorphic as a ring to $H^*(K(\ZZ_m, 1); \ZZ_m) \otimes \ZZ_k$ if $k$ divides $m$.
In particular, if $m/k$ is even, this is $\Lambda_{\ZZ_k}[x] \otimes \ZZ_k[y]$.
:::

::: {.solution}
Let
\[
X=K(\ZZ_m,1),
\qquad k\mid m.
\]
The standard infinite lens-space CW model for $X$ has one cell in every dimension. With coefficients in a ring $R$ on which $m$ acts as zero, its cellular cochain differential is zero, since the integral cellular boundary maps alternate between $0$ and multiplication by $m$. Hence
\[
H^q(X;\ZZ_m)\cong\ZZ_m,
\qquad
H^q(X;\ZZ_k)\cong\ZZ_k
\]
for every $q\ge0$.

The coefficient reduction
\[
\ZZ_m\longrightarrow\ZZ_k
\]
induces a ring homomorphism
\[
H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k
\longrightarrow H^*(X;\ZZ_k).
\]
In each degree the source and target are both free rank-one $\ZZ_k$-modules, and the cellular generator reduces to the cellular generator. Thus the map is an isomorphism degreewise, hence a ring isomorphism:
\[
\boxed{H^*(X;\ZZ_k)
\cong H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k.}
\]

Hatcher's calculation of the $\ZZ_m$ ring gives generators
\[
x\in H^1(X;\ZZ_m),
\qquad y=\beta(x)\in H^2(X;\ZZ_m),
\]
with $y$ polynomial and, when $m$ is even,
\[
x^2=\frac m2\,y,
\]
the unique element of order $2$ in $H^2(X;\ZZ_m)$. If $m/k$ is even, write $m=2rk$. After reduction to $\ZZ_k$,
\[
\frac m2=rk=0\in\ZZ_k,
\]
so $x^2=0$. Therefore in this case
\[
\boxed{H^*(K(\ZZ_m,1);\ZZ_k)
\cong\Lambda_{\ZZ_k}[x]\otimes\ZZ_k[y],
\quad |x|=1,\ |y|=2.}
\]
:::
