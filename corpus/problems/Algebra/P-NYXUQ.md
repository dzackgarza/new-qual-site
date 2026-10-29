---
schema: qual/card@1
id: P-NYXUQ
kind: problem
title: Conjugacy of stabilizers along an orbit
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source asks only "What group-theoretic construct relates the stabilizer of two points in the same orbit under a group action?"; the statement declares the action and asks for a proof of the relation the solution establishes.'
---

::: {.problem}
Let a group $G$ act on a set $X$. How are the stabilizers of two points in the same orbit related? Prove that if $y=g\cdot x$ with $g\in G$ and $x\in X$, then $G_y=gG_xg^{-1}$.
:::

::: {.solution}

::: pf

::: {.pf-step #forward}

$gG_xg^{-1}\subseteq G_y$.

::: pf-proof

For $h\in G_x$,
$$
(ghg^{-1})\cdot y=gh\cdot x=g\cdot x=y.
$$

:::

:::

::: pf-step

$G_y=gG_xg^{-1}$, so stabilizers of points in one orbit are $\boxed{\text{conjugate}}$.

::: pf-proof

Since $x=g^{-1}\cdot y$, step [](#forward){.pf-ref} with the roles of $x$ and $y$ exchanged and $g^{-1}$ in place of $g$ gives $g^{-1}G_yg\subseteq G_x$, that is, $G_y\subseteq gG_xg^{-1}$.

:::

:::

:::

:::
