---
schema: qual/card@1
id: P-KPFEF
kind: problem
title: Vanishing of $L^1$ tails without $f(x)\to 0$; a decreasing $f\in L^1([1,\infty))$
  has $xf(x)\to 0$; $xf(x)\to 0$ need not imply integrability
classification:
  areas:
  - real-analysis
  topics:
  - Small Tails
  - L¹
  - Limits
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 2 of the UGA Spring 2020 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced invalid tail estimates and monotonicity inequalities, and repaired the part (c) counterexample at the endpoint x=1.
---

::: {.problem}
a. Prove that if $f\in L^1(\RR)$ then
\[
\lim_{N\to \infty} \int _{\abs{x} \geq N} \abs{f(x)} \, dx = 0
,\]
and demonstrate that it is not necessarily the case that $f(x) \to 0$ as $\abs{x}\to \infty$.

b. Prove that if $f\in L^1([1, \infty))$ and is decreasing, then $\lim_{x\to\infty}f(x) =0$ and in fact $\lim_{x\to \infty} xf(x) = 0$.

c. If $f: [1, \infty) \to [0, \infty)$ is decreasing with $\lim_{x\to \infty} xf(x) = 0$, does this ensure that $f\in L^1([1, \infty))$?
:::

:::{.concept}
\envlist
- Limits
- Cauchy Criterion for Integrals: $\int_a^\infty f(x) \,dx$ converges iff for every $\eps>0$ there exists an $M_0$ such that $A,B\geq M_0$ implies $\abs{\int_A^B f} < \eps$, i.e. $\abs{\int_A^B f} \converges{A\to\infty}\to 0$.
- Integrals of $L^1$ functions have vanishing tails: $\int_{N}^\infty \abs{f} \converges{N\to\infty}\too 0$.
- Mean Value Theorem for Integrals: $\int_a^b f(t)\, dt = (b-a) f(c)$ for some $c\in [a, b]$.
:::

::: solution
<1>1. Prove the $L^1$ tails vanish, and give a counterexample to pointwise decay.
::: proof
Since $|f|\in L^1(\mathbb R)$ and
\[
\mathbf1_{\{|x|\ge N\}}|f(x)|\longrightarrow0
\]
pointwise as $N\to\infty$, while
\[
0\le \mathbf1_{\{|x|\ge N\}}|f(x)|\le |f(x)|,
\]
the Dominated Convergence Theorem gives
\[
\boxed{\int_{|x|\ge N}|f(x)|\,dx\longrightarrow0.}
\]

Pointwise decay need not follow. For example, let
\[
f(x)=\sum_{k=1}^\infty \mathbf1_{[k,k+2^{-k}]}(x).
\]
The intervals are disjoint up to endpoints and
\[
\|f\|_1=\sum_{k=1}^\infty 2^{-k}<\infty,
\]
so $f\in L^1(\mathbb R)$. But $f(k)=1$ for every positive integer $k$, hence $f(x)$ does not tend to $0$ as $x\to\infty$.
:::

<1>2. If $f$ is decreasing and integrable on $[1,\infty)$, prove $f(x)\to0$ and $xf(x)\to0$.
::: proof
Because $f$ is decreasing, the extended limit
\[
L:=\lim_{x\to\infty}f(x)
\]
exists. If $L\ne0$ or $|L|=\infty$, then $|f(x)|$ is bounded below by a positive constant for all sufficiently large $x$, contradicting $f\in L^1([1,\infty))$. Hence
\[
L=0.
\]
Since $f$ is decreasing and tends to $0$, necessarily $f(x)\ge0$ for every $x\ge1$.

For $x\ge2$ and $t\in[x/2,x]$, monotonicity gives $f(t)\ge f(x)$. Therefore
\[
\frac{x}{2}f(x)
\le \int_{x/2}^{x} f(t)\,dt
\le \int_{x/2}^{\infty}|f(t)|\,dt.
\]
The last tail tends to $0$ because $f\in L^1$. Thus
\[
0\le xf(x)
\le 2\int_{x/2}^{\infty}|f(t)|\,dt
\longrightarrow0.
\]
Consequently
\[
\boxed{xf(x)\to0,}
\]
and the already established $f(x)\to0$ follows as well.
:::

<1>3. Show that $xf(x)\to0$ does not imply integrability.
::: proof
Define
\[
f(x)=
\begin{cases}
1/e,&1\le x\le e,\\
\dfrac1{x\log x},&x>e.
\end{cases}
\]
This function is nonnegative and decreasing on $[1,\infty)$. Moreover, for $x>e$,
\[
xf(x)=\frac1{\log x}\longrightarrow0.
\]
However,
\[
\int_1^\infty f(x)\,dx
\ge \int_e^\infty \frac{dx}{x\log x}
=\infty.
\]
Hence the condition $xf(x)\to0$ does not imply $f\in L^1([1,\infty))$.
:::
:::
