---
schema: qual/card@1
id: P-HLKLH
kind: problem
title: A holomorphic function with $\abs{f}=1$ on the unit circle, or $\abs{f}\geq 1$ with an interior point of modulus less than $1$, covers the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
  - Rouché
  - Zeros
relations: []
review: draft
---

::: {.problem}
Let $f$ be non-constant and holomorphic in an open set containing the closed unit disc.

(a) Show that if $\abs{f(z)} = 1$ whenever $\abs{z} = 1$, then the image of $f$ contains the unit disc.

> Hint: Show that $f(z) = w_0$ has a root for every $w_0 \in \DD$, for which it suffices to show that $f(z) = 0$ has a root.
> Conclude using the maximum modulus principle.

(b) If $\abs{f(z)} \geq 1$ whenever $\abs{z} = 1$ and there exists a $z_0\in \DD$ such that $\abs{f(z_0)} < 1$, then the image of $f$ contains the unit disc.
:::

::: {.solution}
For (a), first show that $f$ has a zero in $\DD$. If it did not, then
$1/f$ would be holomorphic in a neighborhood of $\overline{\DD}$ and
$\abs{1/f}=1$ on $\partial\DD$. The maximum-modulus principle applied to
$f$ and $1/f$ would give both $\abs{f}\le1$ and $\abs{f}\ge1$ in $\DD$; hence
$\abs{f}\equiv1$, forcing $f$ to be constant, contrary to hypothesis.

Now fix $w\in\DD$. On $\abs{z}=1$,
$$
\abs{w}<1=\abs{f(z)}.
$$
Rouché's theorem shows that $f-w$ and $f$ have the same number of zeros in
$\DD$. Since $f$ has at least one zero, so does $f-w$. Thus every
$w\in\DD$ lies in $f(\DD)$.

For (b), if $f$ had no zero in $\DD$, then $1/f$ would be holomorphic
there and satisfy $\abs{1/f}\le1$ on the boundary. The maximum principle would
give $\abs{f}\ge1$ throughout $\DD$, contradicting the given point $z_0$.
Hence $f$ has a zero. For any $\abs{w}<1$ we have on the boundary
$$
\abs{w}<1\le\abs{f(z)},
$$
so Rouché again implies that $f-w$ has a zero. Therefore
$$
\boxed{\DD\subset f(\DD)}
$$
in both cases.
:::
