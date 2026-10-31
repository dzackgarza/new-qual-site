---
schema: qual/card@1
id: P-PRACT20-W6-20
kind: problem
title: Standard deviation of the density $\frac34(1-x^2)$ on $[-1,1]$
classification:
  areas:
  - prelim
  topics:
  - Probability
relations: []
review: draft
---

::: {.problem}
Let $X$ be a random variable with density function $f(x) = \frac{3}{4}(1 - x^{2})$, for $x \in [-1, 1]$ (and $f(x) = 0$ elsewhere).
What is the standard deviation of $X$?
:::

::: {.solution}
The variance of $X$ is

$$
\operatorname{Var}(X)=E(X^2)-E(X)^2,
$$

and since $X$ has density $f$,

$$
E(g(X))=\int_\RR g(x)f(x)\,dx.
$$

Thus

$$
E(X)=\int_\RR xf(x)\,dx=\frac34\int_{-1}^1(x-x^3)\,dx=0,
$$

since the integrand is odd. Next,

$$
E(X^2)=\int_\RR x^2f(x)\,dx=\frac34\int_{-1}^1(x^2-x^4)\,dx=\frac34\left(\frac23-\frac25\right)=\frac34\cdot\frac{4}{15}=\frac15.
$$

The standard deviation is the square root of the variance, so it equals $\frac{1}{\sqrt5}$.
:::
