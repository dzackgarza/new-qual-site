---
schema: qual/card@1
id: P-UCLAB17F-05
kind: problem
title: Finite rank and finite-dimensional kernel operators
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2017, `assets/attachments/basic-17F.pdf`.
---

::: {.problem}
Let $V,W$ be infinite-dimensional complex vector spaces and let $\operatorname{Lin}(V,W)$ be the vector space of linear maps.

(a) Is the set of finite-rank maps a subspace?

(b) Is the set of maps with finite-dimensional kernel a subspace?

(c) What is the intersection of these two sets? Prove all claims.
:::

::: {.solution}

Let
$$
X=
\{T\in\operatorname{Lin}(V,W):\operatorname{rank}T<\infty\}
$$
and
$$
Y=
\{T\in\operatorname{Lin}(V,W):\dim\ker T<\infty\}.
$$

::: pf

::: {.pf-step #s1-1}

The zero map belongs to $X$.


::: pf-proof

Its image is
$$
\{0\},
$$
which has dimension $0$.

:::

:::

::: {.pf-step #s1-2}

If $T,S\in X$, then
$$
T+S\in X.
$$


::: pf-proof

For every $v\in V$,
$$
(T+S)v
=
Tv+Sv.
$$
Hence
$$
\operatorname{im}(T+S)
\subseteq
\operatorname{im}T+\operatorname{im}S.
$$
Both spaces on the right are finite-dimensional, so their sum is finite-dimensional.
Therefore
$$
\operatorname{rank}(T+S)<\infty.
$$

:::

:::

::: {.pf-step #s1-3}

If $T\in X$ and $\lambda\in\CC$, then
$$
\lambda T\in X.
$$


::: pf-proof

If $\lambda=0$, then $\lambda T$ is the zero map, which belongs to $X$ by step [](#s1-1){.pf-ref}.
If $\lambda\ne0$, then
$$
\operatorname{im}(\lambda T)
=
\operatorname{im}T,
$$
so the rank remains finite.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{X\text{ is a subspace of }\operatorname{Lin}(V,W)}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} verify the zero-vector, addition, and scalar-multiplication conditions for a subspace.

:::

:::

::: {.pf-step #s1-5}

The zero map does not belong to $Y$.


::: pf-proof

For the zero map,
$$
\ker 0=V.
$$
By hypothesis, $V$ is infinite-dimensional.
Thus
$$
\dim\ker0=\infty,
$$
so the zero map is not in $Y$.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{Y\text{ is not a subspace of }\operatorname{Lin}(V,W)}.
$$


::: pf-proof

Every linear subspace must contain the zero vector.
Step [](#s1-5){.pf-ref} shows that $Y$ does not contain the zero map.

:::

:::

::: {.pf-step #s1-7}

Suppose
$$
T\in X\cap Y.
$$
Then both
$$
\ker T
$$
and
$$
\operatorname{im}T
$$
are finite-dimensional.


::: pf-proof

Membership in $X$ means finite rank, hence finite-dimensional image.
Membership in $Y$ means finite-dimensional kernel.

:::

:::

::: {.pf-step #s1-8}

If both $\ker T$ and $\operatorname{im}T$ are finite-dimensional, then $V$ is finite-dimensional.


::: pf-proof

Choose a basis
$$
k_1,\ldots,k_r
$$
of $\ker T$.
Choose a basis
$$
w_1,\ldots,w_s
$$
of $\operatorname{im}T$.
For each $j$, choose
$$
v_j\in V
$$
such that
$$
Tv_j=w_j.
$$

We claim that
$$
k_1,\ldots,k_r,v_1,\ldots,v_s
$$
spans $V$.
Let $v\in V$.
Since $Tv\in\operatorname{im}T$,
$$
Tv
=
\sum_{j=1}^s a_jw_j
=
T\left(
\sum_{j=1}^s a_jv_j
\right).
$$
Thus
$$
v-\sum_{j=1}^s a_jv_j
\in
\ker T,
$$
so it is a linear combination of
$$
k_1,\ldots,k_r.
$$
Hence the finite displayed list spans $V$.
Therefore $V$ is finite-dimensional.

:::

:::

::: {.pf-step #s1-9}

Since $V$ is infinite-dimensional,
$$
\boxed{X\cap Y=\varnothing}.
$$


::: pf-proof

If some $T$ belonged to $X\cap Y$, steps [](#s1-7){.pf-ref} through [](#s1-8){.pf-ref} would imply that $V$ is finite-dimensional, contradicting the hypothesis.
Thus no such map exists.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers part (a), step [](#s1-6){.pf-ref} answers part (b), and step [](#s1-9){.pf-ref} answers part (c).

:::

:::

:::
