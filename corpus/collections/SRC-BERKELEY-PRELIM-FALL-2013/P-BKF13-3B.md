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
<1>1. For every $x\in(0,1)$, the defining integral for $g(x)$ is
absolutely convergent.

::: {.proof}
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

<1>2. For every $x\in(0,1)$,
$$
|g(x)|
\le
\int_x^1\frac{|f(t)|}{t}\,dt.
$$

::: {.proof}
This is the triangle inequality for the absolutely convergent integral
from step <1>1.
:::

<1>3. One has the estimate
$$
\int_0^1 |g(x)|\,dx
\le
\int_0^1 |f(t)|\,dt.
$$

::: {.proof}
By step <1>2 and Tonelli's theorem for the nonnegative integrand,
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

<1>4. Consequently,
$$
\boxed{
\int_0^1|g(x)|\,dx<\infty.
}
$$

::: {.proof}
This follows immediately from step <1>3 and the assumed integrability
of $f$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
