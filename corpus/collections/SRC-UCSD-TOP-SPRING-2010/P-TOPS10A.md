---
schema: qual/card@1
id: P-TOPS10A
kind: problem
title: "Any map from a simply connected CW complex to RP^{n+1} is null-homotopic"
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Projective Spaces
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $M$ be a simply connected $n$-dimensional CW complex.
Show that any map from $M$ to $\mathbb{RP}^{n+1}$ is homotopic to the constant map.
:::

::: {.solution}
<1>1. Let $f: M \to \RP^{n+1}$ be any map.
::: {.proof}
take an arbitrary map.
:::

<1>2. $f$ lifts to a map $\tilde f: M \to S^{n+1}$.
::: {.proof}
$M$ is simply connected, so $f_*(\pi_1(M)) = 0 \subseteq \pi_1(\RP^{n+1}) = \ZZ/2$; by the lifting criterion, $f$ lifts to the universal cover $S^{n+1}$ of $\RP^{n+1}$.
:::

<1>3. $\tilde f$ is nullhomotopic.
<2>1. $S^{n+1}$ is $n$-connected: $\pi_i(S^{n+1}) = 0$ for all $i \le n$.
::: {.proof}
standard fact about spheres.
:::
<2>2. $M$ is an $n$-dimensional CW complex.
::: {.proof}
hypothesis.
:::
<2>3. Hence any map $M \to S^{n+1}$ is nullhomotopic.
::: {.proof}
by cellular approximation, $\tilde f$ is homotopic to a map into the $n$-skeleton of $S^{n+1}$, which is a single point (since $S^{n+1}$ has no cells in dimensions $1, \ldots, n$); equivalently, obstruction theory: the obstructions to nullhomotopy live in $H^i(M; \pi_i(S^{n+1})) = 0$ for $i \le n$.
:::

<1>4. Hence $f = p \circ \tilde f$ is nullhomotopic.
::: {.proof}
a nullhomotopy of $\tilde f$ composes with the covering map $p: S^{n+1} \to \RP^{n+1}$ to give a nullhomotopy of $f$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
