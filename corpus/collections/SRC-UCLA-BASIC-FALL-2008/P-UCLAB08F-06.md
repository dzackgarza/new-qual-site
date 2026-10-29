---
schema: qual/card@1
id: P-UCLAB08F-06
kind: problem
title: Rank-nullity from first principles
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
Let $V$ be an $n$-dimensional vector space and $T\colon V\to V$ linear.
Prove, without merely quoting the rank-nullity theorem, that
$$
\dim\ker T+\dim\operatorname{range}T=n.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
v_1,\ldots,v_k
$$
be a basis of $\ker T$.


::: pf-proof

The kernel is a subspace of the finite-dimensional vector space $V$, so it has a finite basis. Write
$$
k=\dim\ker T.
$$

:::

:::

::: {.pf-step #s1-2}

Extend the basis in step [](#s1-1){.pf-ref} to a basis
$$
v_1,\ldots,v_k,v_{k+1},\ldots,v_n
$$
of $V$.


::: pf-proof

Every linearly independent set in a finite-dimensional vector space extends to a basis.

:::

:::

::: {.pf-step #s1-3}

The vectors
$$
Tv_{k+1},\ldots,Tv_n
$$
span $\operatorname{range}T$.


::: pf-proof

Let $w\in\operatorname{range}T$. Then
$$
w=Tv
$$
for some
$$
v=\sum_{i=1}^n a_iv_i.
$$
Since $v_i\in\ker T$ for $i\le k$,
$$
w
=
Tv
=
\sum_{i=k+1}^n a_iTv_i.
$$
Hence the displayed vectors span the range.

:::

:::

::: {.pf-step #s1-4}

The vectors
$$
Tv_{k+1},\ldots,Tv_n
$$
are linearly independent.


::: pf-proof

Suppose
$$
\sum_{i=k+1}^n a_iTv_i=0.
$$
Then
$$
T\left(\sum_{i=k+1}^n a_iv_i\right)=0,
$$
so
$$
\sum_{i=k+1}^n a_iv_i\in\ker T
=
\operatorname{span}\{v_1,\ldots,v_k\}.
$$
But it also lies in
$$
\operatorname{span}\{v_{k+1},\ldots,v_n\}.
$$
Since the full list in step [](#s1-2){.pf-ref} is a basis, these two spans intersect only in $0$. Therefore
$$
a_{k+1}=\cdots=a_n=0.
$$

:::

:::

::: {.pf-step #s1-5}

One has
$$
\dim\operatorname{range}T=n-k.
$$


::: pf-proof

By steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}, the $n-k$ vectors
$$
Tv_{k+1},\ldots,Tv_n
$$
form a basis of $\operatorname{range}T$.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\dim\ker T+\dim\operatorname{range}T=n
}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\dim\ker T=k,
$$
and by step [](#s1-5){.pf-ref},
$$
\dim\operatorname{range}T=n-k.
$$
Adding gives $n$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the desired formula without invoking rank-nullity as a black box.

:::

:::

:::
