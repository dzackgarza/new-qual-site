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
\[
\|v-v_W\|\leq\|v-w\|
\]
for every $w\in W$.
Deduce that equality holds if and only if $w=v_W$.
:::

::: {.solution}
Let
\[
w_1,\ldots,w_m
\]
be an orthonormal basis of the finite-dimensional subspace $W$.

<1>1. Define
\[
\boxed{
v_W
=
\sum_{j=1}^m
\langle v,w_j\rangle w_j
}.
\]
Then
\[
v_W\in W.
\]

::: {.proof}
The vector is a finite linear combination of basis vectors of $W$.
:::

<1>2. The vector
\[
v-v_W
\]
is orthogonal to $W$.

::: {.proof}
For each basis vector $w_k$,
\[
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
\]
Hence $v-v_W$ is orthogonal to every basis vector of $W$, and therefore to every vector in $W$.
:::

<1>3. For every $w\in W$,
\[
v-w
=
(v-v_W)+(v_W-w),
\]
and the two summands are orthogonal.

::: {.proof}
The displayed decomposition is algebraic.
By step <1>2,
\[
v-v_W
\perp
W.
\]
Since
\[
v_W-w\in W,
\]
the two summands are orthogonal.
:::

<1>4. For every $w\in W$,
\[
\|v-w\|^2
=
\|v-v_W\|^2
+
\|v_W-w\|^2.
\]

::: {.proof}
Apply the Pythagorean theorem to the orthogonal decomposition in step <1>3.
:::

<1>5. For every $w\in W$,
\[
\boxed{
\|v-v_W\|
\le
\|v-w\|
}.
\]

::: {.proof}
By step <1>4,
\[
\|v-w\|^2
=
\|v-v_W\|^2
+
\|v_W-w\|^2
\ge
\|v-v_W\|^2.
\]
Both sides are nonnegative, so taking square roots gives the inequality.
:::

<1>6. Equality
\[
\|v-v_W\|
=
\|v-w\|
\]
holds if and only if
\[
w=v_W.
\]

::: {.proof}
By step <1>4, equality of the norms is equivalent to
\[
\|v_W-w\|^2=0.
\]
This holds exactly when
\[
w=v_W.
\]
:::

<1>7. The minimizing vector is unique.

::: {.proof}
Suppose
\[
u\in W
\]
also satisfies
\[
\|v-u\|
\le
\|v-w\|
\]
for every $w\in W$.
Taking
\[
w=v_W
\]
gives
\[
\|v-u\|
\le
\|v-v_W\|.
\]
But step <1>5, applied to $w=u$, gives the reverse inequality.
Thus
\[
\|v-u\|
=
\|v-v_W\|.
\]
By step <1>6,
\[
u=v_W.
\]
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves existence of a best approximant, step <1>7 proves uniqueness, and step <1>6 gives the equality criterion.
:::
:::
