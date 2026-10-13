---
schema: qual/card@1
id: P-UCLAB10F-07
kind: problem
title: Isometric embedding of finite-dimensional inner-product spaces
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
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Problem 7. Let $V$ and $W$ be complex inner-product spaces with
\[
\dim V\le\dim W<\infty.
\]
Prove that there is a linear map $T:V\to W$ such that
\[
\langle T(v),T(v')\rangle_W=\langle v,v'\rangle_V
\]
for all $v,v'\in V$.
:::

::: {.solution}
Let
\[
m=\dim V,
\qquad
n=\dim W,
\]
so that $m\le n$.

<1>1. There is an orthonormal basis
\[
v_1,\ldots,v_m
\]
of $V$.

::: {.proof}
Choose any basis of $V$ and apply the Gram--Schmidt process.
:::

<1>2. There are orthonormal vectors
\[
w_1,\ldots,w_m
\]
in $W$.

::: {.proof}
Choose an orthonormal basis
\[
w_1,\ldots,w_n
\]
of $W$ by Gram--Schmidt. Since $m\le n$, retain its first $m$ vectors.
:::

<1>3. Define
\[
T:V\to W
\]
by
\[
T\left(\sum_{i=1}^m a_iv_i\right)
=
\sum_{i=1}^m a_iw_i.
\]
Then $T$ is a well-defined linear map.

::: {.proof}
Every vector of $V$ has a unique coordinate expansion in the basis $v_1,\ldots,v_m$, so the formula is well-defined. It is linear because it is defined by sending the basis vector $v_i$ to $w_i$ and extending linearly.
:::

<1>4. For
\[
v=\sum_{i=1}^m a_iv_i
\qquad\text{and}\qquad
v'=\sum_{i=1}^m b_iv_i,
\]
one has
\[
\langle Tv,Tv'\rangle_W
=
\sum_{i=1}^m a_i\overline{b_i}.
\]

::: {.proof}
By step <1>3,
\[
Tv=\sum_i a_iw_i,
\qquad
Tv'=\sum_i b_iw_i.
\]
Since the $w_i$ are orthonormal,
\[
\begin{aligned}
\langle Tv,Tv'\rangle_W
&=
\sum_{i,j}a_i\overline{b_j}\langle w_i,w_j\rangle_W\\
&=
\sum_i a_i\overline{b_i}.
\end{aligned}
\]
:::

<1>5. One also has
\[
\langle v,v'\rangle_V
=
\sum_{i=1}^m a_i\overline{b_i}.
\]

::: {.proof}
The vectors $v_1,\ldots,v_m$ form an orthonormal basis of $V$, so the same computation as in step <1>4 applies.
:::

<1>6. Therefore
\[
\boxed{
\langle T(v),T(v')\rangle_W
=
\langle v,v'\rangle_V
}
\]
for all $v,v'\in V$.

::: {.proof}
Compare the formulas in steps <1>4 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 constructs the required linear map, and step <1>6 proves that it preserves the inner product.
:::
:::
