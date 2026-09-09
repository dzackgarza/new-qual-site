---
schema: qual/card@1
id: P-HCAX17
kind: problem
title: Laurent coefficients and growth on a punctured disk
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Isolated Singularities
relations: []
review: draft
---

::: problem
Let $f$ be holomorphic on the punctured unit disk.

a. Write the Laurent expansion of $f$ and give bounds on its coefficients in terms of the values of $f$ on circles.

b. Relate these bounds to the radii of convergence of the positive and negative parts.

c. What additional conclusions follow if $f$ is bounded?
:::

::: solution
The Laurent expansion on $0<|z|<1$ is
\[
f(z)=\sum_{n=-\infty}^{\infty}a_nz^n,
\qquad
a_n=\frac{1}{2\pi i}\int_{|\zeta|=r}
\frac{f(\zeta)}{\zeta^{n+1}}\,d\zeta,
\]
for every $0<r<1$. If
\[
M(r)=\max_{|\zeta|=r}|f(\zeta)|,
\]
then Cauchy's estimate gives, for every $n\in\mathbb Z$,
\[
|a_n|\le M(r)r^{-n}.
\]

For $n\ge0$, fixing any $r<1$ gives
\[
\limsup_{n\to\infty}|a_n|^{1/n}\le r^{-1}.
\]
Letting $r\uparrow1$ shows that the positive-power series
\(
\sum_{n\ge0}a_nz^n
\)
has radius of convergence at least $1$.

For the negative part, write $m=-n>0$. Then
\[
|a_{-m}|\le M(r)r^m.
\]
For each fixed $r>0$ this implies
\[
\limsup_{m\to\infty}|a_{-m}|^{1/m}\le r.
\]
Since $r$ may be arbitrarily small, the series
\(
\sum_{m\ge1}a_{-m}w^m
\)
has infinite radius of convergence in $w=1/z$. Equivalently, the negative Laurent part converges for every $z\ne0$.

If $f$ is bounded on the punctured disk, say $|f|\le B$, then for every $m\ge1$,
\[
|a_{-m}|\le Br^m
\]
for all $0<r<1$. Letting $r\downarrow0$ gives $a_{-m}=0$. Thus the principal part vanishes, so the singularity at $0$ is removable and
\[
f(z)=\sum_{n=0}^{\infty}a_nz^n
\]
extends holomorphically across $0$.
:::
