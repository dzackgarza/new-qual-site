---
schema: qual/card@1
id: P-UGAP09S-05
kind: problem
title: The range of a linear map is a subspace of dimension at most the domain
classification:
  areas: [prelim]
  topics:
  - Linear Maps
  - Vector Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $V$ be a finite-dimensional vector space and let $T:V\to W$ be linear. Give self-contained proofs that
$$
\operatorname{Range}(T)=\{y\in W:y=Tx\text{ for some }x\in V\}
$$
is a subspace of $W$ and that
$$
\dim\operatorname{Range}(T)\le \dim V.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The zero vector of $W$ belongs to $\operatorname{Range}(T)$.


::: pf-proof

Since $T$ is linear,
$$
T(0_V)=0_W.
$$
Thus
$$
0_W\in\operatorname{Range}(T).
$$

:::

:::

::: {.pf-step #s1-2}

The range is closed under linear combinations.


::: pf-proof

Let
$$
y_1=T(x_1),
\qquad
y_2=T(x_2)
$$
belong to $\operatorname{Range}(T)$, and let $a,b$ be scalars. By linearity,
$$
ay_1+by_2
=aT(x_1)+bT(x_2)
=T(ax_1+bx_2).
$$
Hence
$$
ay_1+by_2\in\operatorname{Range}(T).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{\operatorname{Range}(T)\text{ is a subspace of }W}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} verify the subspace criteria.

:::

:::

::: {.pf-step #s1-4}

If
$$
\{v_1,\dots,v_n\}
$$
is a basis of $V$, then
$$
\{T(v_1),\dots,T(v_n)\}
$$
spans $\operatorname{Range}(T)$.


::: pf-proof

Let $y\in\operatorname{Range}(T)$. Then
$$
y=T(x)
$$
for some $x\in V$. Since the $v_i$ form a basis,
$$
x=\sum_{i=1}^n c_i v_i
$$
for some scalars $c_i$. Therefore
$$
y
=T(x)
=T\!\left(\sum_{i=1}^n c_i v_i\right)
=\sum_{i=1}^n c_i T(v_i).
$$
Thus every vector in the range lies in the span of the listed images.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\boxed{\dim\operatorname{Range}(T)\le\dim V}.
$$


::: pf-proof

Let
$$
n=\dim V.
$$
By step [](#s1-4){.pf-ref}, $\operatorname{Range}(T)$ is spanned by at most $n$ vectors.
Any finite-dimensional vector space spanned by $n$ vectors has dimension at
most $n$. Hence
$$
\dim\operatorname{Range}(T)\le n=\dim V.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the subspace assertion and step [](#s1-5){.pf-ref} proves the dimension
bound.

:::

:::

:::
