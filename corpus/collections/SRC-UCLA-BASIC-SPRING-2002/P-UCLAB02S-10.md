---
schema: qual/card@1
id: P-UCLAB02S-10
kind: problem
title: Best approximation by a finite-dimensional subspace of an inner-product space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
Let $V$ be a complex inner-product space, let $W\subset V$ be a finite-dimensional subspace, and let $v\in V$.
Prove that there exists a unique vector $v_W\in W$ such that
$$
\|v-v_W\|\leq\|v-w\|
$$
for every $w\in W$.
Deduce that equality holds if and only if $w=v_W$.
:::

::: {.solution}

Let
$$
w_1,\ldots,w_m
$$
be an orthonormal basis of the finite-dimensional subspace $W$.

::: pf

::: pf-step

Define
$$
\boxed{
v_W
=
\sum_{j=1}^m
\langle v,w_j\rangle w_j
}.
$$
Then
$$
v_W\in W.
$$


::: pf-proof

The vector is a finite linear combination of basis vectors of $W$.

:::

:::

::: {.pf-step #s1-2}

The vector
$$
v-v_W
$$
is orthogonal to $W$.


::: pf-proof

For each basis vector $w_k$,
$$
\begin{aligned}
\langle v-v_W,w_k\rangle
&=
\langle v,w_k\rangle
-
\sum_{j=1}^m
\langle v,w_j\rangle
\langle w_j,w_k\rangle\\
&=
\langle v,w_k\rangle
-
\langle v,w_k\rangle\\
&=
0.
\end{aligned}
$$
Hence $v-v_W$ is orthogonal to every basis vector of $W$, and therefore to every vector in $W$.

:::

:::

::: {.pf-step #s1-3}

For every $w\in W$,
$$
v-w
=
(v-v_W)+(v_W-w),
$$
and the two summands are orthogonal.


::: pf-proof

The displayed decomposition is algebraic.
By step [](#s1-2){.pf-ref},
$$
v-v_W
\perp
W.
$$
Since
$$
v_W-w\in W,
$$
the two summands are orthogonal.

:::

:::

::: {.pf-step #s1-4}

For every $w\in W$,
$$
\|v-w\|^2
=
\|v-v_W\|^2
+
\|v_W-w\|^2.
$$


::: pf-proof

Apply the Pythagorean theorem to the orthogonal decomposition in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

For every $w\in W$,
$$
\boxed{
\|v-v_W\|
\le
\|v-w\|
}.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\|v-w\|^2
=
\|v-v_W\|^2
+
\|v_W-w\|^2
\ge
\|v-v_W\|^2.
$$
Both sides are nonnegative, so taking square roots gives the inequality.

:::

:::

::: {.pf-step #s1-6}

Equality
$$
\|v-v_W\|
=
\|v-w\|
$$
holds if and only if
$$
w=v_W.
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, equality of the norms is equivalent to
$$
\|v_W-w\|^2=0.
$$
This holds exactly when
$$
w=v_W.
$$

:::

:::

::: {.pf-step #s1-7}

The minimizing vector is unique.


::: pf-proof

Suppose
$$
u\in W
$$
also satisfies
$$
\|v-u\|
\le
\|v-w\|
$$
for every $w\in W$.
Taking
$$
w=v_W
$$
gives
$$
\|v-u\|
\le
\|v-v_W\|.
$$
But step [](#s1-5){.pf-ref}, applied to $w=u$, gives the reverse inequality.
Thus
$$
\|v-u\|
=
\|v-v_W\|.
$$
By step [](#s1-6){.pf-ref},
$$
u=v_W.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves existence of a best approximant, step [](#s1-7){.pf-ref} proves uniqueness, and step [](#s1-6){.pf-ref} gives the equality criterion.

:::

:::

:::
