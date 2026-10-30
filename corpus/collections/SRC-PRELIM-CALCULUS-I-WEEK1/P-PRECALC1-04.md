---
schema: qual/card@1
id: P-PRECALC1-04
kind: problem
title: Minimum of $e^x-cx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $c > 0$. Find the minimum value of $f(x) = e^{x} - cx$ among $x \in \RR$.
:::

::: {.solution}

Let
$$
f(x)=e^x-cx,
\qquad
c>0.
$$

::: pf

::: {.pf-step #s1-1}

The derivative is
$$
\boxed{
f'(x)=e^x-c}.
$$


::: pf-proof

Differentiate term by term.

:::

:::

::: pf-step

The critical-point equation
$$
f'(x)=0
$$
is equivalent to
$$
e^x=c.
$$


::: pf-proof

Use step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

Since $c>0$, the unique critical point is
$$
\boxed{
x=\log c}.
$$


::: pf-proof

The exponential function is a bijection
$$
\RR\to(0,\infty),
$$
with inverse $\log$.

:::

:::

::: pf-step

The second derivative is
$$
\boxed{
f''(x)=e^x>0}
$$
for every $x\in\RR$.


::: pf-proof

Differentiate step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

Hence $f$ is strictly convex on $\RR$.


::: pf-proof

A twice differentiable function with
$$
f''(x)>0
$$
everywhere is strictly convex.

:::

:::

::: pf-step

Therefore the unique critical point $x=\log c$ is the global
minimum point.


::: pf-proof

A strictly convex differentiable function has at most one critical point,
and any critical point is its global minimizer.

:::

:::

::: {.pf-step #s1-7}

Evaluate:
$$
\begin{aligned}
f(\log c)
&=
e^{\log c}
-c\log c\\
&=
c-c\log c.
\end{aligned}
$$


::: pf-proof

Use
$$
e^{\log c}=c.
$$

:::

:::

::: {.pf-step #s1-8}

Hence the minimum value is
$$
\boxed{
c(1-\log c)}.
$$


::: pf-proof

Factor $c$ from step [](#s1-7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the requested minimum value.

:::

:::

:::
