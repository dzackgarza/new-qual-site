---
schema: qual/card@1
id: P-ALGS25A
kind: problem
title: No simple group of order $pq\ell$ for distinct primes $p < q < \ell$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $p < q < \ell$ are distinct primes.
Prove that there is no simple group of order $pq\ell$.
:::

::: {.solution}

::: pf

::: pf-step

Suppose for contradiction that \(G\) is simple of order \(pq\ell\), where \(p<q<\ell\).

::: pf-proof

We assume simplicity and derive an impossible element count.

:::

:::

::: {.pf-step #s2}

The number \(n_\ell\) of Sylow \(\ell\)-subgroups is \(pq\).

::: pf-proof

Sylow's theorems give
\[
n_\ell\mid pq,
\qquad
n_\ell\equiv1\pmod\ell.
\]
Simplicity rules out \(n_\ell=1\). The proper divisors \(p\) and \(q\) are both strictly smaller than \(\ell\), so neither can be congruent to \(1\pmod\ell\). Hence \(n_\ell=pq\).

:::

:::

::: {.pf-step #s3}

The Sylow \(\ell\)-subgroups contain exactly
\[
pq(\ell-1)
\]
distinct nonidentity elements.

::: pf-proof

Each Sylow \(\ell\)-subgroup has prime order \(\ell\), so distinct ones intersect only in the identity. There are \(pq\) such subgroups by step [](#s2){.pf-ref}, each contributing \(\ell-1\) nonidentity elements.

:::

:::

::: {.pf-step #s4}

Therefore only
\[
pq-1
\]
nonidentity elements of \(G\) remain outside all Sylow \(\ell\)-subgroups.

::: pf-proof

The total number of nonidentity elements is \(pq\ell-1\). Subtract the number in step [](#s3){.pf-ref}:
\[
pq\ell-1-pq(\ell-1)=pq-1.
\]

:::

:::

::: pf-step

Simplicity forces the number \(n_q\) of Sylow \(q\)-subgroups to satisfy \(n_q\ge\ell\).

::: pf-proof

Sylow's theorems give
\[
n_q\mid p\ell,
\qquad
n_q\equiv1\pmod q.
\]
Simplicity rules out \(n_q=1\). The divisor \(p\) is smaller than \(q\), so it cannot be congruent to \(1\pmod q\). Thus the only remaining possible divisors are \(\ell\) and \(p\ell\), both at least \(\ell\).

:::

:::

::: {.pf-step #s6}

The Sylow \(q\)-subgroups therefore contain at least
\[
\ell(q-1)
\]
distinct nonidentity elements, all outside the Sylow \(\ell\)-subgroups.

::: pf-proof

Distinct subgroups of prime order \(q\) intersect only in the identity, so the \(n_q\) Sylow \(q\)-subgroups contribute \(n_q(q-1)\ge\ell(q-1)\) distinct nonidentity elements. An element of order \(q\) cannot lie in a subgroup of order \(\ell\).

:::

:::

::: {.pf-step #s7}

One has
\[
\ell(q-1)>pq-1.
\]

::: pf-proof

Since \(\ell>q\),
\[
\ell(q-1)>q(q-1).
\]
Since \(q>p\) are integers, \(q-1\ge p\), so \(q(q-1)\ge pq>pq-1\).

:::

:::

::: pf-step

This contradicts step [](#s4){.pf-ref}. Hence no group of order \(pq\ell\) is simple.

::: pf-proof

By steps [](#s6){.pf-ref} and [](#s7){.pf-ref} there would be more than \(pq-1\) nonidentity elements outside the Sylow \(\ell\)-subgroups, while step [](#s4){.pf-ref} says there are exactly \(pq-1\).

:::

:::

:::

:::
