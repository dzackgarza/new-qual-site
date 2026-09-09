---
schema: qual/card@1
id: P-N27XI
kind: problem
title: $Z(R)\cong Z(M_n(R))$ via $r\mapsto rI_n$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Matrices
  - Isomorphism Theorems
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $R$ be a ring with identity $1 \ne 0$, and let $M_n(R)$ be the ring of $n \times n$ matrices over $R$ ($n \ge 1$).
Prove that the center of the matrix ring $M_n(R)$ consists precisely of scalar matrices $r I_n$ where $r \in Z(R)$, and hence:
$$Z(M_n(R)) \cong Z(R) \quad \text{via the ring isomorphism } r \mapsto r I_n.$$
:::

::: solution
For $n=1$, this is immediate because $M_1(R)=R$.
Assume $n\ge2$ and let
\[
A=(a_{kl})\in Z(M_n(R)).
\]
For the matrix units $E_{ij}$, centrality gives
\[
AE_{ij}=E_{ij}A
\qquad(1\le i,j\le n).
\]

Fix $i\neq j$. Comparing the $(i,j)$ entries gives
\[
a_{ii}=a_{jj},
\]
so all diagonal entries equal some $r\in R$. Comparing the $(k,j)$ entries for $k\neq i$ gives
\[
a_{ki}=0.
\]
As $i$ varies, every off-diagonal entry vanishes. Hence
\[
A=rI_n.
\]

Now let $x\in R$. Since $A$ commutes with $xE_{11}$,
\[
(rx)E_{11}=A(xE_{11})=(xE_{11})A=(xr)E_{11},
\]
so $rx=xr$. Thus $r\in Z(R)$.

Conversely, if $r\in Z(R)$ and $B=(b_{ij})\in M_n(R)$, then
\[
(rI_n)B=(rb_{ij})=(b_{ij}r)=B(rI_n),
\]
so $rI_n\in Z(M_n(R))$. Therefore
\[
Z(M_n(R))=\{rI_n:r\in Z(R)\}.
\]
The map
\[
Z(R)\longrightarrow Z(M_n(R)),\qquad r\longmapsto rI_n,
\]
is plainly a bijective ring homomorphism.
:::
