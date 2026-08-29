---
schema: qual/card@1
id: P-PS4CG
kind: problem
title: A group of order $p^2 q$ has a unique Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Classification
  - Simple Groups
relations: []
review: draft
---

::: problem
Since $n_p \neq 1$ by assumption, we must have $n_p = q$.
Now consider sub-cases for $n_q$:

- $n_q = p$: Sylow gives $n_q \equiv 1 \mod q$, so $p \equiv 1 \mod q$.
  With $1 \leq p < q$ this reads $p = 1$, which is impossible for a prime.

- $n_q = p^2$: count the elements of order exactly $q$.

  A Sylow $q\dash$subgroup has prime order $q$, so two distinct ones intersect in a subgroup of order dividing $q$ and properly contained in each, hence trivially.
  The $n_q = p^2$ of them therefore contribute
  \[
  \abs{ \union_{S_q \in \mathrm{Syl}(q, G)} S_q\setminus\theset{e} } = n_q(q-1) = p^2(q-1)
  \]
  distinct elements of order $q$.
  That leaves
  \[
  \abs{G} - p^2(q-1) = p^2 q - p^2 q + p^2 = p^2
  \]
  elements of $G$ whose order is not $q$.

  Now every Sylow $p\dash$subgroup has order $p^2$ and consists of elements of $p\dash$power order, so it is contained in that set of exactly $p^2$ elements.
  A subgroup of order $p^2$ inside a set of size $p^2$ is the whole set, so there is only one Sylow $p\dash$subgroup and $n_p = 1$.
  This contradicts $n_p = q > 1$.
  $\qed$

> The same union bound cannot be applied to the Sylow $p\dash$subgroups.
> They have order $p^2$, which is not prime, so two distinct ones may meet in a subgroup of order $p$ and the count $n_p(p^2-1)$ would overcount.
:::
