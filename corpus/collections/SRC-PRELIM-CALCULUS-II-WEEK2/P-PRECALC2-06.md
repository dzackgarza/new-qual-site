---
schema: qual/card@1
id: P-PRECALC2-06
kind: problem
title: Integral of $\frac{x^2+b^2}{x^2+a^2}$ over $[0,a]$
classification:
  areas:
  - prelim
  topics:
  - Integrals
relations: []
review: draft
---

::: {.problem}
Evaluate $\displaystyle \int_{0}^{a} \frac{x^{2} + b^{2}}{x^{2} + a^{2}}\, dx$ where $a, b > 0$ are constant.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Rewrite the integrand as
$$
\boxed{
\frac{x^2+b^2}{x^2+a^2}
=
1+\frac{b^2-a^2}{x^2+a^2}}.
$$


::: pf-proof

Since
$$
x^2+b^2
=
(x^2+a^2)+(b^2-a^2),
$$
division by $x^2+a^2$ gives the identity.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\int_0^a
\frac{x^2+b^2}{x^2+a^2}\,dx
=
a
+
(b^2-a^2)
\int_0^a
\frac{dx}{x^2+a^2}.
$$


::: pf-proof

Integrate the two terms in step [](#s1-1){.pf-ref} separately, using
$$
\int_0^a1\,dx=a.
$$

:::

:::

::: pf-step

Set
$$
\boxed{u=\frac{x}{a}}.
$$


::: pf-proof

Since $a>0$, this substitution is valid on the whole interval.

:::

:::

::: {.pf-step #s1-4}

Then
$$
x=au,
\qquad
dx=a\,du,
$$
and the bounds $x=0,a$ become $u=0,1$.


::: pf-proof

Differentiate
$$
x=au,
$$
and substitute the two endpoints.

:::

:::

::: {.pf-step #s1-5}

Hence
$$
\int_0^a
\frac{dx}{x^2+a^2}
=
\frac1a
\int_0^1
\frac{du}{1+u^2}.
$$


::: pf-proof

Substitute step [](#s1-4){.pf-ref}:
$$
\begin{aligned}
\int_0^a\frac{dx}{x^2+a^2}
&=
\int_0^1
\frac{a\,du}{a^2u^2+a^2}\\
&=
\frac1a
\int_0^1
\frac{du}{1+u^2}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\int_0^a
\frac{dx}{x^2+a^2}
=
\frac{\pi}{4a}}.
$$


::: pf-proof

Since
$$
\int\frac{du}{1+u^2}
=
\arctan u,
$$
step [](#s1-5){.pf-ref} gives
$$
\frac1a
\left[
\arctan u
\right]_0^1
=
\frac1a
\left(
\frac{\pi}{4}-0
\right).
$$

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{
\int_0^a
\frac{x^2+b^2}{x^2+a^2}\,dx
=
a+\frac{\pi(b^2-a^2)}{4a}}.
$$


::: pf-proof

Insert step [](#s1-6){.pf-ref} into step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the requested value.

:::

:::

:::
