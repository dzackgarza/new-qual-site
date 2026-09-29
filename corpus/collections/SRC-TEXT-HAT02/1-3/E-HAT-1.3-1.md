---
schema: qual/card@1
id: E-HAT-1.3-1
kind: problem
title: Restriction of a covering space to a subspace
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Intersected an evenly covered neighborhood in X with the subspace A and checked the restricted sheets explicitly.
---

::: {.problem}
For a covering space $p: \tilde{X} \to X$ and a subspace $A \subset X$, let $\tilde{A} = p^{-1}(A)$.
Show that the restriction $p: \tilde{A} \to A$ is a covering space.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Fix $a\in A$ and choose an evenly covered open neighborhood $U\subseteq X$ of $a$ for the covering $p:\widetilde X\to X$.

::: pf-proof

Since $p$ is a covering map, there is an open set $U\ni a$ and pairwise disjoint open subsets $V_\lambda\subseteq\widetilde X$ such that
\[
p^{-1}(U)=\coprod_{\lambda\in\Lambda}V_\lambda
\]
and each restriction
\[
p|_{V_\lambda}:V_\lambda\longrightarrow U
\]
is a homeomorphism.

:::

:::

::: {.pf-step #s2}

The set
\[
U_A=U\cap A
\]
is an open neighborhood of $a$ in the subspace $A$.

::: pf-proof

This is the definition of the subspace topology.

:::

:::

::: {.pf-step #s3}

Its inverse image under the restricted map is
\[
p^{-1}(U_A)\cap\widetilde A
=
\coprod_{\lambda\in\Lambda}(V_\lambda\cap\widetilde A).
\]

::: pf-proof

By definition,
\[
\widetilde A=p^{-1}(A).
\]
Hence
\[
p^{-1}(U_A)
=p^{-1}(U\cap A)
=p^{-1}(U)\cap p^{-1}(A)
=\left(\coprod_\lambda V_\lambda\right)\cap\widetilde A.
\]
Intersecting preserves the disjointness of the sheets, giving the displayed decomposition.
Each $V_\lambda\cap\widetilde A$ is open in the subspace $\widetilde A$.

:::

:::

::: {.pf-step #s4}

For every $\lambda$, the restriction
\[
p:V_\lambda\cap\widetilde A\longrightarrow U_A
\]
is a homeomorphism.

::: pf-proof

The homeomorphism
\[
p|_{V_\lambda}:V_\lambda\to U
\]
restricts to a homeomorphism between the inverse image of $A\cap U$ and $A\cap U$.
But that inverse image is exactly
\[
V_\lambda\cap p^{-1}(A)=V_\lambda\cap\widetilde A.
\]

:::

:::

::: pf-step

Therefore every point of $A$ has an evenly covered neighborhood for
\[
p|_{\widetilde A}:\widetilde A\to A,
\]
so this restriction is a covering map.

::: pf-proof

The point $a$ in step [](#s1){.pf-ref} was arbitrary, and steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} verify the covering-space definition over $U_A$.

:::

:::

:::

:::
