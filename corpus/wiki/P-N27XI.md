---
schema: qual/card@1
id: P-N27XI
kind: problem
title: "Thus by the first isomorphism theorem, we have $Z(R) \\cong Z(M_n(R))$."
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
Thus by the first isomorphism theorem, we have $Z(R) \cong Z(M_n(R))$.

# Problem 2

## Part 1

If $A,B$ are (skew)-symmetric, then $A^t = \pm A$ and $B^t = \pm B$ respectively. But then 
$$
(A+B)^t = A^t + B^t = \pm A + \pm B = \pm(A + B),
$$

which shows that $A+B$ is (skew)-symmetric.

## Part 2

$\implies$: 
Suppose that whenever $A,B$ are symmetric then $AB$ is symmetric as well.

We then have $(AB)^t = AB$ by assumption, and then by calculation we have $(AB^t) = B^t A^t = BA$, so $AB = BA$.

$\impliedby$:
Suppose that $AB = BA$ and $A, B$ are symmetric.
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

