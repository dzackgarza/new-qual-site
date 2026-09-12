---
schema: qual/card@1
id: P-HGRO10
kind: problem
title: A finite nonabelian group with no smaller nontrivial quotient
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Group Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Give an example of a finite nonabelian group with no nontrivial homomorphic image of smaller order.
:::

::: solution
Take $G=A_5$.

<1>1. The group $A_5$ is nonabelian and simple.
::: proof
It is nonabelian, for example because $(123)$ and $(345)$ do not commute.

To prove simplicity, note that the conjugacy classes in $A_5$ have sizes
\[
1,\qquad 20,\qquad 15,\qquad 12,\qquad 12,
\]
corresponding respectively to the identity, the $3$-cycles, the products of two
disjoint transpositions, and the two conjugacy classes of $5$-cycles.
Any normal subgroup is a union of conjugacy classes containing the identity, and
its order must divide $60$. No sum of $1$ with a proper nonempty subcollection
of $20,15,12,12$ divides $60$. Hence the only normal subgroups are $1$ and
$A_5$.
:::

<1>2. Every homomorphism $f:A_5\to Q$ is either trivial or injective.
::: proof
The kernel of $f$ is normal in $A_5$. By <1>1 it is either $A_5$, in which case
$f$ is trivial, or $1$, in which case $f$ is injective.
:::

<1>3. Therefore $A_5$ has no nontrivial homomorphic image of smaller order.
::: proof
If the image of $f$ is nontrivial, <1>2 gives
\[
|f(A_5)|=|A_5|=60.
\]
Thus no nontrivial image has smaller order.
:::
:::
