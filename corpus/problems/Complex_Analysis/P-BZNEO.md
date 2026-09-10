---
schema: qual/card@1
id: P-BZNEO
kind: problem
title: Principal part of $P/Q$ at a simple or double root of $Q$
classification:
  areas:
  - complex-analysis
  topics:
  - Principal Parts
  - Poles
  - Residues
  - Polynomials
relations: []
review: draft
---

::: problem
Let $P, Q$ be polynomials with no common zeros.
Assume $a$ is a root of $Q$.
Find the principal part of $P/Q$ at $z=a$ in terms of $P$ and $Q$ if $a$ is (1) a simple root, and (2) a double root.
:::

::: solution
If $a$ is a simple zero of $Q$, write $Q(z)=(z-a)q(z)$ with
$q(a)=Q'(a)\ne0$. Then
\[
\frac{P(z)}{Q(z)}=rac{P(z)/q(z)}{z-a},
\]
so the principal part is
\[
\boxed{\frac{P(a)}{Q'(a)}\frac1{z-a}}.
\]

Now suppose $a$ is a double zero. Write
\[
Q(z)=(z-a)^2q(z),
\qquad q(a)=\frac{Q''(a)}2\ne0.
\]
Set $h=P/q$, which is holomorphic near $a$. Then
\[
\frac{P(z)}{Q(z)}=\frac{h(z)}{(z-a)^2}
=\frac{h(a)}{(z-a)^2}+\frac{h'(a)}{z-a}+\text{holomorphic terms}.
\]
Since
\[
q'(a)=\frac{Q'''(a)}6,
\]
we have
\[
h(a)=\frac{2P(a)}{Q''(a)}
\]
and
\[
h'(a)
=\frac{2P'(a)}{Q''(a)}
-\frac{2P(a)Q'''(a)}{3Q''(a)^2}.
\]
Thus the principal part is
\[
\boxed{
\frac{2P(a)}{Q''(a)}\frac1{(z-a)^2}
+\left(
\frac{2P'(a)}{Q''(a)}
-\frac{2P(a)Q'''(a)}{3Q''(a)^2}
\right)\frac1{z-a}.}
\]
:::
