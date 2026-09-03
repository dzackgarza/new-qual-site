---
schema: qual/card@1
id: E-AMD-KRMOU3CI
kind: problem
title: Groups of order $pqr$ have a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Simple Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every group of order $pqr$ with $p<q<r$ primes contains a normal Sylow subgroup, and hence is never simple.
:::

::: solution
**Goal:** Prove that $G$ of order $pqr$ ($p < q < r$ primes) has a normal Sylow subgroup.

<1>1. Sylow $r$-subgroup analysis:
    *Proof:*
    <2>1. By the Sylow theorems, $n_r \equiv 1 \pmod r$ and $n_r \mid pq$.
    <2>2. The divisors of $pq$ are $1, p, q, pq$.
    <2>3. If $n_r = 1$, then $G$ has a normal Sylow $r$-subgroup. Done.

<1>2. Suppose $n_r > 1$:
    *Proof:*
    <2>1. Since $n_r \equiv 1 \pmod r$ and $n_r \in \{p, q, pq\}$, and $r > q > p$, we need $n_r \ge r + 1 > q$, so $n_r = pq$.
    <2>2. Each Sylow $r$-subgroup has order $r$ (prime, hence cyclic), and distinct Sylow $r$-subgroups intersect trivially.
    <2>3. The $pq$ Sylow $r$-subgroups contribute $pq(r - 1)$ elements of order $r$.

<1>3. Sylow $q$-subgroup analysis under $n_r = pq$:
    *Proof:*
    <2>1. $n_q \equiv 1 \pmod q$ and $n_q \mid pr$.
    <2>2. If $n_q = 1$, done.
    <2>3. Since $q > p$, $p \not\equiv 1 \pmod q$. Thus $n_q \in \{r, pr\}$.
    <2>4. If $n_q = r$, we need $r \equiv 1 \pmod q$. If $n_q = pr$, we need $pr \equiv 1 \pmod q$.

<1>4. Element counting argument:
    *Proof:*
    <2>1. The $pq$ Sylow $r$-subgroups contribute $pq(r-1)$ non-identity elements.
    <2>2. If $n_q > 1$, the Sylow $q$-subgroups contribute at least $r(q-1)$ non-identity elements (the minimum case $n_q = r$).
    <2>3. Total non-identity elements from Sylow $r$- and $q$-subgroups: at least $pq(r-1) + r(q-1)$.
    <2>4. The remaining elements (excluding identity): $pqr - 1 - pq(r-1) - r(q-1) = pq - 1 - r(q-1) = pq - 1 - rq + r$.
    <2>5. For $p < q < r$: $pq - rq + r - 1 = q(p - r) + (r - 1) < 0$ since $p < r$ implies $q(p-r) < -q$ while $r - 1 < q(r - p)$.
    <2>6. This means fewer than $p$ non-identity elements remain, but the Sylow $p$-subgroup requires $p - 1$ such elements.
    <2>7. Thus $n_p = 1$ (the Sylow $p$-subgroup is normal), or the count forces $n_q = 1$ or $n_r = 1$.

<1>5. Conclusion:
    In all cases, at least one Sylow subgroup is normal, so $G$ has a proper non-trivial normal subgroup and is never simple. Q.E.D.
:::
