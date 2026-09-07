---
schema: qual/card@1
id: P-ALGF10I
kind: problem
title: "Examples of right noetherian not left noetherian, and DCC without ACC"
classification:
  areas:
  - algebra
  topics:
  - Ring Theory
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 9 of the official UCSD Algebra Qualifying Examination, Fall 2010; both requested examples agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the triangular-ring example is right Noetherian by finite right composition length and not left Noetherian via an infinite chain of left ideals; verified the Prüfer p-group satisfies DCC but not ACC.
---

::: {.problem}
(a) Give an example of a right Noetherian ring that is not left Noetherian.

(b) Give an example of a module that satisfies the descending chain condition on submodules, but not the ascending chain condition on submodules.
:::


::: {.solution}
<1>1. A right Noetherian ring which is not left Noetherian is
\[
R=
\left\{
\begin{pmatrix}
a&m\\
0&b
\end{pmatrix}
:a\in k,\ m,b\in K
\right\},
\qquad
K:=k(t),
\]
where \(k\) is any field and \(k\subset K\) is the natural inclusion.
::: {.proof}
Let
\[
e_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
e_2=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
As a right \(R\)-module,
\[
R_R=e_1R\oplus e_2R.
\]
The module \(e_2R\) consists of matrices
\[
\begin{pmatrix}0&0\\0&b\end{pmatrix}
\qquad(b\in K)
\]
and is simple: its right action factors through the lower-right copy of the field \(K\), and it is one-dimensional over \(K\).

Inside \(e_1R\), let
\[
M:=
\left\{
\begin{pmatrix}0&m\\0&0\end{pmatrix}:m\in K
\right\}.
\]
This is a simple right \(R\)-module for the same reason: right multiplication acts on \(m\) through the lower-right entry in \(K\).
The quotient \(e_1R/M\) is one-dimensional over the upper-left field \(k\), hence simple.
Therefore \(e_1R\) has composition length \(2\), while \(e_2R\) has composition length \(1\).
Thus \(R_R\) has finite length, so it is a Noetherian right module over itself.
Hence \(R\) is right Noetherian.

For the left side, observe that left multiplication on \(M\) is given by
\[
\begin{pmatrix}a&x\\0&b\end{pmatrix}
\begin{pmatrix}0&m\\0&0\end{pmatrix}
=
\begin{pmatrix}0&am\\0&0\end{pmatrix}.
\]
Thus every \(k\)-linear subspace \(W\subseteq K\) determines a left ideal
\[
L_W:=
\left\{
\begin{pmatrix}0&w\\0&0\end{pmatrix}:w\in W
\right\}.
\]
Since \(1,t,t^2,\ldots\) are linearly independent over \(k\), the subspaces
\[
W_n:=\operatorname{span}_k\{1,t,\ldots,t^n\}
\]
form a strictly increasing chain.
Consequently
\[
L_{W_0}\subsetneq L_{W_1}\subsetneq L_{W_2}\subsetneq\cdots
\]
is a strictly increasing chain of left ideals of \(R\).
Hence \(R\) is not left Noetherian.
:::

<1>2. A module satisfying DCC but not ACC is the Prüfer \(p\)-group
\[
C_{p^\infty}:=\bigcup_{n\ge1}\mu_{p^n}\subset\mathbb C^\times,
\]
viewed as a \(\mathbb Z\)-module, where
\[
\mu_{p^n}:=\{z\in\mathbb C^\times:z^{p^n}=1\}.
\]
::: {.proof}
Each \(\mu_{p^n}\) is cyclic of order \(p^n\), and
\[
\mu_p\subsetneq\mu_{p^2}\subsetneq\mu_{p^3}\subsetneq\cdots.
\]
Thus \(C_{p^\infty}\) does not satisfy the ascending chain condition.

We show it satisfies the descending chain condition.
For each \(n\), \(\mu_{p^n}\) is the unique subgroup of \(C_{p^\infty}\) of order \(p^n\).
Let \(H\le C_{p^\infty}\).
If \(H\) contains elements of arbitrarily large order, then for every \(n\) it contains an element of order at least \(p^n\); a suitable power of that element generates \(\mu_{p^n}\).
Hence
\[
\mu_{p^n}\subseteq H
\]
for every \(n\), so
\[
H=C_{p^\infty}.
\]
Therefore every proper subgroup \(H\) has bounded element orders and is contained in some finite cyclic subgroup \(\mu_{p^N}\).
In particular every proper subgroup is finite.

Now consider any descending chain of subgroups of \(C_{p^\infty}\).
If every term is the whole group, the chain is constant.
Otherwise, after the first proper term, every subsequent term lies inside a finite group \(\mu_{p^N}\), so the descending chain must stabilize.
Thus \(C_{p^\infty}\) satisfies DCC but not ACC.
:::
:::
