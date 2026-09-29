---
schema: qual/card@1
id: P-ALGS24A
kind: problem
title: Groups of order $p^2 q$ are solvable
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Classification
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
Suppose $p$ and $q$ are two distinct primes and $G$ is a group of order $p^2 q$.
Prove that $G$ is solvable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let \(n_p\) and \(n_q\) be the numbers of Sylow \(p\)- and Sylow \(q\)-subgroups of \(G\). Then
\[
n_p\mid q,\qquad n_p\equiv1\pmod p,
\]
and
\[
n_q\mid p^2,\qquad n_q\equiv1\pmod q.
\]

::: pf-proof

These are the divisibility and congruence conclusions of Sylow's theorems.

:::

:::

::: {.pf-step #s2}

If \(p>q\), then the Sylow \(p\)-subgroup is normal.

::: pf-proof

By step [](#s1){.pf-ref}, \(n_p\in\{1,q\}\). If \(n_p=q\), then \(q\equiv1\pmod p\), which is impossible because \(1<q<p\). Hence \(n_p=1\).

:::

:::

::: {.pf-step #s3}

Suppose \(p<q\). If \(n_q=1\), then the Sylow \(q\)-subgroup is normal. Otherwise \(p=2\) and \(q=3\).

::: pf-proof

By step [](#s1){.pf-ref}, \(n_q\in\{1,p,p^2\}\). Since \(p<q\), the value \(p\) cannot be congruent to \(1\pmod q\). Thus if \(n_q\ne1\), then \(n_q=p^2\). Hence
\[
p^2\equiv1\pmod q,
\]
so \(q\mid(p-1)(p+1)\). Because \(q>p\), one has \(q\nmid p-1\), hence \(q\mid p+1\). Therefore \(q\le p+1\), and since \(q>p\), one gets \(q=p+1\). The only consecutive positive integers that are both prime are \(2\) and \(3\), so \((p,q)=(2,3)\).

:::

:::

::: {.pf-step #s4}

In the exceptional case \(|G|=12\), \(G\) still has a normal Sylow subgroup.

::: pf-proof

If \(n_3=1\), the Sylow \(3\)-subgroup is normal. Otherwise \(n_3=4\). Distinct subgroups of order \(3\) intersect trivially, so the four Sylow \(3\)-subgroups contribute
\[
4(3-1)=8
\]
distinct nonidentity elements. Thus exactly four elements of \(G\) are not among those eight nonidentity elements; this four-element set includes the identity. Every Sylow \(2\)-subgroup has order \(4\) and contains no element of order \(3\), so it is contained in that four-element set and hence equals it. Therefore the Sylow \(2\)-subgroup is unique and normal.

:::

:::

::: pf-step

In every case, \(G\) has a normal Sylow subgroup \(N\) of order \(p^2\) or \(q\).

::: pf-proof

Use step [](#s2){.pf-ref} when \(p>q\), and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} when \(p<q\).

:::

:::

::: {.pf-step #s6}

The subgroup \(N\) and the quotient \(G/N\) are both abelian.

::: pf-proof

A group of prime order is cyclic, and every group of order the square of a prime is abelian. If \(|N|=p^2\), then \(|G/N|=q\); if \(|N|=q\), then \(|G/N|=p^2\).

:::

:::

::: pf-step

Therefore \(G\) is solvable.

::: pf-proof

By step [](#s6){.pf-ref}, both \(N\) and \(G/N\) are solvable. An extension of a solvable group by a solvable group is solvable.

:::

:::

:::

:::
