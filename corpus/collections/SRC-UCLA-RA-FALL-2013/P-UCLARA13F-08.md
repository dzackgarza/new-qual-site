---
schema: qual/card@1
id: P-UCLARA13F-08
kind: problem
title: Two integral limits
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
Compute the following limits.

(a) For $n\in\NN$,
$$
\lim_{k\to\infty}\int_0^k x^n\left(1-\frac{x}{k}\right)^k\,dx.
$$

(b)
$$
\lim_{k\to\infty}\int_0^\infty\left(1+\frac{x}{k}\right)^{-k}\cos(x/k)\,dx.
$$
:::

::: {.solution}

::: pf

::: pf-step

For part (a), extend the integrand to $[0,\infty)$ by setting
$$
F_k(x)=
\begin{cases}
x^n(1-x/k)^k,&0\leq x\leq k,\\
0,&x>k.
\end{cases}
$$


::: pf-proof

Then the integral in part (a) is exactly $\int_0^\infty F_k(x)\,dx$.

:::

:::

::: {.pf-step #s1-2}

For every fixed $x\geq0$,
$$
F_k(x)\longrightarrow x^ne^{-x}.
$$


::: pf-proof

For all sufficiently large $k$, one has $x<k$, and the standard exponential limit gives
$$
\left(1-\frac{x}{k}\right)^k\to e^{-x}.
$$

:::

:::

::: {.pf-step #s1-3}

For $0\leq x\leq k$,
$$
0\leq\left(1-\frac{x}{k}\right)^k\leq e^{-x}.
$$


::: pf-proof

For $0\leq t<1$, $\log(1-t)\leq-t$. Taking $t=x/k$ gives
$$
k\log(1-x/k)\leq-x,
$$
and exponentiation yields the estimate. At $x=k$ the left side is zero.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
0\leq F_k(x)\leq x^ne^{-x},
$$
and $x^ne^{-x}\in L^1([0,\infty))$.


::: pf-proof

The bound follows from step [](#s1-3){.pf-ref}, including the region $x>k$ where $F_k=0$. The gamma integral
$$
\int_0^\infty x^ne^{-x}\,dx=n!
$$
is finite.

:::

:::

::: {.pf-step #s1-5}

Dominated convergence gives
$$
\boxed{
\lim_{k\to\infty}\int_0^k x^n\left(1-\frac{x}{k}\right)^kdx=n!.}
$$


::: pf-proof

Apply the dominated convergence theorem using steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref}, then evaluate the gamma integral.

:::

:::

::: {.pf-step #s1-6}

For part (b), substitute
$$
x=kt.
$$
Then
$$
\int_0^\infty\left(1+\frac{x}{k}\right)^{-k}\cos(x/k)\,dx
=k\int_0^\infty(1+t)^{-k}\cos t\,dt.
$$


::: pf-proof

Under $x=kt$, one has $dx=kdt$, $1+x/k=1+t$, and $\cos(x/k)=\cos t$.

:::

:::

::: {.pf-step #s1-7}

Integrating by parts once gives, for $k>1$,
$$
k\int_0^\infty(1+t)^{-k}\cos t\,dt
=\frac{k}{k-1}
-\frac{k}{k-1}\int_0^\infty(1+t)^{1-k}\sin t\,dt.
$$


::: pf-proof

Since
$$
(1+t)^{-k}=-\frac1{k-1}\frac d{dt}(1+t)^{1-k},
$$
integration by parts yields
$$
\int_0^\infty(1+t)^{-k}\cos t\,dt
=\frac1{k-1}
-\frac1{k-1}\int_0^\infty(1+t)^{1-k}\sin t\,dt.
$$
The boundary term at infinity vanishes for $k>1$, and the value at $0$ is $1/(k-1)$. Multiply by $k$.

:::

:::

::: {.pf-step #s1-8}

For $k>2$,
$$
\left|\int_0^\infty(1+t)^{1-k}\sin t\,dt\right|
\leq\frac1{k-2}.
$$


::: pf-proof

Use $|\sin t|\leq1$ and compute
$$
\int_0^\infty(1+t)^{1-k}\,dt=\frac1{k-2}.
$$

:::

:::

::: {.pf-step #s1-9}

Hence the error term in step [](#s1-7){.pf-ref} tends to zero, while
$$
\frac{k}{k-1}\to1.
$$


::: pf-proof

By step [](#s1-8){.pf-ref}, the absolute value of the error term is at most
$$
\frac{k}{(k-1)(k-2)}\to0.
$$
The first term plainly tends to $1$.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
\lim_{k\to\infty}\int_0^\infty\left(1+\frac{x}{k}\right)^{-k}\cos(x/k)\,dx=1.}
$$


::: pf-proof

Combine steps [](#s1-6){.pf-ref} through [](#s1-9){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-5){.pf-ref} and [](#s1-10){.pf-ref} give the two requested limits.

:::

:::

:::
