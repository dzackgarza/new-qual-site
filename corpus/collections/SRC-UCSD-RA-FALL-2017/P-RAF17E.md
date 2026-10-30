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

::: {.problem}
Let $g : \RR^d \to \RR^d$ be a measurable function which is essentially bounded, i.e. there exists $M < \infty$ such that $\abs{g(x)} \leq M$ for $m$-a.e. $x \in \RR^d$.
For $f \in L^1(m) := L^1(\RR^d, m)$, let
$$
(f * g)(x) = \int_{\RR^d} f(x-y)g(y)\,dy.
$$

1. Show $(f * g)(x)$ is well defined (i.e. the integral exists) and $\abs{(f * g)(x)} \leq M\norm{f}_1$ for all $x \in \RR^d$.

2. Show $(f * g)(x)$ may also be written as
$$
(f * g)(x) = \int_{\RR^d} f(y)g(x - y)\,dy.
$$

3. Verify $(f_n * g)(x)$ is continuous in $x$ for any $f_n \in C_c(\RR^d)$.

4. Show, for $f \in L^1(m)$, that $f * g$ may be written as a uniformly convergent limit of continuous functions and hence $(f * g)(x)$ is continuous in $x$.
:::

::: {.solution}

::: pf

::: pf-step

Prove existence and the uniform bound.

::: pf-proof

For every $x\in\RR^d$,
$$
\int_{\RR^d}\abs{f(x-y)g(y)}\,dy
\le M\int_{\RR^d}\abs{f(x-y)}\,dy
=M\norm{f}_1<\infty.
$$
Thus $(f*g)(x)$ is well defined for every $x$, and
$$
\boxed{\abs{(f*g)(x)}\le M\norm{f}_1.}
$$

:::

:::

::: pf-step

Rewrite the convolution by a change of variables.

::: pf-proof

In
$$
(f*g)(x)=\int f(x-y)g(y)\,dy,
$$
make the change of variables $z=x-y$. Since Lebesgue measure is translation invariant,
$$
(f*g)(x)
=\int_{\RR^d} f(z)g(x-z)\,dz.
$$
Renaming $z$ as $y$ gives the desired formula.

:::

:::

::: pf-step

Prove continuity for $f_n\in C_c(\RR^d)$.

::: pf-proof

For $h\in\RR^d$,
$$
\begin{aligned}
\abs{(f_n*g)(x+h)-(f_n*g)(x)}
&\le M\int_{\RR^d}\abs{f_n(x+h-y)-f_n(x-y)}\,dy\\
&=M\norm{\tau_h f_n-f_n}_1,
\end{aligned}
$$
where $(\tau_hf_n)(z)=f_n(z+h)$. Since $f_n\in L^1$, translations are continuous in $L^1$:
$$
\norm{\tau_hf_n-f_n}_1\longrightarrow0
\qquad(h\to0).
$$
The bound is independent of $x$, so $f_n*g$ is in fact uniformly continuous.

:::

:::

::: pf-step

Approximate a general $f\in L^1$ by compactly supported continuous functions.

::: pf-proof

Choose $f_n\in C_c(\RR^d)$ such that
$$
\norm{f_n-f}_1\longrightarrow0.
$$
By Step 1 applied to $f_n-f$,
$$
\sup_{x\in\RR^d}\abs{(f_n*g)(x)-(f*g)(x)}
\le M\norm{f_n-f}_1
\longrightarrow0.
$$
Thus $f_n*g\to f*g$ uniformly. Each $f_n*g$ is continuous by Step 3, so the uniform limit $f*g$ is continuous. Hence
$$
\boxed{f*g\in C(\RR^d).}
$$

:::

:::

:::

:::
