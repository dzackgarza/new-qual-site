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
<1>1. Define
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

::: {.proof}
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

<1>2. The function $g$ is strictly increasing on $\RR$.

::: {.proof}
This follows from step <1>1 and the mean value theorem.
:::

<1>3. For every $x>0$,
$$
g(x)>0.
$$

::: {.proof}
By step <1>2, if $x>0$ then
$$
g(x)>g(0).
$$
Since $f(0)=0$,
$$
g(0)=e^0f(0)=0.
$$
:::

<1>4. For every $x>0$,
$$
\boxed{f(x)>0}.
$$

::: {.proof}
From the definition of $g$,
$$
f(x)=e^x g(x).
$$
For $x>0$, step <1>3 gives $g(x)>0$, and $e^x>0$. Hence $f(x)>0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
