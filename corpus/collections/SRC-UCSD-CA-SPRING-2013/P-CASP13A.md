---
schema: qual/card@1
id: P-CASP13A
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

::: {.problem}
Choose 4 of the following theorems, and write out their statements carefully and completely.
From among these, choose 2, and sketch their proofs.

- The Cauchy Estimates and Liouville's Theorem

- Rouché's Theorem

- Hurwitz's Theorem

- The Riemann Mapping Theorem

- Runge's Theorem

- The Open Mapping Theorem

- The Mittag-Leffler Theorem

- The Maximum Modulus Principle

- The Monodromy Theorem

- The Great Picard Theorem

- Carathéodory's Theorem

- The Poisson Integral Formula
:::

::: {.solution}
One possible choice is the following four theorems.

**Rouché's theorem.** Let $D$ be a bounded domain whose boundary is a finite
union of positively oriented simple closed curves, and let $f,g$ be holomorphic
on a neighborhood of $\overline D$. If
\[
|g(z)|<|f(z)|\qquad(z\in\partial D),
\]
then $f$ and $f+g$ have the same number of zeros in $D$, counted with
multiplicity.

**Hurwitz's theorem.** Let $G$ be a domain and let $f_n$ be holomorphic and
zero-free on $G$. If $f_n\to f$ uniformly on compact subsets of $G$, then
either $f$ is zero-free or $f\equiv0$. Equivalently, if $f$ is nonzero and
has a zero at $a$, then every sufficiently small disk about $a$ contains a
zero of $f_n$ for all sufficiently large $n$.

**Riemann mapping theorem.** Every nonempty simply connected proper domain
$G\subsetneq\mathbb C$ is conformally equivalent to the unit disk. If
$a\in G$, there is a unique conformal map $F:G\to\mathbb D$ satisfying
$F(a)=0$ and $F'(a)>0$.

**Open mapping theorem.** A nonconstant holomorphic function on a domain maps
open sets to open sets.

We sketch proofs of Rouché and the open mapping theorem.

For Rouché, on $\partial D$ the homotopy
\[
f_t=f+t g,
\qquad 0\le t\le1,
\]
never vanishes, since $|tg|<|f|$. Therefore the winding number of
$f_t(\partial D)$ about $0$ is independent of $t$. By the argument principle,
that winding number is the number of zeros of $f_t$ in $D$, counted with
multiplicity. Thus $f=f_0$ and $f+g=f_1$ have the same zero count.

For the open mapping theorem, fix $z_0\in G$ and write
\[
f(z)-f(z_0)=(z-z_0)^m h(z),
\]
where $m\ge1$ and $h(z_0)\ne0$. On a sufficiently small circle
$|z-z_0|=r$, the quantity $|f(z)-f(z_0)|$ has a positive minimum $\delta$.
If $|w-f(z_0)|<\delta$, then on that circle
\[
|w-f(z_0)|<|f(z)-f(z_0)|.
\]
Rouché's theorem implies that
$f(z)-w$ and $f(z)-f(z_0)$ have the same number $m$ of zeros inside the
circle. Hence every $w$ near $f(z_0)$ lies in the image of $f$, proving that
$f(G)$ is open.
:::
