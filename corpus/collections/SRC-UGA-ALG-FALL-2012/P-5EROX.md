---
schema: qual/card@1
id: P-5EROX
kind: problem
title: $AB-BA=A$ implies $\det A=0$ in characteristic zero, but not in characteristic
  $2$
classification:
  areas:
  - algebra
  topics:
  - Trace
  - Determinants
  - Matrices
relations: []
review: draft
---

::: problem
Let $k$ be a field of characteristic zero and $A, B \in M_n(k)$ be two square $n\times n$ matrices over $k$ such that $AB - BA = A$.
Prove that $\det A = 0$.

Moreover, when the characteristic of $k$ is 2, find a counterexample to this statement.
:::

::: solution
Assume first that $\operatorname{char}k=0$. Suppose for contradiction that
$A$ is invertible. From
\[
AB-BA=A
\]
and right multiplication by $A^{-1}$ we obtain
\[
ABA^{-1}-B=I_n.
\]
Taking traces and using invariance of trace under conjugation gives
\[
0=\operatorname{tr}(ABA^{-1})-\operatorname{tr}(B)
=\operatorname{tr}(I_n)=n.
\]
This is impossible in characteristic zero. Hence $A$ is not invertible, so
\[
\boxed{\det A=0}.
\]

In characteristic $2$, take
\[
A=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
B=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\]
Since $A^{-1}=A$,
\[
ABA^{-1}
=\begin{pmatrix}1&0\\0&0\end{pmatrix}
=B+I_2
\]
in characteristic $2$. Therefore
$ABA^{-1}-B=I_2$, equivalently $AB-BA=A$. But
\[
\det A=-1=1\ne0
\]
in characteristic $2$. Thus this pair is the required counterexample.
:::
