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

(a) For $n\in\mathbb N$,
\[
\lim_{k\to\infty}\int_0^k x^n\left(1-\frac{x}{k}\right)^k\,dx.
\]

(b)
\[
\lim_{k\to\infty}\int_0^\infty\left(1+\frac{x}{k}\right)^{-k}\cos(x/k)\,dx.
\]
:::

::: {.solution}
<1>1. For part (a), extend the integrand to $[0,\infty)$ by setting
\[
F_k(x)=
\begin{cases}
x^n(1-x/k)^k,&0\leq x\leq k,\\
0,&x>k.
\end{cases}
\]

::: {.proof}
Then the integral in part (a) is exactly $\int_0^\infty F_k(x)\,dx$.
:::

<1>2. For every fixed $x\geq0$,
\[
F_k(x)\longrightarrow x^ne^{-x}.
\]

::: {.proof}
For all sufficiently large $k$, one has $x<k$, and the standard exponential limit gives
\[
\left(1-\frac{x}{k}\right)^k\to e^{-x}.
\]
:::

<1>3. For $0\leq x\leq k$,
\[
0\leq\left(1-\frac{x}{k}\right)^k\leq e^{-x}.
\]

::: {.proof}
For $0\leq t<1$, $\log(1-t)\leq-t$. Taking $t=x/k$ gives
\[
k\log(1-x/k)\leq-x,
\]
and exponentiation yields the estimate. At $x=k$ the left side is zero.
:::

<1>4. Therefore
\[
0\leq F_k(x)\leq x^ne^{-x},
\]
and $x^ne^{-x}\in L^1([0,\infty))$.

::: {.proof}
The bound follows from step <1>3, including the region $x>k$ where $F_k=0$. The gamma integral
\[
\int_0^\infty x^ne^{-x}\,dx=n!
\]
is finite.
:::

<1>5. Dominated convergence gives
\[
\boxed{
\lim_{k\to\infty}\int_0^k x^n\left(1-\frac{x}{k}\right)^kdx=n!.}
\]

::: {.proof}
Apply the dominated convergence theorem using steps <1>2--<1>4, then evaluate the gamma integral.
:::

<1>6. For part (b), substitute
\[
x=kt.
\]
Then
\[
\int_0^\infty\left(1+\frac{x}{k}\right)^{-k}\cos(x/k)\,dx
=k\int_0^\infty(1+t)^{-k}\cos t\,dt.
\]

::: {.proof}
Under $x=kt$, one has $dx=kdt$, $1+x/k=1+t$, and $\cos(x/k)=\cos t$.
:::

<1>7. Integrating by parts once gives, for $k>1$,
\[
k\int_0^\infty(1+t)^{-k}\cos t\,dt
=\frac{k}{k-1}
-\frac{k}{k-1}\int_0^\infty(1+t)^{1-k}\sin t\,dt.
\]

::: {.proof}
Since
\[
(1+t)^{-k}=-\frac1{k-1}\frac d{dt}(1+t)^{1-k},
\]
integration by parts yields
\[
\int_0^\infty(1+t)^{-k}\cos t\,dt
=\frac1{k-1}
-\frac1{k-1}\int_0^\infty(1+t)^{1-k}\sin t\,dt.
\]
The boundary term at infinity vanishes for $k>1$, and the value at $0$ is $1/(k-1)$. Multiply by $k$.
:::

<1>8. For $k>2$,
\[
\left|\int_0^\infty(1+t)^{1-k}\sin t\,dt\right|
\leq\frac1{k-2}.
\]

::: {.proof}
Use $|\sin t|\leq1$ and compute
\[
\int_0^\infty(1+t)^{1-k}\,dt=\frac1{k-2}.
\]
:::

<1>9. Hence the error term in step <1>7 tends to zero, while
\[
\frac{k}{k-1}\to1.
\]

::: {.proof}
By step <1>8, the absolute value of the error term is at most
\[
\frac{k}{(k-1)(k-2)}\to0.
\]
The first term plainly tends to $1$.
:::

<1>10. Therefore
\[
\boxed{
\lim_{k\to\infty}\int_0^\infty\left(1+\frac{x}{k}\right)^{-k}\cos(x/k)\,dx=1.}
\]

::: {.proof}
Combine steps <1>6--<1>9.
:::

<1>11. Q.E.D.

::: {.proof}
Steps <1>5 and <1>10 give the two requested limits.
:::
:::
