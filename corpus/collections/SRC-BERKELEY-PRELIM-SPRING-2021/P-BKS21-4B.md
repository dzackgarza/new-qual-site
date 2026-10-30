---
schema: qual/card@1
id: P-BKS21-4B
kind: problem
title: The sum $\sum_{k\ge0} r^k\cos(k\theta)$ for $0<r<1$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
If $0<r<1$, find
$$
\sum_{k=0}^{\infty}r^k\cos(k\theta).
$$
Your final answer should not involve complex numbers.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $\abs{re^{i\theta}}=r<1$,
$$
\sum_{k=0}^{\infty}r^ke^{ik\theta}
=
\frac{1}{1-re^{i\theta}}.
$$


::: pf-proof

This is the geometric-series identity
$$
\sum_{k=0}^{\infty}z^k=\frac1{1-z}
$$
with $z=re^{i\theta}$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\frac{1}{1-re^{i\theta}}
=
\frac{1-r\cos\theta+ir\sin\theta}
{1-2r\cos\theta+r^2}.
$$


::: pf-proof

Multiply numerator and denominator by the complex conjugate
$$
1-re^{-i\theta}.
$$
Then
$$
(1-re^{i\theta})(1-re^{-i\theta})
=
1-r(e^{i\theta}+e^{-i\theta})+r^2
=
1-2r\cos\theta+r^2,
$$
while
$$
1-re^{-i\theta}
=
1-r\cos\theta+ir\sin\theta.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\sum_{k=0}^{\infty}r^k\cos(k\theta)
=
\frac{1-r\cos\theta}
{1-2r\cos\theta+r^2}
}.
$$


::: pf-proof

Taking real parts in step [](#s1-1){.pf-ref} and using step [](#s1-2){.pf-ref} gives the displayed formula. The denominator is real and positive because
$$
1-2r\cos\theta+r^2=\abs{1-re^{i\theta}}^2>0.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required real-valued expression.

:::

:::

:::
