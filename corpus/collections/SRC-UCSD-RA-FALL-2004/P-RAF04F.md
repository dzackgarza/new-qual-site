---
schema: qual/card@1
id: P-RAF04F
kind: problem
title: "L^1 convergence of derivatives implies absolute continuity of the limit"
classification:
  areas:
  - real-analysis
  topics:
  - Absolute Continuity
  - L1 Convergence
  - Fundamental Theorem of Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the official UCSD Fall 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $f_n : \mathbb{R} \to \mathbb{R}$ be a sequence of absolutely continuous functions such that $f_n' \in L^1(\mathbb{R}, m)$ and $c := \lim_{n \to \infty} f_n(0)$ exists in $\mathbb{R}$.
Further assume there exists $g \in L^1(\mathbb{R}, m)$ such that $\lim_{n \to \infty} \int_\mathbb{R} |g(x) - f_n'(x)| \, dx = 0$.

(a) Show that $f(x) := \lim_{n \to \infty} f_n(x)$ exists for all $x \in \mathbb{R}$.

(b) Show that $f$ is absolutely continuous and $f'(x) = g(x)$ for $m$-a.e. $x$.
:::

::: solution
<1>1. Write each $f_n$ as a primitive of its derivative.
::: proof
Since $f_n$ is absolutely continuous, for every $x\in\mathbb R$,
\[
f_n(x)=f_n(0)+\int_0^x f_n'(t)\,dt.
\]
Define
\[
F(x)=c+\int_0^x g(t)\,dt.
\]
Then
\[
|f_n(x)-F(x)|
\le |f_n(0)-c|+
\left|\int_0^x(f_n'(t)-g(t))\,dt\right|.
\]
For every $x$,
\[
\left|\int_0^x(f_n'-g)\right|
\le \int_{\mathbb R}|f_n'(t)-g(t)|\,dt.
\]
Hence
\[
\sup_{x\in\mathbb R}|f_n(x)-F(x)|
\le |f_n(0)-c|+\|f_n'-g\|_1\longrightarrow0.
\]
Therefore $f_n(x)\to F(x)$ for every $x$, so the pointwise limit exists and
\[
\boxed{f(x)=c+\int_0^x g(t)\,dt.}
\]
:::

<1>2. Prove absolute continuity of the limit.
::: proof
Let $\varepsilon>0$. Since $g\in L^1(\mathbb R)$, the Lebesgue integral is absolutely continuous: there exists $\delta>0$ such that
\[
m(E)<\delta\quad\Longrightarrow\quad\int_E|g|<\varepsilon.
\]
For finitely many pairwise disjoint intervals $(a_j,b_j)$ with
\[
\sum_j(b_j-a_j)<\delta,
\]
we have
\[
\begin{aligned}
\sum_j|f(b_j)-f(a_j)|
&=\sum_j\left|\int_{a_j}^{b_j}g(t)\,dt\right|\\
&\le \int_{\bigcup_j(a_j,b_j)}|g(t)|\,dt
<\varepsilon.
\end{aligned}
\]
Thus $f$ is absolutely continuous.
:::

<1>3. Identify the derivative.
::: proof
The Lebesgue Fundamental Theorem of Calculus applied to
\[
f(x)=c+\int_0^x g(t)\,dt
\]
gives
\[
\boxed{f'(x)=g(x)}
\]
for almost every $x\in\mathbb R$.
:::
:::
