---
schema: qual/card@1
id: E-HK-PPAO
kind: problem
title: Eigenvectors of a triangular matrix
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.4.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise and no printed copy of
    Hoffman and Kunze is retained, so the card cites it by section and number, read from the
    collection index because the card id is coded: it is §1.6 Exercise 4. Each step re-read: the
    matrix product gives (5x_1, x_1 + 5x_2, x_2 + 5x_3); the zero vector works for every scalar;
    a nonzero solution forces c = 5 by a three-step cascade; and with c = 5 the first two
    coordinates vanish and the third is free. The closing sentence records that A is therefore not
    diagonalisable, which the index computation gives. Not claimed: the characteristic polynomial
    or the Jordan form.
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{c c c} 5 & 0 & 0 \\ 1 & 5 & 0 \\ 0 & 1 & 5 \end{array} \right].
$$

For which $X$ does there exist a scalar $c$ such that $AX = cX$ ?
:::


::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and no printed copy of Hoffman and Kunze is retained in `tmp/sources`, so the exercise is cited by section and number rather than by page. It is checked against Hoffman and Kunze, Linear Algebra (1971), §1.6 Exercise 4, whose number is read from the collection index (the card id is coded).

::: pf

::: {.pf-step #system}
For $X=(x_1,x_2,x_3)^{t}$ and a scalar $c$, $AX=cX$ is equivalent to the three equations $(5-c)x_1=0$, $x_1+(5-c)x_2=0$, $x_2+(5-c)x_3=0$.

::: pf-proof
Multiplying $A$ by $X$ gives $(5x_1,\;x_1+5x_2,\;x_2+5x_3)^{t}$, and subtracting $cX=(cx_1,cx_2,cx_3)^{t}$ gives exactly the three displayed equations.
:::

:::

::: {.pf-step #zero}
$X=0$ satisfies $AX=cX$ for every $c$.

::: pf-proof
Both sides are then $0$.
:::

:::

::: {.pf-step #cisfive}
If $X\ne0$ and $AX=cX$ then $c=5$.

::: pf-proof
Suppose $c\ne5$. The first equation forces $x_1=0$; then the second forces $x_2=0$; then the third forces $x_3=0$ because $5-c\ne0$. So $X=0$, contrary to the assumption.
:::

:::

::: {.pf-step #solution}
For $c=5$ the solutions are exactly the multiples of $(0,0,1)^{t}$.

::: pf-proof
With $c=5$ the three equations become $0=0$, $x_1=0$ and $x_2=0$, leaving $x_3$ free; hence $X=t(0,0,1)^{t}$ for some $t$. Conversely any such vector satisfies $AX=5X$, since $A(0,0,t)^{t}=(0,0,5t)^{t}$.
:::

:::

::: {.pf-step}
The vectors admitting a scalar $c$ with $AX=cX$ are exactly the multiples of $(0,0,1)^{t}$.

::: pf-proof
Steps [](#zero){.pf-ref}, [](#cisfive){.pf-ref} and [](#solution){.pf-ref} cover the cases:
$$
\boxed{\{X:AX=cX\text{ for some }c\}=\{t(0,0,1)^{t}:t\in F\},}
$$
and the scalar is $c=5$ for the nonzero members. In particular $A$ has the single eigenvalue $5$, with a one-dimensional eigenspace, so $A$ is not diagonalisable.
:::

:::

:::
:::
