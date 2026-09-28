---
schema: qual/card@1
id: P-BERK98S-05
kind: problem
title: Two-sided ideals of the upper-triangular two-by-two real matrix ring
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A$ be the ring of real $2\times2$ matrices of the form
\[
\begin{pmatrix}a&b\\0&c\end{pmatrix}.
\]
Determine all two-sided ideals of $A$.
:::

::: {.solution}
Let
$$
e_{11}=
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
e_{12}=
\begin{pmatrix}0&1\\0&0\end{pmatrix},
\qquad
e_{22}=
\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$
Then
$$
A=\RR e_{11}\oplus\RR e_{12}\oplus\RR e_{22}.
$$

<1>1. Every two-sided ideal $I\subseteq A$ is an $\RR$-vector subspace.

::: {.proof}
For every $\lambda\in\RR$, the scalar matrix $\lambda I_2$ belongs to
$A$. If $x\in I$, then
$$
\lambda x=(\lambda I_2)x\in I
$$
because $I$ is a left ideal. Together with closure under addition, this
shows that $I$ is an $\RR$-vector subspace.
:::

<1>2. If
$$
x=ae_{11}+be_{12}+ce_{22}\in I,
$$
then each nonzero coordinate component of $x$ belongs to $I$:
$$
ae_{11},\qquad be_{12},\qquad ce_{22}\in I.
$$

::: {.proof}
Since $I$ is a two-sided ideal,
$$
e_{11}xe_{11}=ae_{11}\in I,
\qquad
e_{11}xe_{22}=be_{12}\in I,
\qquad
e_{22}xe_{22}=ce_{22}\in I.
$$
:::

<1>3. If $e_{11}\in I$ or $e_{22}\in I$, then $e_{12}\in I$.

::: {.proof}
The matrix-unit products satisfy
$$
e_{11}e_{12}=e_{12},
\qquad
e_{12}e_{22}=e_{12}.
$$
Thus $e_{11}\in I$ implies $e_{12}\in I$ because $I$ is a right ideal,
and $e_{22}\in I$ implies $e_{12}\in I$ because $I$ is a left ideal.
:::

<1>4. Every two-sided ideal of $A$ is one of
$$
0,
\qquad
\RR e_{12},
\qquad
\RR e_{11}\oplus\RR e_{12},
\qquad
\RR e_{12}\oplus\RR e_{22},
\qquad
A.
$$

::: {.proof}
Let $I$ be a two-sided ideal. By step <1>2, every element of $I$ contributes
its three matrix-unit components separately to $I$. Hence step <1>1 shows
that $I$ is spanned by whichever of
$$
e_{11},\qquad e_{12},\qquad e_{22}
$$
occur in its elements.

By step <1>3, any spanning set containing $e_{11}$ or $e_{22}$ must also
contain $e_{12}$. Therefore the only possible subsets of these matrix units
that can span an ideal are
$$
\varnothing,
\quad
\{e_{12}\},
\quad
\{e_{11},e_{12}\},
\quad
\{e_{12},e_{22}\},
\quad
\{e_{11},e_{12},e_{22}\},
$$
which give exactly the five displayed subspaces.
:::

<1>5. Each of the five subspaces in step <1>4 is a two-sided ideal.

::: {.proof}
The cases $0$ and $A$ are immediate. Also,
$$
A e_{12}\subseteq\RR e_{12},
\qquad
e_{12}A\subseteq\RR e_{12},
$$
so $\RR e_{12}$ is a two-sided ideal.

The subspace $\RR e_{11}\oplus\RR e_{12}$ consists exactly of the
matrices in $A$ whose lower-right entry is zero. Direct multiplication by
an arbitrary upper-triangular matrix on either side preserves that
condition. Likewise, $\RR e_{12}\oplus\RR e_{22}$ consists exactly of
the matrices whose upper-left entry is zero, and that condition is
preserved by multiplication on either side. Thus both are two-sided ideals.
:::

<1>6. Therefore the complete list of two-sided ideals is
$$
\boxed{
0, 
\RR e_{12}, 
\RR e_{11}\oplus\RR e_{12}, 
\RR e_{12}\oplus\RR e_{22}, 
A
}.
$$

::: {.proof}
Step <1>4 proves that no other two-sided ideal exists, and step <1>5
verifies that every listed subspace is a two-sided ideal.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the required classification.
:::
:::
