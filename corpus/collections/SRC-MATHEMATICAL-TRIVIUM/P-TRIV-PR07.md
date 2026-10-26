---
schema: qual/card@1
id: P-TRIV-PR07
kind: problem
title: Probability that $ax^2+bx+c$ has real roots for uniform coefficients
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 7, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let a, b, c be three independent random variables distributed uniformly between 0 and 1. Find the probability that the roots of the equation $a x ^ { 2 } + b x + c = 0$ are real.
:::

The coefficient triple $(a,b,c)$ is uniformly distributed on the unit cube $[0,1]^3$.

::: pf

::: pf-step

The quadratic has real roots exactly when
\[
b^2\geq4ac.
\]


::: pf-proof

Except on the probability-zero set $a=0$, the equation is quadratic. Its roots are real exactly when its discriminant $b^2-4ac$ is nonnegative.

:::

:::

::: pf-step

For fixed $(a,c)$, the admissible $b$-interval has length
\[
\begin{cases}
1-2\sqrt{ac},&ac\leq1/4,\\
0,&ac>1/4.
\end{cases}
\]


::: pf-proof

Since $0\leq b\leq1$, step <1>1 is equivalent to $b\geq2\sqrt{ac}$. Such $b$ exist exactly when $2\sqrt{ac}\leq1$.

:::

:::

::: pf-step

Therefore the desired probability is
\[
P=\iint_{ac\leq1/4}(1-2\sqrt{ac})\,da\,dc.
\]


::: pf-proof

The unit cube has volume $1$, so probability equals volume. Integrating first in $b$ gives precisely the interval length from step <1>2.

:::

:::

::: pf-step

Split the $a$-integral at $a=1/4$:
\[
P=\int_0^{1/4}\int_0^1(1-2\sqrt{ac})\,dc\,da
+\int_{1/4}^{1}\int_0^{1/(4a)}(1-2\sqrt{ac})\,dc\,da.
\]


::: pf-proof

If $0<a\leq1/4$, then $ac\leq1/4$ for every $0\leq c\leq1$. If $a>1/4$, the condition is $c\leq1/(4a)$.

:::

:::

::: pf-step

The first integral equals
\[
\frac1{12}.
\]


::: pf-proof

Integrating first in $c$ gives $1-(4/3)\sqrt a$, so
\[
\int_0^{1/4}\left(1-\frac43\sqrt a\right)da
=\frac14-\frac43\frac23\left(\frac14\right)^{3/2}
=\frac1{12}.
\]

:::

:::

::: pf-step

The second integral equals
\[
\frac1{12}\log4.
\]


::: pf-proof

For fixed $a>1/4$,
\[
\int_0^{1/(4a)}(1-2\sqrt{ac})\,dc
=\frac1{4a}-\frac43\sqrt a\left(\frac1{4a}\right)^{3/2}
=\frac1{12a}.
\]
Integrating from $1/4$ to $1$ gives $(1/12)\log4$.

:::

:::

::: pf-step

Hence
\[
\boxed{P=\frac{1+\log4}{12}}.
\]


::: pf-proof

Add the two contributions from steps <1>5--<1>6.

:::

:::

::: pf-qed

Step <1>7 gives the required probability.

:::

:::
