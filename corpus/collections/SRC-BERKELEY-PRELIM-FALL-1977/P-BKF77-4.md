---
schema: qual/card@1
id: P-BKF77-4
kind: problem
title: Finite-order invertible operator over a finite field
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Used finiteness of GL(V) over a finite field to force a repetition among positive powers of the invertible operator."
---

::: {.problem}
Let $P$ be a linear operator on a finite-dimensional vector space over a finite field. Show that if $P$ is invertible, then $P^n=I$ for some positive integer $n$.
:::

::: {.solution}
Let the underlying field have $q$ elements and let
$$
d=\dim V.
$$
Then $V$ has exactly
$$
q^d
$$
elements, so in particular there are only finitely many functions
$V\to V$, and hence only finitely many invertible linear operators on $V$.

<1>1. The powers of $P$ lie in a finite group.
::: {.proof}
Because $P$ is invertible, every power
$$
P^k\qquad(k\ge0)
$$
is an invertible linear operator. Thus all powers lie in the finite group
$$
GL(V).
$$
:::

<1>2. Two powers must coincide.
::: {.proof}
The infinite sequence
$$
I,P,P^2,P^3,\ldots
$$
takes values in the finite set $GL(V)$. Therefore there exist integers
$$
0\le i<j
$$
such that
$$
P^i=P^j.
$$
:::

<1>3. Cancel the smaller power.
::: {.proof}
Multiplying
$$
P^i=P^j
$$
on the left by $P^{-i}$ gives
$$
I=P^{j-i}.
$$
Since
$$
n=j-i>0,
$$
we have found a positive integer $n$ such that
$$
\boxed{P^n=I.}
$$
:::
:::
