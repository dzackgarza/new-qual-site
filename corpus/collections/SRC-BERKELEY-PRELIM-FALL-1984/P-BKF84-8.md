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

::: pf

::: {.pf-step #s1}

The vector $v$ is an eigenvector of $M$ with eigenvalue
$$
\lambda
=
\norm v^2
=
a^2+b^2+c^2+d^2.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

Every vector in
$$
v^\perp
=
\{x\in\RR^4:v^Tx=0\}
$$
is an eigenvector with eigenvalue $0$.

::: pf-proof

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

:::

::: {.pf-step #s3}

In fact,
$$
E_0(M)=v^\perp,
\qquad
E_\lambda(M)=\RR v.
$$

::: pf-proof

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
Together with step [](#s1){.pf-ref}, this gives $E_\lambda(M)=\RR v$.

:::

:::

::: {.pf-step #s4}

The complete eigenspace decomposition is
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

::: pf-proof

Since $v\neq0$, orthogonal decomposition in Euclidean space gives
$$
\RR^4=\RR v\oplus v^\perp.
$$
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} identify the eigenvalue on each summand. In particular,
these are all eigenvalues.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} gives both the eigenvalues and the requested eigenspace
decomposition.

:::

:::

:::
