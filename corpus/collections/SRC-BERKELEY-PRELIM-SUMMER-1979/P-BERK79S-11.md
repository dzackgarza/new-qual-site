---
schema: qual/card@1
id: P-BERK79S-11
kind: problem
title: Idempotent matrices of equal rank are similar
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For an idempotent A, every vector decomposes uniquely as
    Av+(v-Av), with the first term in im A and the second in ker A. Thus
    V=im A⊕ker A, A acts as identity on its image and zero on its kernel,
    and a basis adapted to this decomposition gives diag(I_r,0). Equal
    ranks therefore give the same normal form for A and B.
---

::: {.problem}
Let $A,B\in M_n(F)$ satisfy
\[
A^2=A,
\qquad
B^2=B.
\]
Suppose $A$ and $B$ have the same rank.
Prove that $A$ and $B$ are similar.
:::

::: {.solution}
Let
$$
V=F^n.
$$

::: pf

::: {.pf-step #s1}

If $A^2=A$, then
$$
V=\operatorname{im}A+\ker A.
$$

::: pf-proof

Let $v\in V$. Then
$$
v
=
Av+(v-Av).
$$
The first term lies in $\operatorname{im}A$. For the second term,
$$
A(v-Av)
=
Av-A^2v
=
Av-Av
=
0,
$$
so
$$
v-Av\in\ker A.
$$
Thus every vector lies in the sum.

:::

:::

::: {.pf-step #s2}

One has
$$
\operatorname{im}A\cap\ker A=\{0\}.
$$

::: pf-proof

Let
$$
w\in\operatorname{im}A\cap\ker A.
$$
Since $w\in\operatorname{im}A$, there is $v\in V$ such that
$$
w=Av.
$$
Then
$$
Aw
=
A^2v
=
Av
=
w.
$$
But $w\in\ker A$, so $Aw=0$. Hence $w=0$.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\boxed{
V=\operatorname{im}A\oplus\ker A.
}
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the sum, and step [](#s2){.pf-ref} shows that it is direct.

:::

:::

::: {.pf-step #s4}

The restriction of $A$ to $\operatorname{im}A$ is the identity,
while its restriction to $\ker A$ is zero.

::: pf-proof

If $w\in\operatorname{im}A$, write
$$
w=Av.
$$
Then
$$
Aw
=
A^2v
=
Av
=
w.
$$
If $w\in\ker A$, then $Aw=0$ by definition.

:::

:::

::: {.pf-step #s5}

If
$$
r=\operatorname{rank}A,
$$
then $A$ is similar to
$$
\boxed{
\begin{pmatrix}
I_r&0\\
0&0
\end{pmatrix}.
}
$$

::: pf-proof

Choose a basis
$$
u_1,\ldots,u_r
$$
of $\operatorname{im}A$ and a basis
$$
w_1,\ldots,w_{n-r}
$$
of $\ker A$. By step [](#s3){.pf-ref}, their union is a basis of $V$. By step [](#s4){.pf-ref},
the matrix of $A$ in this basis is identity on the first $r$ basis vectors
and zero on the remaining $n-r$ basis vectors. Hence it is the displayed
block diagonal matrix.

:::

:::

::: {.pf-step #s6}

If
$$
\operatorname{rank}A
=
\operatorname{rank}B
=
r,
$$
then both $A$ and $B$ are similar to
$$
\begin{pmatrix}
I_r&0\\
0&0
\end{pmatrix}.
$$

::: pf-proof

Step [](#s5){.pf-ref} applies to $A$. Since $B^2=B$ as well, the same argument applies
to $B$, and the common rank hypothesis gives the same integer $r$.

:::

:::

::: {.pf-step #s7}

The matrices $A$ and $B$ are similar:
$$
\boxed{
A\sim B.
}
$$

::: pf-proof

Similarity is transitive. Step [](#s6){.pf-ref} shows that $A$ and $B$ are both
similar to the same block diagonal matrix, so they are similar to each
other.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required conclusion.

:::

:::

:::
