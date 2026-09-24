---
schema: qual/card@1
id: P-BKF16-2A
kind: problem
title: A quadratic Grönwall-type inequality
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: introducing
    the integral upper bound y gives x<=sqrt(y), and differentiating sqrt(y)
    yields the desired estimate after integration.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked positivity of y, the derivative computation, and the endpoint
    value y(a)=1.
---

::: {.problem}
Let $x \colon [ a , b ] \to \mathbb { R }$ and $f \colon [ a , b ] \to \mathbb { R }$ be non-negative continuous functions satisfying

$$
x ^ { 2 } ( t ) \leq 1 + \int _ { a } ^ { t } f ( s ) x ( s ) d s
$$

for $a \leq t \leq b$ . Show that

$$
x ( t ) \leq 1 + { \frac { 1 } { 2 } } \int _ { a } ^ { t } f ( s ) d s
$$

for $a \leq t \leq b$
:::

::: {.solution}
Define
$$
y(t)
\coloneqq
1+\int_a^t f(s)x(s)\,ds.
$$

<1>1. For every $t\in[a,b]$,
$$
y(t)\ge1
\qquad\text{and}\qquad
x(t)\le\sqrt{y(t)}.
$$

::: {.proof}
Both $f$ and $x$ are nonnegative, so
$$
\int_a^t f(s)x(s)\,ds\ge0
$$
and hence $y(t)\ge1$. The hypothesis gives
$$
x(t)^2\le y(t).
$$
Since $x(t)\ge0$, taking nonnegative square roots yields
$$
x(t)\le\sqrt{y(t)}.
$$
:::

<1>2. The function $y$ is differentiable and satisfies
$$
y'(t)
=
f(t)x(t)
\le
f(t)\sqrt{y(t)}.
$$

::: {.proof}
The integrand $fx$ is continuous, so the fundamental theorem of
calculus gives
$$
y'(t)=f(t)x(t).
$$
The inequality follows from step <1>1 and $f(t)\ge0$.
:::

<1>3. For $t\in[a,b]$,
$$
\left(2\sqrt{y(t)}\right)'
\le
f(t).
$$

::: {.proof}
By step <1>1, $y(t)\ge1>0$. Therefore
$$
\left(2\sqrt y\right)'
=
\frac{y'}{\sqrt y}.
$$
Dividing the inequality in step <1>2 by the positive quantity
$\sqrt{y(t)}$ gives
$$
\frac{y'(t)}{\sqrt{y(t)}}
\le
f(t).
$$
:::

<1>4. For every $t\in[a,b]$,
$$
\sqrt{y(t)}
\le
1+\frac12\int_a^t f(s)\,ds.
$$

::: {.proof}
Integrate step <1>3 from $a$ to $t$:
$$
2\sqrt{y(t)}-2\sqrt{y(a)}
\le
\int_a^t f(s)\,ds.
$$
By definition,
$$
y(a)=1,
$$
so
$$
2\sqrt{y(t)}-2
\le
\int_a^t f(s)\,ds.
$$
Divide by $2$.
:::

<1>5. Hence
$$
\boxed{
x(t)
\le
1+\frac12\int_a^t f(s)\,ds
}
$$
for every $a\le t\le b$.

::: {.proof}
Step <1>1 gives
$$
x(t)\le\sqrt{y(t)},
$$
and step <1>4 gives the required upper bound for $\sqrt{y(t)}$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the desired inequality.
:::
:::
