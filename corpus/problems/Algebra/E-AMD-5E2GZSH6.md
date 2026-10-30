---
schema: qual/card@1
id: E-AMD-5E2GZSH6
kind: problem
title: Burnside's orbit-counting lemma
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
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove Burnside's Orbit-Counting Lemma: If a finite group $G$ acts on a finite set $X$, then the number of orbits $\cardinality{X/G}$ is given by:
$$
\cardinality{X/G} = \frac{1}{\cardinality{G}} \sum_{g \in G} \cardinality{X^g},
$$
where $X^g = \{x \in X \mid g \cdot x = x\}$ is the fixed point set of $g$.
:::

::: {.solution}
Let $S=\{(g,x)\in G\times X:g\cdot x=x\}$, and write $G_x$ for the stabilizer of $x$.

::: pf

::: {.pf-step #count-g}
$\abs S=\sum_{g\in G}\abs{X^g}$.

::: pf-proof
For fixed $g\in G$, the pairs $(g,x)\in S$ are those with $x\in X^g$.
:::

:::

::: {.pf-step #count-x}
$\abs S=\abs G\,\abs{X/G}$.

::: pf-proof
For fixed $x\in X$, the pairs $(g,x)\in S$ are those with $g\in G_x$, so $\abs S=\sum_{x\in X}\abs{G_x}$. If $\mathcal O$ is an orbit and $x\in\mathcal O$, orbit-stabilizer gives $\abs{G_x}=\abs G/\abs{\mathcal O}$, so $\sum_{x\in\mathcal O}\abs{G_x}=\abs G$. Summing over the $\abs{X/G}$ orbits gives the claim.
:::

:::

::: pf-step
$\boxed{\abs{X/G}=\frac1{\abs G}\sum_{g\in G}\abs{X^g}}$.

::: pf-proof
Equate the two counts of steps [](#count-g){.pf-ref} and [](#count-x){.pf-ref} and divide by $\abs G$.
:::

:::

:::

:::
