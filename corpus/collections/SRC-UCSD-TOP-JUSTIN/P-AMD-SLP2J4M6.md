---
schema: qual/card@1
id: P-AMD-SLP2J4M6
kind: problem
title: Topological groups have abelian fundamental group
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Fundamental Group
  - Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: >-
    Sheet 2, Problem 11 first asks for abelianness of the fundamental
    group of a topological group, then asks for the Klein bottle
    deduction. The former appeared only in the solution. The
    nonabelianity proof also used an abelian quotient in error.
---

::: {.problem}
Prove that the fundamental group $\pi_1(G,e)$ of a topological group
$G$ is abelian, where $e$ is the identity. Deduce that the Klein
bottle $K$ cannot be a topological group.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The fundamental group of the Klein bottle $K$ is nonabelian:
$$
\pi_1(K)\cong\langle a,b\mid aba^{-1}=b^{-1}\rangle.
$$

::: pf-proof

This is the standard presentation obtained from the square model of
the Klein bottle. To see that it is nonabelian, map it to the
isometry group of $\RR$ by taking $a$ to the reflection $x\mapsto-x$
and $b$ to the translation $x\mapsto x+1$. These isometries satisfy
$aba^{-1}=b^{-1}$ but do not commute.

:::

:::

::: {.pf-step #s2}

The fundamental group of every topological group is abelian.

::: pf-proof

Let $G$ be a topological group with identity $e$. On based loops at $e$ there are two products: concatenation $*$ and pointwise multiplication
$$
(\alpha\cdot\beta)(t)=\alpha(t)\beta(t).
$$
They have the same unit and satisfy the interchange law
$$
(\alpha*\beta)\cdot(\gamma*\delta)
=(\alpha\cdot\gamma)*(\beta\cdot\delta).
$$
The Eckmann--Hilton argument therefore shows that the induced product on $\pi_1(G,e)$ is commutative.

:::

:::

::: pf-step

Hence the Klein bottle cannot admit a topological-group structure.

::: pf-proof

If $K$ were a topological group, step [](#s2){.pf-ref} would force $\pi_1(K)$ to be abelian, contradicting step [](#s1){.pf-ref}.

:::

:::

:::

:::
