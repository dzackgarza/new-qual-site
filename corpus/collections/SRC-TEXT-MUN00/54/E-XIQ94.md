---
schema: qual/card@1
id: E-XIQ94
kind: problem
title: The order of the rectangles in the lifting-of-homotopies proof
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

In defining the map $\overline{F}$ in the proof of Lemma 54.2, why were we so careful about the order in which we considered the small rectangles?
:::

::: {.solution}
Lemma 54.2 states: for a covering map $p: E \to B$ with $p(e_0) = b_0$ and a continuous $F: I \times I \to B$ with $F(0, 0) = b_0$, there is a unique lifting $\overline{F}: I \times I \to E$ with $\overline{F}(0, 0) = e_0$. The proof subdivides $I \times I$ into rectangles $R$, each mapped by $F$ into an evenly covered open set $U$, and extends $\overline{F}$ one rectangle at a time.

::: pf

::: {.pf-step #s1}

When $\overline{F}$ is already defined on a connected subset $C$ of $R$, it extends uniquely and continuously to $R$.

::: pf-proof

$p^{-1}(U)$ is a disjoint union of open slices $V_\alpha$. The connected set $\overline{F}(C)$ lies in $p^{-1}(U)$, so it lies in a single slice $V_0$. Define $\overline{F} = (p|_{V_0})^{-1} \circ F$ on $R$. This is continuous and agrees with the given values on $C$, since $p \circ \overline{F} = F$ there and $p|_{V_0}$ is injective.

:::

:::

::: {.pf-step #s2}

Taking the rectangles row by row, from left to right within a row, the part of each rectangle on which $\overline{F}$ is already defined is the union of its left and bottom edges, which is connected.

::: pf-proof

At the step for a rectangle $R$, the rectangles already treated are those in lower rows and those to the left in the same row, together with the left and bottom edges of $I \times I$, where $\overline{F}$ was first defined by path lifting. Their union meets $R$ exactly in the left and bottom edges of $R$.

:::

:::

::: pf-qed

With another order, the part of a rectangle on which $\overline{F}$ is already defined can be disconnected, for example its left and right edges. The values of $\overline{F}$ on the two pieces could then lie in different slices over $U$, and no continuous lift over $R$ would agree with both. The order of step [](#s2){.pf-ref} makes that set connected at every step, so step [](#s1){.pf-ref} applies to every rectangle and the pieces fit together into a continuous $\overline{F}$.

:::

:::

:::
