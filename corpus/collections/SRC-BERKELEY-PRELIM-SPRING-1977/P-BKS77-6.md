---
schema: qual/card@1
id: P-BKS77-6
kind: problem
title: Structure questions for $GL_2(\mathbb R)$ and its orthogonal subgroup
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $G$ be the set of real $2\times2$ matrices of nonzero determinant, with ordinary matrix multiplication.

1. Show that $G$ is a group.
2. Find its center.
3. Show that the real orthogonal matrices form a subgroup $O\le G$, and give an example showing that $O$ is not normal in $G$.
4. Find a nontrivial homomorphism from $G$ onto an abelian group.
:::

::: {.solution}
<1>1. The set
$$
G=GL_2(\mathbb R)
$$
is a group under matrix multiplication.

::: {.proof}
Matrix multiplication is associative. The identity matrix $I$ has determinant $1$, so $I\in G$. If $A,B\in G$, then
$$
\det(AB)=\det(A)\det(B)\neq0,
$$
so $AB\in G$. Finally, if $A\in G$, then $A$ is invertible and
$$
\det(A^{-1})=\det(A)^{-1}\neq0,
$$
so $A^{-1}\in G$.
:::

<1>2. The center of $G$ is
$$
\boxed{
Z(G)=\{\lambda I:\lambda\in\mathbb R^\times\}
}.
$$

::: {.proof}
Every nonzero scalar matrix commutes with every matrix, so the displayed set is contained in $Z(G)$.

Conversely, let
$$
A=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}
\in Z(G).
$$
Since $A$ commutes with
$$
D=
\begin{pmatrix}
1&0\\
0&2
\end{pmatrix},
$$
the equality $AD=DA$ gives
$$
b=0,
\qquad
c=0.
$$
Thus $A=\operatorname{diag}(a,d)$. Since $A$ also commutes with
$$
S=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
$$
the equality $AS=SA$ gives $a=d$. Hence $A=aI$, and because $A\in G$, one has $a\neq0$.
:::

<1>3. The set
$$
O\coloneqq
\{Q\in G:QQ^T=I\}
$$
is a subgroup of $G$.

::: {.proof}
The identity belongs to $O$. If $Q,R\in O$, then
$$
(QR)(QR)^T
=
QRR^TQ^T
=
QQ^T
=I,
$$
so $QR\in O$. If $Q\in O$, then $Q^{-1}=Q^T$, and therefore
$$
Q^{-1}(Q^{-1})^T
=
Q^TQ
=I,
$$
so $Q^{-1}\in O$. Thus $O\leq G$.
:::

<1>4. The subgroup $O$ is not normal in $G$.

::: {.proof}
Take
$$
A=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix}
\in G,
\qquad
Q=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\in O.
$$
Then
$$
AQA^{-1}
=
\begin{pmatrix}
0&-2\\
\frac12&0
\end{pmatrix}.
$$
Its first column has Euclidean norm $1/2$, so the matrix is not orthogonal. Thus
$$
AQA^{-1}\notin O,
$$
and therefore $O$ is not normal in $G$.
:::

<1>5. The determinant gives a nontrivial surjective homomorphism
$$
\boxed{
\det:G\longrightarrow\mathbb R^\times
}.
$$

::: {.proof}
The group $\mathbb R^\times$ is abelian under multiplication, and
$$
\det(AB)=\det(A)\det(B),
$$
so determinant is a group homomorphism. It is surjective because for every $r\in\mathbb R^\times$,
$$
\det
\begin{pmatrix}
r&0\\
0&1
\end{pmatrix}
=r.
$$
It is nontrivial, for example because $\det(\operatorname{diag}(2,1))=2\neq1$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 answer the four parts.
:::
:::
