---
schema: qual/card@1
id: P-TOPS07H
kind: problem
title: "Suspension of a homology 3-sphere is homotopy equivalent to S^4"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspensions
  - Homotopy Type
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $M^3$ be a homology sphere — a closed $3$-manifold having the same homology groups as $S^3$ — and let $X = \Sigma M$ be its suspension.
What are the fundamental group and homology groups of $X$?
Show that $X$ is homotopy equivalent to $S^4$.
:::

::: {.solution}
<1>1. $\pi_1(X) = 1$.
::: {.proof}
the suspension of a path-connected space is simply connected (the two cones are contractible and their intersection is $M$, which is path-connected, so van Kampen gives the trivial group).
:::

<1>2. $H_0(X) = \ZZ$.
::: {.proof}
$X$ is path-connected.
:::

<1>3. $H_1(X) = 0$.
::: {.proof}
$H_1(X) \cong H_0(M)$ by the suspension isomorphism, and $H_0(M) = \ZZ$; more precisely $\widetilde H_{n+1}(\Sigma M) \cong \widetilde H_n(M)$, so $H_1(X) \cong \widetilde H_0(M) = 0$.
:::

<1>4. $H_2(X) = 0$.
::: {.proof}
$H_2(X) \cong \widetilde H_1(M) = 0$ (since $M$ is a homology sphere, $\widetilde H_1(M) = 0$).
:::

<1>5. $H_3(X) = 0$.
::: {.proof}
$H_3(X) \cong \widetilde H_2(M) = 0$ (homology sphere).
:::

<1>6. $H_4(X) = \ZZ$.
::: {.proof}
$H_4(X) \cong \widetilde H_3(M) = \ZZ$ (homology sphere).
:::

<1>7. Hence $X$ has the homology of $S^4$ and trivial fundamental group.
::: {.proof}
<1>1–<1>6.
:::

<1>8. $X$ is a simply connected CW complex, so it is homotopy equivalent to $S^4$.
::: {.proof}
by the Hurewicz theorem, $\pi_4(X) \cong H_4(X) = \ZZ$; a generator $S^4 \to X$ induces an isomorphism on all homology groups, hence (Whitehead's theorem) is a homotopy equivalence.
:::

<1>9. Q.E.D.
::: {.proof}
<1>7 and <1>8.
:::
:::
