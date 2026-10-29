---
schema: qual/card@1
id: E-NTLQD
kind: problem
title: Finite products and unions of compact spaces are compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Product Topology
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "a finite product or union compact spaces"; the missing "of" is supplied and a stray "Exercise" heading inside the statement is removed.
---

::: {.exercise}
Show that a finite product or union of compact spaces is again compact.

:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $K_1,\dots,K_r$ are compact subspaces of one space, then $K_1\cup\cdots\cup K_r$ is compact.

::: pf-proof

An open cover restricts to an open cover of each $K_i$. Choose a finite subcover for each; the union of these finitely many finite families covers the whole union.

:::

:::

::: {.pf-step #s2}

If $X$ and $Y$ are compact, then $X\times Y$ is compact.

::: pf-proof

Let $\mathcal U$ cover $X\times Y$. For each $(x,y)$ choose a basic rectangle $A\times B$ containing it and lying in some member of $\mathcal U$. Fixing $x$, compactness of $Y$ gives finitely many such rectangles covering $\{x\}\times Y$; intersect their $A$-factors to obtain a neighborhood $A_x$ of $x$ whose entire strip $A_x\times Y$ is covered by finitely many members of $\mathcal U$. Compactness of $X$ gives finitely many $A_x$ covering $X$, hence a finite subcover of $X\times Y$.

:::

:::

::: pf-step

Induction gives compactness of every finite product and finite union of compact spaces.

::: pf-proof

Apply steps [](#s1){.pf-ref} and [](#s2){.pf-ref} repeatedly.

:::

:::

:::

:::
