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

::: pf

::: {.pf-step #s1}

Define
$$
g(t)\coloneqq e^{-Kt}y(t).
$$
Then
$$
g'(t)\leq0
$$
for every $t\geq0$.

::: pf-proof

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

:::

::: {.pf-step #s2}

For every $t\geq0$,
$$
g(t)\leq g(0)=y(0).
$$

::: pf-proof

Step [](#s1){.pf-ref} shows that $g$ is nonincreasing on $[0,\infty)$.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{y(t)\leq e^{Kt}y(0)}
$$
for every $t\geq0$.

::: pf-proof

Step [](#s2){.pf-ref} gives
$$
e^{-Kt}y(t)\leq y(0).
$$
Multiplying by the positive number $e^{Kt}$ yields the displayed
inequality.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required conclusion.

:::

:::

:::
