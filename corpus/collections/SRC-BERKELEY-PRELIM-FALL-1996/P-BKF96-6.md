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

::: pf

::: {.pf-step #s1}

The matrix $A$ is diagonalizable over $\RR$, with eigenvalues among
$\{1,-1\}$.

::: pf-proof

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

:::

::: pf-step

Both $1$ and $-1$ occur as eigenvalues of $A$.

::: pf-proof

If $A=I$, then
$$
AB+BA=2B=0,
$$
so $B=0$, contradicting $B^2=I$. The same contradiction follows if
$A=-I$. Since step [](#s1){.pf-ref} makes $A$ diagonalizable with eigenvalues only
$\pm1$, it follows that both eigenvalues occur.

:::

:::

::: {.pf-step #s3}

Choose a nonzero vector $v$ with
$$
Av=v.
$$
Then $Bv$ is a nonzero eigenvector of $A$ with eigenvalue $-1$.

::: pf-proof

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

:::

::: {.pf-step #s4}

The vectors
$$
v,\ Bv
$$
form a basis of $\RR^2$.

::: pf-proof

By step [](#s3){.pf-ref}, they are nonzero eigenvectors of $A$ for the distinct
eigenvalues $1$ and $-1$. Hence they are linearly independent. Since the
space has dimension $2$, they form a basis.

:::

:::

::: {.pf-step #s5}

In the ordered basis $(v,Bv)$, the matrices of $A$ and $B$ are
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

::: pf-proof

For $A$, step [](#s3){.pf-ref} gives
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

:::

::: {.pf-step #s6}

There is an invertible real matrix $T$ satisfying the two required
conjugation identities.

::: pf-proof

Let
$$
P=
\begin{pmatrix}
\vert&\vert\\
v&Bv\\
\vert&\vert
\end{pmatrix}.
$$
Step [](#s4){.pf-ref} makes $P$ invertible. Step [](#s5){.pf-ref} says
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

:::

::: pf-qed

Step [](#s6){.pf-ref} constructs the required real invertible matrix $T$.

:::

:::

:::
