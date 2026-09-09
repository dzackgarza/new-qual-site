---
schema: qual/card@1
id: P-RASP24D
kind: problem
title: "Weak convergence in l^p characterized by pointwise convergence and boundedness"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2024 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $A$ be a set and $1 < p < \infty$.
Prove that a sequence $f_n \in \ell^p(A)$ converges weakly to $f \in \ell^p(A)$ if and only if $(f_n)$ converges to $f$ pointwise and $\sup_n \|f_n\|_p < \infty$.
:::

::: solution
Let $q=p/(p-1)$.

<1>1. Weak convergence implies pointwise convergence.
::: proof
For each $a\in A$, define
\[
\delta_a(h):=h(a).
\]
Then
\[
|\delta_a(h)|\le \|h\|_p,
\]
so $\delta_a\in(\ell^p(A))^*$. If $f_n\rightharpoonup f$, then
\[
f_n(a)=\delta_a(f_n)\longrightarrow\delta_a(f)=f(a)
\]
for every $a\in A$.
:::

<1>2. Weak convergence implies norm boundedness.
::: proof
For each $n$, define
\[
T_n:(\ell^p(A))^*\to\mathbb C,
\qquad
T_n(\varphi)=\varphi(f_n).
\]
For each fixed $\varphi$, weak convergence of $f_n$ makes the scalar sequence $T_n(\varphi)$ convergent, hence bounded. Since $(\ell^p(A))^*$ is Banach, the Uniform Boundedness Principle gives
\[
\sup_n\|T_n\|<\infty.
\]
Under the canonical embedding of a normed space into its bidual,
\[
\|T_n\|=\|f_n\|_p.
\]
Therefore
\[
\sup_n\|f_n\|_p<\infty.
\]
:::

<1>3. Assume pointwise convergence and uniform boundedness, and prove weak convergence.
::: proof
Assume
\[
f_n(a)\to f(a)
\quad\text{for every }a\in A,
\qquad
\sup_n\|f_n\|_p\le M.
\]
Let $g\in\ell^q(A)$. Since $q<\infty$, finitely supported functions are dense in $\ell^q(A)$. Thus for every $\varepsilon>0$ there is a finite set $F\subset A$ such that, with
\[
g_F:=g\mathbf1_F,
\]
we have
\[
\|g-g_F\|_q<\varepsilon.
\]

For the finite-support part,
\[
\sum_{a\in A}(f_n(a)-f(a))g_F(a)
=\sum_{a\in F}(f_n(a)-f(a))g(a)
\longrightarrow0
\]
by pointwise convergence.

For the tail, Hölder's inequality gives
\[
\begin{aligned}
\left|
\sum_{a\in A}(f_n(a)-f(a))(g(a)-g_F(a))
\right|
&\le \|f_n-f\|_p\,\|g-g_F\|_q\\
&\le (M+\|f\|_p)\varepsilon.
\end{aligned}
\]
Hence
\[
\limsup_{n\to\infty}
\left|
\sum_{a\in A}(f_n(a)-f(a))g(a)
\right|
\le (M+\|f\|_p)\varepsilon.
\]
Since $\varepsilon$ is arbitrary,
\[
\sum_{a\in A}f_n(a)g(a)
\longrightarrow
\sum_{a\in A}f(a)g(a)
\]
for every $g\in\ell^q(A)$. Since
\[
(\ell^p(A))^*=\ell^q(A)
\qquad(1<p<\infty),
\]
this is exactly
\[
\boxed{f_n\rightharpoonup f\text{ in }\ell^p(A).}
\]
:::
:::
