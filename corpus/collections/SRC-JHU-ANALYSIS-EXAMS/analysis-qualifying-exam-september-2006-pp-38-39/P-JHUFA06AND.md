---
schema: qual/card@1
id: P-JHUFA06AND
kind: problem
title: "Maximal derivative of a disk map into the upper half plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the disk, upper-half-plane target and value 3i with September 2006 problem 4 and its unit-disk convention; restored the missing map arrow."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the Cayley normalization and derivative factor, and proved that every displayed extremizer maps into the open upper half-plane and attains the maximum."
---

Let $D=\{z\in\mathbb C:|z|<1\}$ and $H=\{w\in\mathbb C:\operatorname{Im}w>0\}$. Let $f:D\to H$ be holomorphic.

Suppose that $f ( 0 ) = 3 i$ . Find the maximal possible value of $\left| f ^ { \prime } ( 0 ) \right|$

::: solution
The maximum is $\boxed{6}$.

<1>1. Schwarz's lemma gives $|f'(0)|\leq6$.
::: proof
Define
$$
g(z)=\frac{f(z)-3i}{f(z)+3i}.
$$
The denominator is nonzero since $f(z)\in H$. For every
$w\in H$, the identity
$$
|w+3i|^2-|w-3i|^2=12\operatorname{Im}w>0
$$
shows that the same fractional transformation has modulus
less than one. Thus $g:D\to D$ is holomorphic and $g(0)=0$.
Differentiation at zero yields
$$
g'(0)=\frac{6i}{(f(0)+3i)^2}f'(0)=\frac{f'(0)}{6i}.
$$
Schwarz's lemma gives $|g'(0)|\leq1$, hence the asserted
bound [@SS03].
:::

<1>2. Explicit maps attain the bound.
::: proof
For $|\lambda|=1$, set
$$
f_\lambda(z)=3i\frac{1+\lambda z}{1-\lambda z}.
$$
Its denominator has no zero in $D$, and direct computation gives
$$
\operatorname{Im}f_\lambda(z)
=3\frac{1-|z|^2}{|1-\lambda z|^2}>0.
$$
Hence $f_\lambda:D\to H$ is holomorphic, with
$f_\lambda(0)=3i$ and $f_\lambda'(0)=6i\lambda$.
Its derivative has modulus six, so the upper bound is a
maximum. Moreover, equality in step <1>1 forces
$g(z)=\lambda z$ by the equality case of Schwarz's lemma
[@SS03]; inversion gives precisely the displayed maps.
:::
:::
