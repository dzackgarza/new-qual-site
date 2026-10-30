---
schema: qual/card@1
id: P-PRECALC1-14
kind: problem
title: Integral of the sign function over $[-1,1]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Define $f ( 0 ) = 0$ and $\begin{array} { r } { f ( x ) = \frac { \abs{ x } } { x } } \end{array}$ for $x \neq 0$ . Compute $\int _ { - 1 } ^ { 1 } f ( x ) d x .$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For
$$
x<0,
$$
one has
$$
\boxed{
f(x)=-1}.
$$


::: pf-proof

If $x<0$, then
$$
\abs{x}=-x,
$$
so
$$
\frac{\abs{x}}{x}
=
\frac{-x}{x}
=
-1.
$$

:::

:::

::: {.pf-step #s1-2}

For
$$
x>0,
$$
one has
$$
\boxed{
f(x)=1}.
$$


::: pf-proof

If $x>0$, then
$$
\abs{x}=x,
$$
so
$$
\frac{\abs{x}}{x}=1.
$$

:::

:::

::: {.pf-step #s1-3}

The value $f(0)=0$ does not affect the definite integral.


::: pf-proof

Changing the value of a bounded function at a single point does not change
its Riemann or Lebesgue integral.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\int_{-1}^{1}f(x)\,dx
=
\int_{-1}^{0}(-1)\,dx
+
\int_{0}^{1}1\,dx.
$$


::: pf-proof

Use steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} and split the integral at $0$.

:::

:::

::: {.pf-step #s1-5}

The first integral is
$$
\boxed{-1}.
$$


::: pf-proof

$$
\int_{-1}^{0}(-1)\,dx
=
-\bigl(0-(-1)\bigr)
=
-1.
$$

:::

:::

::: {.pf-step #s1-6}

The second integral is
$$
\boxed{1}.
$$


::: pf-proof

$$
\int_0^1 1\,dx=1.
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\int_{-1}^{1}f(x)\,dx=0}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref}:
$$
-1+1=0.
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested integral.

:::

:::

:::
