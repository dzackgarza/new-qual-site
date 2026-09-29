---
schema: qual/card@1
id: P-BKF11-9B
kind: problem
title: Uniform convergence of inverses of uniformly convergent bijections
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked that the uniform bound for f_n-f may be evaluated at g_n(y)
    uniformly in y and then transferred through the uniformly continuous g.
---

::: {.problem}
Let $X$ and $Y$ be metric spaces, with metrics $d_X$ and $d_Y$, respectively.
Let $f,f_1,f_2,\ldots$ be bijections from $X$ to $Y$, with inverses $g,g_1,g_2,\ldots$, respectively.
Assume that:

1. $g$ is uniformly continuous; and

2. $f_n\to f$ uniformly as $n\to\infty$.

Prove that $g_n\to g$ uniformly as $n\to\infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Fix $\varepsilon>0$. There exist $\delta>0$ and
$N\in\NN$ such that
$$
d_Y(y,y')<\delta
\quad\Longrightarrow\quad
d_X(g(y),g(y'))<\varepsilon
$$
for all $y,y'\in Y$, and
$$
d_Y(f_n(x),f(x))<\delta
$$
for all $x\in X$ and all $n\ge N$.

::: pf-proof

The first assertion is the uniform continuity of $g$. After choosing
such a $\delta$, the uniform convergence $f_n\to f$ gives an
$N$ for which the second inequality holds simultaneously for every
$x\in X$ whenever $n\ge N$.

:::

:::

::: {.pf-step #s2}

For every $n\ge N$ and every $y\in Y$,
$$
d_X(g_n(y),g(y))<\varepsilon.
$$

::: pf-proof

Fix $n\ge N$ and $y\in Y$, and put
$$
x\coloneqq g_n(y).
$$
Since $g_n=f_n^{-1}$,
$$
f_n(x)=y.
$$
The second inequality in step [](#s1){.pf-ref} therefore gives
$$
d_Y(f(x),y)
=d_Y(f(x),f_n(x))
<\delta.
$$
Apply the first inequality in step [](#s1){.pf-ref} to the two points
$f(x)$ and $y$. Since $g=f^{-1}$,
$$
\begin{aligned}
d_X(g_n(y),g(y))
&=d_X(x,g(y))\\
&=d_X(g(f(x)),g(y))\\
&<\varepsilon.
\end{aligned}
$$
The estimate is independent of $y$.

:::

:::

::: {.pf-step #s3}

Hence
$$
\boxed{g_n\longrightarrow g\text{ uniformly on }Y}.
$$

::: pf-proof

Given arbitrary $\varepsilon>0$, step [](#s1){.pf-ref} produces an $N$ such
that step [](#s2){.pf-ref} holds for every $y\in Y$ and every $n\ge N$. This is
exactly the definition of uniform convergence.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
