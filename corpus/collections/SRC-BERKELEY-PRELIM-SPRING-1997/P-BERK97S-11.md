---
schema: qual/card@1
id: P-BERK97S-11
kind: problem
title: Decay of the even solution of $f''=(x^2-1)f$
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
Suppose $f:\mathbb R\to\mathbb R$ satisfies
\[
f''(x)=(x^2-1)f(x)
\]
for every $x\in\mathbb R$, with
\[
f(0)=1,
\qquad
f'(0)=0.
\]
Show that
\[
f(x)\longrightarrow0
\qquad(x\to\infty).
\]
:::

::: {.solution}
<1>1. The function
$$
g(x)\coloneqq e^{-x^2/2}
$$
satisfies the same differential equation and initial conditions as $f$.

::: {.proof}
Differentiating gives
$$
g'(x)=-x e^{-x^2/2}
$$
and
$$
g''(x)
=(x^2-1)e^{-x^2/2}
=(x^2-1)g(x).
$$
Also
$$
g(0)=1,
\qquad
g'(0)=0.
$$
Thus $g$ satisfies precisely the initial-value problem stated for $f$.
:::

<1>2. One has
$$
f(x)=e^{-x^2/2}
$$
for every $x\in\RR$.

::: {.proof}
The equation
$$
y''=(x^2-1)y
$$
is a linear second-order differential equation with continuous coefficient
$x^2-1$. The uniqueness theorem for its initial-value problem says that two
solutions with the same values of $y(0)$ and $y'(0)$ coincide. Step <1>1
shows that $f$ and $g$ have the same equation and initial data, so $f=g$.
:::

<1>3. Therefore
$$
\boxed{\lim_{x\to\infty}f(x)=0}.
$$

::: {.proof}
By step <1>2,
$$
f(x)=e^{-x^2/2}.
$$
Since $x^2/2\to\infty$ as $x\to\infty$, the right-hand side tends to
$0$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required limit.
:::
:::
