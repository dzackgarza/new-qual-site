---
schema: qual/card@1
id: P-ALGS08D
kind: problem
title: "Structure of Galois group when an intermediate field has degree 2"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Compared the statement with Problem 4 on page 2 of the official Spring 2008 algebra exam and with its reproduction in the UCSD field-theory review sheet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked the degree-index correspondence and the index-two normality conclusion, including the case Gal(F/L) is trivial.
---

::: problem
Suppose there exists an intermediate field $L$ of the Galois extension $F/E$ of degree 2 over $E$.
What can we say about $\operatorname{Gal}(F/E)$?
:::

::: {.solution}
<1>1. The subgroup corresponding to $L$ has index $2$ in $\operatorname{Gal}(F/E)$.
::: {.proof}
Set
\[
G=\operatorname{Gal}(F/E)
\qquad\text{and}\qquad
H=\operatorname{Gal}(F/L).
\]
By the fundamental theorem of Galois theory,
\[
[G:H]=[L:E]=2.
\]
Thus $G$ contains a subgroup of index $2$.
:::

<1>2. Consequently $H$ is normal and $G$ has a quotient isomorphic to $C_2$.
::: {.proof}
Every subgroup of index $2$ is normal: the two left cosets and the two right cosets both consist of $H$ and its complement, so they coincide.
Hence
\[
H\trianglelefteq G.
\]
The quotient has order
\[
|G/H|=[G:H]=2,
\]
and therefore
\[
G/H\cong C_2.
\]
Equivalently, $G$ admits a surjective homomorphism onto $C_2$.
In particular $|G|$ is even.

This is the general structural conclusion: $\operatorname{Gal}(F/E)$ has a normal subgroup of index $2$.
:::
:::
