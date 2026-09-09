---
schema: qual/card@1
id: P-ALGS22A
kind: problem
title: "Classification of groups of order 2022 with normal Sylow 2-subgroup"
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

::: problem
Let $G$ be a group of order $2022 = (2)(3)(337)$.
Suppose that the Sylow 2-subgroup of $G$ is normal.
Classify such groups $G$ up to isomorphism.
:::


::: {.solution}
<1>1. Let \(P\in\operatorname{Syl}_2(G)\) and \(R\in\operatorname{Syl}_{337}(G)\). Then \(P\cong C_2\), \(R\cong C_{337}\), and both are normal in \(G\).
::: {.proof}
The subgroup \(P\) has order \(2\) and is normal by hypothesis. For \(R\), Sylow gives \(n_{337}\mid6\) and \(n_{337}\equiv1\pmod{337}\), so \(n_{337}=1\). Thus \(R\trianglelefteq G\).
:::

<1>2. The subgroup \(P\) is central, and \(PR\cong C_2\times C_{337}\cong C_{674}\) is normal of order \(674\).
::: {.proof}
Conjugation gives a homomorphism \(G\to\operatorname{Aut}(P)\). Since \(P\cong C_2\) has trivial automorphism group, \(P\le Z(G)\). Also \(P\cap R=1\), and two normal subgroups with trivial intersection commute because \([P,R]\subseteq P\cap R\). Hence \(PR\cong P\times R\), and it is normal as a product of normal subgroups.
:::

<1>3. Let \(Q\in\operatorname{Syl}_3(G)\). Then \(Q\cong C_3\), \(G=PRQ\), and
\[
G\cong (C_2\times C_{337})\rtimes C_3.
\]
::: {.proof}
The subgroup \(Q\) has order \(3\) and intersects \(PR\) trivially. Since \(|PR||Q|=674\cdot3=2022=|G|\), one has \(G=PRQ\). Because \(PR\trianglelefteq G\), this is a semidirect product.
:::

<1>4. The action of \(Q\) on \(P\) is trivial, and its action on \(R\) is either trivial or the unique nontrivial homomorphism
\[
C_3\longrightarrow\operatorname{Aut}(C_{337})\cong C_{336}.
\]
::: {.proof}
The action on \(P\) is trivial because \(P\le Z(G)\). Since \(R\cong C_{337}\), its automorphism group is cyclic of order \(336\). A homomorphism from \(C_3\) has image of order \(1\) or \(3\). The cyclic group \(C_{336}\) has a unique subgroup of order \(3\), so there is one nontrivial action up to isomorphism.
:::

<1>5. Hence there are exactly two isomorphism classes:
\[
C_{2022}
\]
and
\[
C_2\times(C_{337}\rtimes C_3),
\]
where in the second group a generator of \(C_3\) acts on \(C_{337}\) by any automorphism of order \(3\).
::: {.proof}
The trivial action gives \(C_2\times C_{337}\times C_3\cong C_{2022}\), since the three orders are pairwise coprime. The unique nontrivial action gives the second group. It is nonabelian, so the two groups are not isomorphic. By <1>4 there are no further actions and hence no further groups.
:::
:::
