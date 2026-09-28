---
schema: qual/card@1
id: P-BERK83SU-11
kind: problem
title: Jordan form over $\mathbb F_3$ of the matrix with diagonal $2$ and off-diagonal $1$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Writing A=I+N with N the all-ones matrix, one has N^2=3N=0 over
    F_3 and rank N=1. Thus the only eigenvalue is 1, with eigenspace
    ker N={(x,y,z):x+y+z=0} of dimension 2. Hence the Jordan type is
    one block of size 2 and one block of size 1.
---

::: {.problem}
Over $\mathbb F_3=\mathbb Z/3\mathbb Z$, find the eigenvalues, eigenvectors, and Jordan canonical form of
\[
A=
\begin{pmatrix}
2&1&1\\
1&2&1\\
1&1&2
\end{pmatrix}.
\]
:::

::: {.solution}
Let
$$
N=A-I
=
\begin{pmatrix}
1&1&1\\
1&1&1\\
1&1&1
\end{pmatrix}.
$$

<1>1. One has
$$
N^2=0
$$
in $M_3(\FF_3)$.

::: {.proof}
Every entry of $N^2$ is
$$
1+1+1=3=0
$$
in $\FF_3$. Hence $N^2$ is the zero matrix.
:::

<1>2. The only eigenvalue of $A$ is
$$
\boxed{1}.
$$

::: {.proof}
Suppose $Av=\lambda v$ for a nonzero $v$. Since $A=I+N$,
$$
Nv=(\lambda-1)v.
$$
Applying $N$ and using step <1>1 gives
$$
0
=
N^2v
=
(\lambda-1)Nv
=
(\lambda-1)^2v.
$$
Because $v\neq0$ and $\FF_3$ is a field,
$$
(\lambda-1)^2=0,
$$
so $\lambda=1$.
:::

<1>3. The eigenspace for the eigenvalue $1$ is
$$
\boxed{
E_1
=
\left\{
\begin{pmatrix}x\\y\\z\end{pmatrix}
\in\FF_3^3:
x+y+z=0
\right\}
}.
$$

::: {.proof}
The equation $Av=v$ is equivalent to $Nv=0$. For
$$
v=
\begin{pmatrix}x\\y\\z\end{pmatrix},
$$
one has
$$
Nv
=
\begin{pmatrix}
x+y+z\\
x+y+z\\
x+y+z
\end{pmatrix}.
$$
Thus $Nv=0$ exactly when $x+y+z=0$. This is one nontrivial linear
equation in three variables, so $E_1$ has dimension $2$.
:::

<1>4. The nilpotent matrix $N=A-I$ has rank $1$.

::: {.proof}
All three rows of $N$ are equal and nonzero, so its row space is
one-dimensional.
:::

<1>5. The Jordan canonical form of $A$ consists of one block of size
$2$ and one block of size $1$, both for eigenvalue $1$.

::: {.proof}
Step <1>1 shows that every Jordan block of $A$ for eigenvalue $1$ has
size at most $2$. Step <1>4 shows that $N=A-I$ is nonzero, so $A$ is
not diagonalizable and at least one block has size $2$. Since the total
dimension is $3$, the only possibility is the partition
$$
3=2+1.
$$
:::

<1>6. A Jordan basis is given by
$$
w=
\begin{pmatrix}1\\1\\1\end{pmatrix},
\qquad
v=
\begin{pmatrix}1\\0\\0\end{pmatrix},
\qquad
u=
\begin{pmatrix}1\\2\\0\end{pmatrix}.
$$

::: {.proof}
One has
$$
Nw=0,
\qquad
Nv=w,
\qquad
Nu=0.
$$
Thus
$$
Aw=w,
\qquad
Av=v+w,
\qquad
Au=u.
$$
Moreover,
$$
\det
\begin{pmatrix}
1&1&1\\
1&0&2\\
1&0&0
\end{pmatrix}
=2\neq0
$$
in $\FF_3$, so $(w,v,u)$ is a basis.
:::

<1>7. Relative to the basis in step <1>6, the Jordan form is
$$
\boxed{
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix}
}.
$$

::: {.proof}
The coordinate identities in step <1>6 give the three columns of the
displayed matrix.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>2, <1>3, and <1>7 give respectively the eigenvalue,
eigenvectors, and Jordan canonical form requested.
:::
:::
