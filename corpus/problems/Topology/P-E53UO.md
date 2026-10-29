---
schema: qual/card@1
id: P-E53UO
kind: problem
title: Attaching a $2$-cell along homotopic maps yields homotopy-equivalent spaces
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
  - Retracts
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source text was a worked argument (cylinder X cup_H B^2 x I retracting onto either lid, citing Hatcher Proposition 0.18) in place of a question. The statement now poses the result; the argument is the solution."
---

::: {.problem}
Let $X$ be a topological space and let $f,g:S^1\to X$ be homotopic maps. Show that the spaces $X\cup_f B^2$ and $X\cup_g B^2$ obtained by attaching a $2$-cell along $f$ and along $g$ are homotopy equivalent.
:::

::: {.solution}

::: pf

::: pf-step

Let $H:S^1\times I\to X$ be a homotopy from $f$ to $g$ and form
$$R=X\cup_H(B^2\times I),$$
attaching the lateral boundary $S^1\times I$ by $H$.

::: pf-proof

This quotient is well-defined because $S^1=\partial B^2$.

:::

:::

::: pf-step

The cylinder $B^2\times I$ deformation retracts, relative to its lateral boundary, onto $(S^1\times I)\cup(B^2\times\{0\})$.

::: pf-proof

Radial projection from the point $(0,2)\in\RR^2\times\RR$ sends each point of $B^2\times I$ to the point where the ray from $(0,2)$ through it meets $(S^1\times I)\cup(B^2\times\{0\})$. This map is a retraction, and the straight-line homotopy to the identity stays in $B^2\times I$ and fixes that subspace pointwise.

:::

:::

::: pf-step

Hence $R$ deformation retracts onto $X\cup_fB^2$; using the other lid it deformation retracts onto $X\cup_gB^2$.

::: pf-proof

Because the collapse fixes the attaching lateral boundary, it descends through the quotient. At the bottom lid $H(-,0)=f$, and at the top lid $H(-,1)=g$.

:::

:::

::: pf-step

Therefore
$$\boxed{X\cup_fB^2\simeq X\cup_gB^2.}$$

::: pf-proof

Both are deformation retracts of $R$.

:::

:::

:::

:::
