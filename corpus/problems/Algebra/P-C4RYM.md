---
schema: qual/card@1
id: P-C4RYM
kind: problem
title: Burnside's lemma
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source reads "Prove Burnside's theorem." without stating it; the statement names Burnside's lemma, which the card proves, and states it.
---

::: {.problem}
Let a finite group $G$ act on a finite set $X$, and write $X^g=\{x\in X:gx=x\}$ and $X/G$ for the set of orbits. Prove Burnside's lemma:
$$
\abs{X/G}=\frac1{\abs{G}}\sum_{g\in G}\abs{X^g}.
$$
:::

::: {.solution}
Let $S=\{(g,x)\in G\times X:gx=x\}$, and let $G_x$ and $Gx$ denote the stabilizer and orbit of $x$.

::: pf

::: {.pf-step #double-count}

$\sum_{g\in G}\abs{X^g}=\abs{S}=\sum_{x\in X}\abs{G_x}$.

::: pf-proof

Count $S$ first by its first coordinate and then by its second.

:::

:::

::: {.pf-step #orbit-sum}

$\sum_{x\in X}\abs{G_x}=\abs{G}\cdot\abs{X/G}$.

::: pf-proof

By the orbit-stabilizer theorem, $\abs{G_x}=\abs{G}/\abs{Gx}$. For an orbit $O$, every $x\in O$ has $Gx=O$, so $\sum_{x\in O}\abs{G_x}=\abs{O}\cdot\abs{G}/\abs{O}=\abs{G}$. Summing over the orbits, which partition $X$, gives the claim.

:::

:::

::: pf-qed

Combining steps [](#double-count){.pf-ref} and [](#orbit-sum){.pf-ref} and dividing by $\abs{G}$ gives the formula.

:::

:::

:::
