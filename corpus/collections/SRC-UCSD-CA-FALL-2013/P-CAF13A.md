---
schema: qual/card@1
id: P-CAF13A
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
Choose 4 of the following theorems, and write out their statements carefully and completely.
From among these, choose 2, and sketch their proofs.

- The Open Mapping Theorem

- Rouché's Theorem

- Runge's Theorem

- The Riemann Mapping Theorem

- The Poisson Integral Formula

- Morera's Theorem

- The Argument Principle

- The Great Picard Theorem

- The Monodromy Theorem

- The Schwarz Reflection Principle
:::

::: solution
Here are four choices.

**Open Mapping Theorem.** If $G\subset\mathbb C$ is a domain and
$f:G\to\mathbb C$ is nonconstant and holomorphic, then $f(G)$ is open.

**Rouché's Theorem.** Let $\gamma$ be a positively oriented simple closed
contour whose interior and boundary lie in a domain on which $f$ and $g$ are
holomorphic. If
\[
|g(z)|<|f(z)|\qquad(z\in\gamma),
\]
then $f$ and $f+g$ have the same number of zeros inside $\gamma$, counted with
multiplicity.

**Morera's Theorem.** Let $G$ be a domain and let $f:G\to\mathbb C$ be
continuous. If
\[
\int_{\partial T}f(z)\,dz=0
\]
for every triangle $T$ whose closure lies in $G$, then $f$ is holomorphic on
$G$.

**Argument Principle.** Let $f$ be meromorphic on a neighborhood of the closure
of a bounded domain bounded by a positively oriented contour $\gamma$, and
assume $f$ has no zeros or poles on $\gamma$. Then
\[
\frac1{2\pi i}\int_\gamma\frac{f'(z)}{f(z)}\,dz=N-P,
\]
where $N$ and $P$ are the numbers of zeros and poles inside $\gamma$, counted
with multiplicity.

We sketch two proofs.

For the **Open Mapping Theorem**, fix $z_0\in G$. Write
\[
f(z)-f(z_0)=(z-z_0)^m h(z),\qquad h(z_0)\ne0,
\]
where $m\ge1$. Choose $r>0$ so that the closed disk about $z_0$ of radius $r$
lies in $G$ and $f(z)\ne f(z_0)$ on $|z-z_0|=r$. Let
\[
\delta=\min_{|z-z_0|=r}|f(z)-f(z_0)|>0.
\]
If $|w-f(z_0)|<\delta$, then on that circle
\[
|(f(z)-w)-(f(z)-f(z_0))|=|w-f(z_0)|<|f(z)-f(z_0)|.
\]
Rouché's theorem shows that $f-w$ has the same number of zeros in the disk as
$f-f(z_0)$, in particular at least one. Thus every sufficiently small
neighborhood of $f(z_0)$ lies in $f(G)$.

For **Morera's Theorem**, work first in a disk $D\Subset G$ and fix $z_*\in D$.
Define
\[
F(z)=\int_{[z_*,z]}f(\zeta)\,d\zeta.
\]
The triangle-integral hypothesis implies that the integral is unchanged if the
straight segment is replaced by a polygonal path in $D$. Hence, for small $h$,
\[
F(z+h)-F(z)=\int_{[z,z+h]}f(\zeta)\,d\zeta.
\]
By continuity of $f$,
\[
\frac{F(z+h)-F(z)}{h}\longrightarrow f(z).
\]
Thus $F'=f$ on $D$, so $f$ is holomorphic there. Since every point of $G$ lies
in such a disk, $f$ is holomorphic on $G$.
:::
