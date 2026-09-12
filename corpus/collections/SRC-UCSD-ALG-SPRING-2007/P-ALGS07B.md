---
schema: qual/card@1
id: P-ALGS07B
kind: problem
title: "Intersection of ideals and generators in a PID"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared both parts with Problem 2 on pages 3-4 of the official Spring 2007 UCSD algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the ideal axioms and the PID intersection formula, including the zero-ideal cases via the divisibility characterization of a least common multiple.
---

::: problem
Let $I$, $J$ be two ideals in a commutative ring $R$ (with unit).

(a) Define $K = \{x : x \in I \text{ and } x \in J\}$.
Show that $K$ is an ideal.

(b) If $R$ is a principal ideal domain, so $I = (i)$, $J = (j)$, give a formula for a generator $k$ of $K$.
:::

::: {.solution}
<1>1. The set $K=I\cap J$ is an ideal of $R$.
::: {.proof}
Because $I$ and $J$ are ideals, $0\in I$ and $0\in J$, hence $0\in K$.
If $a,b\in K$, then $a,b\in I$ and $a,b\in J$.
Therefore
\[
a-b\in I\qquad\text{and}\qquad a-b\in J,
\]
so $a-b\in K$.
Thus $K$ is an additive subgroup of $R$.

For $r\in R$ and $a\in K$, one has $a\in I\cap J$.
Since both $I$ and $J$ are ideals,
\[
ra\in I\qquad\text{and}\qquad ra\in J.
\]
Hence $ra\in K$.
Thus $K$ is an ideal.
:::

<1>2. If $R$ is a PID, then
\[
I\cap J=(\operatorname{lcm}(i,j)),
\]
where the least common multiple is defined up to multiplication by a unit.
::: {.proof}
Write $I=(i)$ and $J=(j)$.
For any $x\in R$,
\[
x\in I\cap J
\iff i\mid x\text{ and }j\mid x.
\]
Thus the elements of $I\cap J$ are exactly the common multiples of $i$ and $j$.

Since $R$ is a PID, $I\cap J$ is principal; write $I\cap J=(k)$.
Then $k$ itself is a common multiple of $i$ and $j$.
Conversely, every common multiple $x$ lies in $(k)$, so $k\mid x$.
Hence $k$ is a least common multiple of $i$ and $j$ in the divisibility sense.
Therefore one may take
\[
k=\operatorname{lcm}(i,j),
\]
up to a unit.

Equivalently, when $i,j\ne0$, if $d=\gcd(i,j)$ then one may choose
\[
k=\frac{ij}{d}
\]
up to a unit.
The ideal formula $I\cap J=(\operatorname{lcm}(i,j))$ also covers $I=(0)$ or $J=(0)$, in which case the intersection is $(0)$.
:::
:::
