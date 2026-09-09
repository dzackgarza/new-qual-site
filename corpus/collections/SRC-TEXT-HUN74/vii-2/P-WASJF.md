---
schema: qual/card@1
id: P-WASJF
kind: problem
title: One-sided inverses and matrix rank
classification:
  areas:
  - algebra
  topics:
  - Rank and Nullity
  - Matrices
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hungerford VII.2.2 in an independent exercise reproduction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that an $n\times m$ matrix $A$over a division ring $D$ has an $m\times n$ left inverse $B$ (so $BA = I_m$) $\iff \mathrm{rank} A = m$.
Similarly, show $A$ has a right $m\times n$ inverse $\iff \mathrm{rank} A = n$.
:::


::: solution
Regard \(A\) as the matrix of the right-\(D\)-linear map
\[
T:D^m\longrightarrow D^n,
\qquad x\longmapsto Ax.
\]
(Equivalently, use the corresponding left-module convention consistently.)
Its rank is the dimension of its image.

<1>1. \(A\) has a left inverse if and only if \(\operatorname{rank}A=m\).
::: proof
Suppose first that \(B A=I_m\). If \(Ax=0\), then
\[
x=I_mx=BAx=0,
\]
so \(T\) is injective. Hence
\[
\operatorname{rank}A=\dim_D D^m=m.
\]

Conversely, if \(\operatorname{rank}A=m\), then \(T\) is injective. Choose a
basis \(e_1,\ldots,e_m\) of \(D^m\). Then
\(T(e_1),\ldots,T(e_m)\) is linearly independent in \(D^n\); extend it to a
basis of \(D^n\). Define \(S:D^n\to D^m\) by
\[
S(T(e_i))=e_i
\]
for \(1\le i\le m\), and send every added basis vector to \(0\). Then
\(S\circ T=\operatorname{id}_{D^m}\). If \(B\) is the matrix of \(S\), then
\(BA=I_m\).
:::

<1>2. \(A\) has a right inverse if and only if \(\operatorname{rank}A=n\).
::: proof
Suppose \(AC=I_n\) for some \(m\times n\) matrix \(C\). Then the associated
map \(T:D^m\to D^n\) is surjective, since for every \(y\in D^n\),
\[
y=I_ny=ACy=T(Cy).
\]
Thus \(\operatorname{rank}A=n\).

Conversely, if \(\operatorname{rank}A=n\), then \(T\) is surjective. Choose a
basis \(f_1,\ldots,f_n\) of \(D^n\), and choose \(v_i\in D^m\) with
\(T(v_i)=f_i\). There is a unique linear map \(U:D^n\to D^m\) satisfying
\(U(f_i)=v_i\). Then \(T\circ U=\operatorname{id}_{D^n}\). If \(C\) is the
matrix of \(U\), then \(AC=I_n\).
:::
:::
