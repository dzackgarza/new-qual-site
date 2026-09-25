---
schema: qual/card@1
id: P-BKF84-8
kind: problem
title: Eigenvalues and eigenspaces of a rank-one outer-product matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the deterministic MinerU Flash extraction of the Berkeley Fall 1984 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the outer-product description $M=vv^T$ and the resulting orthogonal eigenspace decomposition.
---

::: {.problem}
Let $a,b,c,d\in\mathbb R$, not all zero.
Find the eigenvalues of
\[
\begin{pmatrix}
a^2&ab&ac&ad\\
ab&b^2&bc&bd\\
ac&bc&c^2&cd\\
ad&bd&cd&d^2
\end{pmatrix}
\]
and describe the eigenspace decomposition of $\mathbb R^4$.
:::

::: {.solution}
Let
$$
v
\coloneqq
\begin{pmatrix}
a\\
b\\
c\\
d
\end{pmatrix}
\neq0.
$$
Then the given matrix is
$$
M=vv^T.
$$

<1>1. The vector $v$ is an eigenvector of $M$ with eigenvalue
$$
\lambda
=
\norm v^2
=
a^2+b^2+c^2+d^2.
$$

::: {.proof}
Directly,
$$
Mv
=
vv^Tv
=
(v^Tv)v
=
\norm v^2v.
$$
Since $v\neq0$, one has $\lambda>0$.
:::

<1>2. Every vector in
$$
v^\perp
=
\{x\in\RR^4:v^Tx=0\}
$$
is an eigenvector with eigenvalue $0$.

::: {.proof}
If $x\in v^\perp$, then
$$
Mx
=
vv^Tx
=
v\cdot0
=
0.
$$
Thus
$$
v^\perp\subseteq E_0(M).
$$
:::

<1>3. In fact,
$$
E_0(M)=v^\perp,
\qquad
E_\lambda(M)=\RR v.
$$

::: {.proof}
If $Mx=0$, then
$$
v(v^Tx)=0.
$$
Since $v\neq0$, this forces $v^Tx=0$, so
$x\in v^\perp$. Hence $E_0(M)=v^\perp$.

Now suppose $Mx=\lambda x$, where
$\lambda=\norm v^2>0$. Since
$$
Mx=v(v^Tx)\in\RR v,
$$
one has
$$
x=\lambda^{-1}Mx\in\RR v.
$$
Together with step <1>1, this gives $E_\lambda(M)=\RR v$.
:::

<1>4. The complete eigenspace decomposition is
$$
\boxed{
\RR^4
=
\RR v\oplus v^\perp
},
$$
with eigenvalue
$$
\boxed{a^2+b^2+c^2+d^2}
$$
on the one-dimensional summand $\RR v$ and eigenvalue
$$
\boxed{0}
$$
on the three-dimensional summand $v^\perp$.

::: {.proof}
Since $v\neq0$, orthogonal decomposition in Euclidean space gives
$$
\RR^4=\RR v\oplus v^\perp.
$$
Steps <1>1--<1>3 identify the eigenvalue on each summand. In particular,
these are all eigenvalues.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives both the eigenvalues and the requested eigenspace
decomposition.
:::
:::
