---
schema: qual/card@1
id: P-APAS15D
kind: problem
title: Finite-group complex matrix representations are diagonalizable; infinite counterquestion
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Diagonalization
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group and let $X \colon G \to \mathrm{GL}_n(\mathbb{C})$ be a complex matrix representation of $G$.
For any $g \in G$, prove that the matrix $X(g)$ is diagonalizable.
Is this still true if the group $G$ is infinite?
:::

::: {.solution}
Let \(g\in G\). Because \(G\) is finite, \(g\) has finite order, say
\[
g^m=e.
\]
Applying the representation \(X\),
\[
X(g)^m=X(g^m)=X(e)=I.
\]
Thus the minimal polynomial \(\mu_{X(g)}(t)\) divides
\[
t^m-1.
\]
Over \(\mathbb C\), the polynomial \(t^m-1\) has no repeated roots: its derivative is
\[
mt^{m-1},
\]
and a common root of \(t^m-1\) and \(mt^{m-1}\) would have to be both nonzero and zero, which is impossible. Hence \(t^m-1\) splits into distinct linear factors over \(\mathbb C\). Therefore the minimal polynomial of \(X(g)\) also splits into distinct linear factors.

A complex matrix is diagonalizable if and only if its minimal polynomial has no repeated roots. Hence every \(X(g)\) is diagonalizable.

This fails for infinite groups. Let
\[
G=\mathbb Z
\]
and define a representation \(X:\mathbb Z\to\operatorname{GL}_2(\mathbb C)\) by
\[
X(n)=J^n,
\qquad
J=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
Since \(J\) is invertible, this is a group homomorphism. But
\[
X(1)=J
\]
is not diagonalizable: its only eigenvalue is \(1\), while
\[
J-I=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0,
\]
so its minimal polynomial is \((t-1)^2\). Thus the finite-group hypothesis is essential.
:::
