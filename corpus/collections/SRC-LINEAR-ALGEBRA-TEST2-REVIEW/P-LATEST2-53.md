---
schema: qual/card@1
id: P-LATEST2-53
kind: problem
title: Dimensions of cubic polynomials and a vanishing subspace
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Let $V$ be the real vector space of polynomials of degree at most $3$.
Let
\[
W=\{p\in V:p(0)=p(1)=p(-1)=0\}.
\]
Find $\dim V+\dim W$.

(A) $4$  (B) $5$  (C) $6$  (D) $7$  (E) $8$
:::

::: pf

::: pf-step

The vector space $V$ has dimension $4$.


::: pf-proof

Every polynomial in $V$ has the form
$$
a_0+a_1x+a_2x^2+a_3x^3.
$$
Thus
$$
\{1,x,x^2,x^3\}
$$
is a basis of $V$.
Hence
$$
\dim V=4.
$$

:::

:::

::: pf-step

Every polynomial $p\in W$ is divisible by
$$
x(x-1)(x+1)=x^3-x.
$$


::: pf-proof

The conditions
$$
p(0)=p(1)=p(-1)=0
$$
show that $0$, $1$, and $-1$ are roots of $p$.
By the factor theorem,
$$
x,
\quad
x-1,
\quad
x+1
$$
all divide $p$.
These factors are pairwise relatively prime, so their product divides $p$.
Thus
$$
x(x-1)(x+1)=x^3-x
$$
divides $p$.

:::

:::

::: pf-step

Every polynomial in $W$ is a scalar multiple of $x^3-x$.


::: pf-proof

By step <1>2,
$$
p(x)=(x^3-x)q(x)
$$
for some real polynomial $q$.
If $p\ne0$, then
$$
\deg p\le3
$$
while
$$
\deg(x^3-x)=3.
$$
Therefore
$$
\deg q=0,
$$
so $q$ is a scalar.
The zero polynomial is also a scalar multiple of $x^3-x$.
Hence
$$
W=\operatorname{span}\{x^3-x\}.
$$

:::

:::

::: pf-step

Therefore
$$
\dim W=1.
$$


::: pf-proof

The polynomial
$$
x^3-x
$$
is nonzero and spans $W$ by step <1>3.
Thus it is a basis of $W$.

:::

:::

::: pf-step

Consequently,
$$
\boxed{\dim V+\dim W=4+1=5}.
$$


::: pf-proof

Combine steps <1>1 and <1>4.
This is answer choice $\boxed{\text{(B)}}$.

:::

:::

::: pf-qed

Step <1>5 is the required value.

:::

:::
