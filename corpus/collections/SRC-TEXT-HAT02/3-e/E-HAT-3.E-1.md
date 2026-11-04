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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read. The two halves are right. With $m=0$ in the coefficient ring the lens-space
    complex has zero differential, so $H^q(X;\ZZ_m)=\ZZ_m$ and, for $k\mid m$, $H^q(X;\ZZ_k)=\ZZ_k$ in
    every degree; the coefficient map gives a ring homomorphism
    $H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k\to H^*(X;\ZZ_k)$ which is degreewise between free rank-one
    $\ZZ_k$-modules and carries the cellular generator to the cellular generator, hence is an
    isomorphism of rings because it is a bijective ring map. The final reduction is also right:
    for $m$ even, $x^2=(m/2)y$, and if $m/k$ is even then $m/2\equiv0$ in $\ZZ_k$, so $x^2=0$ and the
    ring is $\Lambda_{\ZZ_k}[x]\otimes\ZZ_k[y]$. The repair attributes the cellular complex (Hatcher
    Example 2.43) instead of appealing to "the standard model". Recorded, because the card should
    not be read as more than the exercise asks: when $m$ is even and $m/k$ is odd, $m/2\not\equiv0$
    in $\ZZ_k$ and $x^2\ne0$, so the conclusion in that case is not $\Lambda\otimes\ZZ_k[y]$; the
    exercise only claims the even case, and the card only displays the even case.
---

::: {.problem}
Show that $H^*(K(\ZZ_m, 1); \ZZ_k)$ is isomorphic as a ring to $H^*(K(\ZZ_m, 1); \ZZ_m) \otimes \ZZ_k$ if $k$ divides $m$.
In particular, if $m/k$ is even, this is $\Lambda_{\ZZ_k}[x] \otimes \ZZ_k[y]$.
:::

::: {.solution}
Let
$$
X=K(\ZZ_m,1),
\qquad k\mid m.
$$
The standard infinite lens-space CW model for $X$ has one cell in every dimension, and its integral cellular boundary maps alternate between $0$ and multiplication by $m$ — the complex that Hatcher computes in Example 2.43. With coefficients in a ring $R$ in which $m=0$ the cellular cochain differential is therefore zero (it is the transpose of a zero map), so the cohomology is the dual of the chains: Hence
$$
H^q(X;\ZZ_m)\cong\ZZ_m,
\qquad
H^q(X;\ZZ_k)\cong\ZZ_k
$$
for every $q\ge0$.

The coefficient reduction
$$
\ZZ_m\longrightarrow\ZZ_k
$$
induces a ring homomorphism
$$
H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k
\longrightarrow H^*(X;\ZZ_k).
$$
In each degree the source and target are both free rank-one $\ZZ_k$-modules, and the cellular generator reduces to the cellular generator. Thus the map is an isomorphism degreewise, hence a ring isomorphism:
$$
\boxed{H^*(X;\ZZ_k)
\cong H^*(X;\ZZ_m)\otimes_{\ZZ_m}\ZZ_k.}
$$

Hatcher's calculation of the $\ZZ_m$ ring gives generators
$$
x\in H^1(X;\ZZ_m),
\qquad y=\beta(x)\in H^2(X;\ZZ_m),
$$
with $y$ polynomial and, when $m$ is even,
$$
x^2=\frac m2\,y,
$$
the unique element of order $2$ in $H^2(X;\ZZ_m)$. If $m/k$ is even, write $m=2rk$. After reduction to $\ZZ_k$,
$$
\frac m2=rk=0\in\ZZ_k,
$$
so $x^2=0$. Therefore in this case
$$
\boxed{H^*(K(\ZZ_m,1);\ZZ_k)
\cong\Lambda_{\ZZ_k}[x]\otimes\ZZ_k[y],
\quad \gradeddegree{x}=1,\ \gradeddegree{y}=2.}
$$
:::
