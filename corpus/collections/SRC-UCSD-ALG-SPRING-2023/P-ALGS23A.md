---
schema: qual/card@1
id: P-ALGS23A
kind: problem
title: "Classification, solvability, and nilpotence of groups of order 55"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: {.problem}
Suppose $G$ is a group of order 55.

(a) Classify possible structures of the group $G$.

(b) Is $G$ always solvable? Justify your answer.

(c) Is $G$ always nilpotent? Justify your answer.
:::

::: {.solution}

::: pf

::: pf-step

Every group \(G\) of order \(55=5\cdot11\) has a unique normal Sylow
\(11\)-subgroup \(Q\cong C_{11}\).

::: pf-proof

If \(n_{11}\) is the number of Sylow \(11\)-subgroups, then Sylow's theorems give
\(n_{11}\mid5\) and \(n_{11}\equiv1\pmod{11}\). Hence \(n_{11}=1\), so
\(Q\trianglelefteq G\). A group of prime order is cyclic, so \(Q\cong C_{11}\).

:::

:::

::: {.pf-step #s2}

If \(P\) is a Sylow \(5\)-subgroup, then \(P\cong C_5\), \(Q\cap P=1\), and
\(G=QP\). Thus
\[
G\cong C_{11}\rtimes_\varphi C_5
\]
for some homomorphism \(\varphi:C_5\to\operatorname{Aut}(C_{11})\).

::: pf-proof

Again, a group of prime order is cyclic, so \(P\cong C_5\). The intersection \(Q\cap P\)
has order dividing both \(11\) and \(5\), hence is trivial. Therefore
\[
|QP|=\frac{|Q||P|}{|Q\cap P|}=55=|G|,
\]
so \(QP=G\). Since \(Q\trianglelefteq G\), this identifies \(G\) with the indicated
semidirect product via the conjugation action of \(P\) on \(Q\).

:::

:::

::: {.pf-step #s3}

There are exactly two isomorphism classes of groups of order \(55\):
\[
C_{55}
\qquad\text{and}\qquad
C_{11}\rtimes C_5
\]
with nontrivial action in the second case.

::: pf-proof

One has
\[
\operatorname{Aut}(C_{11})\cong (\mathbb Z/11\mathbb Z)^\times\cong C_{10}.
\]
A homomorphism \(C_5\to C_{10}\) is either trivial or injective. The trivial action
gives
\[
C_{11}\times C_5\cong C_{55}.
\]
For a nontrivial action, the image must be the unique subgroup of order \(5\) in the
cyclic group \(C_{10}\). Any two injective maps \(C_5\to C_{10}\) differ by an
automorphism of \(C_5\), so the corresponding semidirect products are isomorphic. Hence
there is exactly one nonabelian isomorphism type.

:::

:::

::: pf-step

Every group of order \(55\) is solvable.

::: pf-proof

By step [](#s2){.pf-ref}, \(Q\cong C_{11}\) is normal and
\[
G/Q\cong C_5.
\]
Both \(Q\) and \(G/Q\) are abelian, so \(G\) has a subnormal series
\[
1\trianglelefteq Q\trianglelefteq G
\]
with abelian factors. Thus \(G\) is solvable. This applies to both isomorphism types in
step [](#s3){.pf-ref}.

:::

:::

::: pf-step

A group of order \(55\) need not be nilpotent: \(C_{55}\) is nilpotent, whereas
the nonabelian semidirect product is not.

::: pf-proof

The cyclic group \(C_{55}\) is abelian, hence nilpotent. In the nonabelian semidirect
product, the Sylow \(5\)-subgroup cannot be normal; if both Sylow subgroups were normal,
their product would be the direct product \(C_{11}\times C_5\), which is abelian. A
finite group is nilpotent if and only if all of its Sylow subgroups are normal.
Therefore the nonabelian group is not nilpotent.

:::

:::

:::

:::
