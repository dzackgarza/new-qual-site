---
schema: qual/card@1
id: P-APA23E
kind: problem
title: Reynolds operator with conjugate character on an irreducible complex $G$-module
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
  - Invariant Theory
relations: []
review: draft
---

::: problem
Let $G$ be a finite group and let $V$ be a finite-dimensional $G$-module over $\mathbb{C}$.
Let $\chi \colon G \to \mathbb{C}$ be the character of $V$ and consider the linear operator $\varphi \colon V \to V$ given by
\[
\varphi(v) := \sum_{g \in G} \overline{\chi}(g)\, (g \cdot v),
\]
where $\overline{\chi}(g)$ denotes the complex conjugate of $\chi(g)$.
Assume that $V$ is irreducible.

Prove that there exists a complex number $c \in \mathbb{C}$ such that $\varphi(v) = cv$ for all $v \in V$, and find the value of $c$.
:::
