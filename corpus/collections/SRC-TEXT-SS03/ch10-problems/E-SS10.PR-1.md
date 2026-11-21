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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` at its printed folio (the scan runs nineteen pages ahead): the
    statement is Problem 1 at the head of the Chapter 10 Problems, printed p. 297, and its printed words
    are the card's except in one respect recorded here: the book prints "where a and k are positive
    integers", while the card says nonnegative. Both claims are true -- the standard three-squares
    theorem excludes every n = 4^a(8k+7) with a, k >= 0, and 7 itself (a = k = 0) is not a sum of three
    squares -- so the card states the theorem in its usual, slightly stronger form and the printed
    hypothesis is the weaker one. The statement is left as the card has it, and this difference is the
    reason. Not checked in this pass: the argument, which the edit does not touch.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Two corrections to the events above, both verified on the printed page today. The locator
    "printed p. 297" is wrong: Chapter 10's Problem 1 is on printed p. 314 (PDF p. 333), where the
    page head reads "314 Chapter 10. APPLICATIONS OF THETA FUNCTIONS" above "5 Problems". Printed
    p. 297 is inside the chapter's text. And the exercise block no longer alters the hypothesis: it
    now carries the printed "where $a$ and $k$ are positive integers" and the printed converse
    sentence, so its lead sentence that "the statement below is its wording" is true again; the
    strengthening to $a,k\ge0$ that the proof delivers, and the reason the printed converse fails at
    $n=7$, are recorded in the remark instead of being written into the statement. The asterisk
    before "1." is recorded there too. The argument was read and holds: odd squares are $1$ mod $8$
    and a sum of three squares is never $7$ mod $8$, and $4\mid x^2+y^2+z^2$ forces all three even,
    so $a$-fold division reduces to the residue obstruction.
---

::: {.exercise}
This is Problem 1 of Chapter 10 of Stein and Shakarchi, *Complex Analysis*, retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; the statement below is its wording.

Suppose $n=4^a(8k+7)$, where $a$ and $k$ are positive integers. Show that $n$ cannot be written as a sum of three integer squares. The converse, that every $n$ that is not of that form can be written as the sum of three squares, is a difficult theorem of Legendre and Gauss.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 10, Problem 1). Its converse is false as literally printed: with $a=k=0$ the number $7=4^0(8\cdot0+7)$ is not of the printed form, and $7$ is not a sum of three squares. The argument below proves the statement for $a,k\ge0$, which is the form in which both halves are true.
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
