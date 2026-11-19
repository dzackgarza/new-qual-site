---
schema: qual/card@1
id: T-PIO2B
kind: theorem
title: Maschke's theorem
slogan: 'If $\ch(k)\nmid\abs G$, every finite-dimensional $k[G]$-module splits into simple summands.'
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Characteristic
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a finite group and $k$ a field with $\ch(k)\nmid \abs G$.
Then every finite-dimensional representation of $G$ over $k$ is a direct sum of irreducible representations.
:::

::: {.proof}
For a subrepresentation $W\subseteq V$, choose any $k$-linear projection $\pi\colon V\to W$ and average it over the group:
$$
\pi_G \coloneqq {1\over \abs G}\sum_{g\in G} g\,\pi\,g^{-1}.
$$
The coefficient $\abs G$ is invertible in $k$ by the hypothesis on the characteristic.
For $h\in G$ the substitution $g\mapsto hg$ in the sum gives $h\pi_G h^{-1} = \pi_G$, so $\pi_G$ is $G$-equivariant.
Each $g\pi g^{-1}$ maps $V$ into $W$ and fixes $W$ pointwise, because $W$ is $G$-stable, so the same holds for $\pi_G$: it is a $G$-equivariant projection onto $W$, and its kernel is a $G$-stable complement.
Splitting off one irreducible summand at a time and inducting on $\dim V$ decomposes $V$ into irreducibles.
:::
