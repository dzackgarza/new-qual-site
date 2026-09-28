---
schema: qual/card@1
id: P-BKF96-6
kind: problem
title: Simultaneous normal form for two anticommuting involutions on $\mathbb R^2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Chose a +1 eigenvector v of A. Anticommutation makes Bv a nonzero -1
    eigenvector, and B^2=I makes B swap the basis v,Bv.
---

::: {.problem}
Let $A,B$ be real $2\times2$ matrices satisfying
\[
A^2=B^2=I,
\qquad
AB+BA=0.
\]
Show that there exists a real invertible $2\times2$ matrix $T$ such that
\[
TAT^{-1}=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
TBT^{-1}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
:::

::: {.solution}
<1>1. The matrix $A$ is diagonalizable over $\RR$, with eigenvalues among
$\{1,-1\}$.

::: {.proof}
The relation
$$
A^2=I
$$
shows that the minimal polynomial of $A$ divides
$$
t^2-1=(t-1)(t+1).
$$
This polynomial splits over $\RR$ with distinct roots, so $A$ is
diagonalizable and its eigenvalues lie in $\{1,-1\}$.
:::

<1>2. Both $1$ and $-1$ occur as eigenvalues of $A$.

::: {.proof}
If $A=I$, then
$$
AB+BA=2B=0,
$$
so $B=0$, contradicting $B^2=I$. The same contradiction follows if
$A=-I$. Since step <1>1 makes $A$ diagonalizable with eigenvalues only
$\pm1$, it follows that both eigenvalues occur.
:::

<1>3. Choose a nonzero vector $v$ with
$$
Av=v.
$$
Then $Bv$ is a nonzero eigenvector of $A$ with eigenvalue $-1$.

::: {.proof}
The relation
$$
AB=-BA
$$
gives
$$
A(Bv)
=
-B(Av)
=
-Bv.
$$
Moreover, $Bv\neq0$ because $B^2=I$ makes $B$ invertible.
:::

<1>4. The vectors
$$
v,\ Bv
$$
form a basis of $\RR^2$.

::: {.proof}
By step <1>3, they are nonzero eigenvectors of $A$ for the distinct
eigenvalues $1$ and $-1$. Hence they are linearly independent. Since the
space has dimension $2$, they form a basis.
:::

<1>5. In the ordered basis $(v,Bv)$, the matrices of $A$ and $B$ are
$$
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
\qquad\text{and}\qquad
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
$$
respectively.

::: {.proof}
For $A$, step <1>3 gives
$$
Av=v,
\qquad
A(Bv)=-Bv.
$$
For $B$,
$$
Bv=Bv
$$
is the second basis vector, while
$$
B(Bv)
=
B^2v
=
v
$$
is the first basis vector. These coordinate actions give the two displayed
matrices.
:::

<1>6. There is an invertible real matrix $T$ satisfying the two required
conjugation identities.

::: {.proof}
Let
$$
P=
\begin{pmatrix}
\vert&\vert\\
v&Bv\\
\vert&\vert
\end{pmatrix}.
$$
Step <1>4 makes $P$ invertible. Step <1>5 says
$$
P^{-1}AP
=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
$$
and
$$
P^{-1}BP
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$
Taking
$$
T=P^{-1}
$$
gives exactly the required formulas.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 constructs the required real invertible matrix $T$.
:::
:::
