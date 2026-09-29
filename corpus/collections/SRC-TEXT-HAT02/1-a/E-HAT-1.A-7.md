---
schema: qual/card@1
id: E-HAT-1.A-7
kind: problem
title: Nontrivial normal subgroup of infinite index in finitely generated free group is not finitely generated
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
If $F$ is a finitely generated free group and $N$ is a nontrivial normal subgroup of infinite index, show, using covering spaces, that $N$ is not finitely generated.
:::

::: {.solution}

::: pf

::: pf-step

Let $F = \pi_1(X)$ where $X$ is a finite wedge of circles (a finite graph with one vertex).

::: pf-proof

a finitely generated free group is the fundamental group of a finite wedge of circles.

:::

:::

::: {.pf-step #s2}

$N$ corresponds to a connected covering space $p: \tilde X \to X$ with $p_*(\pi_1(\tilde X)) = N$.

::: pf-proof

the fundamental theorem of covering spaces.

:::

:::

::: pf-step

Since $N$ is normal, $\tilde X$ is a normal (regular) covering, and its deck group is $F/N$, which is infinite (since $N$ has infinite index).

::: pf-proof

a normal subgroup corresponds to a regular covering, and the deck group is $F/N$.

:::

:::

::: pf-step

$\tilde X$ is a graph (a covering of a graph is a graph), and it is infinite.

::: pf-proof

the deck group $F/N$ is infinite, so $\tilde X$ has infinitely many sheets, hence infinitely many vertices.

:::

:::

::: {.pf-step #s5}

$\pi_1(\tilde X) = N$ is the fundamental group of an infinite graph.

::: pf-proof

Step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s6}

The fundamental group of an infinite graph is not finitely generated.

::: pf-proof

::: {.pf-step #s6-1}

An infinite graph has infinitely many edges.

::: pf-proof

a finite graph has finitely many edges; $\tilde X$ is infinite, so it has infinitely many edges.

:::

:::

::: {.pf-step #s6-2}

The fundamental group of a graph is free on the edges not in a maximal tree.

::: pf-proof

standard fact.

:::

:::

::: pf-step

An infinite graph has a maximal tree whose complement has infinitely many edges, so its fundamental group is free on infinitely many generators.

::: pf-proof

Steps [](#s6-1){.pf-ref} and [](#s6-2){.pf-ref}.

:::

:::

::: pf-step

Hence $\pi_1(\tilde X)$ is not finitely generated.

::: pf-proof

a free group on infinitely many generators is not finitely generated.

:::

:::

:::

:::

::: {.pf-step #s7}

Therefore $N$ is not finitely generated.

::: pf-proof

Steps [](#s5){.pf-ref} and [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref}.

:::

:::

:::
