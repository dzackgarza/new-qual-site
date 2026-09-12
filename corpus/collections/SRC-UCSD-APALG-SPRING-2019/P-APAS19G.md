---
schema: qual/card@1
id: P-APAS19G
kind: problem
title: Real irreducible endomorphisms need not be scalar; complexification
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: problem
Let $G$ be a finite group and let $X\colon G\to\mathrm{GL}_d(\mathbb{R})$ be an irreducible matrix representation of $G$ over the field of real numbers.
Let $T\colon\mathbb{R}^d\to\mathbb{R}^d$ be an endomorphism of $X$.

(a) Give an example to show that $T$ is not necessarily a scalar transformation.

(b) Suppose that $T$ is not a scalar transformation.
Consider the representation $X'\colon G\to\mathrm{GL}_d(\mathbb{C})$ given by viewing real matrices as complex matrices:
\[
X'(g):=X(g)\qquad\text{for all }g\in G.
\]
Is it possible for $X'$ to be irreducible (as a complex matrix representation)?
Justify your answer.
:::

::: solution
For (a), let \(G=C_4=\langle g:g^4=1
angle\) and let \(V=\mathbb R^2\) with
\[
X(g)=J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
As a real representation this is irreducible, because a nonzero proper invariant subspace would be a real eigenline for \(J\), but \(J\) has characteristic polynomial \(t^2+1\) and hence no real eigenvalue. The endomorphism \(T=J\) commutes with the image of \(G\), but \(T\) is not a real scalar multiple of the identity.

For (b), suppose \(T\) is a non-scalar real endomorphism commuting with \(X(G)\). Regard both \(X(g)\) and \(T\) as complex matrices. Then \(T\) still commutes with every \(X'(g)\). If \(X'\) were irreducible over \(\mathbb C\), Schur's lemma would imply
\[
T=cI
\]
for some \(c\in\mathbb C\). Since \(T\) has real entries, this would force \(c\in\mathbb R\), contradicting that \(T\) is not a scalar transformation. Therefore \(X'\) cannot be irreducible.
:::
