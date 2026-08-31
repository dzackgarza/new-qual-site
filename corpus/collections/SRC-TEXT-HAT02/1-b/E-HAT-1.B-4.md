---
schema: qual/card@1
id: E-HAT-1.B-4
kind: exercise
title: "Amalgamated products via van Kampen"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Use van Kampen's theorem to compute $A *_C$ as a quotient of $A * \mathbb{Z}$, as stated in the text.

::: {.solution}
**Goal.** Use van Kampen to express the amalgamated product $A *_C$ as a quotient of $A * \ZZ$.

<1>1. Setup: $A$ is a space with $\pi_1(A) = A$ (abusing notation), and $C$ is a subspace with $\pi_1(C) = C$, attached along a map.
<2>1. The amalgamated product $A *_C$ is $\pi_1(A) *_{\pi_1(C)} \pi_1(\cdot)$.
::: {.proof}
this is the fundamental group of the space obtained by gluing $A$ to another space along $C$.
:::

<1>2. Attach a $2$-cell (or a cylinder) to $A$ along a loop representing a generator of $C$.
<2>1. Attaching a $2$-cell along a loop $\gamma$ kills $\gamma$ in $\pi_1$.
::: {.proof}
the attaching map makes $\gamma$ null-homotopic.
:::
<2>2. The resulting space has fundamental group $\pi_1(A) / \langle\!\langle \gamma \rangle\!\rangle$.
::: {.proof}
van Kampen: attaching a $2$-cell along $\gamma$ quotients $\pi_1(A)$ by the normal closure of $\gamma$.
:::

<1>3. $A *_C$ is the quotient of $A * \ZZ$ by the relation identifying the generator of $\ZZ$ with the image of $C$.
<2>1. $A * \ZZ$ is $\pi_1$ of $A$ wedged with a circle.
::: {.proof}
van Kampen for a wedge: $\pi_1(A \vee S^1) = \pi_1(A) * \pi_1(S^1) = A * \ZZ$.
:::
<2>2. The amalgamated product $A *_C$ is obtained by identifying the generator of $\ZZ$ with the image of the generator of $C$ in $A$.
::: {.proof}
this is the definition of the amalgamated free product: $A *_C = (A * \ZZ)/\langle\!\langle i_*(c) \cdot t^{-1} \rangle\!\rangle$ where $t$ is the generator of $\ZZ$ and $i_*: C \to A$ is the inclusion.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3.2 expresses $A *_C$ as the quotient of $A * \ZZ$ by the stated relation.
:::
:::
