---
schema: qual/card@1
id: E-HAT-4.G-2
kind: problem
title: Projection from $\Delta X$ is a fiber bundle
classification:
  areas:
  - topology
  topics:
  - CW Complexes
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that if $X$ is a complex of spaces in which all the maps are homeomorphisms, then the projection $\Delta X \to \Gamma$ is a fiber bundle.
:::

::: {.solution}

::: pf

::: pf-step

Structure of the total space $\Delta X$:

::: pf-proof

::: pf-step

A complex of spaces $X$ over a graph $\Gamma$ consists of a vertex space $X_v$ for each $v \in \Gamma$, an edge space $X_e$ for each edge $e \in \Gamma$, and attaching maps $f_{e, 0}: X_e \to X_{d_0(e)}$ and $f_{e, 1}: X_e \to X_{d_1(e)}$.
The realization $\Delta X$ is the quotient space:
\[
\Delta X = \left( \bigsqcup_{v \in \Gamma^{(0)}} X_v \sqcup \bigsqcup_{e \in \Gamma^{(1)}} (X_e \times [0, 1]) \right) \Big/ \sim,
\]
where $(x, 0) \sim f_{e, 0}(x)$ and $(x, 1) \sim f_{e, 1}(x)$ for all $x \in X_e$.

::: pf-proof

definition of the total space of a complex of spaces.

:::

:::

::: pf-step

The projection $p: \Delta X \to \Gamma$ maps $X_v \mapsto v$ and $(x, t) \in X_e \times [0, 1] \mapsto t \in e$.
Because all attaching maps $f_{e, i}$ are homeomorphisms and $\Gamma$ is connected, all vertex spaces $X_v$ and edge spaces $X_e$ are homeomorphic to a common fiber space $F$.

::: pf-proof

composition of homeomorphisms along paths in $\Gamma$.

:::

:::

:::

:::

::: {.pf-step #s2}

Local triviality over open edges:

::: pf-proof

::: pf-step

Let $e$ be an edge of $\Gamma$, and let $U_e = \operatorname{int}(e) \cong (0, 1)$ be the open interior of $e$.
The preimage is $p^{-1}(U_e) = X_e \times (0, 1)$.

::: pf-proof

interior of edge has no quotient identifications.

:::

:::

::: pf-step

Using the homeomorphism $\phi_e: X_e \xrightarrow{\sim} F$, we have a trivializing homeomorphism:
\[
p^{-1}(U_e) = X_e \times U_e \xrightarrow{\phi_e \times \operatorname{id}} F \times U_e,
\]
which satisfies $\operatorname{pr}_1 \circ (\phi_e \times \operatorname{id}) = p$.

::: pf-proof

direct Cartesian product.

:::

:::

:::

:::

::: {.pf-step #s3}

Local triviality over vertex neighborhoods:

::: pf-proof

::: pf-step

For each vertex $v \in \Gamma^{(0)}$, let $U_v \subset \Gamma$ be the open star of $v$, consisting of $v$ together with open half-edges $[0, 1/2)$ for all edges incident to $v$.

::: pf-proof

open star basis for 1-complexes.

:::

:::

::: pf-step

The preimage $p^{-1}(U_v)$ is the union of $X_v$ and $X_e \times [0, 1/2)$ for each incident edge $e$, glued via $(x, 0) \sim f_{e, v}(x)$.
Since each $f_{e, v}: X_e \xrightarrow{\sim} X_v$ is a homeomorphism, the map $(x, t) \mapsto (f_{e, v}(x), t)$ is a homeomorphism $X_e \times [0, 1/2) \xrightarrow{\sim} X_v \times [0, 1/2)$.

::: pf-proof

product of homeomorphisms.

:::

:::

::: pf-step

Under these maps, the gluing along $t = 0$ corresponds to the identity map on $X_v$.
Thus we obtain a canonical homeomorphism:
\[
\psi_v: p^{-1}(U_v) \xrightarrow{\sim} X_v \times U_v \cong F \times U_v,
\]
which commutes with the projection $p$.

::: pf-proof

gluing local product charts along the identity at the vertex.

:::

:::

:::

:::

::: pf-step

Conclusion:
Every point in $\Gamma$ has an open neighborhood $U$ with $p^{-1}(U) \cong F \times U$, so $p: \Delta X \to \Gamma$ is a fiber bundle with fiber $F$. Q.E.D.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
