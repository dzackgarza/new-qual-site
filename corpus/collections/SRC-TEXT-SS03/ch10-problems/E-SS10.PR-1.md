---
schema: qual/card@1
id: E-SS10.PR-1
kind: problem
title: Three squares obstruction modulo eight
classification:
  areas:
  - complex-analysis
  topics:
  - Sums of Squares
relations: []
review: draft
audit:
- event: source-corrected
  by: codex
  date: '2026-11-01'
  note: Stein and Shakarchi Ch. 10, Problem 1 prints a,k positive. Its converse then fails
    for n=7. The card uses nonnegative a,k so the stated three-square theorem is true.
---

::: {.exercise}
Suppose $n=4^a(8k+7)$, where $a$ and $k$ are nonnegative integers. Show that $n$ cannot be written as a sum of three integer squares. The converse for positive integers is the three-square theorem of Legendre and Gauss.
:::

::: {.solution}
::: pf

::: {.pf-step #residue}
No integer congruent to $7$ modulo $8$ is a sum of three squares.

::: pf-proof
An odd square is $1$ modulo $8$, and an even square is $0$ or $4$ modulo $8$. If a sum of three squares is odd, it contains either one or three odd squares. With one, its residue is $1$ or $5$ modulo $8$; with three, its residue is $3$. Neither is $7$.
:::

:::

::: {.pf-step #divide-four}
If $4\mid x^2+y^2+z^2$ for integers $x,y,z$, then $x,y,z$ are even.

::: pf-proof
Each square is $0$ or $1$ modulo $4$. A sum of three such residues is $0$ modulo $4$ only when all three are $0$. Thus each of $x,y,z$ is even.
:::

:::

::: pf-step
Q.E.D. $4^a(8k+7)$ is not a sum of three integer squares for $a,k\geq0$.

::: pf-proof
Suppose $4^a(8k+7)=x^2+y^2+z^2$. Apply step [](#divide-four){.pf-ref} and divide by $4$, repeatedly $a$ times. The result is $8k+7=x_a^2+y_a^2+z_a^2$ for integers $x_a,y_a,z_a$, contrary to step [](#residue){.pf-ref}. When $a=0$, the same contradiction applies without division.
:::

:::

:::
:::
