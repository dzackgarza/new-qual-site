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

::: {.problem}
Let $R$ be a ring with identity $1 \ne 0$, and let $M_n(R)$ be the ring of $n \times n$ matrices over $R$ ($n \ge 1$).
Prove that the center of the matrix ring $M_n(R)$ consists precisely of scalar matrices $r I_n$ where $r \in Z(R)$, and hence:
$$Z(M_n(R)) \cong Z(R) \quad \text{via the ring isomorphism } r \mapsto r I_n.$$
:::

::: {.solution}
Write $E_{ij}$ for the matrix units, so that $(AE_{ij})_{kl}=a_{ki}\delta_{jl}$ and $(E_{ij}A)_{kl}=\delta_{ik}a_{jl}$ for $A=(a_{kl})\in M_n(R)$.

::: pf

::: {.pf-step #scalar}
Every $A=(a_{kl})\in Z(M_n(R))$ is a scalar matrix $rI_n$ with $r\in R$.

::: pf-proof
For $n=1$ there is nothing to prove.
For $n\ge2$, fix $i\ne j$; then $AE_{ij}=E_{ij}A$.
Comparing $(i,j)$ entries gives $a_{ii}=a_{jj}$, and comparing $(k,j)$ entries for $k\ne i$ gives $a_{ki}=0$.
As $i$ and $j$ vary, all diagonal entries are equal to some $r$ and all off-diagonal entries vanish.
:::

:::

::: {.pf-step #central}
If $rI_n\in Z(M_n(R))$, then $r\in Z(R)$.

::: pf-proof
For $x\in R$, $(rx)E_{11}=(rI_n)(xE_{11})=(xE_{11})(rI_n)=(xr)E_{11}$, so $rx=xr$.
:::

:::

::: {.pf-step #converse}
If $r\in Z(R)$, then $rI_n\in Z(M_n(R))$.

::: pf-proof
For $B=(b_{ij})\in M_n(R)$, $(rI_n)B=(rb_{ij})=(b_{ij}r)=B(rI_n)$.
:::

:::

::: pf-step
$r\mapsto rI_n$ is a ring isomorphism $Z(R)\to Z(M_n(R))$.

::: pf-proof
By steps [](#scalar){.pf-ref}, [](#central){.pf-ref} and [](#converse){.pf-ref}, $Z(M_n(R))=\{rI_n:r\in Z(R)\}$, so the map is well defined and surjective.
It is injective, and it preserves sums, products and the identity, because $rI_n+sI_n=(r+s)I_n$ and $(rI_n)(sI_n)=(rs)I_n$.
:::

:::

:::

:::
