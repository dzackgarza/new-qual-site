---
schema: qual/card@1
id: P-KPCIE
kind: problem
title: Midpoint recurrence $x_n=\frac{x_{n-1}+x_{n-2}}{2}$ converges to $\frac{a+2b}{3}$
classification:
  areas:
  - complex-analysis
  topics:
  - Sequences of Numbers
  - Completeness
  - Convergence
relations: []
review: draft
---

::: {.problem}
Let $x_0 = a, x_1 = b$, and set
$$
x_n \coloneqq {x_{n-1} + x_{n-2} \over 2} \quad n\geq 2
.$$

Show that $\theset{x_n}$ is a Cauchy sequence and find its limit in terms of $a$ and $b$.
:::

::: {.solution}
Let $d_n=x_n-x_{n-1}$ for $n \geq 1$.

::: pf

::: {.pf-step #differences}
$\abs{d_n}=2^{1-n}\abs{b-a}$ for $n \geq 1$.

::: pf-proof
$d_1 = b - a$, and for $n \geq 2$, $d_n = \frac{x_{n-2} - x_{n-1}}{2} = -\frac12 d_{n-1}$.
:::

:::

::: {.pf-step #cauchy}
$(x_n)$ is Cauchy.

::: pf-proof
For $m>n$, step [](#differences){.pf-ref} gives
$$
\abs{x_m-x_n} \le\sum_{j=n+1}^m\abs{d_j} \le \abs{b-a}\sum_{j=n+1}^\infty2^{1-j} =2^{1-n}\abs{b-a},
$$
which tends to $0$ as $n\to\infty$.
:::

:::

::: {.pf-step #invariant}
$x_{n-1}+2x_n = a + 2b$ for every $n \geq 1$.

::: pf-proof
For $n \geq 2$, $x_{n-1}+2x_n = x_{n-1}+x_{n-1}+x_{n-2} = x_{n-2}+2x_{n-1}$, and for $n = 1$ the value is $a + 2b$.
:::

:::

::: pf-step
$\lim x_n = \boxed{\frac{a+2b}{3}}$.

::: pf-proof
By step [](#cauchy){.pf-ref} and completeness, $x_n \to L$ for some $L$.
Letting $n \to \infty$ in step [](#invariant){.pf-ref} gives $3L = a + 2b$.
:::

:::

:::
:::
