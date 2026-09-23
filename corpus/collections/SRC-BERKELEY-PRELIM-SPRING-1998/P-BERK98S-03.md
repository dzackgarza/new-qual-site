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

<1>1. The map $S$ has a unique fixed point $x_0\in M$.

::: {.proof}
By hypothesis, $S=T^2$ is a strict contraction of the nonempty complete
metric space $M$ into itself. The contraction mapping theorem therefore
gives a unique point $x_0\in M$ such that
$$
S(x_0)=x_0.
$$
:::

<1>2. The point $T(x_0)$ is also fixed by $S$.

::: {.proof}
Using $S=T^2$ and step <1>1,
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

<1>3. The point $x_0$ is fixed by $T$.

::: {.proof}
By steps <1>1 and <1>2, both $x_0$ and $T(x_0)$ are fixed points of $S$.
The fixed point of $S$ is unique by step <1>1, so
$$
T(x_0)=x_0.
$$
:::

<1>4. The point $x_0$ is the unique fixed point of $T$.

::: {.proof}
Let $y\in M$ satisfy $T(y)=y$. Then
$$
S(y)=T^2(y)=T(y)=y,
$$
so $y$ is a fixed point of $S$. By the uniqueness in step <1>1,
$y=x_0$. Together with step <1>3, this proves both existence and uniqueness.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
