---
schema: qual/card@1
id: P-NQRYU
kind: problem
title: The center of $M_n(R)$ is $Z(R)I_n$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Matrices
  - Rings
relations: []
review: draft
---

::: problem
Prove that for any ring $R$ with identity and $n\ge 1$,
\[
Z(M_n(R))=Z(R)I_n.
\]
:::

::: {.solution}
Let $A=(a_{ij})\in Z(M_n(R))$.

<1>1. Commuting with the matrix units forces $A$ to be scalar.
::: {.proof}
Let $E_{ij}$ be the usual matrix unit. Since $AE_{ij}=E_{ij}A$ for all $i,j$, compare entries. For $i\ne j$, the equality with $E_{jj}$ gives
\[
a_{ij}=0,
\]
so $A$ is diagonal. Then the equality with $E_{ij}$ gives
\[
a_{ii}=a_{jj}
\]
for all $i,j$. Thus
\[
A=rI_n
\]
for some $r\in R$.
:::

<1>2. The scalar $r$ lies in $Z(R)$.
::: {.proof}
For arbitrary $s\in R$, the matrix $sE_{11}$ lies in $M_n(R)$. Since $rI_n$ is central,
\[
(rI_n)(sE_{11})=(sE_{11})(rI_n).
\]
The $(1,1)$ entries are respectively $rs$ and $sr$, so $rs=sr$. As $s$ was arbitrary, $r\in Z(R)$.
:::

<1>3. Conversely, every $rI_n$ with $r\in Z(R)$ is central.
::: {.proof}
For any $B=(b_{ij})\in M_n(R)$,
\[
(rI_n)B=(rb_{ij}),\qquad B(rI_n)=(b_{ij}r).
\]
Since $r\in Z(R)$, these matrices are equal.
:::

Therefore $Z(M_n(R))=Z(R)I_n$.
:::
