---
schema: qual/card@1
id: P-APA22G
kind: problem
title: Spectrum of the sum of all transpositions on the Specht module $S^{(4,2,1)}$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Symmetric Functions
relations: []
review: draft
---

::: {.problem}
Let $(S_{\lambda}, \rho_{\lambda})$ be the irreducible representation of the complex group algebra of the symmetric group $S_7$ corresponding to the partition $\lambda = (4, 2, 1)$.
Using Murphy's theorem (or otherwise), determine the spectrum of $\rho_{\lambda}(T)$, where $T$ is the sum of all transpositions.
:::


::: {.solution}
Let $T\coloneqq\sum_{1\le i<j\le7}(ij)\in\CC[S_7]$ and $\lambda=(4,2,1)$.

::: pf

::: {.pf-step #scalar}

$\rho_\lambda(T)=3I$.

::: pf-proof

$T=\sum_{k=2}^7X_k$, where $X_k\coloneqq\sum_{i<k}(ik)$ are the Jucys--Murphy elements. By Murphy's theorem, in the Young seminormal basis of $S_\lambda$ indexed by standard tableaux $t$, each $X_k$ acts diagonally with eigenvalue the content $j-i$ of the box $(i,j)$ of $t$ containing $k$. Summing over $k$, $T$ acts on each basis vector by the sum of the contents of all boxes of $\lambda$ other than the box $(1,1)$ holding $1$, whose content is $0$. For $\lambda=(4,2,1)$ this sum is $(0+1+2+3)+(-1+0)+(-2)=3$.

:::

:::

::: pf-step

The spectrum of $\rho_\lambda(T)$ is $\boxed{\{3\}}$, with multiplicity $\dim S_\lambda=35$.

::: pf-proof

By step [](#scalar){.pf-ref}, $3$ is the only eigenvalue. The hook lengths of $(4,2,1)$ are $6,4,2,1$; $3,1$; $1$, with product $144$, so the hook length formula gives $\dim S_\lambda=7!/144=35$.

:::

:::

:::
:::
