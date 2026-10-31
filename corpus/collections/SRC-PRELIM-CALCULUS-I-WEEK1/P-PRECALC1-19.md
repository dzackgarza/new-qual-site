---
schema: qual/card@1
id: P-PRECALC1-19
kind: problem
title: Symmetric difference quotient $\frac{f(x_0+h)-f(x_0-h)}{h}$
classification:
  areas:
  - prelim
  topics:
  - Differentiation
  - Limits
relations: []
review: draft
---

::: {.problem}
Suppose that $f$ is differentiable at $x = x_{0}$. What is $\displaystyle \lim_{h \to 0} \frac{f(x_{0} + h) - f(x_{0} - h)}{h}$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Add and subtract $f(x_0)$ in the numerator:
$$
\begin{aligned}
f(x_0+h)-f(x_0-h)
={}&
\bigl(f(x_0+h)-f(x_0)\bigr)\\
&+
\bigl(f(x_0)-f(x_0-h)\bigr).
\end{aligned}
$$


::: pf-proof

The two added terms $+f(x_0)$ and $-f(x_0)$ cancel.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\boxed{
\frac{f(x_0+h)-f(x_0-h)}{h}
=
\frac{f(x_0+h)-f(x_0)}{h}
+
\frac{f(x_0-h)-f(x_0)}{-h}}.
$$


::: pf-proof

Divide step [](#s1-1){.pf-ref} by $h$, and rewrite
$$
\frac{f(x_0)-f(x_0-h)}{h}
=
\frac{f(x_0-h)-f(x_0)}{-h}.
$$

:::

:::

::: {.pf-step #s1-3}

Since $f$ is differentiable at $x_0$,
$$
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0)}{h}
=
f'(x_0)}.
$$


::: pf-proof

This is the definition of the derivative.

:::

:::

::: {.pf-step #s1-4}

Also,
$$
\boxed{
\lim_{h\to0}
\frac{f(x_0-h)-f(x_0)}{-h}
=
f'(x_0)}.
$$


::: pf-proof

Set
$$
k=-h.
$$
Then $k\to0$ as $h\to0$, and the quotient becomes
$$
\frac{f(x_0+k)-f(x_0)}{k}.
$$
Apply differentiability.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\boxed{
\lim_{h\to0}
\frac{f(x_0+h)-f(x_0-h)}{h}
=
2f'(x_0)}.
$$


::: pf-proof

Take limits in step [](#s1-2){.pf-ref} and use steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested limit.

:::

:::

:::
