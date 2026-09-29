---
schema: qual/card@1
id: P-BKF13-3B
kind: problem
title: Integrability of $\int_x^1 f(t)/t\,dt$ for integrable $f$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in g and moved the codomain inside math against F13_Exam.pdf page 14 problem 3B.
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2013 solution packet and its
    order-of-integration estimate.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked existence of g(x) for x>0 and the Tonelli estimate reducing its
    L1 norm to the assumed L1 norm of f.
---

::: {.problem}
Suppose that $f : (0, 1) \to \mathbf{R}$ is a continuous function with $\int_0^1 |f(t)| \, dt < \infty$. Define $g : (0, 1) \to \mathbf{R}$ by

$$
g(x) = \int_x^1 \frac{f(t)}{t} \, dt.
$$

Show that $\int_0^1 |g(x)| \, dx < \infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every $x\in(0,1)$, the defining integral for $g(x)$ is
absolutely convergent.

::: pf-proof

On the interval $[x,1]$ one has $1/t\le1/x$. Therefore
$$
\int_x^1\left|\frac{f(t)}t\right|\,dt
\le
\frac1x\int_x^1|f(t)|\,dt
\le
\frac1x\int_0^1|f(t)|\,dt
<\infty.
$$
Thus $g(x)$ is well-defined.

:::

:::

::: {.pf-step #s2}

For every $x\in(0,1)$,
$$
|g(x)|
\le
\int_x^1\frac{|f(t)|}{t}\,dt.
$$

::: pf-proof

This is the triangle inequality for the absolutely convergent integral
from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

One has the estimate
$$
\int_0^1 |g(x)|\,dx
\le
\int_0^1 |f(t)|\,dt.
$$

::: pf-proof

By step [](#s2){.pf-ref} and Tonelli's theorem for the nonnegative integrand,
$$
\begin{aligned}
\int_0^1|g(x)|\,dx
&\le
\int_0^1\int_x^1\frac{|f(t)|}{t}\,dt\,dx\\
&=
\int_0^1\int_0^t\frac{|f(t)|}{t}\,dx\,dt\\
&=
\int_0^1
\frac{|f(t)|}{t}\,t\,dt\\
&=
\int_0^1|f(t)|\,dt.
\end{aligned}
$$
The right-hand side is finite by hypothesis.

:::

:::

::: {.pf-step #s4}

Consequently,
$$
\boxed{
\int_0^1|g(x)|\,dx<\infty.
}
$$

::: pf-proof

This follows immediately from step [](#s3){.pf-ref} and the assumed integrability
of $f$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
