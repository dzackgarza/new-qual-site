---
schema: qual/card@1
id: P-PWNEA
kind: problem
title: Integral closure of $\ZZ$ in $\QQ(i)$
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Number Theory
  - Commutative Algebra
relations: []
review: draft
---

::: problem
Determine the integral closure of $\ZZ$ in $\QQ(i)$.
:::

::: {.solution}
The integral closure is
\[
\ZZ[i].
\]

Every Gaussian integer $a+bi$ with $a,b\in\ZZ$ is integral over $\ZZ$, since it satisfies
\[
x^2-2ax+(a^2+b^2)=0.
\]
Thus $\ZZ[i]$ is contained in the integral closure.

Conversely, let
\[
\alpha=a+bi\in\QQ(i)
\]
be integral over $\ZZ$, with $a,b\in\QQ$. Its conjugate $\bar\alpha=a-bi$ is also integral. Hence the trace and norm
\[
\alpha+\bar\alpha=2a,
\qquad
\alpha\bar\alpha=a^2+b^2
\]
are rational algebraic integers, hence integers.

Write
\[
2a=m\in\ZZ.
\]
Then
\[
(2b)^2=4(a^2+b^2)-m^2\in\ZZ.
\]
Since $2b\in\QQ$ and its square is an integer, $2b=k\in\ZZ$. Now
\[
m^2+k^2=4(a^2+b^2)
\]
is divisible by $4$. Squares modulo $4$ are $0$ or $1$, so $m$ and $k$ must both be even. Therefore $a,b\in\ZZ$, and hence $\alpha\in\ZZ[i]$.

Thus the integral closure of $\ZZ$ in $\QQ(i)$ is exactly $\ZZ[i]$.
:::
