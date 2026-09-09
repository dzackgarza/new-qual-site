---
schema: qual/card@1
id: P-O2H7G
kind: problem
title: $HK$ is a subgroup when $H\le N_G(K)$; a counterexample when $K$ is not a subgroup
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Centralizers and Normalizers
  - Counterexamples
relations: []
review: draft
---

::: problem
Let $H,K\le G$ and suppose $H\le N_G(K)$. Prove that $HK$ is a subgroup of $G$.
Give a counterexample if $K$ is only a subset, not a subgroup.
:::

::: {.solution}
<1>1. If $H\le N_G(K)$, then $HK\le G$.
::: {.proof}
The identity belongs to $HK$. Let $h_1k_1,h_2k_2\in HK$. Since $h_2\in N_G(K)$,
\[
k_1h_2=h_2(h_2^{-1}k_1h_2)
\]
with $h_2^{-1}k_1h_2\in K$. Hence
\[
(h_1k_1)(h_2k_2)=h_1h_2\,(h_2^{-1}k_1h_2)k_2\in HK.
\]
Also, for $hk\in HK$,
\[
(hk)^{-1}=k^{-1}h^{-1}=h^{-1}(hk^{-1}h^{-1})\in HK
\]
because $h^{-1}\in N_G(K)$. Therefore $HK$ is a subgroup.
:::

<1>2. The subgroup hypothesis on $K$ is necessary.
::: {.proof}
Take the additive group $G=\ZZ$, let $H=2\ZZ$, and let $K=\{0,1\}$. Since $G$ is abelian, every element normalizes every subset in the setwise sense, but
\[
H+K=2\ZZ\cup(2\ZZ+1)=\ZZ.
\]
This particular choice still gives a subgroup, so choose instead $H=\{0\}$ and $K=\{0,1\}$. Then $H+K=\{0,1\}$ is not a subgroup of $\ZZ$ because $1+1=2\notin\{0,1\}$.
:::
:::
