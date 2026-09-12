---
schema: qual/card@1
id: P-ALGS06F
kind: problem
title: "Projective, flat, and injective module constructions via tensor and Hom"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $R$ be a commutative ring and let $M$ and $N$ be $R$-modules.
Prove the following.

(a) If $M$ and $N$ are projective $R$-modules, then $M \otimes_R N$ is a projective $R$-module.

(b) If $M$ and $N$ are flat $R$-modules, then $M \otimes_R N$ is a flat $R$-module.

(c) If $M$ is a flat $R$-module and $N$ is an injective $R$-module, then $\operatorname{Hom}_R(M, N)$ is an injective $R$-module.

(d) Let $p$ be a prime number and let $\mathbb{Z}_{(p)}$ denote the localization of $\mathbb{Z}$ with respect to its prime ideal $p\mathbb{Z}$.
Show that $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_{(p)}, \mathbb{Q}/\mathbb{Z})$ is an injective $\mathbb{Z}$-module.
:::

::: {.solution}
<1>1. If $F$ and $G$ are free $R$-modules, then $F\otimes_R G$ is free.
::: {.proof}
Write
\[
F\cong\bigoplus_{i\in I}R,
\qquad
G\cong\bigoplus_{j\in J}R.
\]
Tensor product commutes with direct sums in each variable, so
\[
F\otimes_R G
\cong
\bigoplus_{(i,j)\in I\times J}(R\otimes_R R)
\cong
\bigoplus_{I\times J}R,
\]
which is free.
:::

<1>2. If $M$ and $N$ are projective, then $M\otimes_RN$ is projective.
::: {.proof}
Choose modules $M'$ and $N'$ and free modules $F,G$ such that
\[
F\cong M\oplus M',
\qquad
G\cong N\oplus N'.
\]
Then
\[
F\otimes_R G
\cong
(M\otimes_RN)
\oplus(M\otimes_RN')
\oplus(M'\otimes_RN)
\oplus(M'\otimes_RN').
\]
By <1>1, $F\otimes_R G$ is free. Hence $M\otimes_RN$ is a direct summand of a free module and therefore projective. This proves part (a).
:::

<1>3. If $M$ and $N$ are flat, then $M\otimes_RN$ is flat.
::: {.proof}
For every $R$-module $X$, associativity of tensor product gives a natural isomorphism
\[
X\otimes_R(M\otimes_RN)
\cong
(X\otimes_RM)\otimes_RN.
\]
Thus the functor
\[
-\otimes_R(M\otimes_RN)
\]
is naturally isomorphic to the composite
\[
(-\otimes_RM)\quad\text{followed by}\quad(-\otimes_RN).
\]
Both functors are exact because $M$ and $N$ are flat, so their composite is exact. Hence $M\otimes_RN$ is flat. This proves part (b).
:::

<1>4. Let $M$ be flat and $N$ injective. Then $\operatorname{Hom}_R(M,N)$ is injective.
::: {.proof}
Let $A\hookrightarrow B$ be an injective homomorphism of $R$-modules. Flatness of $M$ makes
\[
A\otimes_RM\longrightarrow B\otimes_RM
\]
injective. Since $N$ is injective, every homomorphism
\[
A\otimes_RM\longrightarrow N
\]
extends to $B\otimes_RM$.

By the tensor--Hom adjunction,
\[
\operatorname{Hom}_R(A,\operatorname{Hom}_R(M,N))
\cong
\operatorname{Hom}_R(A\otimes_RM,N),
\]
and similarly with $B$ in place of $A$. Therefore every map
\[
A\longrightarrow\operatorname{Hom}_R(M,N)
\]
extends to $B$. This is precisely the injectivity of $\operatorname{Hom}_R(M,N)$. This proves part (c).
:::

<1>5. The $\mathbb Z$-module $\mathbb Z_{(p)}$ is flat.
::: {.proof}
Every localization $S^{-1}R$ is flat as an $R$-module. Here
\[
\mathbb Z_{(p)}=S^{-1}\mathbb Z,
\qquad
S=\mathbb Z\setminus p\mathbb Z.
\]
:::

<1>6. The $\mathbb Z$-module $\mathbb Q/\mathbb Z$ is injective.
::: {.proof}
A $\mathbb Z$-module is injective if and only if it is divisible. The group $\mathbb Q/\mathbb Z$ is divisible: given $q+\mathbb Z$ and a nonzero integer $n$,
\[
n\left(\frac qn+\mathbb Z\right)=q+\mathbb Z.
\]
Hence $\mathbb Q/\mathbb Z$ is injective.
:::

<1>7. Therefore
\[
\operatorname{Hom}_\mathbb Z(\mathbb Z_{(p)},\mathbb Q/\mathbb Z)
\]
is an injective $\mathbb Z$-module.
::: {.proof}
Apply part (c), proved in <1>4, with
\[
R=\mathbb Z,
\qquad
M=\mathbb Z_{(p)},
\qquad
N=\mathbb Q/\mathbb Z.
\]
The hypotheses hold by <1>5 and <1>6. This proves part (d).
:::
:::
