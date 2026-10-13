---
schema: qual/card@1
id: P-TRIV-LA20
kind: problem
title: Commutators and anticommutators of the Pauli matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $\sigma _ { i } , i = 1 , 2 , 3$ be the Pauli matrices.

(a) Calculate $\left[ \sigma _ { i } , \sigma _ { j } \right] \equiv \sigma _ { i } \sigma _ { j } - \sigma _ { j } \sigma _ { i } , i , j = 1 , 2 , 3 .$

(b) Calculate $\{ \sigma _ { i } , \sigma _ { j } \} \equiv \sigma _ { i } \sigma _ { j } + \sigma _ { j } \sigma _ { i } , i , j = 1 , 2 , 3 .$

(c) Calculate $[ \sigma _ { i } , [ \sigma _ { j } , \sigma _ { k } ] ] + [ \sigma _ { j } , [ \sigma _ { k } , \sigma _ { i } ] ] + [ \sigma _ { k } , [ \sigma _ { i } , \sigma _ { j } ] ] .$
:::

::: {.solution}
<1>1. The Pauli matrices satisfy
$$
\sigma_1^2=\sigma_2^2=\sigma_3^2=I.
$$

::: {.proof}
Direct multiplication of each Pauli matrix by itself gives the identity
matrix.
:::

<1>2. Their cyclic products satisfy
$$
\sigma_1\sigma_2=i\sigma_3,
\qquad
\sigma_2\sigma_3=i\sigma_1,
\qquad
\sigma_3\sigma_1=i\sigma_2.
$$

::: {.proof}
For example,
$$
\sigma_1\sigma_2
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
\begin{pmatrix}
0&-i\\
i&0
\end{pmatrix}
=
\begin{pmatrix}
i&0\\
0&-i
\end{pmatrix}
=
i\sigma_3.
$$
The other two identities follow by the same direct multiplication.
:::

<1>3. Reversing the order changes the sign:
$$
\sigma_2\sigma_1=-i\sigma_3,
\qquad
\sigma_3\sigma_2=-i\sigma_1,
\qquad
\sigma_1\sigma_3=-i\sigma_2.
$$

::: {.proof}
This follows by direct multiplication, or by taking the adjoint of the
identities in step <1>2 and using $\sigma_i^\dagger=\sigma_i$.
:::

<1>4. Therefore, for all $i,j\in\{1,2,3\}$,
$$
\boxed{
\sigma_i\sigma_j
=
\delta_{ij}I
+
i\sum_{k=1}^3\varepsilon_{ijk}\sigma_k.
}
$$

::: {.proof}
If $i=j$, step <1>1 gives the identity. If $i\neq j$, steps <1>2--<1>3
give the product with the sign determined by the Levi-Civita symbol.
:::

<1>5. The commutator is
$$
\boxed{
[\sigma_i,\sigma_j]
=
2i\sum_{k=1}^3\varepsilon_{ijk}\sigma_k.
}
$$

::: {.proof}
Subtract the formula in step <1>4 with $i,j$ interchanged. The Kronecker
delta terms cancel, while
$$
\varepsilon_{jik}=-\varepsilon_{ijk}.
$$
:::

<1>6. Part (a) follows.

::: {.proof}
This is step <1>5.
:::

<1>7. The anticommutator is
$$
\boxed{
\{\sigma_i,\sigma_j\}
=
2\delta_{ij}I.
}
$$

::: {.proof}
Add the formula in step <1>4 to the same formula with $i,j$ interchanged.
The Levi-Civita terms cancel and the two Kronecker-delta terms add.
:::

<1>8. Part (b) follows.

::: {.proof}
This is step <1>7.
:::

<1>9. Matrix commutators satisfy the Jacobi identity
$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$

::: {.proof}
Expand all three commutators:
$$
\begin{aligned}
[X,[Y,Z]]
&=XYZ-XZY-YZX+ZYX,\\
[Y,[Z,X]]
&=YZX-YXZ-ZXY+XZY,\\
[Z,[X,Y]]
&=ZXY-ZYX-XYZ+YXZ.
\end{aligned}
$$
Every monomial cancels with its opposite.
:::

<1>10. Hence
$$
\boxed{
[\sigma_i,[\sigma_j,\sigma_k]]
+
[\sigma_j,[\sigma_k,\sigma_i]]
+
[\sigma_k,[\sigma_i,\sigma_j]]
=0.
}
$$

::: {.proof}
Apply step <1>9 with
$$
X=\sigma_i,
\qquad
Y=\sigma_j,
\qquad
Z=\sigma_k.
$$
:::

<1>11. Part (c) follows.

::: {.proof}
This is step <1>10.
:::

<1>12. Q.E.D.

::: {.proof}
Steps <1>6, <1>8, and <1>11 establish parts (a), (b), and (c), respectively.
:::
:::
