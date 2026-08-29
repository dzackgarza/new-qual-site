---
schema: qual/card@1
id: P-NLMMW
kind: problem
title: Groups of order $pq$ need not be nilpotent
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Classification
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
If $|G| = pq$ (distinct primes), is $G$ necessarily nilpotent?
:::

::: solution
**Goal:** Prove that a group of order $pq$ need not be nilpotent by exhibiting a counterexample.

<1>1. Counterexample: $S_3$:
    *Proof:*
    <2>1. $|S_3| = 6 = 2 \cdot 3$.
    <2>2. The center of $S_3$ is trivial: $Z(S_3) = \{e\}$.
    <2>3. For a nilpotent group, the upper central series must reach $G$ in finitely many steps. Since $Z_1(S_3) = Z(S_3) = \{e\}$, the series is $\{e\} = Z_0 = Z_1 = \cdots$ and never reaches $S_3$.
    <2>4. Thus $S_3$ is not nilpotent.

<1>2. General criterion:
    *Proof:*
    <2>1. A finite group is nilpotent if and only if it is the direct product of its Sylow subgroups.
    <2>2. Equivalently, $G$ is nilpotent iff every Sylow subgroup is normal.
    <2>3. For $|G| = pq$ with $p < q$: the Sylow $q$-subgroup is always normal ($n_q = 1$), but $n_p = q$ is possible when $q \equiv 1 \pmod p$.
    <2>4. When $n_p > 1$ (i.e. $q \equiv 1 \pmod p$), the Sylow $p$-subgroup is not normal, so $G$ is not nilpotent. The non-abelian group $\mathbb{Z}_q \rtimes \mathbb{Z}_p$ in this case is the counterexample.

<1>3. Conclusion:
    Groups of order $pq$ are not necessarily nilpotent; $S_3 \cong \mathbb{Z}_3 \rtimes \mathbb{Z}_2$ is a counterexample. Q.E.D.
:::
