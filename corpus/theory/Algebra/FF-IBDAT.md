---
schema: qual/card@1
id: FF-IBDAT
kind: fact
title: Lying over and going up for integral extensions
prompts:
- What is the going up theorem?
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Prime Ideals
  - Commutative Algebra
relations: []
review: draft
---

::: {.fact}
Let $R\subseteq S$ be an [[D-DEFINTEG|integral extension]] of commutative rings.

(a) Lying over: for every [[D-5BM46|prime ideal]] $\mfp\subseteq R$ there is a prime ideal $\mathfrak q\subseteq S$ with $\mathfrak q\cap R=\mfp$.
Equivalently, the map $\Spec S\to\Spec R$, $\mathfrak q\mapsto\mathfrak q\cap R$, is surjective.

(b) Going up: if $\mfp_1\subseteq\mfp_2$ are prime ideals of $R$ and $\mathfrak q_1$ is a prime ideal of $S$ with $\mathfrak q_1\cap R=\mfp_1$, then there is a prime ideal $\mathfrak q_2\supseteq\mathfrak q_1$ of $S$ with $\mathfrak q_2\cap R=\mfp_2$.
:::
