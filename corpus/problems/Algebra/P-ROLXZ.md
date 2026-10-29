---
schema: qual/card@1
id: P-ROLXZ
kind: problem
title: Kernels of irreducible representations and exactness of induction
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Exact Sequences
relations: []
review: draft
---

::: {.problem}
Let $H\le G$ and let representations be modules over a commutative coefficient ring $R$.

(a) What can be said about the kernel of an irreducible representation of $G$?

(b) What is the kernel of a direct sum of representations?

(c) Is induction $\operatorname{Ind}_H^G$ left exact, right exact, or exact?
:::

::: {.solution}
For a representation $\rho:G\to\Aut_R(V)$, let $\ker\rho\coloneqq\{g\in G:\rho(g)=1_V\}$.

::: pf

::: pf-step
(a) $\ker\rho$ is a normal subgroup of $G$, and an irreducible $\rho$ factors through a faithful irreducible representation of $G/\ker\rho$. If $R=\CC$ and $G$ is finite, then moreover $Z(G/\ker\rho)$ is cyclic.

::: pf-proof
$\ker\rho$ is the kernel of a homomorphism. The induced representation $\bar\rho$ of $G/\ker\rho$ on $V$ is faithful, and it has the same invariant subspaces as $\rho$, so it is irreducible. Over $\CC$, Schur's lemma makes each central element of $G/\ker\rho$ act by a scalar, so $\bar\rho$ embeds $Z(G/\ker\rho)$ in $\CC^\times$; a finite subgroup of $\CC^\times$ is cyclic.
:::

:::

::: pf-step
(b) $\ker\bigl(\bigoplus_i\rho_i\bigr)=\bigcap_i\ker\rho_i$.

::: pf-proof
An element acts trivially on the direct sum exactly when it acts trivially on every summand.
:::

:::

::: pf-step
(c) $\operatorname{Ind}_H^G(M)\coloneqq R[G]\otimes_{R[H]}M$ is $\boxed{\text{exact}}$, hence both left and right exact.

::: pf-proof
Choose representatives $g_i$ of the left cosets $G/H$. Then $R[G]=\bigoplus_i g_iR[H]$ is a free right $R[H]$-module, hence flat. Tensoring with a flat right module is an exact functor from left $R[H]$-modules to $R[G]$-modules.
:::

:::

:::
:::
