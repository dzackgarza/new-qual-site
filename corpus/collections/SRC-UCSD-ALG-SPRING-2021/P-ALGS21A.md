---
schema: qual/card@1
id: P-ALGS21A
kind: problem
title: "Classification of groups of order 56 with all Sylow subgroups cyclic"
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
Classify up to isomorphism all groups $G$ of order 56 with the property that all Sylow subgroups of $G$ are cyclic.
Write down a presentation for each group you find.
:::

::: {.solution}

::: pf

::: pf-step

Let \(P\in\operatorname{Syl}_7(G)\). Then \(n_7\in\{1,8\}\).

::: pf-proof

By Sylow's theorem, \(n_7\mid 8\) and \(n_7\equiv1\pmod7\). The only possibilities are \(1\) and \(8\).

:::

:::

::: pf-step

In fact \(n_7=1\), so the Sylow \(7\)-subgroup \(P\cong C_7\) is normal.

::: pf-proof

Suppose \(n_7=8\). Distinct Sylow \(7\)-subgroups intersect trivially, so their union contains
\[
1+8(7-1)=49
\]
elements. Thus exactly \(7\) nonidentity elements of \(G\) lie outside that union. Any Sylow \(2\)-subgroup has order \(8\), hence has exactly \(7\) nonidentity elements, and none of those can lie in a subgroup of order \(7\). Therefore every Sylow \(2\)-subgroup consists of the identity together with those same seven remaining elements. Hence the Sylow \(2\)-subgroup is unique and normal.

Then both a Sylow \(7\)-subgroup and a Sylow \(2\)-subgroup would be normal. Their intersection is trivial, so they commute elementwise and their product is direct of order \(56\). In particular the Sylow \(7\)-subgroup would then be unique, contradicting \(n_7=8\). Thus \(n_7=1\).

:::

:::

::: pf-step

Let \(Q\in\operatorname{Syl}_2(G)\). By hypothesis \(P\cong C_7\) and \(Q\cong C_8\), and
\[
G=P Q\cong C_7\rtimes_\varphi C_8
\]
for some homomorphism
\[
\varphi:C_8\longrightarrow\operatorname{Aut}(C_7)\cong C_6.
\]

::: pf-proof

Since \(P\trianglelefteq G\), \(PQ\) is a subgroup. Also \(P\cap Q=1\) because their orders are coprime, so
\[
|PQ|=|P||Q|=7\cdot8=56=|G|.
\]
Thus \(G=PQ\), giving the indicated semidirect product. The action is conjugation by \(Q\) on \(P\).

:::

:::

::: pf-step

The image of \(\varphi\) has order at most \(2\). Hence there are only two possible actions: the trivial action, and the unique nontrivial action whose image has order \(2\).

::: pf-proof

The image order divides both \(|C_8|=8\) and \(|\operatorname{Aut}(C_7)|=6\), so it divides \(\gcd(8,6)=2\). Since \(C_6\) has a unique subgroup of order \(2\), there is exactly one nontrivial image. Also \(C_8\) has a unique quotient of order \(2\), so the nontrivial homomorphism is unique up to automorphisms of source and target.

:::

:::

::: pf-step

For the trivial action,
\[
G\cong C_7\times C_8\cong C_{56}.
\]
A presentation is
\[
\langle a,b\mid a^7=b^8=1,\ bab^{-1}=a\rangle.
\]

::: pf-proof

Trivial conjugation gives the direct product. Since \(7\) and \(8\) are coprime, \(C_7\times C_8\) is cyclic of order \(56\).

:::

:::

::: pf-step

For the nontrivial action, a generator \(b\) of \(C_8\) acts by the unique order-two automorphism of \(C_7\), namely inversion. Thus
\[
G\cong\langle a,b\mid a^7=b^8=1,\ bab^{-1}=a^{-1}\rangle.
\]

::: pf-proof

The automorphism group of \(C_7\) is cyclic of order \(6\). Its unique element of order \(2\) sends every element to its inverse, so the unique nontrivial action is \(a\mapsto a^{-1}\).

:::

:::

::: pf-step

These two groups are nonisomorphic and both satisfy the required Sylow condition.

::: pf-proof

The first group is abelian. The second is nonabelian because \(a\ne a^{-1}\) in \(C_7\), so they are not isomorphic. In each group the exhibited Sylow \(7\)-subgroup is cyclic of order \(7\), and the exhibited Sylow \(2\)-subgroup is cyclic of order \(8\); all Sylow subgroups are conjugate to these, hence cyclic.

:::

:::

:::

:::
