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

::: problem
Suppose $p < q < \ell$ are distinct primes.
Prove that there is no simple group of order $pq\ell$.
:::

::: {.solution}
<1>1. Suppose for contradiction that \(G\) is simple of order \(pq\ell\), where \(p<q<\ell\).
::: {.proof}
We assume simplicity and derive an impossible element count.
:::

<1>2. The number \(n_\ell\) of Sylow \(\ell\)-subgroups is \(pq\).
::: {.proof}
Sylow's theorems give
\[
n_\ell\mid pq,
\qquad
n_\ell\equiv1\pmod\ell.
\]
Simplicity rules out \(n_\ell=1\). The proper divisors \(p\) and \(q\) are both strictly smaller than \(\ell\), so neither can be congruent to \(1\pmod\ell\). Hence \(n_\ell=pq\).
:::

<1>3. The Sylow \(\ell\)-subgroups contain exactly
\[
pq(\ell-1)
\]
distinct nonidentity elements.
::: {.proof}
Each Sylow \(\ell\)-subgroup has prime order \(\ell\), so distinct ones intersect only in the identity. There are \(pq\) such subgroups by <1>2, each contributing \(\ell-1\) nonidentity elements.
:::

<1>4. Therefore only
\[
pq-1
\]
nonidentity elements of \(G\) remain outside all Sylow \(\ell\)-subgroups.
::: {.proof}
The total number of nonidentity elements is \(pq\ell-1\). Subtract the number in <1>3:
\[
pq\ell-1-pq(\ell-1)=pq-1.
\]
:::

<1>5. Simplicity forces the number \(n_q\) of Sylow \(q\)-subgroups to satisfy \(n_q\ge\ell\).
::: {.proof}
Sylow's theorems give
\[
n_q\mid p\ell,
\qquad
n_q\equiv1\pmod q.
\]
Simplicity rules out \(n_q=1\). The divisor \(p\) is smaller than \(q\), so it cannot be congruent to \(1\pmod q\). Thus the only remaining possible divisors are \(\ell\) and \(p\ell\), both at least \(\ell\).
:::

<1>6. The Sylow \(q\)-subgroups therefore contain at least
\[
\ell(q-1)
\]
distinct nonidentity elements, all outside the Sylow \(\ell\)-subgroups.
::: {.proof}
Distinct subgroups of prime order \(q\) intersect only in the identity, so the \(n_q\) Sylow \(q\)-subgroups contribute \(n_q(q-1)\ge\ell(q-1)\) distinct nonidentity elements. An element of order \(q\) cannot lie in a subgroup of order \(\ell\).
:::

<1>7. One has
\[
\ell(q-1)>pq-1.
\]
::: {.proof}
Since \(\ell>q\),
\[
\ell(q-1)>q(q-1).
\]
Since \(q>p\) are integers, \(q-1\ge p\), so \(q(q-1)\ge pq>pq-1\).
:::

<1>8. This contradicts <1>4. Hence no group of order \(pq\ell\) is simple.
::: {.proof}
By <1>6 and <1>7 there would be more than \(pq-1\) nonidentity elements outside the Sylow \(\ell\)-subgroups, while <1>4 says there are exactly \(pq-1\).
:::
:::
