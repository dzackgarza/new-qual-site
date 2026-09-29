---
schema: qual/card@1
id: P-BERK98S-03
kind: problem
title: If $T^2$ is a strict contraction, then $T$ has a unique fixed point
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $M$ be a nonempty complete metric space and let $T:M\to M$. Suppose
\[
T\circ T=T^2
\]
is a strict contraction. Prove that $T$ has a unique fixed point in $M$.
:::

::: {.solution}
Put
$$
S\coloneqq T^2.
$$

::: pf

::: {.pf-step #s1}

The map $S$ has a unique fixed point $x_0\in M$.

::: pf-proof

By hypothesis, $S=T^2$ is a strict contraction of the nonempty complete
metric space $M$ into itself. The contraction mapping theorem therefore
gives a unique point $x_0\in M$ such that
$$
S(x_0)=x_0.
$$

:::

:::

::: {.pf-step #s2}

The point $T(x_0)$ is also fixed by $S$.

::: pf-proof

Using $S=T^2$ and step [](#s1){.pf-ref},
$$
\begin{aligned}
S(T(x_0))
&=T^2(T(x_0))\\
&=T(T^2(x_0))\\
&=T(S(x_0))\\
&=T(x_0).
\end{aligned}
$$
Thus $T(x_0)$ is a fixed point of $S$.

:::

:::

::: {.pf-step #s3}

The point $x_0$ is fixed by $T$.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, both $x_0$ and $T(x_0)$ are fixed points of $S$.
The fixed point of $S$ is unique by step [](#s1){.pf-ref}, so
$$
T(x_0)=x_0.
$$

:::

:::

::: {.pf-step #s4}

The point $x_0$ is the unique fixed point of $T$.

::: pf-proof

Let $y\in M$ satisfy $T(y)=y$. Then
$$
S(y)=T^2(y)=T(y)=y,
$$
so $y$ is a fixed point of $S$. By the uniqueness in step [](#s1){.pf-ref},
$y=x_0$. Together with step [](#s3){.pf-ref}, this proves both existence and uniqueness.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
