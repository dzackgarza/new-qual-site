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

::: problem
How many automorphisms does the abstract field $\CC$ have?
How can an automorphism of a subfield, for example $\sqrt2\mapsto-\sqrt2$ on $\QQ(\sqrt2)$, be extended to an automorphism of $\CC$?
:::

::: {.solution}
As an abstract field,
\[
|\Aut(\CC)|=2^{2^{\aleph_0}}.
\]
These automorphisms are generally wildly discontinuous; the only continuous field automorphisms are the identity and complex conjugation.

<1>1. Any automorphism of a subfield $F\subseteq\CC$ extends to an automorphism of $\CC$.
::: {.proof}
Let $\sigma:F\to F$ be a field automorphism. Choose a transcendence basis $B$ of $\CC/F$. Extend $\sigma$ to an automorphism of the purely transcendental field $F(B)$ by fixing every element of $B$.

By definition of transcendence basis, $\CC$ is algebraic over $F(B)$; since $\CC$ is algebraically closed, the standard extension theorem for embeddings into algebraically closed fields extends this automorphism of $F(B)$ to an automorphism of $\CC$.

In particular, the nontrivial automorphism of $\QQ(\sqrt2)$ given by $\sqrt2\mapsto-\sqrt2$ extends to an automorphism of $\CC$.
:::

<1>2. There are at least $2^{2^{\aleph_0}}$ automorphisms.
::: {.proof}
Let $B$ be a transcendence basis of $\CC/\QQ$. Since $|\CC|=2^{\aleph_0}$ and $\overline\QQ$ is countable, one has
\[
|B|=2^{\aleph_0}.
\]
Every permutation of $B$ extends to an automorphism of $\QQ(B)$ and then, by <1>1, to an automorphism of $\CC$. The number of permutations of a set of cardinality $\mathfrak c=2^{\aleph_0}$ is
\[
2^{\mathfrak c}=2^{2^{\aleph_0}}.
\]
:::

<1>3. There are at most $2^{2^{\aleph_0}}$ automorphisms.
::: {.proof}
Every automorphism is a function $\CC\to\CC$. Hence
\[
|\Aut(\CC)|\le |\CC|^{|\CC|}
=\mathfrak c^{\mathfrak c}
=2^{\mathfrak c}.
\]
Combining with <1>2 gives equality.
:::
:::
