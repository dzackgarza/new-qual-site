---
schema: qual/card@1
id: P-UCLAB15F-07
kind: problem
title: Possible ranks of a product of two rank-three rectangular matrices
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
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $A,B$ be two $4\times5$ matrices of rank $3$, and let
$$
C=A^TB,
$$
a $5\times5$ matrix.
Find all possible values of $\operatorname{rank}C$.
For each possible rank, give explicit matrices realizing it, and prove that all other values are impossible.
:::

::: {.solution}

Regard
$$
B:\RR^5\to\RR^4
$$
and
$$
A^T:\RR^4\to\RR^5.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\dim\ker(A^T)=1.
$$


::: pf-proof

Since
$$
\operatorname{rank}A=3,
$$
one has
$$
\operatorname{rank}A^T=3.
$$
The domain of $A^T$ has dimension $4$, so rank-nullity gives
$$
\dim\ker(A^T)
=
4-3
=1.
$$

:::

:::

::: {.pf-step #s1-2}

The rank of $C=A^TB$ is
$$
\operatorname{rank}C
=
\operatorname{rank}B
-
\dim\bigl(\operatorname{im}B\cap\ker A^T\bigr).
$$


::: pf-proof

Restrict $A^T$ to the three-dimensional subspace
$$
\operatorname{im}B\subseteq\RR^4.
$$
Then
$$
\operatorname{im}(A^TB)
=
A^T(\operatorname{im}B).
$$
The kernel of the restricted map
$$
A^T\restrict_{\operatorname{im}B}
$$
is exactly
$$
\operatorname{im}B\cap\ker A^T.
$$
Rank-nullity on $\operatorname{im}B$ gives
$$
\dim A^T(\operatorname{im}B)
=
\dim\operatorname{im}B
-
\dim(\operatorname{im}B\cap\ker A^T).
$$
Since
$$
\dim\operatorname{im}B=\operatorname{rank}B=3,
$$
this is the displayed formula.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\operatorname{rank}C\in\{2,3\}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
\ker A^T
$$
is one-dimensional.
Hence
$$
\dim(\operatorname{im}B\cap\ker A^T)
$$
is either $0$ or $1$.
Step [](#s1-2){.pf-ref} then gives
$$
\operatorname{rank}C
=
3
\quad\text{or}\quad
2.
$$
Thus no other rank is possible.

:::

:::

::: {.pf-step #s1-4}

Rank $3$ occurs.


::: pf-proof

Take
$$
A=B=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&0&0
\end{pmatrix}.
$$
Both matrices have rank $3$.
Then
$$
A^TB
=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&0&0\\
0&0&0&0&0
\end{pmatrix},
$$
which has rank $3$.

:::

:::

::: {.pf-step #s1-5}

Rank $2$ occurs.


::: pf-proof

Take
$$
A=
\begin{pmatrix}
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0\\
0&0&0&0&0
\end{pmatrix}
$$
and
$$
B=
\begin{pmatrix}
0&0&0&0&0\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&1&0&0
\end{pmatrix}.
$$
Again both have rank $3$.
Now
$$
A^TB
=
\begin{pmatrix}
0&0&0&0&0\\
1&0&0&0&0\\
0&1&0&0&0\\
0&0&0&0&0\\
0&0&0&0&0
\end{pmatrix},
$$
which has rank $2$.

:::

:::

::: {.pf-step #s1-6}

Hence the complete list of possible values is
$$
\boxed{\operatorname{rank}(A^TB)\in\{2,3\}}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} rules out every other value, while steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} realize both listed values.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required classification.

:::

:::

:::
