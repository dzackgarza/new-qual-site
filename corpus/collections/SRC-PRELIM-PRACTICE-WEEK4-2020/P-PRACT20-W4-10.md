---
schema: qual/card@1
id: P-PRACT20-W4-10
kind: problem
title: Solution sets of second-order equations that are subspaces of $C(\mathbb R)$
classification:
  areas:
  - applied-algebra
  topics:
  - Ordinary Differential Equations
  - Linear Algebra
  - Subspaces
relations: []
review: draft
---

::: {.problem}
Which of the following are linear subspaces of the continuous functions from R to R?

I. $\{ f : f$ is twice differentiable and $f ^ { \prime \prime } ( x ) - 2 f ^ { \prime } ( x ) + 3 f ( x ) = 0$ for all x}

II. $\{ g : g$ is twice differentiable and $g ^ { \prime \prime } ( x ) = 3 g ^ { \prime } ( x )$ for all x}

III. $\{ h : h$ is twice differentiable and $h ^ { \prime \prime } ( x ) = h ( x ) + 1 { \mathrm { ~ f o r ~ a l l ~ } } x \}$
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
