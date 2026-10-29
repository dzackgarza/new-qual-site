---
schema: qual/card@1
id: P-UGAP13F-02
kind: problem
title: Determine which matrix data are preserved by similarity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Suppose $A,B,C$ are $n\times n$ matrices, $A$ is invertible, and
$$
ABA^{-1}=C.
$$
Give quick proofs, citing relevant facts about trace, determinant, and eigenvalues, of whichever statements are true:

(a) $\det B=\det C$.

(b) $\operatorname{tr}B=\operatorname{tr}C$.

(c) $B$ and $C$ have the same eigenvectors.

(d) $B$ and $C$ have the same eigenvalues.
:::

::: {.solution}

Since
$$
C=ABA^{-1},
$$
the matrices $B$ and $C$ are similar.

::: pf

::: {.pf-step #s1-1}

Statement (a) is true:
$$
\boxed{
\det B=\det C.
}
$$


::: pf-proof

Using multiplicativity of the determinant,
$$
\begin{aligned}
\det C
&=
\det(ABA^{-1})\\
&=
(\det A)(\det B)(\det A^{-1})\\
&=
(\det A)(\det B)\frac1{\det A}\\
&=
\det B.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-2}

Statement (b) is true:
$$
\boxed{
\operatorname{tr}B
=
\operatorname{tr}C.
}
$$


::: pf-proof

Use the cyclic property of trace:
$$
\operatorname{tr}(XY)
=
\operatorname{tr}(YX).
$$
Then
$$
\begin{aligned}
\operatorname{tr}C
&=
\operatorname{tr}(ABA^{-1})\\
&=
\operatorname{tr}(BA^{-1}A)\\
&=
\operatorname{tr}B.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

Statement (c) is false in general.


::: pf-proof

Take
$$
B
=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
\qquad
A
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
$$
Then
$$
A^{-1}
=
\begin{pmatrix}
1&-1\\
0&1
\end{pmatrix},
$$
and
$$
C
=
ABA^{-1}
=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix}.
$$

The vector
$$
e_2
=
\begin{pmatrix}
0\\
1
\end{pmatrix}
$$
is an eigenvector of $B$ with eigenvalue $2$.
But
$$
Ce_2
=
\begin{pmatrix}
1\\
2
\end{pmatrix},
$$
which is not a scalar multiple of $e_2$.
Thus $B$ and $C$ need not have the same eigenvectors.

:::

:::

::: {.pf-step #s1-4}

What similarity preserves is the eigenspace structure up to $A$:
if
$$
Bv=\lambda v,
$$
then
$$
C(Av)=\lambda(Av).
$$


::: pf-proof

Starting from
$$
Bv=\lambda v,
$$
compute
$$
\begin{aligned}
C(Av)
&=
ABA^{-1}Av\\
&=
ABv\\
&=
A(\lambda v)\\
&=
\lambda(Av).
\end{aligned}
$$
Because $A$ is invertible,
$$
v\ne0
\Longrightarrow
Av\ne0.
$$
Thus $A$ carries each eigenspace of $B$ isomorphically onto the
corresponding eigenspace of $C$.

:::

:::

::: {.pf-step #s1-5}

Statement (d) is true:
$$
\boxed{
B
\text{ and }
C
\text{ have the same eigenvalues}.
}
$$


::: pf-proof

Their characteristic polynomials agree:
$$
\begin{aligned}
\det(\lambda I-C)
&=
\det\bigl(
\lambda I-ABA^{-1}
\bigr)\\
&=
\det\bigl(
A(\lambda I-B)A^{-1}
\bigr)\\
&=
\det(\lambda I-B)
\end{aligned}
$$
by step [](#s1-1){.pf-ref} applied to
$$
\lambda I-B.
$$
Therefore the roots of the two characteristic polynomials, with algebraic
multiplicity, are identical.

:::

:::

::: {.pf-step #s1-6}

The complete classification is
$$
\boxed{
\begin{array}{c|cccc}
\text{statement}&(a)&(b)&(c)&(d)\\
\hline
\text{true?}
&\mathrm{yes}
&\mathrm{yes}
&\mathrm{no}
&\mathrm{yes}
\end{array}
}
$$


::: pf-proof

Collect steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the requested answer.

:::

:::

:::
