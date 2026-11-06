---
schema: qual/card@1
id: P-PRACT20-W3-07
kind: problem
title: Taylor series of the sine integral $\int_0^x\frac{\sin t}{t}\,dt$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 3 of the retained solutions booklet GRE Prep: Calculus
    II & III Practice Problem Solutions by Christian Parkinson
    (assets/attachments/Week3_solns.pdf), which prints this problem and a worked
    solution. The practice sheet itself is not retained and the collection's
    provenance list is empty, so the printed statement in that booklet is the
    source used for the statement. the printed problem asks for the Taylor series about 0 of the same integral of sin(t)/t, and the printed solution gives the same series
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The booklet's chain is transcribed: the sine series divided by t, then integrated term by term, giving the series with the extra factor 2n+1 in the denominator, with convergence for all x stated.
---

::: {.problem}
Find the Taylor Series for $\displaystyle f(x) = \int_{0}^{x} \frac{\sin(t)}{t}\, dt$ about $x = 0$.
:::

::: {.solution}

Let $f(x)=\int_0^x\frac{\sin t}{t}\,dt$, with the integrand extended by $1$ at
$t=0$; expand about $x=0$.

::: pf

::: {.pf-step #sine}

$\dfrac{\sin t}{t}=\displaystyle\sum_{n\ge0}\frac{(-1)^nt^{2n}}{(2n+1)!}$ for
all real $t$.

::: pf-proof

The Taylor series of $\sin t$ about $0$ is
$\sum_{n\ge0}\frac{(-1)^nt^{2n+1}}{(2n+1)!}$, convergent for every real $t$
since the coefficients decay factorially; dividing by $t\ne0$ gives the stated
series, which therefore converges for every real $t$ and defines the
continuous extension at $t=0$, where its value is $1$.

:::

:::

::: {.pf-step #integrate}

$\boxed{\displaystyle
f(x)=\sum_{n\ge0}\frac{(-1)^nx^{2n+1}}{(2n+1)!\,(2n+1)}}$ for all real $x$.

::: pf-proof

A power series may be integrated term by term on any closed interval inside
its interval of convergence, and here that interval is all of $\RR$:
integrating $\frac{(-1)^nt^{2n}}{(2n+1)!}$ from $0$ to $x$ gives
$\frac{(-1)^nx^{2n+1}}{(2n+1)(2n+1)!}$, so summing gives the displayed series,
which converges for all $x$ by comparison with the series for $\sin x$. This
is the Taylor series of $f$ about $0$, since $f$ is given by a convergent
power series in $x$.

:::

:::

:::


:::
