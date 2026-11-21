---
schema: qual/card@1
id: E-IXKVS
kind: problem
title: Root location from small lower coefficients
classification:
  areas:
  - topology
  topics:
  - Fundamental Theorem of Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 56: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-56-the-fundamental-theorem-of-algebra/problem-1-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-56-the-fundamental-theorem-of-algebra/problem-1-solution.txt), and against Munkres,
    Topology (2000), Section 56 Exercise 1, printed p. 356. dbFin divides out the zero roots and, with $g(w)=1+a_{n-1}w+\cdots+a_0w^n$, uses $|g(w)|\ge1-\sum|a_i|>0$ on the closed disc; the card's is the same estimate written directly for a root $z$ with $|z|\ge1$, dividing the equation by $z^n$. Nothing needed repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the division by z^n under |z| >= 1, the term-
    by-term bound |a_k| |z|^{-j} <= |a_k|, the resulting 1 < 1, and the equivalent statement
    for the hint's polynomial g with |w| <= 1, which is the substitution w = 1/z. The
    argument is the card's own, following the book's hint; no retained solution set covers
    this exercise. The printed statement needed no repair.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Two corrections and one structural repair on 2026-11-19. The rendered
    preamble said "The argument is the card's own, following the book's hint; no
    retained solution set covers this exercise", which is false, since the event
    of 2026-11-11 cites dbFin's Section 56 Problem 1 solution and compares it
    with the card's estimate. The page carried no citation; the exercise is
    Munkres, Topology (2000), Section 56, Exercise 1, printed p. 356 (PDF p. 371,
    printed page = PDF page - 15), and the preamble now cites dbFin's solution
    and that page. The last step only announced that the earlier steps had
    answered the question, which STYLE-08 forbids: it is dropped, the step for
    the hint's polynomial now precedes the conclusion, and the conclusion is the
    QED step. No statement or argument changes: the division by z^n at a root of
    modulus at least 1, the bound 1 <= S < 1, and the equivalent statement for g
    on the closed disc are the ones the card had.

---

::: {.exercise}

Given a polynomial equation

$$
x^n + a_{n-1}x^{n-1} + \dots + a_1 x + a_0 = 0
$$

with real or complex coefficients.
Show that if $\abs{a_{n-1}} + \cdots + \abs{a_1} + \abs{a_0} < 1$, then all the roots of the equation lie interior to the unit ball $B^2$.
[Hint: Let $g(x) = 1 + a_{n-1}x + \cdots + a_1 x^{n-1} + a_0 x^n$, and show that $g(x) \neq 0$ for $x \in B^2$.]
:::

::: {.solution}
The estimate is that of the published solution of dbFin, "Section 56: Problem 1 Solution", which divides out the zero roots and shows that $g(w)=1+a_{n-1}w+\cdots+a_0w^n$ has no zero with $\abs w\le1$; here the same estimate is made directly, dividing the equation by $z^n$ at a root of modulus at least $1$. The exercise is Munkres, *Topology* (2000), Section 56, Exercise 1, printed p. 356, and $g$ is the polynomial its hint names.

Let $p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0$ and $S=\abs{a_{n-1}}+\cdots+\abs{a_0}<1$.

::: pf

::: {.pf-step #setup}
Let $p(z)=z^{n}+a_{n-1}z^{n-1}+\dots+a_{1}z+a_{0}$ and let $S=\abs{a_{n-1}}+\dots+\abs{a_{0}}<1$. If $p(z)=0$ and $\abs{z}\ge1$, then $z\ne0$ and
$$
1=-\Big(\frac{a_{n-1}}{z}+\frac{a_{n-2}}{z^{2}}+\dots+\frac{a_{0}}{z^{n}}\Big).
$$

::: pf-proof
$p(z)=0$ divides by $z^{n}$, which is legitimate because $\abs{z}\ge1$ gives $z\ne0$; the left side becomes $1$ and the other terms are the displayed fractions, so moving them to the other side gives the identity.
:::

:::

::: {.pf-step #bound}
Under that hypothesis $1<S$, a contradiction.

::: pf-proof
Taking absolute values in step [](#setup){.pf-ref} and using the triangle inequality,
$$
1\le\frac{\abs{a_{n-1}}}{\abs{z}}+\frac{\abs{a_{n-2}}}{\abs{z}^{2}}+\dots+\frac{\abs{a_{0}}}{\abs{z}^{n}}.
$$
Since $\abs{z}\ge1$ we have $\abs{z}^{-k}\le1$ for each $k\ge1$, so the right side is at most $\abs{a_{n-1}}+\dots+\abs{a_{0}}=S<1$; hence $1<1$.
:::

:::

::: {.pf-step #hint}
The polynomial $g(w)=1+a_{n-1}w+a_{n-2}w^{2}+\dots+a_{0}w^{n}$ of the hint has no zero with $\abs{w}\le1$.

::: pf-proof
If $g(w)=0$ then $1=-\big(a_{n-1}w+a_{n-2}w^{2}+\dots+a_{0}w^{n}\big)$, and taking absolute values with $\abs{w}\le1$ gives
$$
1\le\abs{a_{n-1}}\abs{w}+\abs{a_{n-2}}\abs{w}^{2}+\dots+\abs{a_{0}}\abs{w}^{n}\le S<1,
$$
which is impossible; so $g$ vanishes nowhere on the closed unit disk. This is the same computation as step [](#bound){.pf-ref} with $w=1/z$, and it is the form the hint asks for.
:::

:::

::: {.pf-step #roots}
No zero of $p$ satisfies $\abs{z}\ge1$; that is, every root of the equation lies in the open unit ball.

::: pf-proof
Steps [](#setup){.pf-ref} and [](#bound){.pf-ref} exclude every $z$ with $p(z)=0$ and $\abs{z}\ge1$, so each root $z$ satisfies $\abs{z}<1$, which is the interior of the unit ball.
:::

:::


:::

:::
