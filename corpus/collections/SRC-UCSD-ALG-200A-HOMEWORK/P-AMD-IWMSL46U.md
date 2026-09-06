---
schema: qual/card@1
id: P-AMD-IWMSL46U
kind: problem
title: Every finite group of even order has an element of order $2$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Checked the card against the source-audited UCSD Math 200A Fall 2016 Homework 1 collection occurrence. The live provenance PDF endpoint timed out during this review, so no claim is made of a fresh PDF comparison. Independently corroborated the result as the p=2 case of Cauchy's theorem and in published treatments of even-order groups.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Partitioned the non-self-inverse elements into two-element inverse pairs. Since the identity is self-inverse and |G| is even, there must be another self-inverse element; being nonidentity, it has order exactly 2.
---

::: {.problem}
Given: $|G|<\infty, |G| = 0\mod 2$

Show: $\exists g\in G \ni o(g)  = 2$
:::

::: {.solution}
Let
\[
S=\{g\in G:g\ne g^{-1}\}.
\]

<1>1. The set $S$ has even cardinality.
::: {.proof}
If $g\in S$, then
\[
g^{-1}\ne(g^{-1})^{-1}=g,
\]
so $g^{-1}\in S$.
Moreover, by the definition of $S$,
\[
g\ne g^{-1}.
\]
Thus the involution
\[
g\longmapsto g^{-1}
\]
partitions $S$ into disjoint two-element sets
\[
\{g,g^{-1}\}.
\]
Hence $|S|$ is even.
:::

<1>2. There is an element $h\in G\setminus S$ with $h\ne e$.
::: {.proof}
The identity satisfies
\[
e=e^{-1},
\]
so $e\notin S$.
By <1>1, $|S|$ is even, while $|G|$ is even by hypothesis.
Therefore
\[
|G\setminus S|=|G|-|S|
\]
is even.
Since $G\setminus S$ already contains $e$, it cannot consist of the single element $e$.
Hence there exists
\[
h\in G\setminus S,
\qquad h\ne e.
\]
:::

<1>3. The element $h$ from <1>2 has order $2$.
::: {.proof}
Because $h\notin S$,
\[
h=h^{-1}.
\]
Multiplying by $h$ gives
\[
h^2=e.
\]
Since $h\ne e$, its order is not $1$.
Its order divides $2$, so
\[
o(h)=2.
\]
Thus $G$ contains an element of order $2$.
:::
:::
