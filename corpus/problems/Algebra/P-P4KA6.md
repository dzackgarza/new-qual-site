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

::: problem
Let $H,K\trianglelefteq G$ satisfy
\[
H\cap K=\{e\},\qquad HK=G.
\]
Prove that $G\cong H\times K$. Generalize the criterion to finitely many normal subgroups.
:::

::: {.solution}
<1>1. The subgroups $H$ and $K$ commute elementwise.
::: {.proof}
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

<1>2. Multiplication gives an isomorphism.
::: {.proof}
Define
\[
\mu:H\times K\to G,\qquad (h,k)\mapsto hk.
\]
By <1>1 it is a homomorphism. It is surjective because $HK=G$. If $hk=e$, then $h=k^{-1}\in H\cap K$, so $h=k=e$. Thus $\mu$ is injective.
:::

<1>3. Finite-family version.
::: {.proof}
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
