---
schema: qual/card@1
id: P-JCEPZ
kind: problem
title: Convergence and limit of $x_{n+1}=\frac{1+x_n}{2+x_n}$ with $x_1>0$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
  - Fixed Points
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UGA Fall 2021 real-analysis qualifying exam; repaired the legacy fixed-point calculation, whose positive root was off by a factor of 2, and supplied a genuine uniform contraction constant.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's proof into numbered steps; the contraction estimate, the fixed-point
    equation and the root choice are unchanged. Checked: positivity of the iterates, the range of
    T, the derivative bound, the completeness of [0, infinity) as a closed subset, and the algebra
    of the fixed-point equation. Not checked against a printed source: the UGA preliminary
    examinations are not retained in tmp/sources and the card records no page.
---

::: {.problem}
Let $\left\{x_{n}\right\}_{n=1}^{\infty}$ be a sequence of real numbers such that $x_{1}>0$ and
$$
x_{n+1}=1-\left(2+x_{n}\right)^{-1}=\frac{1+x_{n}}{2+x_{n}} \text {. }
$$
Prove that the sequence $\left\{x_{n}\right\}$ converges, and find its limit.
:::


::: {.solution}

The argument is the card's own: no solution set for this examination is retained in `tmp/sources`, so nothing below is transcribed, and the card's existing solution is restructured into numbered steps. Here $x_1>0$ and $x_{n+1}=T(x_n)$ with $T(x)=\frac{1+x}{2+x}$; the criterion used is the Banach fixed-point theorem: a map of a complete metric space into itself that contracts distances by a factor $q<1$ has a unique fixed point, and every orbit converges to it.

::: pf

::: {.pf-step #pos}

$x_n>0$ for every $n$, and $T$ maps $[0,\infty)$ into $[1/2,1)$.

::: pf-proof

For $x\geq0$ the number $2+x\geq2$ is positive, so $T(x)=1-\frac{1}{2+x}$ is defined, and $\frac{1}{2+x}\in(0,\frac12]$ gives $T(x)\in[\frac12,1)$. Induction on $n$ from $x_1>0$ then gives $x_n>0$.

:::

:::

::: {.pf-step #deriv}

$T'(x)=\frac{1}{(2+x)^{2}}\leq\frac14$ for $x\geq0$.

::: pf-proof

Differentiate $T(x)=1-(2+x)^{-1}$.

:::

:::

::: {.pf-step #contract}

$\abs{T(x)-T(y)}\leq\frac14\abs{x-y}$ for $x,y\geq0$.

::: pf-proof

The mean value theorem gives $T(x)-T(y)=T'(c)(x-y)$ for some $c$ between $x$ and $y$, and $c\geq0$ so $T'(c)\leq\frac14$ by step [](#deriv){.pf-ref}.

:::

:::

::: {.pf-step #banach}

The sequence converges, and its limit $L$ satisfies $L=T(L)$.

::: pf-proof

$[0,\infty)$ is a closed subset of $\RR$, hence complete, and $T$ maps it into itself with the contraction estimate of step [](#contract){.pf-ref} and factor $\frac14<1$. The Banach fixed-point theorem then gives a fixed point $L\in[0,\infty)$, unique, with $x_n\to L$; a limit of the recursion $x_{n+1}=T(x_n)$ with $T$ continuous is a fixed point.

:::

:::

::: {.pf-step #quad}

$L^{2}+L-1=0$.

::: pf-proof

From $L=\frac{1+L}{2+L}$: multiplying by $2+L$, which is positive and so nonzero, gives $L(2+L)=1+L$, that is $L^{2}+L-1=0$.

:::

:::

::: {.pf-step #done}

$\lim_{n\to\infty}x_n=\frac{\sqrt5-1}{2}$.

::: pf-proof

The roots of step [](#quad){.pf-ref} are $\frac{-1\pm\sqrt5}{2}$, of which only $\frac{\sqrt5-1}{2}$ is nonnegative; the other is negative and $L\in[0,\infty)$.

:::

:::

:::

:::
