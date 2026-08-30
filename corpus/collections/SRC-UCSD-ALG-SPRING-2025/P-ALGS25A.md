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
---

::: problem
Suppose $p < q < \ell$ are distinct primes.
Prove that there is no simple group of order $pq\ell$.
:::

::: {.solution}
<1>1. Suppose $G$ is simple of order $pq\ell$ with $p<q<\ell$.
Proof: assume for contradiction.

<1>2. $n_\ell \equiv1\pmod\ell$ and $n_\ell\mid pq$, so $n_\ell=pq$.
Proof: Sylow, $n_\ell\neq1$ (otherwise $\ell$-Sylow normal).

<1>3. Then $G$ has $pq(\ell-1)$ elements of order $\ell$.
Proof: $n_\ell$ Sylows intersect trivially, each has $\ell-1$ non-identity elements.

<1>4. $n_q\equiv1\pmod q$ and $n_q\mid p\ell$, so $n_q\in\{1,p\ell\}$; if $n_q=p\ell$ then $p\ell(q-1)$ elements of order $q$.
Proof: Sylow.

<1>5. Counting gives $pq(\ell-1)+p\ell(q-1) > pq\ell$ for $p<q<\ell$, impossible, so $n_q=1$.
Proof: <1>3 and <1>4.

<1>6. Then $G$ has a normal Sylow $q$-subgroup, contradicting simplicity.
Proof: <1>5.

<1>7. Similarly $n_p=1$ leads to contradiction; hence no simple group of order $pq\ell$.
Proof: counting.

<1>8. Q.E.D.
Proof: <1>6.
:::
