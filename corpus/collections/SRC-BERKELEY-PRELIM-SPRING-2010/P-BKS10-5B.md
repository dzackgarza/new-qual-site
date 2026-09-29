---
schema: qual/card@1
id: P-BKS10-5B
kind: problem
title: Vanishing high moments force a continuous function to vanish
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the reduction to all polynomial moments, uniform polynomial approximation, and recovery of the value at zero by continuity.
---

::: {.problem}
Let $f$ be continuous on $[0,1]$ and suppose
$$
\int_0^1 f(x)x^n\,dx=0
$$
for all sufficiently large $n$. Show that $f\equiv0$.

Hint: first treat the case in which the integral vanishes for every $n\ge0$.
:::

::: {.solution}

::: pf

::: {.pf-step #g-polynomial-orthogonal}
Choose an integer $N\geq0$ such that
$$
\int_0^1 f(x)x^n\,dx=0
$$
for every integer $n\geq N$, and set
$$
g(x)\coloneqq x^Nf(x).
$$
Then
$$
\int_0^1 g(x)p(x)\,dx=0
$$
for every polynomial $p$.

::: pf-proof
For every integer $m\geq0$,
$$
\int_0^1 g(x)x^m\,dx
=
\int_0^1 f(x)x^{N+m}\,dx
=
0.
$$
By linearity, the same equality holds with $x^m$ replaced by any
polynomial $p$.
:::

:::

::: {.pf-step #g-l2-norm-zero}
One has
$$
\int_0^1\abs{g(x)}^2\,dx=0.
$$

::: pf-proof
By the Weierstrass approximation theorem, there is a sequence of
polynomials $p_j$ converging uniformly on $[0,1]$ to
$$
\overline{g}.
$$
For real-valued $f$, the conjugation is redundant; the same argument uses
$g$ itself.

By step [](#g-polynomial-orthogonal){.pf-ref},
$$
\int_0^1g(x)p_j(x)\,dx=0
$$
for every $j$. Uniform convergence gives
$$
\begin{aligned}
\abs{
\int_0^1g(x)
\bigl(p_j(x)-\overline{g(x)}\bigr)\,dx
}
&\leq
\norm{g}_{\infty}
\norm{p_j-\overline{g}}_{\infty}
\longrightarrow0.
\end{aligned}
$$
Hence
$$
0
=
\lim_{j\to\infty}
\int_0^1g(x)p_j(x)\,dx
=
\int_0^1\abs{g(x)}^2\,dx.
$$
:::

:::

::: {.pf-step #g-vanishes}
The function $g$ vanishes identically on $[0,1]$.

::: pf-proof
The function
$$
x\longmapsto\abs{g(x)}^2
$$
is continuous and nonnegative. If it were positive at some point, it would
remain bounded below by a positive number on a nondegenerate interval,
making its integral positive. This contradicts step [](#g-l2-norm-zero){.pf-ref}. Therefore
$$
g(x)=0
$$
for every $x\in[0,1]$.
:::

:::

::: {.pf-step #f-vanishes}
The original function $f$ vanishes identically on $[0,1]$.

::: pf-proof
For every $x\in(0,1]$,
$$
0=g(x)=x^Nf(x).
$$
Since $x^N>0$, it follows that
$$
f(x)=0
$$
on $(0,1]$. Continuity at $0$ then gives
$$
f(0)
=
\lim_{x\to0^+}f(x)
=
0.
$$
Thus $f\equiv0$ on $[0,1]$.
:::

:::

::: pf-qed
Step [](#f-vanishes){.pf-ref} is the required conclusion.
:::

:::

:::
