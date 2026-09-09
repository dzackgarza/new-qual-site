---
schema: qual/card@1
id: P-HCAX8
kind: problem
title: Zeros of a polynomial derivative remain in a containing half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Gauss-Lucas Theorem
relations: []
review: draft
---

::: problem
Suppose all zeros of a polynomial lie in one closed half-plane.
Show that every zero of its derivative lies in the same half-plane.
:::

::: solution
Let
\[
p(z)=c\prod_{j=1}^N(z-z_j),
\]
where the zeros $z_j$ are listed with multiplicity and all lie in a closed half-plane $H$.

Any zero of $p'$ which is also a zero of $p$ already lies in $H$, so it remains to consider a point $w$ with
\[
p'(w)=0,
\qquad
p(w)\ne0.
\]
The logarithmic derivative gives
\[
0=\frac{p'(w)}{p(w)}
=\sum_{j=1}^N\frac1{w-z_j}.
\]

Suppose for contradiction that $w\notin H$. After translating and rotating the plane, we may assume
\[
H=\{z:\operatorname{Re}z\ge0\}
\]
and hence $\operatorname{Re}w<0$. Since every $z_j\in H$,
\[
\operatorname{Re}(w-z_j)<0.
\]
Therefore
\[
\operatorname{Re}\frac1{w-z_j}
=\frac{\operatorname{Re}(w-z_j)}{|w-z_j|^2}<0
\]
for every $j$. The sum of these reciprocals consequently has strictly negative real part, contradicting
\[
\sum_{j=1}^N\frac1{w-z_j}=0.
\]

Thus every zero of $p'$ lies in $H$. This is the half-plane form of the Gauss--Lucas theorem.
:::
