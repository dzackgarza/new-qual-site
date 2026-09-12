---
schema: qual/card@1
id: P-V7BGS
kind: problem
title: Groups of prime order are cyclic
classification:
  areas:
  - algebra
  topics:
  - Cyclic Groups
  - Classification
  - Cosets and Lagrange
relations: []
review: draft
---

::: problem
Show that every group of prime order is cyclic.
:::

::: solution
Let $|G|=p$ with $p$ prime, and choose any nonidentity element $g\in G$.
By Lagrange's theorem,
\[
|g|\mid p.
\]
Since $g\ne e$, its order is not $1$, so
\[
|g|=p.
\]
Therefore
\[
|\langle g\rangle|=p=|G|,
\]
and hence
\[
G=\langle g\rangle.
\]
Thus $G$ is cyclic.
:::
