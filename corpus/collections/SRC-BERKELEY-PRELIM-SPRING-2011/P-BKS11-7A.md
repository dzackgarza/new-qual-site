---
schema: qual/card@1
id: P-BKS11-7A
kind: problem
title: Sum of $\sum r^k\cos(k\theta)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2011 solution PDF and independently reviewed the geometric-series computation.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked convergence, extraction of the real part, and rationalization to a real-valued closed form.
---

::: {.problem}
If $0 < r < 1$ , find

$$
\sum _ { k = 0 } ^ { \infty } r ^ { k } \cos ( k \theta ) .
$$

Your final answer should not involve any complex numbers.
:::

::: {.solution}

::: pf

::: {.pf-step #geometric-sum}
With
$$
z\coloneqq re^{i\theta},
$$
one has
$$
\sum_{k=0}^{\infty}z^k
=
\frac{1}{1-z}.
$$

::: pf-proof
Because
$$
\abs{z}=r<1,
$$
the geometric series converges absolutely and has the stated sum.
:::

:::

::: {.pf-step #real-part-equals-series}
The required real series is the real part of the sum in step [](#geometric-sum){.pf-ref}:
$$
\sum_{k=0}^{\infty}r^k\cos(k\theta)
=
\operatorname{Re}
\left(
\frac{1}{1-re^{i\theta}}
\right).
$$

::: pf-proof
For every $k$,
$$
\operatorname{Re}(z^k)
=
\operatorname{Re}(r^ke^{ik\theta})
=
r^k\cos(k\theta).
$$
Absolute convergence permits taking real parts term by term.
:::

:::

::: {.pf-step #rationalized-form}
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
The denominator becomes
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

::: {.pf-step #closed-form}
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
Take the real part of the expression in step [](#rationalized-form){.pf-ref} and apply step [](#real-part-equals-series){.pf-ref}.
The displayed answer contains no complex quantities.
:::

:::

::: pf-qed
Step [](#closed-form){.pf-ref} is the required closed form.
:::

:::

:::
