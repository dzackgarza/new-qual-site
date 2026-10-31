---
schema: qual/card@1
id: P-TRIV-LA37
kind: problem
title: Polar decomposition of $2\times 2$ matrices
classification:
  areas: [prelim]
  topics:
  - Polar Decomposition
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 37, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Write the following matrix $A$ as a product $A = SO$ of a symmetric matrix $S$ and an orthogonal matrix $O$.

(a) $A = \begin{bmatrix} 5 & 0 \\ 4 & 3 \end{bmatrix}$,

(b) $A = \begin{bmatrix} 0 & 0 \\ 4 & -3 \end{bmatrix}$.

In which case is such decomposition unique?
:::

::: {.remark}
The polar decomposition convention is used: the symmetric factor $S$ is
required to be positive semidefinite. Without this positivity condition,
factorizations $A=SO$ with merely symmetric $S$ need not be unique even in the
invertible case.
:::

::: {.solution}

For a real matrix $A$, the left polar factor is
$$
S=(AA^T)^{1/2}.
$$

::: pf

::: pf-step

For
$$
A=
\begin{pmatrix}
5&0\\
4&3
\end{pmatrix},
$$
one has
$$
AA^T
=
\begin{pmatrix}
25&20\\
20&25
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives the displayed matrix.

:::

:::

::: {.pf-step #s1-2}

The eigenvalues of $AA^T$ are $45$ and $5$, with eigenvectors
$(1,1)^T$ and $(1,-1)^T$.


::: pf-proof

The matrix has the form
$$
\begin{pmatrix}
a&b\\
b&a
\end{pmatrix},
$$
whose eigenvalues are $a+b$ and $a-b$. Here
$$
a=25,
\qquad
b=20.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
S
=
(AA^T)^{1/2}
=
\sqrt5
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
}
$$


::: pf-proof

On the eigenvectors from step [](#s1-2){.pf-ref}, the positive square root has eigenvalues
$$
\sqrt{45}=3\sqrt5
\qquad\text{and}\qquad
\sqrt5.
$$
Recombining in the standard basis gives
$$
S=
\begin{pmatrix}
2\sqrt5&\sqrt5\\
\sqrt5&2\sqrt5
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-4}

Since $S$ is invertible,
$$
O=S^{-1}A
=
\boxed{
\frac1{\sqrt5}
\begin{pmatrix}
2&-1\\
1&2
\end{pmatrix}.
}
$$


::: pf-proof

One has
$$
S^{-1}
=
\frac1{3\sqrt5}
\begin{pmatrix}
2&-1\\
-1&2
\end{pmatrix}.
$$
Hence
$$
S^{-1}A
=
\frac1{3\sqrt5}
\begin{pmatrix}
6&-3\\
3&6
\end{pmatrix}
=
\frac1{\sqrt5}
\begin{pmatrix}
2&-1\\
1&2
\end{pmatrix}.
$$

:::

:::

::: pf-step

The matrix $O$ in step [](#s1-4){.pf-ref} is orthogonal.


::: pf-proof

Its columns are
$$
\frac1{\sqrt5}
\begin{pmatrix}2\\1\end{pmatrix},
\qquad
\frac1{\sqrt5}
\begin{pmatrix}-1\\2\end{pmatrix},
$$
which are orthonormal.

:::

:::

::: {.pf-step #s1-6}

Thus part (a) has the polar decomposition
$$
\boxed{
A
=
\sqrt5
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}
\cdot
\frac1{\sqrt5}
\begin{pmatrix}
2&-1\\
1&2
\end{pmatrix}.
}
$$


::: pf-proof

This is the product of the matrices from steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

For
$$
A=
\begin{pmatrix}
0&0\\
4&-3
\end{pmatrix},
$$
one has
$$
AA^T
=
\begin{pmatrix}
0&0\\
0&25
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives the displayed matrix.

:::

:::

::: pf-step

Hence the positive semidefinite factor is
$$
\boxed{
S
=
(AA^T)^{1/2}
=
\begin{pmatrix}
0&0\\
0&5
\end{pmatrix}.
}
$$


::: pf-proof

The matrix in step [](#s1-7){.pf-ref} is diagonal with nonnegative entries, so its positive
square root is obtained by taking the square roots of the diagonal entries.

:::

:::

::: {.pf-step #s1-9}

If
$$
O=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
$$
then the condition $SO=A$ forces
$$
c=\frac45,
\qquad
d=-\frac35.
$$


::: pf-proof

One has
$$
SO
=
\begin{pmatrix}
0&0\\
5c&5d
\end{pmatrix}.
$$
Equating this with $A$ gives the two relations.

:::

:::

::: {.pf-step #s1-10}

Orthogonality then gives exactly two possible first rows:
$$
(a,b)
=
\left(\frac35,\frac45\right)
$$
or
$$
(a,b)
=
\left(-\frac35,-\frac45\right).
$$


::: pf-proof

The second row
$$
\left(\frac45,-\frac35\right)
$$
already has norm $1$. The first row of an orthogonal $2\times2$ matrix must be
a unit vector perpendicular to it. The two such vectors are its two unit
perpendiculars, namely the displayed pair.

:::

:::

::: {.pf-step #s1-11}

Thus two polar factorizations in part (b) are
$$
\boxed{
A
=
\begin{pmatrix}
0&0\\
0&5
\end{pmatrix}
\begin{pmatrix}
3/5&4/5\\
4/5&-3/5
\end{pmatrix}
}
$$
and
$$
\boxed{
A
=
\begin{pmatrix}
0&0\\
0&5
\end{pmatrix}
\begin{pmatrix}
-3/5&-4/5\\
4/5&-3/5
\end{pmatrix}.
}
$$


::: pf-proof

Each second factor is orthogonal by step [](#s1-10){.pf-ref}, and step [](#s1-9){.pf-ref} ensures that
multiplication by $S$ gives the required matrix $A$.

:::

:::

::: {.pf-step #s1-12}

The polar decomposition $A=SO$ with $S$ positive semidefinite is unique
in part (a) and not unique in part (b).


::: pf-proof

In part (a), $A$ is invertible, so $S=(AA^T)^{1/2}$ is positive definite and
invertible. Hence
$$
O=S^{-1}A
$$
is forced, proving uniqueness.

In part (b), $S$ is singular. Step [](#s1-11){.pf-ref} exhibits two distinct orthogonal
extensions with the same product $SO=A$, so the orthogonal factor is not
unique.

:::

:::

::: pf-qed

Steps [](#s1-6){.pf-ref} and [](#s1-11){.pf-ref} give the two decompositions, and step [](#s1-12){.pf-ref} determines
their uniqueness behavior.

:::

:::

:::
