---
schema: qual/card@1
id: P-MMAQ-FBNP7JLLPX
kind: problem
title: Groups of order 57
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Classify all groups of order 57.
:::


::: {.solution}
Since
\[
57=3\cdot 19,
\]
let \(G\) be a group of order \(57\). By Sylow's theorem, the number \(n_{19}\) of Sylow \(19\)-subgroups satisfies
\[
n_{19}\mid3,\qquad n_{19}\equiv1\pmod{19}.
\]
Hence \(n_{19}=1\). Thus the Sylow \(19\)-subgroup \(N\cong C_{19}\) is normal.

Let \(P\) be a Sylow \(3\)-subgroup. Then \(P\cong C_3\), \(N\cap P=1\), and
\[
|NP|=\frac{|N||P|}{|N\cap P|}=57,
\]
so \(G=NP\). Therefore
\[
G\cong C_{19}\rtimes_\varphi C_3
\]
for a homomorphism
\[
\varphi:C_3\longrightarrow \operatorname{Aut}(C_{19}).
\]
Now
\[
\operatorname{Aut}(C_{19})\cong (\mathbb Z/19\mathbb Z)^\times\cong C_{18}.
\]
Since \(C_{18}\) has a unique subgroup of order \(3\), there are, up to automorphisms of \(C_3\) and \(C_{19}\), exactly two possible actions:

1. the trivial action, giving
   \[
   C_{19}\times C_3\cong C_{57};
   \]

2. the unique nontrivial action, whose image is the unique subgroup of order \(3\) in \(C_{18}\), giving one nonabelian semidirect product.

For example, since \(7^3\equiv1\pmod{19}\) and \(7\not\equiv1\pmod{19}\), the nonabelian group can be presented as
\[
\langle a,b\mid a^{19}=b^3=1,\;bab^{-1}=a^7\rangle.
\]
The two groups are not isomorphic because one is abelian and the other is not.

Hence, up to isomorphism, there are exactly two groups of order \(57\):
\[
\boxed{C_{57}}
\qquad\text{and}\qquad
\boxed{C_{19}\rtimes C_3}.
\]
:::
