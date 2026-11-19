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
audit:
  - event: solution-written
    by: claude
    date: 2026-11-19
    note: >-
      Lamport structure over the retained solution, which covers the problem: Week 4 solutions
      (assets/attachments/Week4_solns.pdf), Problem 10, p. 4. Its argument is transcribed and cited
      on the card. One point where the card is more careful than the set: the set exhibits only the
      failure of closure under addition for III, whereas the card also records the simpler reason
      that III omits the zero function, and the subspace test for I and II is written out rather
      than summarised as "solution sets of linear homogeneous equations". No statement repair.
---

::: {.problem}
Which of the following are linear subspaces of the continuous functions from $\RR$ to $\RR$?

I. $\{ f : f \text{ is twice differentiable and } f''(x) - 2f'(x) + 3f(x) = 0 \text{ for all } x \}$

II. $\{ g : g \text{ is twice differentiable and } g''(x) = 3g'(x) \text{ for all } x \}$

III. $\{ h : h \text{ is twice differentiable and } h''(x) = h(x) + 1 \text{ for all } x \}$
:::

::: {.solution}
The argument is transcribed from the retained solution set for this collection, Week 4 solutions (`assets/attachments/Week4_solns.pdf`), Problem 10, p. 4, with one point made explicit. The question asks which of
$$
\mathrm{I}:\ f''=2f'-3f,\qquad \mathrm{II}:\ g''=3g',\qquad \mathrm{III}:\ h''=h+1
$$
on twice differentiable functions $\RR\to\RR$ are linear subspaces of the space of continuous functions.

::: pf

::: {.pf-step #criterion}
A subset $S$ of a vector space of functions is a linear subspace when $0\in S$ and $S$ is closed under addition and under scalar multiplication.

::: pf-proof
This is the subspace test: a nonempty subset closed under addition and scalar multiplication is a subspace, and $0\in S$ is how nonemptiness is verified in practice, since a nonempty subset closed under scalar multiplication contains $0\cdot u=0$.
:::

:::

::: {.pf-step #III}
$\mathrm{III}$ is not a subspace.

::: pf-proof
The zero function fails the defining equation: $0''=0$ while $0+1=1$, so $0\notin\mathrm{III}$ and the test of step [](#criterion){.pf-ref} fails. Equivalently, as the set puts it, $\mathrm{III}$ is not closed under addition: if $h_1,h_2$ satisfy $h''=h+1$ then $(h_1+h_2)''=(h_1+h_2)+2\ne(h_1+h_2)+1$, so the sum does not satisfy the equation that defines the set.
:::

:::

::: {.pf-step #I}
$\mathrm{I}$ and $\mathrm{II}$ are subspaces.

::: pf-proof
Both are defined by a linear homogeneous equation in the function and its derivatives, so the zero function satisfies it, and if two twice differentiable functions satisfy it then so does any linear combination: for $\mathrm{I}$, $(cf+dg)''=c(2f'-3f)+d(2g'-3g)=2(cf+dg)'-3(cf+dg)$, and the same computation with the coefficient $3$ gives $\mathrm{II}$. So both are closed under addition and scalar multiplication and contain $0$, which is step [](#criterion){.pf-ref}.
:::

:::

::: {.pf-step}
The subspaces are exactly $\mathrm{I}$ and $\mathrm{II}$; $\mathrm{III}$ is not one.

::: pf-proof
Step [](#I){.pf-ref} gives the two homogeneous cases and step [](#III){.pf-ref} excludes the inhomogeneous one, so I and II are subspaces of the continuous functions and III is not, which answers the question.
:::

:::

:::

:::
