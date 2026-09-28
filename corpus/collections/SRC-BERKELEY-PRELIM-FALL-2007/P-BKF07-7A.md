---
schema: qual/card@1
id: P-BKF07-7A
kind: problem
title: Factor a matrix satisfying P cubed equals P
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
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained diagonalization and block extraction,
    including the identities V^T U=I_r and P=USV^T.
---

::: {.problem}
Let \(P\in\mathbb R^{n\times n}\) satisfy \(P^3=P\). Let \(r=\operatorname{rank}P>0\). Show that there exist \(U,V\in\mathbb R^{n\times r}\) with
\[
V^TU=I_r
\]
such that
\[
P=USV^T,
\]
where \(S\) is an \(r\times r\) diagonal matrix whose diagonal entries are all \(\pm1\).
:::

::: {.solution}
<1>1. The matrix $P$ is diagonalizable over $\RR$, and every
eigenvalue of $P$ belongs to
$$
\{0,1,-1\}.
$$

::: {.proof}
The relation $P^3=P$ says that $P$ is annihilated by
$$
q(t)=t^3-t=t(t-1)(t+1).
$$
This polynomial splits over $\RR$ into distinct linear factors.
Hence the minimal polynomial of $P$ also has no repeated root, so
$P$ is diagonalizable over $\RR$. Every eigenvalue is a root of
$q$, giving the displayed set.
:::

<1>2. There is an invertible matrix $T\in\RR^{n\times n}$ such that
$$
P=TJT^{-1},
\qquad
J=
\begin{pmatrix}
S&0\\
0&0
\end{pmatrix},
$$
where $S$ is an $r\times r$ diagonal matrix with diagonal entries
all equal to $\pm1$.

::: {.proof}
By step <1>1, choose an eigenbasis for $P$. Since
$r=\operatorname{rank}P$, exactly $r$ diagonal entries in a diagonal
form of $P$ are nonzero. Reorder the eigenbasis so those entries come
first. They are all $\pm1$, giving the displayed block form.
:::

<1>3. Write
$$
T=
\begin{pmatrix}
U&W
\end{pmatrix}
$$
with $U\in\RR^{n\times r}$ the first $r$ columns of $T$, and write
$$
T^{-1}
=
\begin{pmatrix}
V^T\\
Z^T
\end{pmatrix}
$$
with $V^T$ the first $r$ rows of $T^{-1}$.

::: {.proof}
This is simply the block decomposition of $T$ and $T^{-1}$ conforming
to the block sizes $r$ and $n-r$ in step <1>2. In particular
$V\in\RR^{n\times r}$.
:::

<1>4. The matrices $U$ and $V$ satisfy
$$
\boxed{V^TU=I_r}.
$$

::: {.proof}
Since $T^{-1}T=I_n$, the upper-left $r\times r$ block of the product
is
$$
V^TU.
$$
The corresponding block of $I_n$ is $I_r$, proving the claim.
:::

<1>5. The same matrices satisfy
$$
\boxed{P=USV^T}.
$$

::: {.proof}
Using the block forms from steps <1>2--<1>3,
$$
\begin{aligned}
P
&=
\begin{pmatrix}U&W\end{pmatrix}
\begin{pmatrix}
S&0\\
0&0
\end{pmatrix}
\begin{pmatrix}
V^T\\
Z^T
\end{pmatrix}
\\
&=
USV^T.
\end{aligned}
$$
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2, <1>4, and <1>5 give the required matrices and diagonal
matrix $S$.
:::
:::
