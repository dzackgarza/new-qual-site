---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-SEQ1
kind: problem
title: Radii of convergence for sums and coefficientwise products of power series
classification:
  areas:
  - real-analysis
  topics:
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
(January 2006, 1) Let the power series series $\sum_{n=0}^{\infty}a_nx^n$ and $\sum_{n=0}^{\infty}b_nx^n$ have radii of convergence $R_1$ and $R_2$, respectively.

(a) If $R_1\ne R_2$, prove that the radius of convergence, $R$, of the power series $\sum_{n=0}^{\infty}(a_n+b_n)x^n$ is $\min\{R_1,R_2\}$.
    What can be said about $R$ when $R_1=R_2$?

(b) Prove that the radius of convergence, $R$, of $\sum_{n=0}^{\infty}a_nb_nx^n$ satisfies $R\ge R_1R_2$.
    Show by means of an example that this inequality can be strict.
:::

::: {.solution}

::: pf

::: pf-step

(a) If $R_1\ne R_2$, then $R=\min\{R_1,R_2\}$; if $R_1=R_2=R_0$, then $\boxed{R\ge R_0}$, and equality need not hold.

::: pf-proof

::: pf-step

If $R_1\ne R_2$, the radius of $\sum_{n\ge0}(a_n+b_n)x^n$ is $\min\{R_1,R_2\}$.

::: pf-proof

By symmetry suppose $R_1<R_2$, allowing $R_1=0$ or $R_2=\infty$. On $\abs{x}<R_1$, both original series converge absolutely, so their sum does too and $R\ge R_1$. If $R>R_1$, pick a positive real $x$ with $R_1<x<\min\{R,R_2\}$.
Both the sum series and the $b_n$-series converge at $x$, hence their difference $\sum a_nx^n$ converges, contradicting its radius $R_1$.
Thus $R\le R_1$.

:::

:::

::: pf-step

If $R_1=R_2=R_0$, the sum radius satisfies $R\ge R_0$, and equality need not hold.

::: pf-proof

Both series converge absolutely for every $\abs{x}<R_0$, so their sum does as well.
If $R_0=\infty$, this forces $R=\infty$.
For $R_0=1$, the choice $a_n=1$, $b_n=-1$ gives sum radius $\infty$, and $a_n=1$, $b_n=-1+2^{-n}$ gives sum radius $2$.
Equality occurs when $a_n=b_n=1$.

:::

:::

:::

:::

::: pf-step

(b) $R\ge R_1R_2$ whenever the extended-real product is defined, and the inequality can be strict.

::: pf-proof

::: {.pf-step #s3}

For every $0<r<R_1$ and $0<s<R_2$, the coefficientwise product series has radius $R\ge rs$.

::: pf-proof

Absolute convergence of $\sum a_nr^n$ and $\sum b_ns^n$ gives finite constants $A,B$ such that $\abs{a_n}r^n\le A$ and $\abs{b_n}s^n\le B$ for every $n$.
For $\abs{x}<rs$,
$$
\abs{a_nb_nx^n}\le AB\left(\frac{\abs{x}}{rs}\right)^n.
$$
The geometric majorant is summable, proving absolute convergence of the product series on $\abs{x}<rs$.

:::

:::

::: pf-step

$R\ge R_1R_2$ whenever the extended-real product is defined.

::: pf-proof

If both radii are positive, the supremum of $rs$ in step [](#s3){.pf-ref} is $R_1R_2$, including when a radius is infinite.
If either radius is zero and the other finite, $R\ge0$ is automatic.
If one radius is zero and the other infinite, $R_1R_2$ is undefined, and step [](#s3){.pf-ref} is the unambiguous formulation.

:::

:::

::: pf-step

The inequality can be strict.

::: pf-proof

Let $a_{2k}=1,\ a_{2k+1}=0$ and $b_{2k}=0,\ b_{2k+1}=1$.
Both original radii are $1$, whereas $a_nb_n=0$ for every $n$, giving product radius $\infty>1$.

:::

:::

:::

:::

:::

:::

::: {.remark}
The source page literally says “the power series series” in its opening sentence; that wording is preserved here.
:::
