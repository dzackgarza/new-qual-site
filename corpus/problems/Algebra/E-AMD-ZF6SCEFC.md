---
schema: qual/card@1
id: E-AMD-ZF6SCEFC
kind: exercise
title: Groups of order $p^2q^2$ are abelian when $q\nmid p^2-1$ and $p\nmid q^2-1$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Abelian Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that a group of order $p^2 q^2$ where $q$ does not divide $p^2-1$ and $p$ does not divide $q^2-1$ is abelian.
:::

::: solution
**Goal:** Show $G$ is abelian under the Sylow divisibility hypotheses.

<1> Let $|G|=p^2 q^2$ with distinct primes $p$ and $q$.
    *Proof:*
    <2>1. Let $n_p$ be the number of Sylow $p$-subgroups and $n_q$ the number of Sylow $q$-subgroups.
    <2>2. By Sylow:
        $$n_p\mid q^2,\quad n_p\equiv 1 \pmod p,$$
        $$n_q\mid p^2,\quad n_q\equiv 1 \pmod q.$$

<1> Force normality of both Sylow subgroups.
    *Proof:*
    <2>1. The divisors of $q^2$ are $1,q,q^2$.
    <2>2. If $n_p=q$, then $q\equiv1\pmod p$, so $p\mid q-1$, hence $p\mid q^2-1$, contradicting the hypothesis.
    <2>3. If $n_p=q^2$, then $q^2\equiv1\pmod p$, so $p\mid q^2-1$, also excluded.
    <2>4. Hence $n_p=1$, so the Sylow $p$-subgroup $P$ is normal.
    <2>5. If $n_q=p$, then $p\equiv1\pmod q$, so $q\mid p-1$, hence $q\mid p^2-1$, excluded.
    <2>6. If $n_q=p^2$, then $p^2\equiv1\pmod q$, so $q\mid p^2-1$, excluded.
    <2>7. Hence $n_q=1$, so the Sylow $q$-subgroup $Q$ is normal.

<1> Conclude abelian.
    *Proof:*
    <2>1. $P\cap Q=\{e\}$ because $|P|$ and $|Q|$ are coprime.
    <2>2. $PQ$ is a subgroup of $G$ with
        $$|PQ|=\frac{|P||Q|}{|P\cap Q|}=p^2q^2=|G|,$$
        so $PQ=G$.
    <2>3. For $p\in P$ and $q\in Q$, $pq=qp$ because $P$ and $Q$ are normal and intersect trivially.
    <2>4. Therefore every element of $G=P Q$ can be written uniquely as $pq$, and $G\cong P\times Q$.
    <2>5. Direct products of abelian groups are abelian, so $G$ is abelian.

Authored by **Codex 5.3 Spark Extra High**.
:::
