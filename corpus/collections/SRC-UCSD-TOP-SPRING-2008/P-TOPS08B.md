---
schema: qual/card@1
id: P-TOPS08B
kind: problem
title: "Homology of a space as the colimit of homology of its compact subsets"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Colimits
  - Compactness
relations: []
review: draft
---

::: {.problem}
Given a topological space $X$, let $I$ denote the directed set of compact subsets of $X$ under inclusion.
Show that the following canonical map is an isomorphism:
$$
\operatorname{colim}_{K \in I} H_i(K; R) \longrightarrow H_i(X; R),
$$
for any ring $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every singular chain in $X$ is supported in a compact subset of $X$.

::: pf-proof

A singular chain is a finite $R$-linear combination of singular simplices. Each simplex has compact image because its domain is compact, and a finite union of compact subsets is compact.

:::

:::

::: {.pf-step #s2}

Hence every homology class of $X$ lies in the image of the canonical map
$$
\varinjlim_{K\subset X\text{ compact}}H_i(K;R)\longrightarrow H_i(X;R).
$$

::: pf-proof

Represent the class by a cycle $z$. By step [](#s1){.pf-ref}, $z$ is contained in some compact $K$, so it defines a class in $H_i(K;R)$ mapping to the given class.

:::

:::

::: {.pf-step #s3}

The canonical map is injective.

::: pf-proof

Suppose a class represented by $[z]\in H_i(K;R)$ maps to zero in $H_i(X;R)$. Then $z=\partial c$ for some singular $(i+1)$-chain $c$ in $X$. The support of $c$ is compact by step [](#s1){.pf-ref}. Let $L$ be the compact union of $K$ with the support of $c$. Then the image of $[z]$ in $H_i(L;R)$ is zero. This is precisely the equivalence relation defining the directed colimit, so the original colimit class is zero.

:::

:::

::: pf-step

Therefore
$$
\boxed{\varinjlim_{K\subset X\text{ compact}}H_i(K;R)\cong H_i(X;R).}
$$

::: pf-proof

Combine steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
