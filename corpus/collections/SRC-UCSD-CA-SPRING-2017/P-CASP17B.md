---
schema: qual/card@1
id: P-CASP17B
kind: problem
title: 'An entire function with $f(z)f(1/z)$ bounded is a monomial'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
---

::: {.problem}
Let $f : \CC \to \CC$ be entire.
Assume that the function $g(z) = f(z) \cdot f\!\left(\frac{1}{z}\right)$ is bounded on $\CC \setminus \{0\}$.
Show that $f(z) = cz^m$.
:::

::: {.solution}
If $f\equiv0$, the conclusion is immediate. Otherwise let $m$ be the order of
the zero of $f$ at $0$, so
$$
f(z)=z^m h(z),\qquad h(0)\ne0.
$$
Because
$$
g(z)=f(z)f(1/z)
$$
is bounded near $z=0$ and $f(z)\sim h(0)z^m$, we obtain
$$
\abs{f(1/z)}=O(\abs{z}^{-m})\qquad(z\to0).
$$
Equivalently,
$$
\abs{f(w)}=O(\abs{w}^m)\qquad(\abs{w}\to\infty).
$$
Cauchy's estimates then imply that $f$ is a polynomial of degree at most $m$.
Since its zero at $0$ has order exactly $m$, it must be
$$
\boxed{f(z)=cz^m}
$$
for some constant $c\ne0$.
:::
