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
(a) Let $f(x)$ be an irreducible polynomial of degree 4 in $\QQ[x]$ whose splitting field $K$ over $\QQ$ has Galois group $G = \operatorname{Gal}(K/\QQ) \cong S_4$. Let $\theta$ be a root of $f(x)$. Prove that $\QQ(\theta)$ is an extension of $\QQ$ of degree 4 and that there are no intermediate fields strictly between $\QQ$ and $\QQ(\theta)$.

(b) Prove that if $K$ is a Galois extension of $\QQ$ of degree 4, then there is an intermediate subfield strictly between $K$ and $\QQ$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The extension $\QQ(\theta)/\QQ$ has degree four.

::: pf-proof

The irreducible polynomial $f$ of degree four is the minimal polynomial of $\theta$ up to a nonzero scalar, so $[\QQ(\theta):\QQ]=4$.

:::

:::

::: {.pf-step #s2}

The subgroup fixing $\theta$ is maximal in $\operatorname{Gal}(K/\QQ)$.

::: pf-proof

The faithful action on the four roots identifies $G$ with $S_4$. The subgroup $H=\operatorname{Gal}(K/\QQ(\theta))$ is the stabilizer of one root, hence isomorphic to $S_3$ and has index four. If $H<M<G$, the index $[G:M]$ is a proper divisor of four exceeding one, hence equals two. Every index-two subgroup is the kernel of a surjective homomorphism $S_4\to C_2$. All transpositions are conjugate and generate $S_4$, so every such homomorphism sends every transposition to the nonidentity element. Its kernel is therefore $A_4$, the unique index-two subgroup. But $H$ contains transpositions, so $H$ is not contained in $A_4$, a contradiction. Thus $H$ is maximal.

:::

:::

::: {.pf-step #s3}

There is no field strictly between $\QQ$ and $\QQ(\theta)$.

::: pf-proof

The Galois correspondence for $K/\QQ$ identifies the intermediate fields of $\QQ(\theta)/\QQ$ with subgroups $M$ satisfying $H\leq M\leq G$. By step [](#s2){.pf-ref}, only $H$ and $G$ occur, corresponding to $\QQ(\theta)$ and $\QQ$.

:::

:::

::: {.pf-step #s4}

Every Galois extension of $\QQ$ of degree four admits a proper nontrivial intermediate field.

::: pf-proof

Let $L/\QQ$ be Galois with $\cardinality{\operatorname{Gal}(L/\QQ)}=4$. By Cauchy's theorem, its Galois group contains a subgroup $J$ of order two. The fixed field $L^J$ has degree two over $\QQ$ and degree two below $L$ by the Galois correspondence, so $\QQ\subsetneq L^J\subsetneq L$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s3){.pf-ref} prove part (a), and step [](#s4){.pf-ref} proves part (b).

:::

:::

:::
