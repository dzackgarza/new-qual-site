---
schema: qual/card@1
id: P-P4KA6
kind: problem
title: Recognizing direct products
classification:
  areas:
  - algebra
  topics:
  - Direct Products
  - Normal Subgroups
  - Isomorphism Theorems
relations: []
review: draft
---

::: {.problem}
Let $H,K\trianglelefteq G$ satisfy
$$
H\cap K=\{e\},\qquad HK=G.
$$
Prove that $G\cong H\times K$. Generalize the criterion to finitely many normal subgroups.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The subgroups $H$ and $K$ commute elementwise.

::: pf-proof

For $h\in H$ and $k\in K$, the commutator
$$
[h,k]=hkh^{-1}k^{-1}
$$
lies in $H$ because $H$ is normal, and lies in $K$ because $K$ is normal. Hence
$$
[h,k]\in H\cap K=\{e\}.
$$
Thus $hk=kh$.

:::

:::

::: {.pf-step #iso}

The map $\mu\colon H\times K\to G$, $(h,k)\mapsto hk$, is an isomorphism.

::: pf-proof

By step [](#s1){.pf-ref} it is a homomorphism. It is surjective because $HK=G$. If $hk=e$, then $h=k^{-1}\in H\cap K$, so $h=k=e$. Thus $\mu$ is injective.

:::

:::

::: pf-step

If $H_1,\ldots,H_r\trianglelefteq G$ satisfy $G=H_1\cdots H_r$ and $H_i\cap\prod_{j\ne i}H_j=\{e\}$ for every $i$, then multiplication $H_1\times\cdots\times H_r\to G$ is an isomorphism.

::: pf-proof

Induct on $r$; the case $r=2$ is step [](#iso){.pf-ref}. For $r\ge3$, the product $N\coloneqq H_1\cdots H_{r-1}$ is a normal subgroup of $G$, as a product of normal subgroups. The subgroups $H_1,\ldots,H_{r-1}$ of $N$ satisfy the hypotheses inside $N$, because $H_i\cap\prod_{j\ne i,\,j<r}H_j\subseteq H_i\cap\prod_{j\ne i}H_j=\{e\}$, so by induction $N\cong H_1\times\cdots\times H_{r-1}$ by multiplication. Also $N\cap H_r=\{e\}$ and $NH_r=G$, so step [](#iso){.pf-ref} gives $G\cong N\times H_r$ by multiplication. Composing gives the claim.

Pairwise trivial intersections are not enough for $r\ge3$: in $V_4=\{e,a,b,ab\}$ the subgroups $\langle a\rangle,\langle b\rangle,\langle ab\rangle$ intersect pairwise trivially and their product is $V_4$, but $V_4$ has order $4$, not $8$.

:::

:::

:::

:::
