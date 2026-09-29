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
\[
H\cap K=\{e\},\qquad HK=G.
\]
Prove that $G\cong H\times K$. Generalize the criterion to finitely many normal subgroups.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The subgroups $H$ and $K$ commute elementwise.

::: pf-proof

For $h\in H$ and $k\in K$, the commutator
\[
[h,k]=hkh^{-1}k^{-1}
\]
lies in $H$ because $H$ is normal, and lies in $K$ because $K$ is normal. Hence
\[
[h,k]\in H\cap K=\{e\}.
\]
Thus $hk=kh$.

:::

:::

::: pf-step

Multiplication gives an isomorphism.

::: pf-proof

Define
\[
\mu:H\times K\to G,\qquad (h,k)\mapsto hk.
\]
By step [](#s1){.pf-ref} it is a homomorphism. It is surjective because $HK=G$. If $hk=e$, then $h=k^{-1}\in H\cap K$, so $h=k=e$. Thus $\mu$ is injective.

:::

:::

::: pf-step

Finite-family version.

::: pf-proof

Let $H_1,\dots,H_r\trianglelefteq G$. If
\[
G=H_1\cdots H_r
\]
and for every $i$,
\[
H_i\cap \prod_{j\ne i}H_j=\{e\},
\]
then the subgroups commute pairwise and the multiplication map
\[
H_1\times\cdots\times H_r\longrightarrow G
\]
is an isomorphism.

Equivalently, the internal direct-product condition is precisely that the multiplication map be surjective with trivial kernel. Pairwise trivial intersections alone are not sufficient for three or more factors.

:::

:::

:::

:::
