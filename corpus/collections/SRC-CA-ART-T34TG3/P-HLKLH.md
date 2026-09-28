---
schema: qual/card@1
id: P-HLKLH
kind: problem
title: A holomorphic function with $|f|=1$ on the unit circle, or $|f|\geq 1$ with
  an interior point of modulus less than $1$, covers the disc
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

a. Show that if $\abs{f(z)} = 1$ whenever $\abs{z} = 1$, then the image of $f$ contains the unit disc.

> Hint: Show that $f(z) = w_0$ has a root for every $w_0 \in \DD$, for which it suffices to show that $f(z) = 0$ has a root.
> Conclude using the maximum modulus principle.

b. If $\abs{f(z)} \geq 1$ whenever $\abs{z} = 1$ and there exists a $z_0\in \DD$ such that $\abs{f(z_0)} < 1$, then the image of $f$ contains the unit disc.
:::

::: {.solution}
For (a), first show that $f$ has a zero in $\mathbb D$. If it did not, then
$1/f$ would be holomorphic in a neighborhood of $\overline{\mathbb D}$ and
$|1/f|=1$ on $\partial\mathbb D$. The maximum-modulus principle applied to
$f$ and $1/f$ would give both $|f|\le1$ and $|f|\ge1$ in $\mathbb D$; hence
$|f|\equiv1$, forcing $f$ to be constant, contrary to hypothesis.

Now fix $w\in\mathbb D$. On $|z|=1$,
\[
|w|<1=|f(z)|.
\]
Rouché's theorem shows that $f-w$ and $f$ have the same number of zeros in
$\mathbb D$. Since $f$ has at least one zero, so does $f-w$. Thus every
$w\in\mathbb D$ lies in $f(\mathbb D)$.

For (b), if $f$ had no zero in $\mathbb D$, then $1/f$ would be holomorphic
there and satisfy $|1/f|\le1$ on the boundary. The maximum principle would
give $|f|\ge1$ throughout $\mathbb D$, contradicting the given point $z_0$.
Hence $f$ has a zero. For any $|w|<1$ we have on the boundary
\[
|w|<1\le|f(z)|,
\]
so Rouché again implies that $f-w$ has a zero. Therefore
\[
\boxed{\mathbb D\subset f(\mathbb D)}
\]
in both cases.
:::
