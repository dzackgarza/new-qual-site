---
schema: qual/card@1
id: E-SS5.EX-8
kind: problem
title: 'SS 5.8: $\prod_{k=1}^\infty\cos(z/2^k)=\sin z/z$'
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
8. Prove that for every z the product below converges, and

$$
\cos (z / 2) \cos (z / 4) \cos (z / 8) \dots = \prod_ {k = 1} ^ {\infty} \cos (z / 2 ^ {k}) = \frac {\sin z}{z}.
$$

[Hint: Use the fact that sin $2 z = 2 \sin z \cos z . ]$
:::

::: {.solution}
Iterating the double-angle identity
\[
\sin(2w)=2\sin w\cos w
\]
gives, for every positive integer $N$,
\[
\sin z
=2^N\sin\!\left(\frac{z}{2^N}\right)
\prod_{k=1}^N\cos\!\left(\frac{z}{2^k}\right).
\]
Hence, for $z\ne0$,
\[
\prod_{k=1}^N\cos\!\left(\frac{z}{2^k}\right)
=\frac{\sin z/z}{\sin(z/2^N)/(z/2^N)}.
\]
As $N\to\infty$,
\[
\frac{\sin(z/2^N)}{z/2^N}\longrightarrow1.
\]
Therefore
\[
\prod_{k=1}^{\infty}\cos\!\left(\frac{z}{2^k}\right)
=\frac{\sin z}{z}
\]
for $z\ne0$. At $z=0$, every factor equals $1$ and the right side is understood by its removable value $1$. Thus the identity holds for every $z\in\mathbb C$.
:::
