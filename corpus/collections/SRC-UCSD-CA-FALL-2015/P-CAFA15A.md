---
schema: qual/card@1
id: P-CAFA15A
kind: problem
title: 'Classical complex-analysis theorems: statements and proof sketches'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Pick four of the following results from the course and state them clearly.
Then pick two of those four results and sketch their proofs.

- Cauchy's Theorem

- Cauchy's Integral Formula

- Morera's Theorem

- Liouville's Theorem

- Casorati–Weierstrass

- Open Mapping Theorem

- Residue Theorem

- Argument Principle

- Weierstrass' Theorem

- Hurwitz's Theorem

- Reflection Principle

- Riemann Mapping Theorem
:::

::: solution
We choose the following four results.

**Cauchy's integral formula.** If $f$ is holomorphic on a neighborhood of the closed disk $\overline{B(a,R)}$, then for every $z\in B(a,R)$,
\[
f(z)=\frac{1}{2\pi i}\int_{|\zeta-a|=R}\frac{f(\zeta)}{\zeta-z}\,d\zeta.
\]

**Morera's theorem.** If $f$ is continuous on a domain $\Omega$ and
\[
\int_{\partial T}f(z)\,dz=0
\]
for every triangle $T$ whose closure lies in $\Omega$, then $f$ is holomorphic on $\Omega$.

**Liouville's theorem.** Every bounded entire function is constant.

**The open mapping theorem.** If $f$ is nonconstant and holomorphic on a domain $\Omega$, then $f(\Omega)$ is open.

We sketch proofs of Liouville and the open mapping theorem.

For Liouville, if $|f|\le M$ on $\mathbb C$, then Cauchy's estimate on the circle $|z-a|=R$ gives
\[
|f'(a)|\le \frac{M}{R}.
\]
Letting $R\to\infty$ gives $f'(a)=0$ for every $a$, hence $f$ is constant.

For the open mapping theorem, let $a\in\Omega$ and write
\[
f(z)-f(a)=(z-a)^m g(z),
\]
where $m\ge1$ and $g$ is holomorphic with $g(a)\ne0$. Shrink to a disk $\overline{B(a,r)}\subset\Omega$ on which $g$ has no zero. On $|z-a|=r$, let
\[
\eta=\min |f(z)-f(a)|>0.
\]
If $|w-f(a)|<\eta$, then on the boundary
\[
|(f(z)-f(a))-(f(z)-w)|=|w-f(a)|<|f(z)-f(a)|.
\]
Rouché's theorem implies that $f(z)-w$ and $f(z)-f(a)$ have the same number of zeros in $B(a,r)$, namely $m$. Thus every such $w$ lies in $f(B(a,r))$, so $f(a)$ is an interior point of the image.
:::
