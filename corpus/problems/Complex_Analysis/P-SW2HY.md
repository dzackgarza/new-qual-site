---
schema: qual/card@1
id: P-SW2HY
kind: problem
title: $\bigl(\frac12(-1+\sqrt{3}i)\bigr)^n+\bigl(\frac12(-1-\sqrt{3}i)\bigr)^n$ equals
  $2$ if $3\mid n$ and $-1$ otherwise
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Let $n$ be a natural number.
Show that

$$
[1 / 2(-1+\sqrt{3} i)]^{n}+[1 / 2(-1-\sqrt{3} i)]^{n}
$$

is equal to 2 if $n$ is a multiple of 3 , and it is equal to $-1$ otherwise.
:::

::: {.solution}
The two numbers are
\[
\frac{-1+\sqrt3\,i}{2}=e^{2\pi i/3},
\qquad
\frac{-1-\sqrt3\,i}{2}=e^{-2\pi i/3}.
\]
Therefore their $n$th powers sum to
\[
e^{2\pi i n/3}+e^{-2\pi i n/3}
=2\cos\frac{2\pi n}{3}.
\]
If $3\mid n$, this equals $2$. If $3\nmid n$, then
$n\equiv1$ or $2\pmod3$, so the cosine is $-1/2$ and the sum is $-1$.
Thus the stated dichotomy holds.
:::
