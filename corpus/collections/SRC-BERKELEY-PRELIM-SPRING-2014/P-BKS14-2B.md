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
Prove that every nonempty closed convex subset of $\RR^n$, with the Euclidean norm, has a unique element of minimum norm.
:::

::: {.solution}
Let
$$
C\subseteq\RR^n
$$
be nonempty, closed, and convex.

::: pf

::: {.pf-step #s1}

Choose
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

::: pf-proof

The point $a$ belongs to both $C$ and the closed ball, so $K$ is
nonempty.

The set $C$ is closed by hypothesis, and the closed ball is closed and
bounded. Hence $K$ is closed and bounded in $\RR^n$. By the
Heine--Borel theorem, $K$ is compact.

:::

:::

::: {.pf-step #s2}

There exists
$$
x_0\in K
$$
such that
$$
\norm{x_0}
=
\min_{x\in K}\norm{x}.
$$

::: pf-proof

The norm function
$$
x\longmapsto\norm{x}
$$
is continuous, and $K$ is nonempty compact by step [](#s1){.pf-ref}. Therefore the
extreme value theorem gives a minimizer.

:::

:::

::: {.pf-step #s3}

The point $x_0$ from step [](#s2){.pf-ref} minimizes the norm on all of $C$.

::: pf-proof

Since
$$
a\in K,
$$
step [](#s2){.pf-ref} gives
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
Points of $K$ have norm at least $\norm{x_0}$ by step [](#s2){.pf-ref}. Hence no
point of $C$ has smaller norm.

:::

:::

::: {.pf-step #s4}

Suppose
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

::: pf-proof

This follows from convexity of $C$.

:::

:::

::: {.pf-step #s5}

If $x\neq y$, then
$$
\norm{m}<r.
$$

::: pf-proof

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

:::

::: {.pf-step #s6}

The minimum-norm point of $C$ is unique.

::: pf-proof

If two distinct minimizers existed, step [](#s4){.pf-ref} would put their midpoint
in $C$, while step [](#s5){.pf-ref} would give that midpoint strictly smaller norm.
This contradicts minimality.

:::

:::

::: {.pf-step #s7}

Every nonempty closed convex subset of $\RR^n$ therefore has a
$$
\boxed{\text{unique element of minimum norm}}.
$$

::: pf-proof

Existence is step [](#s3){.pf-ref}, and uniqueness is step [](#s6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required result.

:::

:::

:::
