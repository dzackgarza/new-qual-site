---
schema: qual/card@1
id: P-IKJXT
kind: problem
title: $\QQ[\theta]$ for an $S_4$-quartic has no intermediate fields, unlike Galois
  extensions of degree $4$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Permutations
relations: []
review: draft
---

::: {.problem}
(a) Let $f(x)$ be an irreducible polynomial of degree 4 in $\mathbb{Q}[x]$ whose splitting field $K$ over $\mathbb{Q}$ has Galois group $G = \operatorname{Gal}(K/\mathbb{Q}) \cong S_4$. Let $\theta$ be a root of $f(x)$. Prove that $\mathbb{Q}(\theta)$ is an extension of $\mathbb{Q}$ of degree 4 and that there are no intermediate fields strictly between $\mathbb{Q}$ and $\mathbb{Q}(\theta)$.

(b) Prove that if $K$ is a Galois extension of $\mathbb{Q}$ of degree 4, then there is an intermediate subfield strictly between $K$ and $\mathbb{Q}$.
:::

::: {.solution}
<1>1. The extension $\mathbb Q(\theta)/\mathbb Q$ has degree four.

::: {.proof}
The irreducible polynomial $f$ of degree four is the minimal polynomial of $\theta$ up to a nonzero scalar, so $[\mathbb Q(\theta):\mathbb Q]=4$.
:::

<1>2. The subgroup fixing $\theta$ is maximal in $\operatorname{Gal}(K/\mathbb Q)$.

::: {.proof}
The faithful action on the four roots identifies $G$ with $S_4$. The subgroup $H=\operatorname{Gal}(K/\mathbb Q(\theta))$ is the stabilizer of one root, hence isomorphic to $S_3$ and has index four. If $H<M<G$, the index $[G:M]$ is a proper divisor of four exceeding one, hence equals two. Every index-two subgroup is the kernel of a surjective homomorphism $S_4\to C_2$. All transpositions are conjugate and generate $S_4$, so every such homomorphism sends every transposition to the nonidentity element. Its kernel is therefore $A_4$, the unique index-two subgroup. But $H$ contains transpositions, so $H$ is not contained in $A_4$, a contradiction. Thus $H$ is maximal.
:::

<1>3. There is no field strictly between $\mathbb Q$ and $\mathbb Q(\theta)$.

::: {.proof}
The Galois correspondence for $K/\mathbb Q$ identifies the intermediate fields of $\mathbb Q(\theta)/\mathbb Q$ with subgroups $M$ satisfying $H\leq M\leq G$. By step <1>2, only $H$ and $G$ occur, corresponding to $\mathbb Q(\theta)$ and $\mathbb Q$.
:::

<1>4. Every Galois extension of $\mathbb Q$ of degree four admits a proper nontrivial intermediate field.

::: {.proof}
Let $L/\mathbb Q$ be Galois with $|\operatorname{Gal}(L/\mathbb Q)|=4$. By Cauchy's theorem, its Galois group contains a subgroup $J$ of order two. The fixed field $L^J$ has degree two over $\mathbb Q$ and degree two below $L$ by the Galois correspondence, so $\mathbb Q\subsetneq L^J\subsetneq L$.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 and <1>3 prove part (a), and step <1>4 proves part (b).
:::
:::
