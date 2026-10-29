---
schema: qual/card@1
id: P-NWE54
kind: problem
title: Cauchy property and limit of the midpoint recurrence $x_n=(x_{n-1}+x_{n-2})/2$
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
x_n \definedas {x_{n-1} + x_{n-2} \over 2} \quad n\geq 2.
$$

Show that $\theset{x_n}$ is a Cauchy sequence and find its limit in terms of $a$ and $b$.
:::

::: {.solution}
::: pf

::: {.pf-step #closed-form}
$x_n=\frac{a+2b}{3}+\frac{2(a-b)}{3}\left(-\frac12\right)^n$ for all $n\ge0$.

::: pf-proof
The characteristic equation $2r^2-r-1=(2r+1)(r-1)=0$ has roots $1$ and $-\frac12$, so $x_n=A+B\left(-\frac12\right)^n$. The conditions $a=A+B$ and $b=A-\frac B2$ give $A=\frac{a+2b}{3}$ and $B=\frac{2(a-b)}{3}$.
:::

:::

::: pf-step
$(x_n)$ is Cauchy with $\lim_{n\to\infty}x_n=\boxed{\frac{a+2b}{3}}$.

::: pf-proof
In step [](#closed-form){.pf-ref} the second term tends to $0$, so $(x_n)$ converges to $\frac{a+2b}{3}$, and a convergent sequence is Cauchy.
:::

:::

:::
:::
