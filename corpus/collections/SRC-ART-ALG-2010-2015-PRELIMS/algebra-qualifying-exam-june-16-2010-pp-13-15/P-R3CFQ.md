---
schema: qual/card@1
id: P-R3CFQ
kind: problem
title: Rational canonical form of a $3\times 3$ matrix over $\mathbb{Q}$, and a non-similar
  matrix with the same characteristic polynomial
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared all nine matrix entries and both requests with June 2010 Rings and Modules 4 on PDF page 14."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the cyclic basis and its determinant, AP=PC by exact matrix arithmetic, the characteristic and minimal polynomial, and the rank obstruction to similarity of the second matrix."
---

::: {.problem}
Let $A$ be the following matrix (over $\mathbb{Q}$) $$\begin{pmatrix} -2 & 1 & 1 \\ -4 & 3 & 1 \\ -6 & 6 & -1 \end{pmatrix}.$$ Find the rational canonical form for $A$.
Give a $3 \times 3$ matrix $B$ which has the same characteristic polynomial as $A$, but which is not similar to $A$.
:::

::: {.solution}
The rational canonical form and a suitable second matrix are
$$
C=\begin{pmatrix}0&0&2\\1&0&3\\0&1&0\end{pmatrix},
\qquad
B=\begin{pmatrix}2&0&0\\0&-1&0\\0&0&-1\end{pmatrix}.
$$

<1>1. The vector $v=(1,0,0)^{\mathsf T}$ is cyclic for $A$,
and $P^{-1}AP=C$ for the matrix $P$ below.

::: {.proof}
Direct multiplication gives
$$
Av=\begin{pmatrix}-2\\-4\\-6\end{pmatrix},\quad
A^2v=\begin{pmatrix}-6\\-10\\-6\end{pmatrix},\quad
A^3v=\begin{pmatrix}-4\\-12\\-18\end{pmatrix}=2v+3Av.
$$
Thus
$$
P=(v\ Av\ A^2v)
=\begin{pmatrix}1&-2&-6\\0&-4&-10\\0&-6&-6\end{pmatrix},
\qquad \det P=24-60=-36\ne0.
$$
Its columns form a basis. In this basis, $A$ sends the
first vector to the second, the second to the third,
and the third to twice the first plus three times the
second. These three identities say exactly that $AP=PC$,
so $P^{-1}AP=C$.
:::

<1>2. The matrix $C$ is the rational canonical form, with
single invariant factor
$f(t)=t^3-3t-2=(t-2)(t+1)^2$.

::: {.proof}
The companion matrix of a monic polynomial
$t^3+c_2t^2+c_1t+c_0$ has subdiagonal entries one and
last column $(-c_0,-c_1,-c_2)^{\mathsf T}$ [@DF04].
Hence $C$ is the companion matrix of $f$.
The cyclic basis in step <1>1 identifies the
$\mathbb Q[t]$-module with $\mathbb Q[t]/(f)$: the map
$g\mapsto g(A)v$ is onto; division by $f$ reduces any
element in its kernel to a polynomial of degree at most
two, whose coefficients must vanish by independence of
$v,Av,A^2v$. Here $f(A)v=0$ is the displayed identity
for $A^3v$. Thus the kernel is exactly $(f)$, establishing
the single invariant factor and the asserted rational form.

For completeness, expanding the determinant of $tI-C$
gives $t(t^2-3)-2=t^3-3t-2$. Similarity therefore gives
$\chi_A=f$. The cyclic-basis argument also proves that
the minimal polynomial has degree three and equals $f$.
:::

<1>3. The matrix $B$ has the same characteristic polynomial
as $A$ but is not similar to $A$.

::: {.proof}
Its diagonal entries give
$\chi_B(t)=(t-2)(t+1)^2=\chi_A(t)$.
On the other hand,
$$
A+I=\begin{pmatrix}-1&1&1\\-4&4&1\\-6&6&0\end{pmatrix}
$$
has rank two. Its second column is the negative of the
first, so its rank is at most two, while the minor in
rows one and two and columns one and three is
$(-1)(1)-(1)(-4)=3\ne0$.
But $B+I=\operatorname{diag}(3,0,0)$ has rank one.
If $A$ and $B$ were similar, adding the identity would
preserve that similarity and hence their ranks, a contradiction.
This proves the required failure of similarity.
:::
:::
