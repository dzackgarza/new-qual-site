---
schema: qual/card@1
id: P-MMCHV
kind: problem
title: Termwise differentiation of $\sum n^{-x}$ on $(1,\infty)$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
  - Differentiation
  - Uniform Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UGA August 2016 real-analysis qualifying exam; supplied the missing uniform-convergence argument needed for termwise differentiation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps and supplied two estimates the prose used without
    proof: that log n grows slower than any positive power, so log n <= C n^delta for a constant C
    and every n >= 2, and the arithmetic a - delta = (a+1)/2 > 1 that makes the majorant a p-series
    with exponent above 1. Also stated the differentiation theorem in the form applied: a series of
    C^1 functions converging at one point whose derivative series converges uniformly has a
    differentiable sum with the derivative series as its derivative. The mathematics is the
    transcribing sessions' own; no defect found.
---

::: {.problem}
Define
$$
f(x) = \sum_{n=1}^{\infty} \frac{1}{n^{x}}.
$$ 
Show that $f$ converges to a differentiable function on $(1, \infty)$ and that
$$
f'(x)  =\sum_{n=1}^{\infty}\left(\frac{1}{n^{x}}\right)^{\prime}.
$$

> Hint:
$$
\left(\frac{1}{n^{x}}\right)' = -\frac{1}{n^{x}} \ln n
$$
:::

::: {.solution}

The argument is the card's own, as the card's audit records; the statement is Problem 1 of the UGA August 2016 real-analysis qualifying examination.

For $x>1$ put $f(x)=\sum_{n=1}^{\infty}n^{-x}$ and $f_{N}(x)=\sum_{n=1}^{N}n^{-x}$, so that $f_{N}\to f$ pointwise on $(1,\infty)$.

::: pf

::: {.pf-step #uniform}
$\sum_{n}n^{-x}$ converges uniformly on every compact interval $[a,b]\subset(1,\infty)$.

::: pf-proof
For $x\in[a,b]$ and $n\geq1$ we have $n^{-x}\leq n^{-a}$, because $x\geq a>0$ and $t\mapsto n^{-t}$ is decreasing. The series $\sum_{n}n^{-a}$ converges, being a $p$-series with $p=a>1$. The Weierstrass $M$-test with $M_{n}=n^{-a}$ therefore gives uniform convergence on $[a,b]$.
:::

:::

::: {.pf-step #log-bound}
With $\delta=(a-1)/2>0$ there is $C>0$ such that $\log n\leq Cn^{\delta}$ for every $n\geq2$.

::: pf-proof
$\log n/n^{\delta}\to0$ as $n\to\infty$, since $\log$ grows slower than any positive power; a sequence tending to $0$ is bounded, so $\log n/n^{\delta}\leq C'$ for all $n\geq2$ and some $C'$, which is the assertion with $C=C'$. (At $n=1$ the logarithm vanishes.)
:::

:::

::: {.pf-step #derivative-series}
$\sum_{n}(\log n)\,n^{-x}$ converges uniformly on $[a,b]$.

::: pf-proof
The derivative of $n^{-x}$ in $x$ is $-(\log n)n^{-x}$. For $x\in[a,b]$, step [](#log-bound){.pf-ref} gives $\abs{(\log n)n^{-x}}=(\log n)n^{-x}\leq Cn^{\delta}n^{-a}=Cn^{-(a-\delta)}$ for $n\geq2$, the first factor contributing nothing at $n=1$ since $\log1=0$. Now $a-\delta=a-\tfrac{a-1}{2}=\tfrac{a+1}{2}>1$ because $a>1$, so $\sum_{n}n^{-(a-\delta)}$ is a convergent $p$-series and the $M$-test gives uniform convergence of the derivative series on $[a,b]$.
:::

:::

::: {.pf-step #differentiable}
$f$ is differentiable on $(1,\infty)$ and $f'(x)=\sum_{n}(\log n)\,n^{-x}$.

::: pf-proof
Each $f_{N}$ is a finite sum of $C^{1}$ functions, and $f_{N}\to f$ at every point of $[a,b]$ by step [](#uniform){.pf-ref}; the derivative series $\sum_{n}(n^{-x})'$ converges uniformly on $[a,b]$ by step [](#derivative-series){.pf-ref}. The theorem on termwise differentiation (a series of $C^{1}$ functions converging at one point whose derivatives converge uniformly is $C^{1}$ there, with termwise derivative) applies on $[a,b]$, so $f'(x)=\sum_{n}(n^{-x})'$ for $x\in[a,b]$. Every $x>1$ lies in such an interval, for instance $\bigl[(1+x)/2,\,(3+x)/2\bigr]$.
:::

:::

::: {.pf-step}
$f$ is differentiable on $(1,\infty)$ and $f'(x)=\sum_{n=1}^{\infty}\bigl(n^{-x}\bigr)'=-\sum_{n}\frac{\log n}{n^{x}}$.

::: pf-proof
Step [](#differentiable){.pf-ref} gives differentiability and the identity at every $x>1$, which is the assertion of the problem; substituting $-(n^{-x})'=(\log n)n^{-x}$ gives the displayed form.
:::

:::

:::

:::
