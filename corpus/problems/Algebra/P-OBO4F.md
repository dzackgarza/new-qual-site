---
schema: qual/card@1
id: P-OBO4F
kind: problem
title: $g^{\lvert G\rvert}=e$ for every $g\in G$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Cyclic Groups
relations: []
review: draft
---

::: problem
Let $G$ be a finite group of order $n$. Prove that
\[
g^n=e
\]
for every $g\in G$.
:::

::: {.solution}
For any $g\in G$, the cyclic subgroup $\langle g\rangle$ has order $|g|$. By Lagrange's theorem,
\[
|g|\mid |G|=n.
\]
Write $n=k|g|$. Then
\[
g^n=g^{k|g|}=(g^{|g|})^k=e.
\]
Thus every element satisfies $g^{|G|}=e$.
:::
