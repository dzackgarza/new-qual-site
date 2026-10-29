---
schema: qual/card@1
id: E-PER08-9.3
kind: problem
title: Mayer--Vietoris in degree one with connected intersection
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Prove or give a counterexample: given two path connected open sets $U$ and $V$ whose union is $X$ and whose intersection $U\cap V$ is path connected, there exists a short exact sequence of abelian groups
$$
0\longrightarrow H_1(U\cap V)\longrightarrow H_1(U)\oplus H_1(V)\longrightarrow H_1(X)\longrightarrow 0.
$$
:::

::: {.solution}
The statement is false.
Take $X = S^2$, and let $U$ and $V$ be open neighborhoods of the closed northern and southern hemispheres, each obtained by adding a thin open band around the equator.

::: pf

::: {.pf-step #spaces}
$U$ and $V$ are contractible and $U \cap V \simeq S^1$; all three are path connected.

::: pf-proof
Each of $U$ and $V$ is homeomorphic to an open disk.
The intersection $U \cap V$ is an open band around the equator, homeomorphic to $S^1 \times (-1, 1)$, which deformation retracts onto the equator.
:::

:::

::: pf-step
No short exact sequence $0 \to H_1(U \cap V) \to H_1(U) \oplus H_1(V) \to H_1(X) \to 0$ exists for this cover.

::: pf-proof
By step [](#spaces){.pf-ref}, $H_1(U \cap V) \cong \ZZ$ and $H_1(U) \oplus H_1(V) = 0$.
An injection $\ZZ \to 0$ does not exist.
In the Mayer–Vietoris sequence $H_2(X) \xrightarrow{\partial} H_1(U \cap V) \to H_1(U) \oplus H_1(V) \to H_1(X) \to \tilde H_0(U \cap V) = 0$, the map onto $H_1(X)$ is surjective, but the connecting map $\partial\colon H_2(S^2) \cong \ZZ \to H_1(U \cap V) \cong \ZZ$ is an isomorphism, so the left map is not injective.
:::

:::

:::
:::
