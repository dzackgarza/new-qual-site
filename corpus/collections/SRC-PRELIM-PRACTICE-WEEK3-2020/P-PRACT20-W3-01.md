---
schema: qual/card@1
id: P-PRACT20-W3-01
kind: problem
title: Closed form for the derivative of $\sum_{n\ge1}(-1)^nx^{3n}$
classification:
  areas:
  - prelim
  topics:
  - Power Series
  - Differentiation
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 1 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem is the same series and the same request for a closed form of the derivative
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The printed solution's route is transcribed: sum the geometric series over n >= 0, then differentiate, giving -3x^2/(1+x^3)^2 on (-1,1).
---

::: {.problem}
Suppose $f(x) = \sum_{n=1}^{\infty} (-1)^{n} x^{3n}$ for $x \in (-1, 1)$. Find a closed form for $f'(x)$.
:::

::: {.solution}

Let $f(x)=\sum_{n\ge1}(-1)^nx^{3n}$ for $x\in(-1,1)$.

::: pf

::: {.pf-step #geometric}

$f(x)+1=\dfrac{1}{1+x^3}$ on $(-1,1)$.

::: pf-proof

$\sum_{n\ge0}(-x^3)^n$ is a geometric series with ratio $-x^3$, of modulus
$\abs x^3<1$ on $(-1,1)$, so it converges there to
$\frac{1}{1-(-x^3)}=\frac{1}{1+x^3}$. Adding the $n=0$ term, which is $1$, to
$f$ gives exactly that sum.

:::

:::

::: {.pf-step #derivative}

$\boxed{f'(x)=-\dfrac{3x^2}{(1+x^3)^2}}$ on $(-1,1)$.

::: pf-proof

A power series is differentiable inside its interval of convergence with the
derivative given by term-by-term differentiation, so
$f'(x)=\sum_{n\ge1}(-1)^n3nx^{3n-1}$ on $(-1,1)$; alternatively differentiate
the closed form $\frac{1}{1+x^3}-1$ by the chain rule, which gives
$-\frac{3x^2}{(1+x^3)^2}$. The two agree because the differentiated series
converges on the same interval, the radius being $1$.

:::

:::

:::


:::
