---
schema: qual/card@1
id: P-RAF21B
kind: problem
title: 'Nonnegative Borel functions with infinite integral on every interval'
classification:
  areas:
  - real-analysis
  topics:
  - Borel Measurable Functions
  - Lebesgue Integration
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Does there exist a Borel measurable function $f : \mathbb{R} \to [0, \infty)$ such that $\int_a^b f(x) \, dx = \infty$ for all real numbers $a < b$?
Either find an example or show that no such $f$ exists.
:::

::: solution
<1>1. Choose tiny intervals that visit every rational interval infinitely often.
::: proof
Let $(B_j)_{j\ge1}$ enumerate the open intervals with rational endpoints. Choose a sequence $j(n)$ such that every positive integer occurs infinitely often; for example
\[
1,1,2,1,2,3,1,2,3,4,\ldots.
\]

For each $n$, choose a nonempty open interval
\[
E_n\subset B_{j(n)}
\]
with
\[
m(E_n)\le 2^{-n}.
\]
Set
\[
a_n:=\frac1{m(E_n)}.
\]
Then
\[
\int_{\mathbb R} a_n\mathbf1_{E_n}(x)\,dx=1.
\]
:::

<1>2. Form the nonnegative series and make it finite everywhere.
::: proof
Define
\[
F(x):=\sum_{n=1}^\infty a_n\mathbf1_{E_n}(x).
\]
This is a Borel measurable $[0,\infty]$-valued function. Since
\[
\sum_{n=1}^\infty m(E_n)<\infty,
\]
the Borel--Cantelli lemma gives
\[
m\!\left(\limsup_{n\to\infty}E_n\right)=0.
\]
Thus almost every $x$ belongs to only finitely many of the sets $E_n$, so $F(x)<\infty$ almost everywhere.

Let
\[
N:=\{x:F(x)=\infty\}.
\]
Then $N$ is Borel and $m(N)=0$. Define
\[
f(x):=
\begin{cases}
F(x),&x\notin N,\\
0,&x\in N.
\end{cases}
\]
Then $f:\mathbb R\to[0,\infty)$ is Borel measurable and finite everywhere.
:::

<1>3. Every nonempty interval has infinite integral.
::: proof
Fix $a<b$. Choose a rational interval $B_j$ with
\[
B_j\subset(a,b).
\]
There are infinitely many $n$ with $j(n)=j$, and for all such $n$,
\[
E_n\subset B_j\subset(a,b).
\]
By Tonelli's theorem,
\[
\begin{aligned}
\int_a^b F(x)\,dx
&=\sum_{n=1}^\infty a_n m(E_n\cap(a,b))\\
&\ge \sum_{\{n:j(n)=j\}} a_n m(E_n)\\
&=\sum_{\{n:j(n)=j\}}1
=\infty.
\end{aligned}
\]
Since $f=F$ almost everywhere, the same is true for $f$:
\[
\boxed{\int_a^b f(x)\,dx=\infty\quad\text{for every }a<b.}
\]
Thus such a function exists.
:::
:::
