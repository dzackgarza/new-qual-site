---
schema: qual/card@1
id: P-UCLAB12W-07
kind: problem
title: Number of invertible linear maps over a finite field
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Winter 2012. The source also introduces an unused integer k with 0 <= k <= n; it plays no role in the stated counting problem and is omitted here.
---

::: {.problem}
Let $F$ be the finite field with $p$ elements and let $V$ be an $n$-dimensional vector space over $F$.
Compute the number of invertible linear maps $V\to V$.
A lengthy algebraic expression is acceptable, provided you explain why it is correct.
:::

Fix an ordered basis
$$
e_1,\ldots,e_n
$$
of $V$.

::: pf

::: {.pf-step #s1-1}

A linear map $T:V\to V$ is invertible if and only if
$$
T(e_1),\ldots,T(e_n)
$$
is an ordered basis of $V$.


::: pf-proof

If $T$ is invertible, it preserves linear independence, so the images of the basis vectors form a basis. Conversely, if the images form a basis, then $T$ maps a basis to a basis and is therefore an isomorphism.

:::

:::

::: {.pf-step #s1-2}

There are
$$
p^n-1
$$
choices for $T(e_1)$.


::: pf-proof

The vector space $V$ has $p^n$ elements. The first vector of an ordered basis may be any nonzero vector, so there are $p^n-1$ choices.

:::

:::

::: {.pf-step #s1-3}

After linearly independent vectors
$$
T(e_1),\ldots,T(e_k)
$$
have been chosen, with $0<k<n$, there are
$$
p^n-p^k
$$
choices for $T(e_{k+1})$.


::: pf-proof

The span of $k$ linearly independent vectors is a $k$-dimensional subspace of $V$, hence has exactly $p^k$ elements. The next vector must lie outside this span, so there are $p^n-p^k$ possible choices.

:::

:::

::: {.pf-step #s1-4}

The number of ordered bases of $V$ is
$$
\prod_{k=0}^{n-1}(p^n-p^k).
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the factor $p^n-p^0$ for the first basis vector. Step [](#s1-3){.pf-ref} gives, successively, the factors
$$
p^n-p,
\quad
p^n-p^2,
\quad\ldots,\quad
p^n-p^{n-1}.
$$
Multiplying the independent successive numbers of choices gives the displayed product.

:::

:::

::: {.pf-step #s1-5}

Therefore the number of invertible linear maps $V\to V$ is
$$
\boxed{
\abs{\operatorname{GL}(V)}
=
\prod_{k=0}^{n-1}(p^n-p^k)
}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, assigning an invertible linear map is equivalent to choosing the ordered basis consisting of the images of the fixed basis $e_1,\ldots,e_n$. Step [](#s1-4){.pf-ref} counts those ordered bases.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested count.

:::

:::
