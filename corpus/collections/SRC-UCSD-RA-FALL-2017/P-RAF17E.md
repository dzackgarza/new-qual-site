---
schema: qual/card@1
id: P-RAF17E
kind: problem
title: "Convolution with essentially bounded kernel is continuous"
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
  date: 2026-09-08
  note: Checked against Problem 5 of the official UCSD Fall 2017 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $g : \mathbb{R}^d \to \mathbb{R}^d$ be a measurable function which is essentially bounded, i.e. there exists $M < \infty$ such that $|g(x)| \leq M$ for $m$-a.e. $x \in \mathbb{R}^d$.
For $f \in L^1(m) := L^1(\mathbb{R}^d, m)$, let
$$
(f * g)(x) = \int_{\mathbb{R}^d} f(x-y)g(y)\,dy.
$$

1. Show $(f * g)(x)$ is well defined (i.e. the integral exists) and $|(f * g)(x)| \leq M\|f\|_1$ for all $x \in \mathbb{R}^d$.

2. Show $(f * g)(x)$ may also be written as
$$
(f * g)(x) = \int_{\mathbb{R}^d} f(y)g(x - y)\,dy.
$$

3. Verify $(f_n * g)(x)$ is continuous in $x$ for any $f_n \in C_c(\mathbb{R}^d)$.

4. Show, for $f \in L^1(m)$, that $f * g$ may be written as a uniformly convergent limit of continuous functions and hence $(f * g)(x)$ is continuous in $x$.
:::

::: solution
<1>1. Prove existence and the uniform bound.
::: proof
For every $x\in\mathbb R^d$,
\[
\int_{\mathbb R^d}|f(x-y)g(y)|\,dy
\le M\int_{\mathbb R^d}|f(x-y)|\,dy
=M\|f\|_1<\infty.
\]
Thus $(f*g)(x)$ is well defined for every $x$, and
\[
\boxed{|(f*g)(x)|\le M\|f\|_1.}
\]
:::

<1>2. Rewrite the convolution by a change of variables.
::: proof
In
\[
(f*g)(x)=\int f(x-y)g(y)\,dy,
\]
make the change of variables $z=x-y$. Since Lebesgue measure is translation invariant,
\[
(f*g)(x)
=\int_{\mathbb R^d} f(z)g(x-z)\,dz.
\]
Renaming $z$ as $y$ gives the desired formula.
:::

<1>3. Prove continuity for $f_n\in C_c(\mathbb R^d)$.
::: proof
For $h\in\mathbb R^d$,
\[
\begin{aligned}
|(f_n*g)(x+h)-(f_n*g)(x)|
&\le M\int_{\mathbb R^d}|f_n(x+h-y)-f_n(x-y)|\,dy\\
&=M\|\tau_h f_n-f_n\|_1,
\end{aligned}
\]
where $(\tau_hf_n)(z)=f_n(z+h)$. Since $f_n\in L^1$, translations are continuous in $L^1$:
\[
\|\tau_hf_n-f_n\|_1\longrightarrow0
\qquad(h\to0).
\]
The bound is independent of $x$, so $f_n*g$ is in fact uniformly continuous.
:::

<1>4. Approximate a general $f\in L^1$ by compactly supported continuous functions.
::: proof
Choose $f_n\in C_c(\mathbb R^d)$ such that
\[
\|f_n-f\|_1\longrightarrow0.
\]
By Step 1 applied to $f_n-f$,
\[
\sup_{x\in\mathbb R^d}|(f_n*g)(x)-(f*g)(x)|
\le M\|f_n-f\|_1
\longrightarrow0.
\]
Thus $f_n*g\to f*g$ uniformly. Each $f_n*g$ is continuous by Step 3, so the uniform limit $f*g$ is continuous. Hence
\[
\boxed{f*g\in C(\mathbb R^d).}
\]
:::
:::
