---
schema: qual/card@1
id: P-BERK98S-14
kind: problem
title: Differential Gronwall inequality for a positive scalar function
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
Let $K\in\mathbb R$ and let $y(t)>0$ be differentiable for $t\ge0$. Suppose
\[
y'(t)\le Ky(t)
\]
for $t\ge0$. Prove that
\[
y(t)\le e^{Kt}y(0)
\]
for every $t\ge0$.
:::

::: {.solution}
<1>1. Define
$$
g(t)\coloneqq e^{-Kt}y(t).
$$
Then
$$
g'(t)\leq0
$$
for every $t\geq0$.

::: {.proof}
By the product rule,
$$
\begin{aligned}
g'(t)
&=
-Ke^{-Kt}y(t)+e^{-Kt}y'(t)\\
&=
e^{-Kt}\bigl(y'(t)-Ky(t)\bigr).
\end{aligned}
$$
Since $e^{-Kt}>0$ and $y'(t)\leq Ky(t)$ by hypothesis, the last expression
is nonpositive.
:::

<1>2. For every $t\geq0$,
$$
g(t)\leq g(0)=y(0).
$$

::: {.proof}
Step <1>1 shows that $g$ is nonincreasing on $[0,\infty)$.
:::

<1>3. Therefore
$$
\boxed{y(t)\leq e^{Kt}y(0)}
$$
for every $t\geq0$.

::: {.proof}
Step <1>2 gives
$$
e^{-Kt}y(t)\leq y(0).
$$
Multiplying by the positive number $e^{Kt}$ yields the displayed
inequality.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
