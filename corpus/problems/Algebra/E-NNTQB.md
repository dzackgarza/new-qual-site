---
schema: qual/card@1
id: E-NNTQB
kind: problem
title: Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced Lagrange index formula to the coset partition.
---

::: {.exercise}
Show that if $G$ is finite and $H\le G$, then
$$
[G:H]=\frac{\abs{G}}{\abs{H}}.
$$
:::

::: {.solution}
Here $H$ is a [[D-IQ4OX|subgroup]] of the finite group $G$ and $[G:H]$ is its [[D-VJGH5|index]], the number of left cosets of $H$ in $G$.

::: pf

::: {.pf-step #coset-size}
Every left coset of $H$ has $\abs{H}$ elements.

::: pf-proof
For $g\in G$, the map $H\to gH$, $h\mapsto gh$, is surjective by definition of $gH$ and injective by cancellation.
:::

:::

::: pf-step
$\abs{G}=[G:H]\,\abs{H}$, so $[G:H]=\dfrac{\abs{G}}{\abs{H}}$ and both $\abs{H}$ and $[G:H]$ divide $\abs{G}$.

::: pf-proof
The left cosets of $H$ partition $G$ ([[PR-VUKHO]]), and there are $[G:H]$ of them, each of size $\abs{H}$ by step [](#coset-size){.pf-ref}. Hence $\abs{G}=[G:H]\,\abs{H}$.
:::

:::

:::

:::

::: {.remark title="Variations"}
The order of any element $g$ of a finite group $G$ divides $\abs G$: the cyclic subgroup $\langle g\rangle$ has exactly $\abs g$ elements, so the last step with $H=\langle g\rangle$ gives $\abs G=[G:\langle g\rangle]\,\abs g$. Hence $g^{\abs G}=\bigl(g^{\abs g}\bigr)^{[G:\langle g\rangle]}=e$.
:::
