---
schema: qual/card@1
id: P-HGQ8T
kind: problem
title: '$\implies$:'
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---

$\implies$: Suppose that whenever $A,B$ are symmetric then $AB$ is symmetric as well.

We then have $(AB)^t = AB$ by assumption, and then by calculation we have $(AB^t) = B^t A^t = BA$, so $AB = BA$.

$\impliedby$: Suppose that $AB = BA$ and $A, B$ are symmetric.
We want to show that $AB$ is also symmetric, so we compute
$$
(AB)^t = B^t A^t = BA = BA.
$$
$\qed$

Now let $B \in M_n(R)$ be arbitrary.
We have

- $(BB^t)^t = (B^t)^t B^t = BB^t$, so $BB^t$ is symmetric,

- $(B + B^t)^t = B^t + (B^t)^t = B^t + B = B + B^t$, so $B + B^t$ is symmetric,

- $(B - B^t)^t = B^t - B = - (B + B^t)$, so $B-B^t$ is skew-symmetric
