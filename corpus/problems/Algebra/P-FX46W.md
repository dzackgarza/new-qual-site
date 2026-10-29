---
schema: qual/card@1
id: P-FX46W
kind: problem
title: 'Representations of finite groups: irreducibles, complete reducibility, and
  invariant inner products'
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Inner Product Spaces
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
Let $G$ be a finite group and work with finite-dimensional complex representations.

(a) Define a representation and an irreducible representation of $G$.

(b) Prove that every finite-dimensional complex representation of $G$ is a direct sum of irreducible representations.

(c) Construct a $G$-invariant Hermitian inner product.
:::

::: {.solution}

::: pf

::: pf-step

(a) A representation of $G$ is a homomorphism $\rho:G\to\GL(V)$ for a finite-dimensional complex vector space $V$. It is irreducible if $V\neq0$ and its only $G$-stable subspaces are $0$ and $V$.

::: pf-proof

A subspace $W\subseteq V$ is $G$-stable when $\rho(g)W\subseteq W$ for every $g\in G$.

:::

:::

::: {.pf-step #invariant-product}

(c) Every representation admits a $G$-invariant positive-definite Hermitian inner product.

::: pf-proof

Start with any positive-definite Hermitian inner product $\inner{-}{-}_0$ on $V$ and average it over $G$:
$$
\inner{v}{w}_G
=
\frac1{\abs{G}}\sum_{g\in G}
\inner{\rho(g)v}{\rho(g)w}_0.
$$
This remains Hermitian and positive definite. For $h\in G$,
$$
\inner{\rho(h)v}{\rho(h)w}_G
=
\frac1{\abs{G}}\sum_{g\in G}
\inner{\rho(gh)v}{\rho(gh)w}_0
=
\inner{v}{w}_G,
$$
because $g\mapsto gh$ permutes $G$.

:::

:::

::: {.pf-step #complement}

If $W\subseteq V$ is $G$-stable, then its orthogonal complement $W^\perp$ with respect to $\inner{-}{-}_G$ is also $G$-stable.

::: pf-proof

For $v\in W^\perp$, $w\in W$, and $g\in G$, step [](#invariant-product){.pf-ref} gives
$$
\inner{\rho(g)v}{w}_G
=
\inner{v}{\rho(g^{-1})w}_G=0,
$$
since $\rho(g^{-1})w\in W$. Hence $\rho(g)v\in W^\perp$.

:::

:::

::: pf-step

(b) Every finite-dimensional complex representation of $G$ is a direct sum of irreducible representations.

::: pf-proof

This is Maschke's theorem over $\CC$. Induct on $\dim V$. The zero representation is the empty direct sum, and an irreducible $V$ is its own decomposition. Otherwise choose a nonzero proper $G$-stable subspace $W$. By step [](#complement){.pf-ref},
$$
V=W\oplus W^\perp
$$
as $G$-representations. Apply induction to the two lower-dimensional summands.

:::

:::

:::

:::
