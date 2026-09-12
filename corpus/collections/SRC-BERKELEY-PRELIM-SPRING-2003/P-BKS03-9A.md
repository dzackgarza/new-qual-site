---
schema: qual/card@1
id: P-BKS03-9A
kind: problem
title: The ring $\mathbb Z+3i\mathbb Z$ is not a UFD
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let
\[
R=\{a+3bi:a,b\in\mathbb Z\}.
\]
Prove that $R$ is a subring of $\mathbb C$, an integral domain, and not a unique factorization domain.
:::

::: {.solution}
It’s routine to verify that R is an additive subgroup and is closed under multiplication. Since C is a field, any subring is an integral domain. Consider two factorizations of the integer 10 in R, namely $1 0 = 2 \cdot 5$ and $1 0 = ( 1 + 3 i ) ( 1 - 3 i )$ . The norm $\vert z \vert ^ { 2 } = a ^ { 2 } + 9 b ^ { 2 }$ of any $z \in R$ is an integer, and if $| z | ^ { 2 } < 9$ then b = 0, so z is a real integer. This implies in particular that 2 has no non-trivial factorization in R. If R were a UFD, then 2 would divide 1 + 3i or $1 - 3 i$ . But that can’t be, since $( 1 \pm 3 i ) / 2$ are not in R.
:::
