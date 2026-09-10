---
schema: qual/card@1
id: E-Y3MSR
kind: problem
title: Compact closures in the topology of compact convergence
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

Theorem.
If $X$ is a locally compact Hausdorff space, then a subspace $\mathcal{F}$ of $\mathcal{C}(X, \mathbb{R}^n)$ in the topology of compact convergence has compact closure if and only if $\mathcal{F}$ is pointwise bounded and equicontinuous under either of the standard metrics on $\mathbb{R}^n$.
:::

::: {.solution}
Suppose first that $\overline{\mathcal F}$ is compact in compact convergence. Evaluation at each $x$ is continuous, so $\{f(x):f\in\mathcal F\}$ has compact, hence bounded, closure. Thus $\mathcal F$ is pointwise bounded. If equicontinuity failed at $x$, there would be an $\varepsilon>0$, a net (or sequence after using compactness in the function space locally) $f_i\in\mathcal F$, and $x_i\to x$ with $|f_i(x_i)-f_i(x)|\ge\varepsilon$. Compactness gives a subnet $f_i\to f$ uniformly on a compact neighborhood of $x$ (local compactness lets us choose one containing eventually all $x_i$), contradicting continuity of $f$. Hence $\mathcal F$ is equicontinuous.

Conversely assume pointwise boundedness and equicontinuity. Embed $C(X,\mathbb R^n)$ by restriction into the product
\[
\prod_{K} C(K,\mathbb R^n),
\]
where $K$ ranges over compact subsets and each factor has the uniform topology. For each $K$, Ascoli says the restricted family has compact closure. Hence the closure of the image of $\mathcal F$ lies in a product of compact spaces, so is compact by Tychonoff. The compatibility conditions on overlaps are closed, and the compatible families are exactly restrictions of continuous functions (local compactness is more than enough for this gluing). Thus $\overline{\mathcal F}$ is compact in compact convergence.

The two standard metrics on $\mathbb R^n$ are uniformly equivalent, so pointwise boundedness and equicontinuity are unchanged by choosing either one.
:::
