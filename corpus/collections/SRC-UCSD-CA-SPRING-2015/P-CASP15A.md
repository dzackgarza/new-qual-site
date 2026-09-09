---
schema: qual/card@1
id: P-CASP15A
kind: problem
title: 'Classical complex-analysis theorems: statements and proof sketches'
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy's Theorem
  - Cauchy Integral Formula
  - Morera
  - Liouville's Theorem
  - Casorati-Weierstrass
  - Open Mapping Theorem
  - Maximum Principle
  - Residue Theorem
  - Argument Principle
  - Weierstrass Theorem
  - Hurwitz
  - Reflection Principle
  - Riemann Mapping Theorem
relations: []
review: draft
---

::: problem
Pick four of the following results from the course and state them clearly ($5$ points each).
Then pick two of those four results and sketch their proofs ($10$ points each).

Cauchy's Theorem; Cauchy's integral formula; Morera's Theorem; Liouville's Theorem; Casorati-Weierstrass; Open mapping theorem; Maximum principle; Residue Theorem; Argument Principle; Weierstrass' Theorem; Hurwitz's Theorem; Reflection Principle; Riemann Mapping Theorem.
:::

::: solution
One possible choice is the following.

**Cauchy's theorem.** If $G$ is a simply connected domain and $f\in H(G)$,
then
\[
\int_\gamma f(z)\,dz=0
\]
for every closed piecewise $C^1$ curve $\gamma$ in $G$.

**Morera's theorem.** If $f$ is continuous on a domain $G$ and
\[
\int_{\partial T}f(z)\,dz=0
\]
for every triangle $T$ with $\overline T\subset G$, then $f$ is holomorphic
on $G$.

**Liouville's theorem.** Every bounded entire function is constant.

**Riemann mapping theorem.** Every nonempty simply connected proper domain
$G\subsetneq\mathbb C$ is conformally equivalent to the unit disk.

We sketch proofs of Morera and Liouville.

For Morera, fix a disk $D\Subset G$ and a base point $z_0\in D$. Define
\[
F(z)=\int_{[z_0,z]}f(\zeta)\,d\zeta.
\]
The triangle hypothesis shows that the integral is path independent inside
$D$. Hence
\[
\frac{F(z+h)-F(z)}h
=\frac1h\int_{[z,z+h]}f(\zeta)\,d\zeta\longrightarrow f(z)
\]
by continuity. Thus $F'=f$ on $D$, so $f$ is holomorphic. Since $D$ was
arbitrary, $f\in H(G)$.

For Liouville, suppose $|f|\le M$ on $\mathbb C$. Cauchy's estimate on the
circle $|z-a|=R$ gives
\[
|f'(a)|\le \frac{M}{R}.
\]
Letting $R\to\infty$ yields $f'(a)=0$. Since $a$ was arbitrary, $f$ is
constant.
:::
