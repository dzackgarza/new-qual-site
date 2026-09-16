---
schema: qual/card@1
id: FF-OL75S
kind: fact
title: Burnside's orbit-counting formula
prompts:
- State Burnside's orbit-counting formula.
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
relations: []
review: draft
---

::: {.fact}
Let a finite group $G$ [[D-WYC7C|act]] on a finite set $X$.
Let $X/G$ be the set of orbits, and for $g\in G$ let $X^g=\theset{x\in X\suchthat g\cdot x=x}$ be the set of fixed points of $g$.
Then
$$
\abs{G}\,\abs{X/G}=\sum_{g\in G}\abs{X^g},
$$
so the number of orbits is the average number of fixed points of an element of $G$.
:::

::: {.proof}
Count the set $\theset{(g,x)\in G\times X\suchthat g\cdot x=x}$ in two ways.
Summing over $g$ gives $\sum_{g\in G}\abs{X^g}$.
Summing over $x$ gives $\sum_{x\in X}\abs{G_x}=\sum_{x\in X}\abs G/\abs{G\cdot x}$ by the orbit-stabilizer theorem, and the $\abs{G\cdot x}$ points of each orbit contribute $\abs G$ in total, so this sum is $\abs G\,\abs{X/G}$.
:::
