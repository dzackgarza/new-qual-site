---
schema: qual/card@1
id: P-ALGF08B
kind: problem
title: "A group of order 30 has a normal subgroup"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 2 of the official UCSD Algebra Qualifying Examination, Fall 2008; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the Sylow-count contradiction showing that either the Sylow 3-subgroup or the Sylow 5-subgroup is unique and therefore normal.
---

::: {.problem}
Show that a group of order 30 has a normal subgroup.
:::

::: {.solution}
Let
\[
|G|=30=2\cdot3\cdot5.
\]
We will show that \(G\) has a nontrivial proper normal Sylow subgroup.

<1>1. The number \(n_5\) of Sylow \(5\)-subgroups is either \(1\) or \(6\), and the number \(n_3\) of Sylow \(3\)-subgroups is either \(1\) or \(10\).
::: {.proof}
Sylow's theorem gives
\[
n_5\equiv1\pmod5,
\qquad
n_5\mid6.
\]
The divisors of \(6\) congruent to \(1\pmod5\) are \(1\) and \(6\), so
\[
n_5\in\{1,6\}.
\]
Similarly,
\[
n_3\equiv1\pmod3,
\qquad
n_3\mid10,
\]
so
\[
n_3\in\{1,10\}.
\]
:::

<1>2. It is impossible to have simultaneously \(n_5=6\) and \(n_3=10\).
::: {.proof}
Distinct subgroups of order \(5\) intersect trivially, because their intersection is a subgroup whose order divides \(5\), and a nontrivial intersection would force the two subgroups to coincide.
Hence six Sylow \(5\)-subgroups contribute
\[
6(5-1)=24
\]
distinct nonidentity elements of order \(5\).
Likewise, ten Sylow \(3\)-subgroups contribute
\[
10(3-1)=20
\]
distinct nonidentity elements of order \(3\).
No element counted in the first set can occur in the second, because a nonidentity element cannot have both order \(5\) and order \(3\).
Thus \(G\) would contain at least
\[
24+20=44
\]
distinct nonidentity elements, although \(G\) has only \(29\) nonidentity elements.
This is impossible.
:::

<1>3. Therefore \(G\) has a nontrivial proper normal subgroup.
::: {.proof}
By <1>2, either
\[
n_5=1
\]
or
\[
n_3=1.
\]
A unique Sylow subgroup is invariant under conjugation and hence normal.
Thus either the Sylow \(5\)-subgroup or the Sylow \(3\)-subgroup is a nontrivial proper normal subgroup of \(G\).
:::
:::
