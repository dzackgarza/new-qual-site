---
schema: qual/card@1
id: E-HAT-1.3-28
kind: problem
title: Fundamental group of an orbit space
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
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 28; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Identified the orbit map as the universal cover and its deck group with G.
---

::: {.problem}
Show that for a covering space action of a group $G$ on a simply-connected space $Y$, $\pi_1(Y/G)$ is isomorphic to $G$.
[If $Y$ is locally path-connected, this is a special case of part (c) of Proposition 1.40.]
:::

::: {.solution}
Let
$$
q:Y\to Y/G
$$
be the orbit map, and choose $y_0\in Y$.

::: pf

::: {.pf-step #s1}

The map $q$ is a covering map, and its action on the fiber over $q(y_0)$ identifies that fiber with $G$.

::: pf-proof

The covering space action supplies pairwise disjoint translates of an open neighborhood of each point; the quotient map sends each translate homeomorphically onto the same open subset of $Y/G$.
The fiber over $q(y_0)$ is $\{gy_0:g\in G\}$, and the action is free, so $g\mapsto gy_0$ is a bijection.

:::

:::

::: pf-step

Lifting loops at $q(y_0)$ from $y_0$ defines a homomorphism
$$
\Phi:\pi_1(Y/G,q(y_0))\longrightarrow G,
$$
where the lift of a loop representing $[\alpha]$ ends at $\Phi([\alpha])y_0$.

::: pf-proof

Homotopic based loops have lifts with the same endpoint, so $\Phi$ is well defined.
If the lifts of $\alpha$ and $\beta$ end at $gy_0$ and $hy_0$, respectively, then the lift of their concatenation first follows the lift of $\alpha$ and then the $g$-translate of the lift of $\beta$. It ends at $ghy_0$, so $\Phi([\alpha][\beta])=gh$.

:::

:::

::: pf-step

The homomorphism $\Phi$ is bijective. Therefore
$$
\boxed{\pi_1(Y/G)\cong G.}
$$

::: pf-proof

For each $g\in G$, path connectedness of $Y$ gives a path from $y_0$ to $gy_0$. Its projection is a loop whose class maps to $g$, so $\Phi$ is surjective.
If $\Phi([\alpha])=e$, the lift of $\alpha$ at $y_0$ is a loop. Since $Y$ is simply connected, this lifted loop is nullhomotopic. Its projection is a nullhomotopy of $\alpha$, so $[\alpha]=e$ and $\Phi$ is injective.

:::

:::

:::

:::
