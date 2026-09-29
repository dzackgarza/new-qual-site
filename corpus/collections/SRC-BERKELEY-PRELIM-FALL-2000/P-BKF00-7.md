---
schema: qual/card@1
id: P-BKF00-7
kind: problem
title: A uniformly continuous function on $\mathbb R$ has at most affine growth
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    A uniform-continuity scale for epsilon 1, followed by a subdivision of
    the segment from 0 to x, gives the required affine growth bound.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be uniformly continuous and suppose $f(0)=0$. Prove that there exists $B>0$ such that
\[
|f(x)|\le1+B|x|
\]
for every $x\in\mathbb R$.
:::

::: {.solution}

::: pf

::: {.pf-step #delta-exists}
There exists $\delta>0$ such that
$$
\abs{u-v}<\delta
\quad\Longrightarrow\quad
\abs{f(u)-f(v)}<1
$$
for all $u,v\in\RR$.

::: pf-proof
Apply uniform continuity with $\varepsilon=1$.
:::

:::

::: {.pf-step #B-and-n-defined}
Set
$$
B=\frac{2}{\delta}>0.
$$
For every $x\neq0$, there is an integer $n\ge1$ such that
$$
B\abs{x}<n\le B\abs{x}+1.
$$

::: pf-proof
Take
$$
n=\lfloor B\abs{x}\rfloor+1.
$$
Since $x\neq0$ and $B>0$, this integer is positive and has the displayed
inequalities.
:::

:::

::: {.pf-step #f-x-bound-n}
For $x\neq0$ and $n$ as in step [](#B-and-n-defined){.pf-ref},
$$
\abs{f(x)}<n.
$$

::: pf-proof
For $j=0,\ldots,n$, set
$$
x_j=\frac{j}{n}x.
$$
Then $x_0=0$, $x_n=x$, and step [](#B-and-n-defined){.pf-ref} gives
$$
\abs{x_j-x_{j-1}}
=\frac{\abs{x}}{n}
<\frac1B
=\frac{\delta}{2}
<\delta
$$
for $j=1,\ldots,n$. Hence step [](#delta-exists){.pf-ref} implies
$$
\abs{f(x_j)-f(x_{j-1})}<1
$$
for every $j$. Since $f(0)=0$, the triangle inequality gives
$$
\begin{aligned}
\abs{f(x)}
&=\abs{f(x_n)-f(x_0)}\\
&\le\sum_{j=1}^n\abs{f(x_j)-f(x_{j-1})}\\
&<n.
\end{aligned}
$$
:::

:::

::: {.pf-step #final-bound}
For every $x\in\RR$,
$$
\abs{f(x)}\le\boxed{1+B\abs{x}}.
$$

::: pf-proof
If $x=0$, then $f(0)=0$, so the inequality is immediate. If $x\neq0$,
steps [](#B-and-n-defined){.pf-ref} and [](#f-x-bound-n){.pf-ref} give
$$
\abs{f(x)}<n\le1+B\abs{x}.
$$
Thus the same bound holds for every real $x$.
:::

:::

::: pf-qed
Step [](#final-bound){.pf-ref} gives the required constant $B>0$ and the asserted bound.
:::

:::

:::
