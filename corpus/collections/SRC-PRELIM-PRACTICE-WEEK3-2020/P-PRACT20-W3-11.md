---
schema: qual/card@1
id: P-PRACT20-W3-11
kind: problem
title: Expanding $x^3-x+1$ in powers of $x-2$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 4 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the same four coefficients in the expansion of x^3 - x + 1 about x = 2, and the printed solution gives 7, 11, 6, 1
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's successive-differentiation route is transcribed, with the coefficient formula stated and each derivative evaluated.
---

::: {.problem}
Find $a_{0}, a_{1}, a_{2}, a_{3}$ such that $x^{3} - x + 1 = a_{0} + a_{1}(x - 2) + a_{2}(x - 2)^{2} + a_{3}(x - 2)^{3}$.
:::

::: {.solution}

We want the coefficients of $p(x)=x^3-x+1$ in powers of $x-2$, that is its
Taylor coefficients at $2$.

::: pf

::: {.pf-step #formula}

$a_k=\dfrac{p^{(k)}(2)}{k!}$ for $k=0,1,2,3$.

::: pf-proof

Writing $p(x)=\sum_{k=0}^3a_k(x-2)^k$, differentiating $k$ times and
evaluating at $x=2$ kills every term but the $k$-th, since a term $(x-2)^j$
differentiates to $j(j-1)\cdots(j-k+1)(x-2)^{j-k}$, which vanishes at $2$ for
$j\ne k$ and equals $k!$ for $j=k$. So $p^{(k)}(2)=k!\,a_k$.

:::

:::

::: {.pf-step #values}

$a_0=7$, $a_1=11$, $a_2=6$, $a_3=1$.

::: pf-proof

$p(2)=8-2+1=7$; $p'(x)=3x^2-1$ so $p'(2)=12-1=11$; $p''(x)=6x$ so $p''(2)=12$
and $a_2=\frac{12}{2}=6$; $p'''(x)=6$ so $p'''(2)=6$ and $a_3=\frac{6}{6}=1$.
The last coefficient is also the leading coefficient of the polynomial, $1$,
as expected.

:::

:::

::: {.pf-step #answer}

$\boxed{x^3-x+1=7+11(x-2)+6(x-2)^2+(x-2)^3}$.

::: pf-proof

Substituting the values of step [](#values){.pf-ref} into the expansion of
step [](#formula){.pf-ref} gives the stated identity; expanding the right side
returns $x^3-x+1$, and the identity is exact because a cubic is determined by
its value and first three derivatives at one point.

:::

:::

:::


:::
