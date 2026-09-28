---
schema: qual/card@1
id: P-LARQ1
kind: problem
title: Semidirect-product decompositions of $S_n$ and $O(2)$
classification:
  areas: [algebra]
  topics: [Group Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both semidirect-product requests with Lerman practice problem 1; added n>=2, which is necessary for the symmetric-group factor of order two."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Exhibited explicit order-two complements, checked normal kernels, trivial intersections, and factorizations for both the sign and determinant homomorphisms."
---

::: {.problem}
1. For $n\ge2$, prove that $S_n$ is a semidirect product of $A_n$ and a group of order $2$.

2. Prove that $O(2)$ is a semidirect product of $SO(2)$ and a group of order $2$.
:::


::: {.remark}
The restriction $n\ge2$ is necessary: $S_1=A_1$ is trivial and has no subgroup
of order two.
:::

::: {.solution}
<1>1. For $n\ge2$, $S_n=A_n\rtimes\langle(12)\rangle$.
::: {.proof}
The sign map
$$
\operatorname{sgn}:S_n\to\{\pm1\}
$$
is a surjective homomorphism for $n\ge2$, and its kernel is $A_n$. Therefore
$A_n\triangleleft S_n$ and has index two. Let
$$
\tau=(12),\qquad H=\langle\tau\rangle=\{1,\tau\}.
$$
Then $|H|=2$. Since the transposition $(12)$ is odd while every element of $A_n$ is even,
$$
A_n\cap H=\{1\}.
$$
For any $\sigma\in S_n$, if $\sigma$ is even then $\sigma\in A_n$. If it is
odd, then $\sigma\tau$ is even, so
$$
\sigma=(\sigma\tau)\tau\in A_nH.
$$
Thus $S_n=A_nH$, with $A_n$ normal and $A_n\cap H=1$. This is precisely the
internal semidirect product
$$
S_n=A_n\rtimes H.
$$
The corresponding action of $H$ on $A_n$ is conjugation by the transposition
$\tau$.
:::

<1>2. $O(2)=SO(2)\rtimes\langle R\rangle$ for a reflection $R$.
::: {.proof}
The determinant map
$$
\det:O(2)\to\{\pm1\}
$$
is a homomorphism with kernel $SO(2)$. It is surjective because the reflection
$$
R=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$
belongs to $O(2)$ and has determinant $-1$. Hence $SO(2)\triangleleft O(2)$
and has index two. Let $K=\langle R\rangle=\{I,R\}$. Then $|K|=2$, and
$SO(2)\cap K=\{I\}$ because $R$ has determinant $-1$.

If $A\in O(2)$ has determinant $1$, then $A\in SO(2)$. If $\det A=-1$, then
$AR$ has determinant $1$, so
$$
A=(AR)R\in SO(2)K.
$$
Thus
$$
O(2)=SO(2)K,
\qquad SO(2)\cap K=\{I\},
$$
with $SO(2)$ normal. Therefore
$$
O(2)=SO(2)\rtimes K.
$$
Conjugation by $R$ sends a rotation through angle $\theta$ to the rotation
through angle $-\theta$, giving the usual semidirect-product action.
:::
:::
