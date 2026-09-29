---
schema: qual/card@1
id: P-BKS15-6B
kind: problem
title: Maximal positive-definite subspace for a quadratic form on $\RR^4$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2015 Graduate Preliminary Examination.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the square completion, invertibility of the coordinate change, and the lower and upper bounds for the positive-definite subspace dimension.
---

::: {.problem}
What is the maximal dimension of a subspace of $\RR^4$ on which the quadratic form
$$
x_1x_2-3x_2^2+x_3^2+2x_2x_4+x_4^2
$$
is positive definite?
:::

::: {.solution}
Let
$$
q(x_1,x_2,x_3,x_4)
\coloneqq
x_1x_2-3x_2^2+x_3^2+2x_2x_4+x_4^2.
$$

::: pf

::: {.pf-step #s1}

The quadratic form satisfies
$$
q
=
(x_4+x_2)^2
-
\left(2x_2-\frac{x_1}{4}\right)^2
+
\left(\frac{x_1}{4}\right)^2
+
x_3^2.
$$

::: pf-proof

Expanding the right-hand side gives
$$
\begin{aligned}
&(x_4^2+2x_2x_4+x_2^2)
-
\left(4x_2^2-x_1x_2+\frac{x_1^2}{16}\right)
+
\frac{x_1^2}{16}
+
x_3^2\\
&\qquad=
x_1x_2-3x_2^2+x_3^2+2x_2x_4+x_4^2.
\end{aligned}
$$

:::

:::

::: pf-step

The linear coordinates
$$
y_1=x_3,
\qquad
y_2=x_4+x_2,
\qquad
y_3=2x_2-\frac{x_1}{4},
\qquad
y_4=\frac{x_1}{4}
$$
form an invertible change of coordinates, and in these coordinates
$$
q=y_1^2+y_2^2-y_3^2+y_4^2.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the displayed diagonal form. The coordinate change is invertible because the original coordinates can be recovered by
$$
x_1=4y_4,
\qquad
x_2=\frac{y_3+y_4}{2},
\qquad
x_4=y_2-\frac{y_3+y_4}{2},
\qquad
x_3=y_1.
$$

:::

:::

::: {.pf-step #s3}

There is a $3$-dimensional subspace on which $q$ is positive definite.

::: pf-proof

In the $y$-coordinates, take
$$
W
\coloneqq
\{(y_1,y_2,y_3,y_4):y_3=0\}.
$$
Then $\dim W=3$ and, for every nonzero vector in $W$,
$$
q=y_1^2+y_2^2+y_4^2>0.
$$
Thus $q|_W$ is positive definite.

:::

:::

::: {.pf-step #s4}

No $4$-dimensional subspace of $\RR^4$ can have positive-definite restriction of $q$.

::: pf-proof

The only $4$-dimensional subspace of $\RR^4$ is $\RR^4$ itself. In the $y$-coordinates, the nonzero vector
$$
(0,0,1,0)
$$
satisfies
$$
q(0,0,1,0)=-1<0.
$$
Hence $q$ is not positive definite on the whole space.

:::

:::

::: {.pf-step #s5}

Therefore the maximal dimension is
$$
\boxed{3}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives a positive-definite subspace of dimension $3$, and step [](#s4){.pf-ref} rules out dimension $4$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested maximal dimension.

:::

:::

:::
