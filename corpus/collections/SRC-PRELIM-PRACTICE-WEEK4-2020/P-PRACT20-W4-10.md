---
schema: qual/card@1
id: P-PRACT20-W4-10
kind: problem
title: Solution sets of second-order equations that are subspaces of $C(\RR)$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
  - Linear Algebra
  - Subspaces
relations: []
review: draft
---

::: {.problem}
Which of the following are linear subspaces of the continuous functions from $\RR$ to $\RR$?

I. $\{ f : f \text{ is twice differentiable and } f''(x) - 2f'(x) + 3f(x) = 0 \text{ for all } x \}$

II. $\{ g : g \text{ is twice differentiable and } g''(x) = 3g'(x) \text{ for all } x \}$

III. $\{ h : h \text{ is twice differentiable and } h''(x) = h(x) + 1 \text{ for all } x \}$
:::

::: {.solution}
The answer is that I. and II. are subspaces but III. is not.
The problem with III. is that the set is not closed under addition or scaling.
Indeed, it $h _ { 1 } , h _ { 2 }$ satisfy the equation, then

$$
( h _ { 1 } + h _ { 2 } ) ^ { \prime \prime } = ( h _ { 1 } + h _ { 2 } ) + 2
$$

which is a different equation, so $h _ { 1 } + h _ { 2 }$ does not lie in the solution set.
:::
