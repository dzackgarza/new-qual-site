---
schema: qual/card@1
id: P-YMVNK
kind: problem
title: Stabilizer subgroups of two points in a $G$-set are conjugate
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
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source labels the parts (1) and (2), and part (2) reads "Note that if x_1, x_2 lie in different orbits, their stabilizers need not be conjugate." without a task; the parts are labelled (a) and (b), and (b) asks for a demonstration.'
---

::: {.problem}
Let $X$ be a $G$-set with group action $G \times X \to X$.

(a) Prove that if $x_1, x_2 \in X$ belong to the same $G$-orbit ($x_2 = g \cdot x_1$ for some $g \in G$), then their stabilizer subgroups $\Stab_G(x_1)$ and $\Stab_G(x_2)$ are **conjugate** in $G$:
$$\Stab_G(g \cdot x_1) = g \Stab_G(x_1) g^{-1}.$$

(b) Show that if $x_1, x_2$ lie in different orbits, their stabilizers need not be conjugate.
:::

::: {.solution}

::: pf

::: pf-step
(a) $\Stab_G(gx)=g\Stab_G(x)g^{-1}$ for all $g\in G$ and $x\in X$.

::: pf-proof
For $h\in G$, $h(gx)=gx$ holds if and only if $(g^{-1}hg)x=x$, that is, $g^{-1}hg\in\Stab_G(x)$, that is, $h\in g\Stab_G(x)g^{-1}$.
:::

:::

::: pf-step
(b) Let $S_3$ act on $X=\{1,2,3\}\sqcup\{*\}$, by permutations on $\{1,2,3\}$ and trivially on $*$.
Then $\Stab(1)$ and $\Stab(*)$ are not conjugate.

::: pf-proof
$\Stab(1)=\{e,(23)\}$ has order $2$ and $\Stab(*)=S_3$ has order $6$; conjugate subgroups have equal order.
:::

:::

:::

:::
