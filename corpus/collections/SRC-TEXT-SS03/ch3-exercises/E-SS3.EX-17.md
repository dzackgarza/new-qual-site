---
schema: qual/card@1
id: E-SS3.EX-17
kind: problem
title: Image of a non-constant holomorphic map containing the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
17. Let $f$ be non-constant and holomorphic in an open set containing the closed unit disc.

(a) Show that if $|f(z)| = 1$ whenever $|z| = 1$, then the image of $f$ contains the unit disc.
[Hint: One must show that $f(z) = w_0$ has a root for every $w_0 \in \mathbb{D}$. To do this, it suffices to show that $f(z) = 0$ has a root (why?). Use the maximum modulus principle to conclude.]

(b) If $|f(z)| \geq 1$ whenever $|z| = 1$ and there exists a point $z_0 \in \mathbb{D}$ such that $|f(z_0)| < 1$, then the image of $f$ contains the unit disc.
:::

::: solution
(a) First, $f$ must vanish somewhere in $\mathbb D$. Otherwise $1/f$ would be holomorphic on a neighborhood of the closed disc and satisfy $|1/f|=1$ on $|z|=1$. The maximum modulus principle applied to both $f$ and $1/f$ would give $|f|\le1$ and $|f|\ge1$ in $\mathbb D$, so $|f|\equiv1$ there; then $f$ would be constant, contrary to hypothesis.

Now fix $w_0\in\mathbb D$. On $|z|=1$,
\[
|w_0|<1=|f(z)|.
\]
By Rouché's theorem, $f$ and $f-w_0$ have the same number of zeros in $\mathbb D$. Since $f$ has at least one, so does $f-w_0$. Thus $w_0\in f(\mathbb D)$, and the image contains the unit disc.

(b) Choose $z_0\in\mathbb D$ with $|f(z_0)|<1$. If $f$ had no zero in $\mathbb D$, then $1/f$ would be holomorphic there and continuous on the closed disc. Since $|f|\ge1$ on the boundary, $|1/f|\le1$ there; the maximum modulus principle would give $|1/f|\le1$ throughout the disc, contradicting $|f(z_0)|<1$. Hence $f$ has a zero in $\mathbb D$.

For any $w_0\in\mathbb D$, on $|z|=1$ we have
\[
|w_0|<1\le|f(z)|.
\]
Rouché again shows that $f-w_0$ has as many zeros as $f$, hence at least one. Therefore $f(\mathbb D)$ contains $\mathbb D$.
:::
