---
schema: qual/card@1
id: P-CASP15D
kind: problem
title: '$\int_0^\infty \log x/(x^2-1)\,dx$'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
  - Improper Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the removable
    singularity with limit 1/2 and the convergence at both ends, the substitution x = 1/t
    carried out in full (giving B = A rather than merely a relation between two integrals),
    the doubling I = 2A, Tonelli for the nonnegative series, the moment integral
    1/(2n+1)^2 by u = -log x, and the odd part of zeta(2). The prose's "monotone/dominated
    convergence" is replaced by the single justified use of Tonelli on nonnegative terms.
    The answer pi^2/4 is unchanged. The collection's provenance is the examination paper
    only, so no retained solution set covers the exercise and the argument is the card's
    own.
---

::: {.problem}
Evaluate
$$
\int_0^\infty \frac{\log x}{x^2 - 1} \, dx.
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $I\coloneqq\int_0^\infty\frac{\log x}{x^2-1}dx$, $A\coloneqq\int_0^1\frac{\log x}{x^2-1}dx$ and $B\coloneqq\int_1^\infty\frac{\log x}{x^2-1}dx$.

::: pf

::: {.pf-step #converges}
The integrand extends continuously to $x=1$ with the value $\frac12$, and $I$ converges at both ends.

::: pf-proof
$\log x=(x-1)+O((x-1)^2)$ and $x^2-1=2(x-1)+O((x-1)^2)$ near $1$, so the quotient tends to $\frac12$, and the singularity is removable. Near $0$ the quotient is $\sim-\log x$, integrable, and as $x\to\infty$ it is $O(x^{-2}\log x)$, integrable.
:::

:::

::: {.pf-step #substitution}
$B=A$.

::: pf-proof
Substitute $x=\frac1t$, so $dx=-\frac{dt}{t^2}$, $\log x=-\log t$ and $x^2-1=\frac{1-t^2}{t^2}$, and as $x$ runs from $1$ to $\infty$, $t$ runs from $1$ to $0$:
$$
B=\int_1^{0}\frac{-\log t}{\frac{1-t^2}{t^2}}\left(-\frac{dt}{t^2}\right)=\int_1^0\frac{\log t}{1-t^2}\,dt=-\int_0^1\frac{\log t}{1-t^2}\,dt .
$$
On $(0,1)$ one has $x^2-1=-(1-x^2)$, so the last integral is $-\int_0^1\frac{\log x}{x^2-1}dx=-A$; hence $B=A$.
:::

:::

::: {.pf-step #doubling}
$I=2\displaystyle\int_0^1\frac{-\log x}{1-x^2}\,dx$.

::: pf-proof
$I=A+B=2A$ by step [](#substitution){.pf-ref}, and $A=\int_0^1\frac{-\log x}{1-x^2}dx$ since $x^2-1=-(1-x^2)$ on $(0,1)$.
:::

:::

::: {.pf-step #series}
$\displaystyle\int_0^1\frac{-\log x}{1-x^2}\,dx=\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}$.

::: pf-proof
On $0\le x<1$, $\frac{1}{1-x^2}=\sum_{n\ge0}x^{2n}$ with nonnegative terms. Tonelli's theorem applied to the nonnegative function $\frac{-\log x}{1-x^2}$ on $(0,1)$ lets the integral of the sum be the sum of the integrals, and for each $n$
$$
\int_0^1(-\log x)x^{2n}\,dx=\frac{1}{(2n+1)^2},
$$
as one checks by substituting $u=-\log x$, which gives $\int_0^\infty ue^{-(2n+1)u}du=\frac{1}{(2n+1)^2}$.
:::

:::

::: {.pf-step #odd-sum}
$\displaystyle\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}=\frac{\pi^2}{8}$.

::: pf-proof
The odd terms are the sum of all terms minus the even ones: $\sum_n(2n+1)^{-2}=\sum_{k\ge1}k^{-2}-\sum_{m\ge1}(2m)^{-2}=\left(1-\frac14\right)\zeta(2)$, and $\zeta(2)=\frac{\pi^2}{6}$ gives $\frac34\cdot\frac{\pi^2}{6}=\frac{\pi^2}{8}$.
:::

:::

::: {.pf-step}
$\displaystyle\int_0^\infty\frac{\log x}{x^2-1}\,dx=\boxed{\frac{\pi^2}{4}}$.

::: pf-proof
Steps [](#doubling){.pf-ref}, [](#series){.pf-ref} and [](#odd-sum){.pf-ref} give $I=2\cdot\frac{\pi^2}{8}=\frac{\pi^2}{4}$, which is $1.2337\ldots$ for the record.
:::

:::

:::
:::
