---
schema: qual/card@1
id: P-V4VXC
kind: problem
title: Maclaurin series of $xe^{2x}$ and a remainder bound on $[0,1/2]$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps. The collection is a preliminary examination, so the statement
    is the source and the argument is the card's own. Each step re-read and the arithmetic checked
    against a symbolic computation: the Maclaurin series is sum 2^n x^(n+1)/n!, so T_5 keeps
    n = 0..4 with coefficients 1, 2, 2, 4/3, 2/3; the sixth derivative is (64t + 192)e^{2t}, which
    the closed formula f^(k) = (2^k t + k 2^{k-1})e^{2t} gives at k = 6; on [0,1/2] that is at most
    224e and x^6 is at most 1/64, whence 7e/1440. The card also records that the true maximum error
    on the interval is about 0.0050, so the bound is not attained.
---

::: {.problem}
(a) Find the Maclaurin series expansion of $f(x) = xe^{2x}$ (that is, the Taylor series expansion of $f(x)$ about $a = 0$).

(b) If $T_5(x)$ is the polynomial consisting of the terms of the Maclaurin series of $f(x)$ through degree 5, and $T_5(x)$ is used to approximate $f(x)$ on the interval $[0,1/2]$, find a bound for the maximum error $\abs{f(x) - T_5(x)}$ on $[0,1/2]$.
:::

::: {.solution}
The argument is the card's own; the collection is a preliminary examination, so the statement is the source.

::: pf

::: {.pf-step #series}
$xe^{2x}=\sum_{n\ge0}\frac{2^{n}}{n!}x^{n+1}$.

::: pf-proof
$e^{2x}=\sum_{n\ge0}\frac{(2x)^{n}}{n!}=\sum_{n\ge0}\frac{2^{n}}{n!}x^{n}$ for every real $x$, and multiplying by $x$ multiplies each term by $x$; the series converges for all $x$ and remains the Maclaurin series of the product.
:::

:::

::: {.pf-step #t5}
$T_{5}(x)=x+2x^{2}+2x^{3}+\frac43x^{4}+\frac23x^{5}$.

::: pf-proof
Cut the series of step [](#series){.pf-ref} at degree $5$, that is at $n+1\le5$, i.e. $n\le4$: the coefficients are $\frac{2^{0}}{0!}=1$, $\frac{2^{1}}{1!}=2$, $\frac{2^{2}}{2!}=2$, $\frac{2^{3}}{3!}=\frac43$ and $\frac{2^{4}}{4!}=\frac23$.
:::

:::

::: {.pf-step #derivatives}
$f^{(k)}(t)=(2^{k}t+k\,2^{k-1})e^{2t}$ for $k\ge1$, and in particular $f^{(6)}(t)=(64t+192)e^{2t}$.

::: pf-proof
Induction on $k$: for $k=1$, $f'=e^{2x}+2xe^{2x}=(2x+1)e^{2x}$, which is the formula with $2^{1}=2$ and $1\cdot2^{0}=1$. If $f^{(k)}=(2^{k}t+k2^{k-1})e^{2t}$ then differentiating gives $\bigl(2^{k}+2(2^{k}t+k2^{k-1})\bigr)e^{2t}=\bigl(2^{k+1}t+(k+1)2^{k}\bigr)e^{2t}$, the formula at $k+1$. At $k=6$: $2^{6}=64$ and $6\cdot2^{5}=192$.
:::

:::

::: {.pf-step #taylor}
For $x\in[0,\tfrac12]$, $f(x)-T_{5}(x)=\dfrac{f^{(6)}(\xi)}{6!}x^{6}$ for some $\xi$ between $0$ and $x$.

::: pf-proof
Taylor's theorem with Lagrange remainder for $f$ at $0$: $T_{5}$ is the Taylor polynomial of degree $5$, and the remainder is the sixth derivative at an intermediate point divided by $6!$ times $x^{6}$.
:::

:::

::: {.pf-step #bound}
$\abs{f^{(6)}(\xi)}\le224e$ and $x^{6}\le\tfrac1{64}$ on the interval.

::: pf-proof
On $[0,\tfrac12]$ one has $64\xi\le32$, so $64\xi+192\le224$, and $e^{2\xi}\le e^{1}=e$ because $2\xi\le1$; multiplying gives the first bound. And $x^{6}\le(\tfrac12)^{6}=\tfrac1{64}$.
:::

:::

::: {.pf-step #error}
$\abs{f(x)-T_{5}(x)}\le\dfrac{7e}{1440}$ on $[0,\tfrac12]$.

::: pf-proof
Steps [](#taylor){.pf-ref} and [](#bound){.pf-ref} give
$$
\abs{f(x)-T_{5}(x)}\le\frac{224e}{720}\cdot\frac{1}{64}=\frac{224e}{46080}=\frac{7e}{1440},
$$
using $6!=720$ and $224/46080=7/1440$.
:::

:::

::: {.pf-step}
Both parts are answered.

::: pf-proof
Steps [](#series){.pf-ref}, [](#t5){.pf-ref} and [](#error){.pf-ref} give
$$
\boxed{f(x)=\sum_{n\ge0}\frac{2^{n}}{n!}x^{n+1},\qquad T_{5}(x)=x+2x^{2}+2x^{3}+\frac43x^{4}+\frac23x^{5},\qquad \max_{[0,1/2]}\abs{f-T_{5}}\le\frac{7e}{1440}\approx0.0132.}
$$
The bound is the worst case allowed by Taylor's theorem; the true maximum on the interval is smaller, about $0.0050$, so the estimate is not claimed to be attained.
:::

:::

:::
:::
