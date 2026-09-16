---
schema: qual/card@1
id: T-6CQEB
kind: theorem
title: Correspondence and third isomorphism theorems
classification:
  areas:
  - algebra
  topics:
  - Isomorphism Theorems
  - Normal Subgroups
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group and $N\normal G$ a normal subgroup.

(a) If $N\leq K\leq G$, then $K/N$ is a subgroup of $G/N$.

(b) For $N\leq K\leq G$, $K\normal G$ if and only if $K/N\normal G/N$.

(c) The map $K\mapsto K/N$ is a bijection from the subgroups $K$ of $G$ containing $N$ to the subgroups of $G/N$, and it restricts to a bijection between normal subgroups.

(d) If $N\leq K$ and $K\normal G$, then
$$
\frac{G/N}{K/N} \cong \frac{G}{K}.
$$
:::

::: {.proof}
Let $\pi\colon G\to G/N$ be the quotient map.
(a) $K/N=\pi(K)$ is the image of a subgroup.
(c) The inverse of $K\mapsto\pi(K)$ is $\bar K\mapsto\pi^{-1}(\bar K)$: $\pi^{-1}(\bar K)$ is a subgroup containing $N$, $\pi(\pi^{-1}(\bar K))=\bar K$ since $\pi$ is surjective, and $\pi^{-1}(\pi(K))=KN=K$ since $N\leq K$.
(b) Since $\pi(gKg^{-1})=\pi(g)\pi(K)\pi(g)^{-1}$ and $\pi$ is a bijection on subgroups containing $N$, $gKg^{-1}=K$ for all $g\in G$ if and only if $\bar g(K/N)\bar g^{-1}=K/N$ for all $\bar g\in G/N$; this also gives the second half of (c).
(d) The map $G/N\to G/K$, $gN\mapsto gK$, is well defined because $N\leq K$, and it is a surjective homomorphism with kernel $K/N$; apply the first isomorphism theorem.
:::
