---
schema: qual/card@1
id: E-SS10.EX-5
kind: problem
title: Logarithmic asymptotics of the partition generating function
classification:
  areas:
  - complex-analysis
  topics:
  - Partitions
  - Generating Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, which is the printed hint's route.
    Checked: -log(1 - x^n) = sum_k x^{nk}/k with positive terms, so interchanging the order of
    summation is legitimate and the identity log F(x) = sum_m (1/m) x^m/(1 - x^m) follows; the
    printed inequality follows from 1 - x^m = (1-x)(1 + x + ... + x^{m-1}) with every one of the
    m terms between x^{m-1} and 1; the two-sided termwise bound x^m/m^2 <= (1-x)(1/m)x^m/(1-x^m)
    <= x/m^2 is recomputed in the proof rather than asserted; and the limits of both bounds are
    zeta(2) = pi^2/6 by dominated convergence with the summable bound 1/m^2. Statement and hint
    unchanged; no retained solution set covers the exercises of Stein-Shakarchi.
---

::: {.exercise}
Let
$$
F(x) = \sum_{n=0}^{\infty} p(n) x^n = \prod_{n=1}^{\infty} \frac{1}{1 - x^n}
$$
be the generating function for the partitions. Show that
$$
\log F(x) \sim \frac{\pi^2}{6(1 - x)} \quad \text{as } x \to 1, \text{ with } 0 < x < 1.
$$
[Hint: Use $\log F(x) = \sum \log(1/(1 - x^n))$ and $\log(1/(1 - x^n)) = \sum (1/m) x^{nm}$, so
$$
\log F(x) = \sum \frac{1}{m} \frac{x^m}{1 - x^m}.
$$
Use also $m x^{m-1}(1 - x) < 1 - x^m < m(1 - x)$.]
:::

::: {.solution}
For $0<x<1$ all the double series involved are positive, so expanding $\log(1/(1-x^n))$ and summing over $n$ first is legitimate and gives $\log F(x)=\sum_m\frac1m\frac{x^m}{1-x^m}$; the printed inequality $mx^{m-1}(1-x)\le1-x^m\le m(1-x)$ then squeezes $(1-x)\log F(x)$ between $\sum x^m/m^2$ and $x\sum1/m^2$, both of which tend to $\zeta(2)=\pi^2/6$. The argument is this card's own -- it is the printed hint's route -- since no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #expansion}
For $0<x<1$, $\displaystyle\log F(x)=\sum_{m=1}^\infty\frac1m\frac{x^m}{1-x^m}$.

::: pf-proof
Each factor $\dfrac1{1-x^n}$ is the sum of the convergent geometric series $\sum_{k\ge0}x^{nk}$, and its logarithm is $-\log(1-x^n)=\sum_{k\ge1}\dfrac{x^{nk}}{k}$, since $-\log(1-u)=\sum_{k\ge1}u^k/k$ on $0\le u<1$ and the series has positive terms. All terms of the resulting double series $\sum_{n\ge1}\sum_{k\ge1}x^{nk}/k$ are positive, so it converges to the same sum in either order (monotone convergence for sums of nonnegative reals), and summing over $n$ first gives
$$
\log F(x)=\sum_{k\ge1}\frac1k\sum_{n\ge1}(x^k)^n=\sum_{k\ge1}\frac1k\cdot\frac{x^k}{1-x^k},
$$
the inner sum being geometric with ratio $x^k<1$.
:::

:::


::: {.pf-step #inequality}
For $m\ge1$ and $0<x<1$, $mx^{m-1}(1-x)\le1-x^m\le m(1-x)$.

::: pf-proof
$1-x^m=(1-x)(1+x+\cdots+x^{m-1})$. The sum in parentheses has $m$ terms, each at most $1$ and each at least $x^{m-1}$ because $x<1$ makes $x^j$ decreasing in $j$; so $mx^{m-1}\le1+x+\cdots+x^{m-1}\le m$, and multiplying by the positive number $1-x$ gives the display.
:::

:::


::: {.pf-step #squeeze}
For $m\ge1$, $\displaystyle\frac{x^m}{m^2}\le(1-x)\frac1m\frac{x^m}{1-x^m}\le\frac{x}{m^2}$.

::: pf-proof
By step [](#inequality){.pf-ref}, $1-x^m\ge mx^{m-1}(1-x)$ gives $(1-x)\dfrac1m\dfrac{x^m}{1-x^m}\le\dfrac{(1-x)x^m}{m\cdot mx^{m-1}(1-x)}=\dfrac{x}{m^2}$, and $1-x^m\le m(1-x)$ gives $(1-x)\dfrac1m\dfrac{x^m}{1-x^m}\ge\dfrac{(1-x)x^m}{m\cdot m(1-x)}=\dfrac{x^m}{m^2}$.
:::

:::


::: {.pf-step #bounded}
$\displaystyle\sum_{m\ge1}\frac{x^m}{m^2}\le(1-x)\log F(x)\le x\sum_{m\ge1}\frac1{m^2}$.

::: pf-proof
Multiply the identity of step [](#expansion){.pf-ref} by $1-x>0$ and apply step [](#squeeze){.pf-ref} to each term; the resulting series have nonnegative terms, so summing the inequalities termwise is legitimate, which is exactly the display.
:::

:::


::: {.pf-step #limits}
Both bounds tend to $\zeta(2)=\dfrac{\pi^2}{6}$ as $x\uparrow1$.

::: pf-proof
For $0<x<1$ one has $x^m\le1$ and $x^m\uparrow1$ as $x\uparrow1$ for each fixed $m$; by dominated convergence for series with the summable dominating sequence $1/m^2$ (equivalently by monotone convergence), $\sum_m x^m/m^2\to\sum_m1/m^2=\zeta(2)$, and $x\sum_m1/m^2\to\zeta(2)$ as $x\to1$. The value $\zeta(2)=\pi^2/6$ is Euler's evaluation of the series.
:::

:::


::: {.pf-step #conclusion}
$\displaystyle\log F(x)\sim\frac{\pi^2}{6(1-x)}$ as $x\uparrow1$.

::: pf-proof
By steps [](#bounded){.pf-ref} and [](#limits){.pf-ref} the product $(1-x)\log F(x)$ is squeezed between two quantities with the same limit $\pi^2/6$, so $(1-x)\log F(x)\to\pi^2/6$; dividing by $1-x>0$ gives the asserted asymptotic equivalence.
:::

:::

:::
:::
