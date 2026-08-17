---
schema: qual/card@1
id: E-4CL6A
kind: exercise
title: Complete totally bounded subsets of a metric space are compact
classification:
  areas:
  - real-analysis
  topics:
  - compactness
  - completeness
  - metric-spaces
relations: []
review: draft
solved: true
---

::: exercise
- Show that if a subset of a metric space is complete and totally bounded, then it is compact.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

In a metric space, compactness is equivalent to sequential compactness.
We will show that every sequence in a complete, totally bounded metric space $(X, d)$ has a convergent subsequence.

Let $(x_n)_{n=1}^\infty$ be an arbitrary sequence in $X$.

1. **Constructing nested subsequences by total boundedness:**

   - For $\varepsilon = 1$: Since $X$ is totally bounded, $X$ can be covered by finitely many balls of radius $1$.
     By the Pigeonhole Principle, at least one of these balls contains infinitely many terms of $(x_n)$.
     Let $B(y_1, 1)$ be such a ball, and let $(x_{1, k})_{k=1}^\infty$ be a subsequence of $(x_n)$ entirely contained in $B(y_1, 1)$.

   - For $\varepsilon = 1/2$: The ball $B(y_1, 1)$ (or $X$) is covered by finitely many balls of radius $1/2$.
     At least one ball $B(y_2, 1/2)$ contains infinitely many terms of the subsequence $(x_{1, k})$.
     Let $(x_{2, k})_{k=1}^\infty$ be a subsequence of $(x_{1, k})$ contained in $B(y_2, 1/2)$.

   - Inductively, for each $m \geq 1$: Having chosen the subsequence $(x_{m-1, k})$, covered by finitely many balls of radius $1/m$, we extract a subsequence $(x_{m, k})_{k=1}^\infty$ of $(x_{m-1, k})$ that is entirely contained in some ball $B(y_m, 1/m)$.

2. **Diagonal subsequence:** Consider the diagonal sequence $(z_j)_{j=1}^\infty$ defined by $z_j = x_{j, j}$.

   - For each $m \geq 1$, the tail $(z_j)_{j=m}^\infty$ is a subsequence of $(x_{m, k})_{k=1}^\infty$, so for all $j \geq m$, $z_j \in B(y_m, 1/m)$.

   - Therefore, for any $j, \ell \geq m$:
     $$
     d(z_j, z_\ell) \leq d(z_j, y_m) + d(y_m, z_\ell) < \frac{1}{m} + \frac{1}{m} = \frac{2}{m}.
     $$

3. **Cauchy sequence and convergence:** Given any $\varepsilon > 0$, choose $m \in \mathbb{N}$ such that $\frac{2}{m} < \varepsilon$.
   Then for all $j, \ell \geq m$, $d(z_j, z_\ell) < \varepsilon$.
   Thus $(z_j)_{j=1}^\infty$ is a Cauchy sequence in $X$.

   Since $X$ is **complete**, the Cauchy sequence $(z_j)$ converges to some limit point $x^* \in X$.

4. **Conclusion:** $(z_j)$ is a subsequence of the original sequence $(x_n)$ that converges in $X$.
   Thus, every sequence in $X$ has a convergent subsequence, which proves that $X$ is sequentially compact, and therefore compact.
:::
