---
schema: qual/card@1
id: P-APAF04D
kind: problem
title: Twisting irreducible characters by a linear character; pointwise similarity of representations
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: problem
(a) Prove that if $G$ is finite group and $\lambda(x)$ is a linear character of $G$, then for any irreducible character $\chi$ of $G$, the function $\chi^*$ defined by $\chi^*(\sigma)=\lambda(\sigma)\chi(\sigma)$ for all $\sigma\in G$ is also an irreducible character of $G$.

(b) Let $A:G\to GL_n(\mathbb{C})$ and $B:G\to GL_n(\mathbb{C})$ be two representations of a finite group $G$.
Show that if for all $\sigma\in G$, there exists a matrix $P(\sigma)$ such that
\[
\bigl(P(\sigma)\bigr)^{-1}A(\sigma)P(\sigma)=B(\sigma),
\]
then there exist a nonsingular matrix $T$ such that for all $\sigma$,
\[
T^{-1}A(\sigma)T=B(\sigma).
\]
:::
