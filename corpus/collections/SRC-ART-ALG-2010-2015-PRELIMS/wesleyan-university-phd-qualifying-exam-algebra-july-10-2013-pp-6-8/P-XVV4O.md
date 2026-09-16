---
schema: qual/card@1
id: P-XVV4O
kind: problem
title: A counterexample to the converse of Lagrange's theorem
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked July 2013 Groups 4 on PDF page 6; the item requests an explained counterexample and belongs to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the order of A4, normality forced by index two, and the count of eight distinct 3-cycles forced into a hypothetical subgroup of order six."
---

::: {.problem}
Present and explain an example refuting the converse to Lagrange's Theorem.
:::

::: {.solution}
The group $A_4$ has order $12$, but it has no subgroup of
order $6$, even though $6$ divides $12$.

<1>1. The group $A_4$ has order $12$ and contains eight
distinct elements of order $3$.

::: {.proof}
The sign homomorphism $S_4\to\{1,-1\}$ is surjective
because a transposition has sign $-1$. Its kernel $A_4$
therefore has order $4!/2=12$ [@DF04].
For a $3$-cycle, choose the three letters in four ways and
then one of the two cyclic orientations. This gives exactly
$4\cdot2=8$ distinct $3$-cycles. Each is even, since
$(a\,b\,c)=(a\,c)(a\,b)$, so all eight lie in $A_4$.
They all have order $3$.
:::

<1>2. The group $A_4$ has no subgroup of order $6$.

::: {.proof}
If $H\leq A_4$ had order $6$, its index would be $2$.
Every index-two subgroup is normal: for an element outside
$H$, both its left coset and its right coset are the complement
of $H$, while an element of $H$ has both cosets equal to $H$.
Thus the quotient map $\pi:A_4\to A_4/H$ would be defined,
with target of order $2$.

For a $3$-cycle $c$, the order of $\pi(c)$ divides both $3$
and $2$, so $\pi(c)=1$. Hence all eight distinct $3$-cycles
from step <1>1 would belong to $H$. Together with the identity
they would give at least nine elements in a group of order six,
a contradiction.

Lagrange's theorem asserts that a subgroup order divides the
group order. Here that divisibility holds for $6\mid12$ but
the requested subgroup does not exist, disproving the converse.
:::
:::
