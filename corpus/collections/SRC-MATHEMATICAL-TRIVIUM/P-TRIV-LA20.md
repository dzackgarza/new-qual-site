---
schema: qual/card@1
id: P-TRIV-LA20
kind: problem
title: Commutators and anticommutators of the Pauli matrices
classification:
  areas: [prelim]
  topics:
  - Pauli Matrices
  - Commutators
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Let $\sigma_i$, $i = 1, 2, 3$ be the Pauli matrices.

(a) Calculate $[\sigma_i, \sigma_j] \equiv \sigma_i\sigma_j - \sigma_j\sigma_i$, $i, j = 1, 2, 3$.

(b) Calculate $\{\sigma_i, \sigma_j\} \equiv \sigma_i\sigma_j + \sigma_j\sigma_i$, $i, j = 1, 2, 3$.

(c) Calculate $[\sigma_i, [\sigma_j, \sigma_k]] + [\sigma_j, [\sigma_k, \sigma_i]] + [\sigma_k, [\sigma_i, \sigma_j]]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Pauli matrices satisfy
$$
\sigma_1^2=\sigma_2^2=\sigma_3^2=I.
$$


::: pf-proof

Direct multiplication of each Pauli matrix by itself gives the identity
matrix.

:::

:::

::: {.pf-step #s1-2}

Their cyclic products satisfy
$$
\sigma_1\sigma_2=i\sigma_3,
\qquad
\sigma_2\sigma_3=i\sigma_1,
\qquad
\sigma_3\sigma_1=i\sigma_2.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-3}

Reversing the order changes the sign:
$$
\sigma_2\sigma_1=-i\sigma_3,
\qquad
\sigma_3\sigma_2=-i\sigma_1,
\qquad
\sigma_1\sigma_3=-i\sigma_2.
$$


::: pf-proof

This follows by direct multiplication, or by taking the adjoint of the
identities in step [](#s1-2){.pf-ref} and using $\sigma_i^\dagger=\sigma_i$.

:::

:::

::: {.pf-step #s1-4}

Therefore, for all $i,j\in\{1,2,3\}$,
$$
\boxed{
\sigma_i\sigma_j
=
\delta_{ij}I
+
i\sum_{k=1}^3\varepsilon_{ijk}\sigma_k.
}
$$


::: pf-proof

If $i=j$, step [](#s1-1){.pf-ref} gives the identity. If $i\neq j$, steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}
give the product with the sign determined by the Levi-Civita symbol.

:::

:::

::: {.pf-step #s1-5}

The commutator is
$$
\boxed{
[\sigma_i,\sigma_j]
=
2i\sum_{k=1}^3\varepsilon_{ijk}\sigma_k.
}
$$


::: pf-proof

Subtract the formula in step [](#s1-4){.pf-ref} with $i,j$ interchanged. The Kronecker
delta terms cancel, while
$$
\varepsilon_{jik}=-\varepsilon_{ijk}.
$$

:::

:::

::: {.pf-step #s1-6}

Part (a) follows.


::: pf-proof

This is step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The anticommutator is
$$
\boxed{
\{\sigma_i,\sigma_j\}
=
2\delta_{ij}I.
}
$$


::: pf-proof

Add the formula in step [](#s1-4){.pf-ref} to the same formula with $i,j$ interchanged.
The Levi-Civita terms cancel and the two Kronecker-delta terms add.

:::

:::

::: {.pf-step #s1-8}

Part (b) follows.


::: pf-proof

This is step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Matrix commutators satisfy the Jacobi identity
$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-10}

Hence
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


::: pf-proof

Apply step [](#s1-9){.pf-ref} with
$$
X=\sigma_i,
\qquad
Y=\sigma_j,
\qquad
Z=\sigma_k.
$$

:::

:::

::: {.pf-step #s1-11}

Part (c) follows.


::: pf-proof

This is step [](#s1-10){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} and [](#s1-8){.pf-ref}, and [](#s1-11){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
