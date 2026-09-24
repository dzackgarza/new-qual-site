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
<1>1. There exists $\delta>0$ such that
$$
\abs{u-v}<\delta
\quad\Longrightarrow\quad
\abs{f(u)-f(v)}<1
$$
for all $u,v\in\RR$.

::: {.proof}
Apply uniform continuity with $\varepsilon=1$.
:::

<1>2. Set
$$
B=\frac{2}{\delta}>0.
$$
For every $x\neq0$, there is an integer $n\ge1$ such that
$$
B\abs{x}<n\le B\abs{x}+1.
$$

::: {.proof}
Take
$$
n=\lfloor B\abs{x}\rfloor+1.
$$
Since $x\neq0$ and $B>0$, this integer is positive and has the displayed
inequalities.
:::

<1>3. For $x\neq0$ and $n$ as in step <1>2,
$$
\abs{f(x)}<n.
$$

::: {.proof}
For $j=0,\ldots,n$, set
$$
x_j=\frac{j}{n}x.
$$
Then $x_0=0$, $x_n=x$, and step <1>2 gives
$$
\abs{x_j-x_{j-1}}
=\frac{\abs{x}}{n}
<\frac1B
=\frac{\delta}{2}
<\delta
$$
for $j=1,\ldots,n$. Hence step <1>1 implies
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

<1>4. For every $x\in\RR$,
$$
\abs{f(x)}\le\boxed{1+B\abs{x}}.
$$

::: {.proof}
If $x=0$, then $f(0)=0$, so the inequality is immediate. If $x\neq0$,
steps <1>2 and <1>3 give
$$
\abs{f(x)}<n\le1+B\abs{x}.
$$
Thus the same bound holds for every real $x$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the required constant $B>0$ and the asserted bound.
:::
:::
