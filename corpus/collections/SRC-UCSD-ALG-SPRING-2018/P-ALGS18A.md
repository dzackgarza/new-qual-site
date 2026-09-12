---
schema: qual/card@1
id: P-ALGS18A
kind: problem
title: "A group of order p^2 q with p < q odd primes is solvable"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Suppose $p < q$ are two odd primes.
Prove that a group of order $p^2 q$ is solvable.
:::

::: {.solution}
<1>1. Let \(Q\) be a Sylow \(q\)-subgroup of \(G\), and let \(n_q\) be the number of Sylow \(q\)-subgroups.
Then
\[
n_q\mid p^2,
\qquad
n_q\equiv 1\pmod q.
\]
::: {.proof}
This is Sylow's theorem.
:::

<1>2. We have \(n_q=1\).
::: {.proof}
Since \(n_q\mid p^2\), the possibilities are \(1,p,p^2\). The value \(p\) cannot be congruent to \(1\pmod q\) because \(1<p<q\). If \(p^2\equiv1\pmod q\), then
\[
q\mid p^2-1=(p-1)(p+1).
\]
Because \(q>p\), the prime \(q\) cannot divide \(p-1\). Thus it would divide \(p+1\). But \(p\) and \(q\) are odd primes with \(q>p\), so \(q\ge p+2>p+1\), impossible.
Hence only \(n_q=1\) remains.
:::

<1>3. Therefore \(Q\trianglelefteq G\), and \(Q\) is cyclic, hence abelian.
::: {.proof}
Uniqueness makes \(Q\) normal.
Its order is the prime \(q\), so \(Q\cong C_q\).
:::

<1>4. The quotient \(G/Q\) has order \(p^2\), hence is abelian.
::: {.proof}
Every group of order \(p^2\) is abelian.
:::

<1>5. Consequently \(G\) is solvable.
::: {.proof}
We have an exact sequence
\[
1\longrightarrow Q\longrightarrow G\longrightarrow G/Q\longrightarrow1
\]
with abelian kernel and abelian quotient.
Equivalently, \(G'\subseteq Q\), so \(G''\subseteq Q'=1\). Thus the derived series terminates.
:::
:::
