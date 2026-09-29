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

1. Define a representation and an irreducible representation of $G$.
2. Prove that every finite-dimensional complex representation of $G$ is a direct sum of irreducible representations.
3. Construct a $G$-invariant Hermitian inner product.
:::


::: {.solution}

::: pf

::: pf-step
A representation of $G$ is a homomorphism
\[
\rho:G\to\operatorname{GL}(V)
\]
for a finite-dimensional complex vector space $V$. It is irreducible if its only $G$-stable subspaces are $0$ and $V$.

::: pf-proof
A subspace $W\subseteq V$ is $G$-stable when $\rho(g)W\subseteq W$ for every $g\in G$.
:::

:::

::: pf-step
Every representation admits a $G$-invariant positive-definite Hermitian inner product.

::: pf-proof
Start with any positive-definite Hermitian inner product $\langle-,-\rangle_0$ on $V$ and average it over $G$:
\[
\langle v,w\rangle_G
=
\frac1{|G|}\sum_{g\in G}
\langle\rho(g)v,\rho(g)w\rangle_0.
\]
This remains Hermitian and positive definite. For $h\in G$,
\[
\langle\rho(h)v,\rho(h)w\rangle_G
=
\frac1{|G|}\sum_{g\in G}
\langle\rho(gh)v,\rho(gh)w\rangle_0
=
\langle v,w\rangle_G,
\]
because $g\mapsto gh$ permutes $G$.
:::

:::

::: {.pf-step #s3}
If $W\subseteq V$ is $G$-stable, then its orthogonal complement $W^\perp$ is also $G$-stable.

::: pf-proof
For $v\in W^\perp$, $w\in W$, and $g\in G$, invariance of the inner product gives
\[
\langle\rho(g)v,w\rangle_G
=
\langle v,\rho(g^{-1})w\rangle_G=0,
\]
since $\rho(g^{-1})w\in W$. Hence $\rho(g)v\in W^\perp$.
:::

:::

::: {.pf-step #s4}
Every finite-dimensional complex representation of $G$ is completely reducible.

::: pf-proof
Induct on $\dim V$. If $V$ is irreducible, there is nothing to prove. Otherwise choose a nonzero proper invariant subspace $W$. By step [](#s3){.pf-ref},
\[
V=W\oplus W^\perp
\]
as $G$-representations. Apply induction to the two lower-dimensional summands.

Step [](#s4){.pf-ref} is Maschke's theorem over $\CC$.
:::

:::

:::

:::
