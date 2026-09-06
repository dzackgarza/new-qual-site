---
schema: qual/card@1
id: P-AMD-5Y25FRNQ
kind: problem
title: $A_n$ ($n\geq 5$) has a subgroup of index $n$ but none of smaller index
classification:
  areas:
  - algebra
  topics:
  - Simple Groups
  - Permutations
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 3, Exercise 7(c). Corrected
    the reversed index notation: the source asks that A_n have no subgroup H
    with [A_n:H]<n, while point stabilizers have index exactly n.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    If H<A_n had index m<n, simplicity plus the coset action would force
    |A_n|=n!/2 to divide m!, impossible because n!/2>(n-1)!>=m!. The natural
    action of A_n on n points is transitive, and a point stabilizer therefore
    has index n.
---

::: {.problem}
Assume that $A_n$ is simple for every $n\ge5$.

1. Prove that if $n\ge5$, then $A_n$ has no subgroup $H$ with
   \[
   [A_n:H]<n.
   \]

2. Prove that $A_n$ has a subgroup of index exactly $n$.
:::

::: {.solution}
Fix $n\ge5$.

<1>1. A proper subgroup $H<A_n$ of index $m$ would force
\[
|A_n|\mid m!.
\]
::: {.proof}
Suppose
\[
[A_n:H]=m<\infty.
\]
The action of $A_n$ on the left cosets $A_n/H$ gives a homomorphism
\[
\rho:A_n\longrightarrow S_m.
\]
Its kernel is the normal core of $H$.
Since $H$ is proper, that core is a proper normal subgroup of $A_n$.
By simplicity,
\[
\ker\rho=\{e\}.
\]
Thus $\rho$ is injective, so $A_n$ is isomorphic to a subgroup of $S_m$.
Lagrange's theorem therefore gives
\[
|A_n|\mid |S_m|=m!.
\]
:::

<1>2. No subgroup of $A_n$ has index strictly smaller than $n$.
::: {.proof}
Suppose for contradiction that $H<A_n$ has index
\[
m=[A_n:H]<n.
\]
Then <1>1 gives
\[
|A_n|\mid m!.
\]
But
\[
|A_n|=\frac{n!}{2}=\frac n2\,(n-1)!>(n-1)!
\]
because $n\ge5$, while
\[
m!\le(n-1)!.
\]
Hence $|A_n|>m!$, so the positive integer $|A_n|$ cannot divide $m!$, a contradiction.
:::

<1>3. The natural action of $A_n$ on $\{1,\ldots,n\}$ is transitive.
::: {.proof}
Let $i,j\in\{1,\ldots,n\}$ with $i\ne j$.
Since $n\ge5$, choose $k\notin\{i,j\}$.
The $3$-cycle
\[
(i\ j\ k)
\]
is even, hence lies in $A_n$, and sends $i$ to $j$.
Thus any point can be sent to any other point, so the action is transitive.
:::

<1>4. A point stabilizer in $A_n$ has index $n$.
::: {.proof}
Fix $i\in\{1,\ldots,n\}$ and let
\[
H=(A_n)_i
=\{\sigma\in A_n:\sigma(i)=i\}.
\]
By <1>3, the orbit of $i$ has cardinality $n$.
Orbit-stabilizer therefore gives
\[
[A_n:H]
=|A_n\cdot i|
=n.
\]
Thus $A_n$ has a subgroup of index exactly $n$.
:::
:::
