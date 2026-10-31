---
schema: qual/card@1
id: E-LP6WS
kind: problem
title: The closed topologist's sine curve separates the sphere
classification:
  areas:
  - topology
  topics:
  - Jordan Separation Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $A$ be the subset of $\RR^2$ consisting of the union of the topologist's sine curve and the broken-line path from $(0, -1)$ to $(0, -2)$ to $(1, -2)$ to $(1, \sin 1)$.
See Figure 61.4. We call $A$ the closed topologist's sine curve.
Show that if $C$ is a subspace of $S^2$ homeomorphic to the closed topologist's sine curve, then $C$ separates $S^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$A$ is the union of two compact connected sets $A_1$ and $A_2$ meeting in exactly two points.

::: pf-proof

Let $A_1$ be the topologist's sine curve, including its limit segment $\{0\}\times[-1,1]$. It is the closure of the connected graph $\{(x,\sin(1/x)):0<x\le1\}$, so it is compact and connected. Let $A_2$ be the broken-line path in the question; it is compact and connected. Directly from the description, $A_1\cap A_2=\{(0,-1),(1,\sin1)\}$.

:::

:::

::: {.pf-step #s2}

Munkres's general separation theorem, Theorem 61.4, states that the union of two closed connected subsets of $S^2$ meeting in precisely two points separates $S^2$.

::: pf-proof

Theorem 61.4.

:::

:::

::: {.pf-step #s3}

Let $h:A\to C$ be the given homeomorphism. The sets $h(A_1)$ and $h(A_2)$ are compact, hence closed in $S^2$, and connected. They meet exactly at $h((0,-1))$ and $h((1,\sin1))$, and their union is $C$.

::: pf-proof

hypothesis and step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Applying Theorem 61.4 to $h(A_1)$ and $h(A_2)$ shows that $C$ separates $S^2$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref}.

:::

:::

:::
