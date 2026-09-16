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
\[  
x_n \definedas {x_{n-1} + x_{n-2} \over 2} \quad n\geq 2
.\]

Show that $\theset{x_n}$ is a Cauchy sequence and find its limit in terms of $a$ and $b$.
:::

::: {.solution}
The recurrence
\[
x_n=\frac{x_{n-1}+x_{n-2}}2
\]
has characteristic equation
\[
2r^2-r-1=0,
\]
whose roots are $1$ and $-1/2$. Hence
\[
x_n=A+B\left(-\frac12\right)^n.
\]
The initial conditions give
\[
a=A+B,
\qquad
b=A-\frac B2.
\]
Solving,
\[
A=\frac{a+2b}{3},
\qquad
B=\frac{2(a-b)}{3}.
\]
Therefore
\[
x_n=\frac{a+2b}{3}
+\frac{2(a-b)}{3}\left(-\frac12\right)^n.
\]
Since the second term tends to $0$,
\[
\boxed{\lim_{n\to\infty}x_n=\frac{a+2b}{3}}.
\]
Thus $(x_n)$ converges, and every convergent real sequence is Cauchy.
:::
