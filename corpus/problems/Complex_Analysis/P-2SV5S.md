---
schema: qual/card@1
id: P-2SV5S
kind: problem
title: Laurent expansions of $\frac{z+1}{z(z-1)^2}$ about $z=0$ and $z=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
relations: []
review: draft
---

::: problem
Find the Laurent expansion of
\[
f(z) = {z+1 \over z(z-1)^2}
\]
about $z=0$ and $z=1$ respectively.

> Hint: recall that power series can be differentiated.
:::

::: solution
First decompose
\[
\frac{z+1}{z(z-1)^2}
=\frac1z-\frac1{z-1}+\frac2{(z-1)^2}.
\]

About $z=0$, for $0<|z|<1$ we use
\[
\frac1{1-z}=\sum_{n=0}^\infty z^n,
\qquad
\frac1{(1-z)^2}=\sum_{n=0}^\infty(n+1)z^n,
\]
to obtain
\[
\boxed{
f(z)=\frac1z+\sum_{n=0}^\infty(2n+3)z^n,
\qquad 0<|z|<1.}
\]
For $|z|>1$ instead expand in powers of $z^{-1}$:
\[
\boxed{
f(z)=\sum_{n=2}^\infty(2n-3)z^{-n},
\qquad |z|>1.}
\]

About $z=1$, put $\zeta=z-1$. Then
\[
f(z)=\frac1{1+\zeta}-\frac1\zeta+\frac2{\zeta^2}.
\]
Thus, for $0<|\zeta|<1$,
\[
\boxed{
f(z)=\frac2{\zeta^2}-\frac1\zeta
+\sum_{n=0}^\infty(-1)^n\zeta^n.}
\]
For $|\zeta|>1$,
\[
\boxed{
f(z)=\frac1{\zeta^2}
+\sum_{n=3}^\infty(-1)^{n+1}\zeta^{-n}.}
\]
These are the Laurent expansions on the maximal annuli centered at the two
specified points.
:::
