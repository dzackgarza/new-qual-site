---
schema: qual/card@1
id: P-UFCQH
kind: problem
title: Whether real matrices conjugate over $\CC$ are conjugate over $\RR$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Canonical Forms
  - Matrices
relations: []
review: draft
---

::: problem
Let $A,B\in M_n(\RR)$. If $A$ and $B$ are similar in $M_n(\CC)$, must they already be similar in $M_n(\RR)$?
:::

::: solution
Yes.

Suppose there is some
\[
X\in GL_n(\CC)
\]
with
\[
AX=XB.
\]
Write
\[
X=P+iQ
\]
with $P,Q\in M_n(\RR)$. Since $A$ and $B$ are real, comparing real and imaginary parts gives
\[
AP=PB,
\qquad
AQ=QB.
\]
Hence for every real number $t$,
\[
A(P+tQ)=(P+tQ)B.
\]

Consider the real polynomial
\[
f(t)=\det(P+tQ).
\]
It is not identically zero, because
\[
f(i)=\det(P+iQ)=\det X\ne0.
\]
Therefore $f$ has only finitely many real roots. Choose
\[
t\in\RR
\]
with $f(t)\ne0$. Then
\[
Y=P+tQ\in GL_n(\RR)
\]
and
\[
AY=YB.
\]
Thus
\[
A=YBY^{-1},
\]
so $A$ and $B$ are already similar over $\RR$.
:::
