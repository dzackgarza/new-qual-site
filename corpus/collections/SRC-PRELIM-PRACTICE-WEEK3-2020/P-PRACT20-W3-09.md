---
schema: qual/card@1
id: P-PRACT20-W3-09
kind: problem
title: The $100$th derivative of $3/(x^2+5x+4)$ at $x=2$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Partial Fractions
relations: []
review: draft
---

::: {.problem}
Find $f^{(100)}(2)$ for $f(x) = \frac{3}{x^{2} + 5x + 4}$.
:::

::: {.solution}
Using partial fractions, we find

$$
f(x)=\frac{1}{1+x}-\frac{1}{4+x}.
$$

Expand each term in a geometric series about $x=2$, valid for $\abs{x-2}<3$:

$$
\begin{aligned}
f(x)&=\frac{1}{3+(x-2)}-\frac{1}{6+(x-2)}=\frac13\cdot\frac{1}{1+\frac{x-2}{3}}-\frac16\cdot\frac{1}{1+\frac{x-2}{6}}\\
&=\frac13\sum_{n=0}^{\infty}\frac{(-1)^n(x-2)^n}{3^n}-\frac16\sum_{n=0}^{\infty}\frac{(-1)^n(x-2)^n}{6^n}.
\end{aligned}
$$

The coefficient of $(x-2)^{100}$ is $f^{(100)}(2)/100!$, so
$$
f^{(100)}(2)=100!\left(\frac{1}{3^{101}}-\frac{1}{6^{101}}\right)\approx6.036\times10^{109}.
$$
:::
