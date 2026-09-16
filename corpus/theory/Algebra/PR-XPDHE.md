---
schema: qual/card@1
id: PR-XPDHE
kind: proposition
title: Galois group of an irreducible cubic
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Classification
  - Polynomials
relations: []
review: draft
---

::: {.proposition}
Let $k$ be a field with $\ch k\neq 2$, let $f\in k[x]$ be an irreducible separable cubic with [[D-W3DSO|discriminant]] $\Delta$, and let $G$ be the Galois group of $f$ over $k$, regarded as a subgroup of $S_3$ through its action on the roots of $f$.
Then $G\cong A_3\cong C_3$ if $\Delta$ is a square in $k$, and $G\cong S_3$ otherwise.
:::

::: {.proof}
Since $f$ is irreducible, $G$ acts [[D-7UIPO|transitively]] on the three roots, so $3\divides\abs G$ and $G$ is $A_3$ or $S_3$.
Let $\alpha_1,\alpha_2,\alpha_3$ be the roots and $\delta\coloneqq\prod_{i<j}(\alpha_i-\alpha_j)$, so $\delta^2=\Delta$ and $\delta\neq0$ because $f$ is separable.
Every $\sigma\in G$ satisfies $\sigma(\delta)=\operatorname{sgn}(\sigma)\,\delta$, and $\delta\neq-\delta$ because $\ch k\neq2$.
Hence $\delta$ is fixed by $G$, equivalently $\delta\in k$, if and only if $G\subseteq A_3$.
Since the square roots of $\Delta$ are $\pm\delta$, $\Delta$ is a square in $k$ if and only if $G=A_3$.
:::
