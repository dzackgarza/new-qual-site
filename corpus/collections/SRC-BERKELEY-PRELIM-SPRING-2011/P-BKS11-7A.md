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
<1>1. With
$$
z\coloneqq re^{i\theta},
$$
one has
$$
\sum_{k=0}^{\infty}z^k
=
\frac{1}{1-z}.
$$

::: {.proof}
Because
$$
\abs{z}=r<1,
$$
the geometric series converges absolutely and has the stated sum.
:::

<1>2. The required real series is the real part of the sum in step <1>1:
$$
\sum_{k=0}^{\infty}r^k\cos(k\theta)
=
\operatorname{Re}
\left(
\frac{1}{1-re^{i\theta}}
\right).
$$

::: {.proof}
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

<1>3. One has
$$
\frac{1}{1-re^{i\theta}}
=
\frac{1-r\cos\theta+ir\sin\theta}
{1-2r\cos\theta+r^2}.
$$

::: {.proof}
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

<1>4. Therefore
$$
\boxed{
\sum_{k=0}^{\infty}r^k\cos(k\theta)
=
\frac{1-r\cos\theta}
{1-2r\cos\theta+r^2}
}.
$$

::: {.proof}
Take the real part of the expression in step <1>3 and apply step <1>2.
The displayed answer contains no complex quantities.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required closed form.
:::
:::
