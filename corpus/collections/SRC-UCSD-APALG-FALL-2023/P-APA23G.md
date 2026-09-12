---
schema: qual/card@1
id: P-APA23G
kind: problem
title: Indecomposable modules for $C_4 \times C_3 \times C_2$ over $\mathbb{F}_3$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $G$ be the product group $G = C_4 \times C_3 \times C_2$, where $C_n$ denotes the cyclic group of order $n$, and let $\mathbb{F}_3$ be the field with $3$ elements.
Let $V$ be an indecomposable $G$-module over $\mathbb{F}_3$.
Is $V$ necessarily irreducible?
Justify your answer.
:::

::: {.solution}
No. There are indecomposable $G$-modules over $\mathbb F_3$ that are reducible.

<1>1. Let $V=\mathbb F_3^2$ with basis $e_1,e_2$. Let the $C_4$ and $C_2$ factors act trivially, and let a generator $g$ of the $C_3$ factor act by
\[
J=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]
This defines a $G$-module.
::: {.proof}
Write $J=I+N$ with
\[
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix},
\qquad N^2=0.
\]
In characteristic $3$,
\[
J^3=(I+N)^3=I+3N+3N^2+N^3=I.
\]
Hence the assignment of the generator of $C_3$ to $J$ respects the relation $g^3=1$. The other two factors act trivially, so the three factor actions commute and define a representation of
\[
C_4\times C_3\times C_2.
\]
:::

<1>2. The module $V$ is reducible.
::: {.proof}
The line
\[
L=\mathbb F_3 e_1
\]
is fixed by $J$, since $Je_1=e_1$. The other two group factors act trivially, so $L$ is a nonzero proper $G$-submodule of $V$.
:::

<1>3. The only one-dimensional $J$-invariant subspace of $V$ is $L=\mathbb F_3e_1$.
::: {.proof}
If a one-dimensional subspace $M=\mathbb F_3v$ is $J$-invariant, then $v$ is an eigenvector of $J$. Since
\[
J-I=N
\]
has kernel exactly $\mathbb F_3e_1$, the eigenspace for the only eigenvalue $1$ is precisely $L$. Thus $M=L$.
:::

<1>4. The module $V$ is indecomposable.
::: {.proof}
If $V$ decomposed as a direct sum of two nonzero $G$-submodules, then, because $\dim V=2$, both summands would be one-dimensional. Each would therefore be a one-dimensional $J$-invariant subspace. By <1>3 both would have to equal $L$, which cannot give a direct-sum decomposition of $V$.
Thus $V$ is indecomposable.
:::

<1>5. Hence an indecomposable $G$-module over $\mathbb F_3$ need not be irreducible.
::: {.proof}
The module constructed in <1>1 is reducible by <1>2 and indecomposable by <1>4, providing the required counterexample.
:::
:::
