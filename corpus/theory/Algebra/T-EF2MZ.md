---
schema: qual/card@1
id: T-EF2MZ
kind: theorem
title: 'Sylow''s second theorem: Sylow subgroups are conjugate'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Conjugacy
relations:
- kind: uses
  target: D-7TQ2M
- kind: uses
  target: L-DJKXL
- kind: uses
  target: T-WRMBM
review: draft
---

::: {.theorem}
Let $G$ be a finite group and $p$ a prime.
Any two [[D-7TQ2M|Sylow $p$-subgroups]] of $G$ are [[D-ES7MP|conjugate]]: if $P,Q\in\Syl_p(G)$, then there exists $g\in G$ with $gPg^{-1}=Q$.
In particular, a Sylow $p$-subgroup $P$ is [[D-EKE4Q|normal]] in $G$ if and only if it is the unique Sylow $p$-subgroup of $G$ [@DF04, §4.5, Theorem 18].
:::

::: {.proof}
Write $\abs G=p^a m$ with $p\nmid m$, and let $P$ and $Q$ be Sylow $p$-subgroups of $G$.
Let $P$ act on the set $G/Q$ of left cosets of $Q$ by left translation, $x\cdot gQ=xgQ$.
Since $\abs{G/Q}=m$ is prime to $p$, the [[L-DJKXL|fixed-point congruence]] gives $\abs{(G/Q)^P}\equiv m\not\equiv 0\pmod p$, so some coset $gQ$ is fixed by $P$.
Then $xgQ=gQ$ for every $x\in P$, that is, $g^{-1}Pg\subseteq Q$, and since both groups have order $p^a$, $g^{-1}Pg=Q$.

For the second statement, every conjugate $gPg^{-1}$ has order $p^a$ and is therefore a Sylow $p$-subgroup.
If $P\normal G$, every conjugate of $P$ equals $P$, so by the first statement $P$ is the only Sylow $p$-subgroup.
Conversely, if $P$ is the only Sylow $p$-subgroup, then $gPg^{-1}=P$ for every $g\in G$.
:::
