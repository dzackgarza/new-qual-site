---
schema: qual/card@1
id: P-BKF07-7A
kind: problem
title: Factorization $P=USV^T$ of a real matrix with $P^3=P$
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

::: pf

::: {.pf-step #P-diagonalizable-eigenvalues}
The matrix $P$ is diagonalizable over $\RR$, and every
eigenvalue of $P$ belongs to
$$
\{0,1,-1\}.
$$

::: pf-proof
The relation $P^3=P$ says that $P$ is annihilated by
$$
q(t)=t^3-t=t(t-1)(t+1).
$$
This polynomial splits over $\RR$ into distinct linear factors.
Hence the minimal polynomial of $P$ also has no repeated root, so
$P$ is diagonalizable over $\RR$. Every eigenvalue is a root of
$q$, giving the displayed set.
:::

:::

::: {.pf-step #T-J-decomposition}
There is an invertible matrix $T\in\RR^{n\times n}$ such that
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

::: pf-proof
By step [](#P-diagonalizable-eigenvalues){.pf-ref}, choose an eigenbasis for $P$. Since
$r=\operatorname{rank}P$, exactly $r$ diagonal entries in a diagonal
form of $P$ are nonzero. Reorder the eigenbasis so those entries come
first. They are all $\pm1$, giving the displayed block form.
:::

:::

::: {.pf-step #U-V-block-decomposition}
Write
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

::: pf-proof
This is simply the block decomposition of $T$ and $T^{-1}$ conforming
to the block sizes $r$ and $n-r$ in step [](#T-J-decomposition){.pf-ref}. In particular
$V\in\RR^{n\times r}$.
:::

:::

::: {.pf-step #VtU-identity}
The matrices $U$ and $V$ satisfy
$$
\boxed{V^TU=I_r}.
$$

::: pf-proof
Since $T^{-1}T=I_n$, the upper-left $r\times r$ block of the product
is
$$
V^TU.
$$
The corresponding block of $I_n$ is $I_r$, proving the claim.
:::

:::

::: {.pf-step #P-equals-USVt}
The same matrices satisfy
$$
\boxed{P=USV^T}.
$$

::: pf-proof
Using the block forms from steps [](#T-J-decomposition){.pf-ref} and [](#U-V-block-decomposition){.pf-ref},
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

:::

::: pf-qed
Steps [](#T-J-decomposition){.pf-ref}, [](#VtU-identity){.pf-ref}, and [](#P-equals-USVt){.pf-ref} give the required matrices and diagonal
matrix $S$.
:::

:::

:::
