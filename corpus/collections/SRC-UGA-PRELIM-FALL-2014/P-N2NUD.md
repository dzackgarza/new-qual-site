---
schema: qual/card@1
id: P-N2NUD
kind: problem
title: Equivalence relation $x\sim y$ iff $x^2-4x=y^2-4y$
classification:
  areas:
  - prelim
  topics:
  - Functions and Relations
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured solution of the problem as printed, replacing prose whose (a) was numbered
    as two separate lists and whose (b) listed the values of x^2-4x without saying which
    classes they cut out. The three defining properties are proved in steps, and the
    partition is read off from the six values of the function on A, which is checked to be
    the set of fibres. The argument is the card's own: no retained solution set covers this
    problem.
---

::: {.problem}
Take $A = \{0, 1, 2, 3, 4, 5\}$. Define a relation $R$ on $A$ by $x\, R\, y$ if and only if $x^2 - 4x = y^2 - 4y$.

(a) Prove that $R$ is an equivalence relation.

(b) Exhibit the partition of $A$ whose members are the equivalence classes of $R$.
:::

::: {.solution}
The argument is the card's own; no retained solution set covers this problem.

Throughout, $A=\theset{0,1,2,3,4,5}$ and $x \mathrel{R} y$ means $x^2-4x=y^2-4y$, both sides being values of the function $f(x)=x^2-4x$ on $A$.

::: pf

::: {.pf-step #refl}
(a) $R$ is reflexive.

::: pf-proof
For $x\in A$ the two sides of $x \mathrel{R} x$ are the same number $x^2-4x$, so $x \mathrel{R} x$.
:::

:::

::: {.pf-step #symm}
(a) $R$ is symmetric.

::: pf-proof
If $x \mathrel{R} y$, then $x^2-4x=y^2-4y$, and reading this equality from right to left gives $y^2-4y=x^2-4x$, that is $y \mathrel{R} x$.
:::

:::

::: {.pf-step #trans}
(a) $R$ is transitive, so $R$ is an equivalence relation.

::: pf-proof
If $x \mathrel{R} y$ and $y \mathrel{R} z$, then $x^2-4x=y^2-4y$ and $y^2-4y=z^2-4z$; equality is transitive, so $x^2-4x=z^2-4z$, that is $x \mathrel{R} z$. With steps [](#refl){.pf-ref} and [](#symm){.pf-ref} this makes $R$ an equivalence relation.
:::

:::

::: {.pf-step #classes}
(b) The equivalence classes are $\theset{0,4}$, $\theset{1,3}$, $\theset{2}$ and $\theset{5}$.

::: pf-proof

::: {.pf-step #table}
On $A$ the function $f(x)=x^2-4x$ takes the values $f(0)=0$, $f(1)=-3$, $f(2)=-4$, $f(3)=-3$, $f(4)=0$ and $f(5)=5$.

::: pf-proof
These are the six direct evaluations $0-0$, $1-4$, $4-8$, $9-12$, $16-16$ and $25-20$.
:::

:::

::: {.pf-step #read-off}
Two elements of $A$ are equivalent exactly when they have the same value under $f$, so the classes are the fibres of step [](#table){.pf-ref}: the fibre over $0$ is $\theset{0,4}$, over $-3$ is $\theset{1,3}$, over $-4$ is $\theset{2}$ and over $5$ is $\theset{5}$.

::: pf-proof
By definition $x \mathrel{R} y$ if and only if $f(x)=f(y)$, so the class of $a\in A$ is $\theset{x\in A \mid f(x)=f(a)}$; reading the six values of step [](#table){.pf-ref} gives the four sets listed, which are nonempty, pairwise disjoint, and have union $A$.
:::

:::

:::

:::

:::
:::
