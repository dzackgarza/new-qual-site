---
schema: qual/card@1
id: P-IWMWM
kind: problem
title: No retraction from $S^1\times S^1$ onto a subspace homeomorphic to $S^1\vee
  S^1$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Fundamental Group
  - Surfaces
relations: []
review: draft
---

::: {.problem}
Let $X = S^1 \cross S^1$ and $A\subset X$ be a subspace with $A \cong S^1 \vee S^1$.
Show that there is no retraction from $X$ to $A$.
:::

::: {.solution}
Suppose that $r\colon X \to A$ is a retraction, and let $\iota\colon A \to X$ be the inclusion, so that $r \circ \iota = \id_A$.
Fix a basepoint $a_0 \in A$; all fundamental groups below are based there.

::: pf

::: {.pf-step #injective}
$\iota_*\colon \pi_1(A) \to \pi_1(X)$ is injective.

::: pf-proof
By functoriality, $r_* \circ \iota_* = (r \circ \iota)_* = \id$.
:::

:::

::: {.pf-step #groups}
$\pi_1(A) \cong \ZZ * \ZZ$, which is nonabelian, and $\pi_1(X) \cong \ZZ \times \ZZ$, which is abelian.

::: pf-proof
By the Seifert–van Kampen theorem, $\pi_1(S^1 \vee S^1) \cong \ZZ * \ZZ$, free on generators $a$, $b$.
The commutator $aba^{-1}b^{-1}$ is a reduced word of length four, so it is nontrivial.
The fundamental group of a product is the product of the fundamental groups, so $\pi_1(S^1 \times S^1) \cong \ZZ \times \ZZ$.
:::

:::

::: pf-step
No retraction $X \to A$ exists.

::: pf-proof
The target of $\iota_*$ is abelian by step [](#groups){.pf-ref}, so $\iota_*(aba^{-1}b^{-1}) = \iota_*(a)\iota_*(b)\iota_*(a)^{-1}\iota_*(b)^{-1} = 1$.
The element $aba^{-1}b^{-1}$ is nontrivial by step [](#groups){.pf-ref}, so $\iota_*$ is not injective.
This contradicts step [](#injective){.pf-ref}.
:::

:::

:::
:::
