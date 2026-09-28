---
schema: qual/card@1
id: P-BKF89-6
kind: problem
title: A fixed-distance locus from a closed subset of $\mathbb R^n$ is closed
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $X\subset\mathbb R^n$ be closed and let $r>0$. Define
\[
Y=\{y\in\mathbb R^n:|x-y|=r\text{ for some }x\in X\}.
\]
Show that $Y$ is closed.
:::

::: {.solution}
<1>1. Let $(y_k)$ be a sequence in $Y$ converging to
$$
y\in\RR^n.
$$
For each $k$, choose $x_k\in X$ such that
$$
|x_k-y_k|=r.
$$

::: {.proof}
This is possible by the definition of $Y$.
:::

<1>2. The sequence $(x_k)$ is bounded.

::: {.proof}
Since $y_k\to y$, the sequence $(y_k)$ is bounded. Hence there is $M>0$ such that
$$
|y_k|\leq M
$$
for all $k$. By the triangle inequality,
$$
|x_k|
\leq
|x_k-y_k|+|y_k|
\leq
r+M.
$$
Thus $(x_k)$ is bounded.
:::

<1>3. Some subsequence $(x_{k_j})$ converges to a point $x\in X$.

::: {.proof}
By step <1>2 and the Bolzano--Weierstrass theorem in $\RR^n$, $(x_k)$ has a convergent subsequence
$$
x_{k_j}\longrightarrow x.
$$
Every $x_{k_j}$ lies in the closed set $X$, so its limit $x$ also lies in $X$.
:::

<1>4. The limit point $y$ belongs to $Y$.

::: {.proof}
Along the same subsequence,
$$
y_{k_j}\longrightarrow y.
$$
By continuity of the Euclidean norm,
$$
|x-y|
=
\lim_{j\to\infty}|x_{k_j}-y_{k_j}|
=
r.
$$
Since $x\in X$ by step <1>3, the definition of $Y$ gives $y\in Y$.
:::

<1>5. Therefore
$$
\boxed{Y\text{ is closed}}.
$$

::: {.proof}
Steps <1>1--<1>4 show that every convergent sequence in $Y$ has its limit in $Y$. In the metric space $\RR^n$, this is equivalent to closedness.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
