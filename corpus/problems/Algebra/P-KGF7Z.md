---
schema: qual/card@1
id: P-KGF7Z
kind: problem
title: Automorphisms of $\CC$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Fields
  - Transcendence
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
How many automorphisms does the abstract field $\CC$ have?
How can an automorphism of a subfield, for example $\sqrt2\mapsto-\sqrt2$ on $\QQ(\sqrt2)$, be extended to an automorphism of $\CC$?
:::

::: {.solution}
Write $\mathfrak c=2^{\aleph_0}=\abs{\CC}$.

::: pf

::: {.pf-step #extend}

Every automorphism of a subfield $F\subseteq\CC$ extends to an automorphism of $\CC$. In particular, $\sqrt2\mapsto-\sqrt2$ on $\QQ(\sqrt2)$ extends to $\CC$.

::: pf-proof

Let $\sigma$ be an automorphism of $F$, and choose a transcendence basis $B$ of $\CC/F$. Extend $\sigma$ to an automorphism of the purely transcendental field $F(B)$ fixing every element of $B$. Since $\CC$ is algebraically closed and algebraic over $F(B)$, it is an algebraic closure of $F(B)$, so this automorphism extends to an embedding $\tau:\CC\to\CC$. The image $\tau(\CC)$ is algebraically closed and contains $F(B)$, over which $\CC$ is algebraic, so $\tau(\CC)=\CC$.

:::

:::

::: {.pf-step #lower}

$\abs{\Aut(\CC)}\ge2^{\mathfrak c}$.

::: pf-proof

Let $B$ be a transcendence basis of $\CC/\QQ$. Since $\CC$ is algebraic over $\QQ(B)$, $\abs{\CC}=\max(\abs{B},\aleph_0)$, so $\abs{B}=\mathfrak c$. Every permutation of $B$ induces an automorphism of $\QQ(B)$, which extends to $\CC$ by step [](#extend){.pf-ref}. Distinct permutations give distinct automorphisms, and a set of cardinality $\mathfrak c$ has $2^{\mathfrak c}$ permutations.

:::

:::

::: pf-step

$\abs{\Aut(\CC)}=\boxed{2^{2^{\aleph_0}}}$.

::: pf-proof

Every automorphism is a function $\CC\to\CC$, so $\abs{\Aut(\CC)}\le\mathfrak c^{\mathfrak c}=2^{\mathfrak c}$. Combine with step [](#lower){.pf-ref}.

:::

:::

:::

:::

::: {.remark}
The only automorphisms of $\CC$ that are continuous in the Euclidean topology are the identity and complex conjugation; all others are discontinuous.
:::
