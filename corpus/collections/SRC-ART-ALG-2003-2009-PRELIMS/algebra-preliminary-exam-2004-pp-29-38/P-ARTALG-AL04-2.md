---
schema: qual/card@1
id: P-ARTALG-AL04-2
kind: problem
title: Every group of size 15 is cyclic
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Prove that any group of size 15 is cyclic.
:::

::: {.solution}
Let $G$ be a group of order $15=3\cdot5$.

::: pf

::: pf-step

$G$ has a unique Sylow $3$-subgroup $P\cong\ZZ/3\ZZ$ and a unique Sylow $5$-subgroup $Q\cong\ZZ/5\ZZ$, and both are normal in $G$.

::: pf-proof

By the Sylow theorems, the number $n_3$ of Sylow $3$-subgroups satisfies $n_3\equiv1\pmod3$ and $n_3\mid5$, so $n_3=1$.
Likewise $n_5\equiv1\pmod5$ and $n_5\mid3$, so $n_5=1$.
A unique Sylow $p$-subgroup is normal, since conjugation permutes the Sylow $p$-subgroups.
Groups of prime order are cyclic.

:::

:::

::: {.pf-step #s2}

$G\cong P\times Q$.

::: pf-proof

By Lagrange's theorem, $|P\cap Q|$ divides $\gcd(3,5)=1$, so $P\cap Q=\{e\}$.
For $p\in P$ and $q\in Q$, the commutator $[p,q]=pqp^{-1}q^{-1}$ equals $(pqp^{-1})q^{-1}\in Q$ because $Q\lhd G$, and equals $p(qp^{-1}q^{-1})\in P$ because $P\lhd G$.
Hence $[p,q]\in P\cap Q=\{e\}$, so $pq=qp$.
Therefore $\varphi\colon P\times Q\to G$, $\varphi(p,q)=pq$, is a group homomorphism.
Its kernel is $\{(p,p^{-1}) : p\in P\cap Q\}=\{(e,e)\}$, so $\varphi$ is injective, and $\abs{P\times Q}=15=\abs{G}$ makes it an isomorphism.

:::

:::

::: {.pf-step #s3}

$G$ is cyclic.

::: pf-proof

By step [](#s2){.pf-ref} and the Chinese remainder theorem, $G\cong\ZZ/3\ZZ\times\ZZ/5\ZZ\cong\ZZ/15\ZZ$.
Equivalently, if $P=\langle a\rangle$ and $Q=\langle b\rangle$, then $a$ and $b$ commute and have coprime orders, so $ab$ has order $\operatorname{lcm}(3,5)=15$ and $G=\langle ab\rangle$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves that every group of order $15$ is cyclic.

:::

:::

:::
