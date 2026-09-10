---
schema: qual/card@1
id: E-CT4NT
kind: problem
title: Arzela's theorem over sigma-compact Hausdorff domains
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem (Arzela's theorem, general version).
Let $X$ be a Hausdorff space that is $\sigma$-compact; let $f_n$ be a sequence of functions $f_n: X \to \mathbb{R}^k$.
If the collection $(f_n)$ is pointwise bounded and equicontinuous, then the sequence $f_n$ has a subsequence that converges, in the topology of compact convergence, to a continuous function.

[Hint: Show that $\mathcal{C}(X, \mathbb{R}^k)$ is first-countable.]
:::

::: {.solution}
Choose compact sets $A_1\subset A_2\subset\cdots$ whose interiors cover the $\sigma$-compact Hausdorff space $X$. On $C(X,\mathbb R^k)$ the compact-convergence topology is metrizable, for example by
\[
\rho(f,g)=\sum_{j\ge1}2^{-j}\min\{1,\sup_{A_j}|f-g|\},
\]
so it is first-countable.

For each compact $A_j$, the restricted family $\{f_n|_{A_j}\}$ is pointwise bounded and equicontinuous. By Ascoli on the compact domain $A_j$, its closure in the uniform topology is compact; hence every sequence has a uniformly convergent subsequence on $A_j$. Starting with the original sequence, choose successively subsequences converging uniformly on $A_1,A_2,\dots$. The diagonal subsequence converges uniformly on every $A_j$, hence on every compact subset of $X$, to a function $f$. By the preceding equicontinuous pointwise-limit argument, $f$ is continuous. Thus the diagonal subsequence converges to $f$ in compact convergence.
:::
