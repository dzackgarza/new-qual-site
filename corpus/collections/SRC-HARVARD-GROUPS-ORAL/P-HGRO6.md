---
schema: qual/card@1
id: P-HGRO6
kind: problem
title: Groups of order pq
classification:
  areas: [algebra]
  topics: [Group Theory, Sylow Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard group-theory oral-question extraction, Basic Group Theory, question on groups of order pq.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
What can be said about a group of order $pq$, where $p$ and $q$ are primes?
:::

::: solution
If $p=q$, then every group of order $p^2$ is abelian, hence isomorphic to
$C_{p^2}$ or $C_p\times C_p$. Assume from now on that $p<q$.

<1>1. Every group $G$ of order $pq$ has a unique normal Sylow $q$-subgroup.
::: proof
The number $n_q$ of Sylow $q$-subgroups satisfies
\[
n_q\mid p,
\qquad
n_q\equiv1\pmod q.
\]
Since $p<q$, the only possibility is $n_q=1$.
:::

<1>2. Thus every such group has the form
\[
G\cong C_q\rtimes_\varphi C_p
\]
for some homomorphism $\varphi:C_p\to\Aut(C_q)$.
::: proof
Let $Q$ be the normal Sylow $q$-subgroup and $P$ a Sylow $p$-subgroup. Both
are cyclic because they have prime order. Since $Q\cap P=1$ and
$|QP|=|Q||P|=pq=|G|$, we have $G=QP$. Conjugation by $P$ on $Q$ gives the
required semidirect product.
:::

<1>3. If $p\nmid(q-1)$, then every group of order $pq$ is cyclic.
::: proof
Since $\Aut(C_q)\cong C_{q-1}$, a nontrivial homomorphism
$C_p\to\Aut(C_q)$ exists only if $p\mid(q-1)$. If not, the action in <1>2 is
trivial, so
\[
G\cong C_q\times C_p\cong C_{pq}.
\]
:::

<1>4. If $p\mid(q-1)$, there are exactly two isomorphism types: the cyclic
group $C_{pq}$ and one nonabelian semidirect product $C_q\rtimes C_p$.
::: proof
Because $\Aut(C_q)\cong C_{q-1}$ is cyclic, it has a unique subgroup of order
$p$. Hence every nontrivial action $C_p\to\Aut(C_q)$ has the same image.
Two injections of $C_p$ onto that subgroup differ by an automorphism of
$C_p$, so the corresponding semidirect products are isomorphic. The trivial
action gives $C_{pq}$, while a nontrivial action gives a nonabelian group.
:::
:::
