---
schema: qual/card@1
id: P-JHUSP01RAE
kind: problem
title: "Integral operators with continuous kernel map the unit ball of C[0,1] to a precompact set"
classification:
  areas:
  - real-analysis
  topics:
  - Compact Operators
  - Integral Operators
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 5 of the JHU Real Analysis Qualifying Exam, Spring 2001, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $K\in C([0,1]\times[0,1])$ and define
$$
Tf(x)=\int_0^1K(x,y)f(y)\,dy
$$
for $f\in C([0,1])$. Prove that $Tf\in C([0,1])$. Moreover, prove that
$$
\Omega=\{Tf:\norm{f}_\infty\le1\}
$$
is precompact in $C([0,1])$ with the supremum norm.
:::

::: {.solution}

The argument is the card's own: uniform continuity of the kernel gives both the continuity of $Tf$ and the equicontinuity of the image of the unit ball, and Arzelà--Ascoli plus completeness of $C([0,1])$ turns that into precompactness. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $K\in C([0,1]^{2})$, $\norm{K}_{\infty}=\max\abs K$, and $Tf(x)=\int_{0}^{1}K(x,y)f(y)\,dy$ for $f\in C([0,1])$; let $\Omega=\{Tf:\norm{f}_{\infty}\le1\}$.

::: pf

::: {.pf-step #continuous}
$Tf\in C([0,1])$ for every $f\in C([0,1])$.

::: pf-proof
$K$ is continuous on the compact square, hence uniformly continuous: for $\varepsilon>0$ there is $\delta>0$ with $\abs{K(x,y)-K(x',y)}<\varepsilon$ whenever $\abs{x-x'}<\delta$, uniformly in $y$. So if $x_{n}\to x$ then $\sup_{y}\abs{K(x_{n},y)-K(x,y)}\to0$, and
$$
\abs{Tf(x_{n})-Tf(x)}\le\int_{0}^{1}\abs{K(x_{n},y)-K(x,y)}\abs{f(y)}\,dy\le\norm{f}_{\infty}\sup_{y}\abs{K(x_{n},y)-K(x,y)}\longrightarrow0 .
$$
So $Tf$ is continuous at $x$, and $x$ was arbitrary.
:::

:::

::: {.pf-step #bounded}
$\Omega$ is uniformly bounded: $\abs{Tf(x)}\le\norm{K}_{\infty}$ for every $f$ with $\norm{f}_{\infty}\le1$ and every $x$.

::: pf-proof
$\abs{Tf(x)}\le\int_{0}^{1}\abs{K(x,y)}\abs{f(y)}\,dy\le\norm{K}_{\infty}\norm{f}_{\infty}\le\norm{K}_{\infty}$, using $\abs{K(x,y)}\le\norm{K}_{\infty}$ and $\abs{f(y)}\le\norm{f}_{\infty}\le1$.
:::

:::

::: {.pf-step #equicontinuous}
$\Omega$ is equicontinuous, with a modulus depending only on $K$.

::: pf-proof
For $x,x'\in[0,1]$ and $f$ with $\norm{f}_{\infty}\le1$,
$$
\abs{Tf(x)-Tf(x')}\le\int_{0}^{1}\abs{K(x,y)-K(x',y)}\abs{f(y)}\,dy\le\sup_{y}\abs{K(x,y)-K(x',y)},
$$
and the right-hand side is independent of $f$ and tends to $0$ as $x'\to x$ by the uniform continuity of $K$ on the square. So for $\varepsilon>0$ there is $\delta>0$ with $\abs{Tf(x)-Tf(x')}<\varepsilon$ whenever $\abs{x-x'}<\delta$, for every $f$ in the unit ball at once.
:::

:::

::: {.pf-step #precompact}
$\Omega$ is precompact in the supremum norm.

::: pf-proof
$\Omega$ is a uniformly bounded and equicontinuous family of continuous functions on the compact interval $[0,1]$ by steps [](#bounded){.pf-ref} and [](#equicontinuous){.pf-ref}, so by the Arzelà--Ascoli theorem every sequence in $\Omega$ has a subsequence converging uniformly on $[0,1]$; the limit is continuous, hence lies in $C([0,1])$. A subset of a complete metric space in which every sequence has a convergent subsequence is relatively compact, and $C([0,1])$ is complete in the supremum norm; the closure of $\Omega$ is therefore compact, which is precompactness of $\Omega$.
:::

:::

:::
:::
