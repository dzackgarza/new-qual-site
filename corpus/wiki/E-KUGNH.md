---
schema: qual/card@1
id: E-KUGNH
kind: exercise
title: "Bounded derivatives imply removable singularities"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Bounded derivatives imply removable singularities"}
Suppose $f$ is holomorphic on $\DD\smz$ and there exist $M, k$ such that
\[
\abs{f^{(k)}(z)} \leq {M\over \abs{z}^k} && \forall 0 < \abs z < 1
.\]

Show that if $f$ has a singularity at $z=0$, then it must be removable.

:::

:::{.concept}
\envlist

- $\dd{}{z}$ is a left-shift on power series, $z^m$ is a right-shift.
- $f'$ has the same poles as $f$, possibly with worse order due to the left-shift.
  - In general, if $z_0$ is an order $\ell$ pole of $f$, then it is at least an order $\ell + m$ pole of $f^{(m)}$.

:::

:::{.solution}
Define $F(z) \da z^k f^{(k)}(z)$ and note that $\abs{F(z)} \leq M$ on $\DD\smz$.

If $f$ has an essential singularity at $z=0$, then so does $F$ by considering power series expansions:
\[
f(z) = \sum_{k\in \ZZ} c_k z^k 
\implies z^m f^{(m)}(z) = \sum_{k\leq 1} \tilde c_k z^{-k} + \sum_{k\geq m}\tilde c_{k}z^{k}
,\]
which will still have infinitely many terms in its principal part at $0$.
However, if $F$ had an essential singularity, the image of $F$ in a neighborhood of $0$ would be dense in $\CC$ by Casorati-Weierstrass, contradicting that its image is bounded (by $M$). 

Suppose instead $z=0$ is a pole of order $\ell$ of $f$, so $\abs{f(z)}\to \infty$ as $z\to 0$.
Then again by considering power series expansions, $z=0$ remains a pole of $F$, now of order at worst $\ell$:
\[
f(z) = \bigo(z^{\ell}) 
\implies z^m f^{(m)}(z) \approx z^m \cdot \bigo(z^{\ell - m}) = \bigo(z^\ell)
.\]
But if this is an order $\ell$ pole of $F$, then $\lim_{z\to 0} \abs{F(z)} = \infty$ and $\lim_{z\to 0} z^\ell F(z))$ is finite and nonzero.
Apply the assumed bound yields the last contradiction:
\[
z^{\ell}F(z) = z^{\ell + m}f(z) \leq z^{\ell + m} \cdot Mz^{-m} = z^{\ell} \convergesto{z\to 0} 0
.\]
$\contradiction$

:::

