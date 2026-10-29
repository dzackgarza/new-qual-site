---
schema: qual/card@1
id: P-TOPF10C
kind: problem
title: "A closed simply-connected 3-manifold is homotopy equivalent to S^3"
classification:
  areas:
  - topology
  topics:
  - Homotopy Type
  - Manifolds
  - Homology
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Show that a closed, compact, simply-connected $3$-manifold $M^3$ is homotopy equivalent to $S^3$.
:::

::: {.solution}
Let $M$ be a closed, simply connected $3$-manifold.
A compact manifold has the homotopy type of a CW complex, so Whitehead's theorem applies to $M$.

::: pf

::: {.pf-step #orientable}
$M$ is connected and orientable.

::: pf-proof
A simply connected space is path connected.
The orientation double cover of $M$ is a covering space, and $M$ is simply connected, so it is trivial; hence $M$ is orientable.
:::

:::

::: {.pf-step #homology}
$H_0(M) \cong \ZZ$, $H_1(M) = 0$, $H_2(M) = 0$, and $H_3(M) \cong \ZZ$.

::: pf-proof
$H_0 \cong \ZZ$ because $M$ is path connected, and $H_1(M) \cong \pi_1(M)^{\mathrm{ab}} = 0$.
By step [](#orientable){.pf-ref}, $M$ is closed, connected and orientable, so $H_3(M) \cong \ZZ$ and Poincaré duality gives $H_2(M) \cong H^1(M)$.
By the universal coefficient theorem, $H^1(M) \cong \Hom(H_1(M), \ZZ) = 0$.
:::

:::

::: {.pf-step #degree-one}
There is a map $f\colon M \to S^3$ inducing isomorphisms on all homology groups.

::: pf-proof
Choose a closed coordinate ball $B \subseteq M$, and let $f$ collapse $M \setminus \operatorname{int} B$ to a point, so that $f$ factors through $B / \partial B \cong S^3$.
Then $f$ has degree $\pm 1$: the local homology $H_3(M, M \setminus x) \to H_3(S^3, S^3 \setminus f(x))$ is an isomorphism for $x \in \operatorname{int} B$, and the fundamental class of $M$ restricts to a generator of local homology.
So $f_*$ is an isomorphism on $H_3$.
It is an isomorphism on $H_0$ because both spaces are path connected, and on $H_1$ and $H_2$ because both sides vanish, by step [](#homology){.pf-ref}.
:::

:::

::: pf-step
$M$ is homotopy equivalent to $S^3$.

::: pf-proof
$M$ and $S^3$ are simply connected CW complexes up to homotopy, and the map $f$ of step [](#degree-one){.pf-ref} induces isomorphisms on all integral homology groups.
By the homology form of Whitehead's theorem, $f$ is a homotopy equivalence.
:::

:::

:::
:::
