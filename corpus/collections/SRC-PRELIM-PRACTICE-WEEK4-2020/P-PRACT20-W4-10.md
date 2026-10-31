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
Sets I and II are solution sets of linear homogeneous equations, so they contain $0$ and are closed under addition and scalar multiplication.
Set III does not contain the zero function, since $0''=0\ne0+1$, so it is not a subspace. It is also not closed under addition: if $h_1,h_2$ satisfy the equation, then

$$
(h_1+h_2)''=(h_1+h_2)+2\ne(h_1+h_2)+1,
$$

so $h_1+h_2$ does not lie in the set. Set III is nonempty, since it contains $h\equiv-1$.
:::
