---
schema: qual/card@1
id: P-PRELIM82S-06
kind: problem
title: A differential inequality forces positivity on the positive half-line
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The integrating factor g(x)=e^{-x}f(x) has derivative
    g'(x)=e^{-x}(f'(x)-f(x))>0. Hence g is strictly increasing and
    g(x)>g(0)=0 for x>0; multiplying by e^x gives f(x)>0.
---

::: {.problem}
Suppose $f:\mathbb R\to\mathbb R$ is differentiable, $f'(x)>f(x)$ for every $x\in\mathbb R$, and $f(0)=0$.
Prove that
\[
f(x)>0
\]
for every $x>0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Define
$$
g:\RR\longrightarrow\RR,
\qquad
g(x)=e^{-x}f(x).
$$
Then
$$
g'(x)>0
$$
for every $x\in\RR$.

::: pf-proof

By the product rule,
$$
\begin{aligned}
g'(x)
&=-e^{-x}f(x)+e^{-x}f'(x)\\
&=e^{-x}\bigl(f'(x)-f(x)\bigr).
\end{aligned}
$$
The factor $e^{-x}$ is positive, and the hypothesis gives
$f'(x)-f(x)>0$. Thus $g'(x)>0$.

:::

:::

::: {.pf-step #s2}

The function $g$ is strictly increasing on $\RR$.

::: pf-proof

This follows from step [](#s1){.pf-ref} and the mean value theorem.

:::

:::

::: {.pf-step #s3}

For every $x>0$,
$$
g(x)>0.
$$

::: pf-proof

By step [](#s2){.pf-ref}, if $x>0$ then
$$
g(x)>g(0).
$$
Since $f(0)=0$,
$$
g(0)=e^0f(0)=0.
$$

:::

:::

::: {.pf-step #s4}

For every $x>0$,
$$
\boxed{f(x)>0}.
$$

::: pf-proof

From the definition of $g$,
$$
f(x)=e^x g(x).
$$
For $x>0$, step [](#s3){.pf-ref} gives $g(x)>0$, and $e^x>0$. Hence $f(x)>0$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
