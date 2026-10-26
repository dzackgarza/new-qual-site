---
schema: qual/card@1
id: P-UGAP09F-06
kind: problem
title: Dimension and basis of a trigonometric function space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $V$ be the real vector space spanned by
\[
1,\qquad \sin^2x,\qquad \cos^2x,\qquad \sin(2x),\qquad \cos(2x).
\]
Find $\dim_{\mathbb R}V$ and exhibit a basis for $V$ over $\mathbb R$.
:::

::: pf

::: pf-step

The space $V$ is spanned by
$$
1,\qquad \sin(2x),\qquad \cos(2x).
$$


::: pf-proof

The double-angle identities give
$$
\sin^2x=\frac{1-\cos(2x)}2,
\qquad
\cos^2x=\frac{1+\cos(2x)}2.
$$
Thus each of the five original generators lies in
$\operatorname{span}_{\RR}\{1,\sin(2x),\cos(2x)\}$, while these three functions are themselves among the span of the original generators. Hence the two spans are equal.

:::

:::

::: pf-step

The functions $1$, $\sin(2x)$, and $\cos(2x)$ are linearly independent over $\RR$.


::: pf-proof

Suppose
$$
a+b\sin(2x)+c\cos(2x)=0
$$
for every real $x$. Setting $x=0$ gives $a+c=0$, while setting $x=\pi/2$ gives $a-c=0$. Hence $a=c=0$. Setting $x=\pi/4$ then gives $b=0$. Therefore the only linear relation is the trivial one.

:::

:::

::: pf-step

One has
$$
\boxed{\dim_{\RR}V=3},
$$
with basis
$$
\boxed{\{1,\sin(2x),\cos(2x)\}}.
$$


::: pf-proof

Step <1>1 shows that these three functions span $V$, and step <1>2 shows that they are linearly independent. Hence they form a basis, which has three elements.

:::

:::

::: pf-qed

Step <1>3 gives both the dimension and the requested basis.

:::

:::
