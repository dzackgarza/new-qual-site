---
schema: qual/card@1
id: P-SABYI
kind: problem
title: Structure theorem for finitely generated modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Principal Ideal Domains
  - Abelian Groups
relations: []
review: draft
---

::: {.problem}
State and explain a proof of the structure theorem for finitely generated modules over a PID. What are the module and the PID in the case of finitely generated abelian groups?
:::

::: {.solution}
Let $R$ be a PID and let $M$ be a finitely generated $R$-module. Then there are unique integers $r\ge0$ and nonzero nonunits
\[
d_1\mid d_2\mid\cdots\mid d_s
\]
(up to associates) such that
\[
M\cong R^r\oplus R/(d_1)\oplus\cdots\oplus R/(d_s).
\]
Equivalently, the torsion part may be decomposed into primary cyclic summands.

To prove this, choose generators of $M$. There is a surjection
\[
R^n\twoheadrightarrow M
\]
with kernel $K$. Since submodules of finite free modules over a PID are free, choose a basis of $K$ and obtain a presentation
\[
R^m\xrightarrow{A}R^n\longrightarrow M\longrightarrow0.
\]
Over a PID, elementary row and column operations reduce $A$ to Smith normal form
\[
UAV=\operatorname{diag}(d_1,\ldots,d_s,0,\ldots,0),
\qquad d_1\mid\cdots\mid d_s.
\]
The invertible matrices $U,V$ merely change bases in the free modules, so they do not change the cokernel. Therefore
\[
M\cong\operatorname{coker}(A)
\cong R^{n-s}\oplus\bigoplus_{i=1}^sR/(d_i).
\]
Uniqueness follows from the determinantal divisors, or equivalently from uniqueness of Smith normal form up to associates.

For finitely generated abelian groups, take
\[
R=\ZZ,
\]
and regard the abelian group $A$ as a $\ZZ$-module by repeated addition. The theorem becomes
\[
A\cong\ZZ^r\oplus\ZZ/d_1\ZZ\oplus\cdots\oplus\ZZ/d_s\ZZ,
\qquad d_1\mid\cdots\mid d_s.
\]
:::
