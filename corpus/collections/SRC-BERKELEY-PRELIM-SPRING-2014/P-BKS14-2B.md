---
schema: qual/card@1
id: P-BKS14-2B
kind: problem
title: Unique minimum-norm point in a closed convex set
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
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked compactness-based existence and strict midpoint norm decrease via the parallelogram identity.
---

::: {.problem}
Prove that every nonempty closed convex subset of \(\mathbb R^n\), with the Euclidean norm, has a unique element of minimum norm.
:::

::: {.solution}
Let
$$
C\subseteq\RR^n
$$
be nonempty, closed, and convex.

<1>1. Choose
$$
a\in C
$$
and set
$$
R\coloneqq\norm{a}.
$$
Then
$$
K
\coloneqq
C\cap\overline{B(0,R)}
$$
is nonempty and compact.

::: {.proof}
The point $a$ belongs to both $C$ and the closed ball, so $K$ is
nonempty.

The set $C$ is closed by hypothesis, and the closed ball is closed and
bounded. Hence $K$ is closed and bounded in $\RR^n$. By the
Heine--Borel theorem, $K$ is compact.
:::

<1>2. There exists
$$
x_0\in K
$$
such that
$$
\norm{x_0}
=
\min_{x\in K}\norm{x}.
$$

::: {.proof}
The norm function
$$
x\longmapsto\norm{x}
$$
is continuous, and $K$ is nonempty compact by step <1>1. Therefore the
extreme value theorem gives a minimizer.
:::

<1>3. The point $x_0$ from step <1>2 minimizes the norm on all of $C$.

::: {.proof}
Since
$$
a\in K,
$$
step <1>2 gives
$$
\norm{x_0}\leq\norm{a}=R.
$$
Every point
$$
x\in C\setminus K
$$
lies outside the closed ball of radius $R$, so
$$
\norm{x}>R\geq\norm{x_0}.
$$
Points of $K$ have norm at least $\norm{x_0}$ by step <1>2. Hence no
point of $C$ has smaller norm.
:::

<1>4. Suppose
$$
x,y\in C
$$
are two minimizers with common norm
$$
\norm{x}=\norm{y}=r.
$$
Then their midpoint
$$
m\coloneqq\frac{x+y}{2}
$$
belongs to $C$.

::: {.proof}
This follows from convexity of $C$.
:::

<1>5. If $x\neq y$, then
$$
\norm{m}<r.
$$

::: {.proof}
The parallelogram identity gives
$$
\norm{x+y}^2+\norm{x-y}^2
=
2\norm{x}^2+2\norm{y}^2
=
4r^2.
$$
Therefore
$$
\begin{aligned}
\norm{m}^2
&=
\frac14\norm{x+y}^2\\
&=
r^2-\frac14\norm{x-y}^2.
\end{aligned}
$$
If $x\neq y$, then
$$
\norm{x-y}^2>0,
$$
so
$$
\norm{m}^2<r^2.
$$
Both norms are nonnegative, hence $\norm{m}<r$.
:::

<1>6. The minimum-norm point of $C$ is unique.

::: {.proof}
If two distinct minimizers existed, step <1>4 would put their midpoint
in $C$, while step <1>5 would give that midpoint strictly smaller norm.
This contradicts minimality.
:::

<1>7. Every nonempty closed convex subset of $\RR^n$ therefore has a
$$
\boxed{\text{unique element of minimum norm}}.
$$

::: {.proof}
Existence is step <1>3, and uniqueness is step <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the required result.
:::
:::
