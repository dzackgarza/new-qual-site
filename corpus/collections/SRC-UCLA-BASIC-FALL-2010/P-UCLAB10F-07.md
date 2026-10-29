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
Let $V$ and $W$ be complex inner-product spaces with
$$
\dim V\le\dim W<\infty.
$$
Prove that there is a linear map $T:V\to W$ such that
$$
\langle T(v),T(v')\rangle_W=\langle v,v'\rangle_V
$$
for all $v,v'\in V$.
:::

::: {.solution}

Let
$$
m=\dim V,
\qquad
n=\dim W,
$$
so that $m\le n$.

::: pf

::: pf-step

There is an orthonormal basis
$$
v_1,\ldots,v_m
$$
of $V$.


::: pf-proof

Choose any basis of $V$ and apply the Gram--Schmidt process.

:::

:::

::: pf-step

There are orthonormal vectors
$$
w_1,\ldots,w_m
$$
in $W$.


::: pf-proof

Choose an orthonormal basis
$$
w_1,\ldots,w_n
$$
of $W$ by Gram--Schmidt. Since $m\le n$, retain its first $m$ vectors.

:::

:::

::: {.pf-step #s1-3}

Define
$$
T:V\to W
$$
by
$$
T\left(\sum_{i=1}^m a_iv_i\right)
=
\sum_{i=1}^m a_iw_i.
$$
Then $T$ is a well-defined linear map.


::: pf-proof

Every vector of $V$ has a unique coordinate expansion in the basis $v_1,\ldots,v_m$, so the formula is well-defined. It is linear because it is defined by sending the basis vector $v_i$ to $w_i$ and extending linearly.

:::

:::

::: {.pf-step #s1-4}

For
$$
v=\sum_{i=1}^m a_iv_i
\qquad\text{and}\qquad
v'=\sum_{i=1}^m b_iv_i,
$$
one has
$$
\langle Tv,Tv'\rangle_W
=
\sum_{i=1}^m a_i\overline{b_i}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
Tv=\sum_i a_iw_i,
\qquad
Tv'=\sum_i b_iw_i.
$$
Since the $w_i$ are orthonormal,
$$
\begin{aligned}
\langle Tv,Tv'\rangle_W
&=
\sum_{i,j}a_i\overline{b_j}\langle w_i,w_j\rangle_W\\
&=
\sum_i a_i\overline{b_i}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

One also has
$$
\langle v,v'\rangle_V
=
\sum_{i=1}^m a_i\overline{b_i}.
$$


::: pf-proof

The vectors $v_1,\ldots,v_m$ form an orthonormal basis of $V$, so the same computation as in step [](#s1-4){.pf-ref} applies.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\langle T(v),T(v')\rangle_W
=
\langle v,v'\rangle_V
}
$$
for all $v,v'\in V$.


::: pf-proof

Compare the formulas in steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} constructs the required linear map, and step [](#s1-6){.pf-ref} proves that it preserves the inner product.

:::

:::

:::
