---
schema: qual/card@1
id: P-WESRA05-2
kind: problem
title: Lebesgue measure examples, monotone convergence, and a Cantor-stage function
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $X=[0,1]$, let $\mathcal A$ be the Borel sigma-algebra, and let $\lambda$ be normalized Lebesgue measure.

1. Compute the measures of
   \[
   [1/3,2/5],\qquad \mathbb Q\cap[0,1],\qquad (\mathbb R\setminus\mathbb Q)\cap[0,1],\qquad \overline{\mathbb Q}^{\,\mathrm{alg}}\cap[0,1],
   \]
   where the last set means the algebraic numbers in $[0,1]$.

2. State the monotone convergence theorem for $(X,\mathcal A,\lambda)$.

3. Let $C$ be the middle-thirds Cantor set.
   Define $f:[0,1]\to[0,\infty)$ by setting $f(x)=2^{-n}$ on every interval removed at stage $n$ of the Cantor construction, with the first removed middle third called stage $0$, and $f(x)=\pi$ on $C$.
   Prove that $f$ is measurable and compute $\int_0^1 f\,d\lambda$.
:::

::: {.solution}
<1>1. Compute the elementary measures.
::: {.proof}
The interval has length
\[
\lambda([1/3,2/5])=\frac25-\frac13=\boxed{\frac1{15}}.
\]
The rationals and the algebraic numbers are countable, hence have Lebesgue measure zero.
Therefore
\[
\lambda(\mathbb Q\cap[0,1])=0,
\qquad
\lambda(\{\text{algebraic numbers in }[0,1]\})=0.
\]
Since $[0,1]$ has measure $1$ and the rationals have measure zero,
\[
\lambda((\mathbb R\setminus\mathbb Q)\cap[0,1])=1.
\]
:::

<1>2. State monotone convergence.
::: {.proof}
If $0\le g_1\le g_2\le\cdots$ are measurable on $[0,1]$ and $g_n(x)\to g(x)$ pointwise, then
\[
\boxed{\int_0^1 g\,d\lambda=\lim_{n\to\infty}\int_0^1g_n\,d\lambda,}
\]
with the value $+\infty$ allowed.
:::

<1>3. Prove measurability of the Cantor-stage function.
::: {.proof}
Let $R_n$ be the union of the open intervals removed at stage $n$.
Each $R_n$ is a finite union of open intervals, hence Borel, and $C$ is closed.
The sets
\[
C,R_0,R_1,R_2,\ldots
\]
form a Borel partition of $[0,1]$.
Since $f$ is constant on each member of this countable Borel partition, $f$ is Borel measurable.
:::

<1>4. Compute its integral.
::: {.proof}
At stage $n$ there are $2^n$ removed intervals, each of length $3^{-(n+1)}$.
Hence
\[
\lambda(R_n)=\frac{2^n}{3^{n+1}}.
\]
The Cantor set has measure zero, so its value $\pi$ contributes nothing to the integral.
Therefore
\[
\begin{aligned}
\int_0^1 f\,d\lambda
&=\sum_{n=0}^\infty 2^{-n}\lambda(R_n)\\
&=\sum_{n=0}^\infty 2^{-n}\frac{2^n}{3^{n+1}}\\
&=\sum_{n=0}^\infty\frac1{3^{n+1}}
=\boxed{\frac12}.
\end{aligned}
\]
:::
:::
