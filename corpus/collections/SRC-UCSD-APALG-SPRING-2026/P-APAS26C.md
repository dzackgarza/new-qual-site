---
schema: qual/card@1
id: P-APAS26C
kind: problem
title: Maximal singular vectors of a $G$-map form a subrepresentation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Singular Values
relations: []
review: draft
---

::: {.problem}
Let $(V, \varphi)$ and $(W, \psi)$ be finite-dimensional unitary representations of a group $G$.
Let $A \in \operatorname{Hom}_G(V, W)$ be a $G$-equivariant linear map with operator norm $\sigma_1 > 0$.
Prove that
\[
V_1 = \{v \in V : \|Av\| = \sigma_1 \|v\|\}
\]
is a subrepresentation of $(V, \varphi)$.
:::

::: {.solution}
Because $A$ is $G$-equivariant,
\[
A\varphi(g)=\psi(g)A
\qquad(g\in G).
\]
Since the representations are unitary, taking adjoints and replacing $g$ by $g^{-1}$ gives
\[
A^*\psi(g)=\varphi(g)A^*.
\]
Therefore
\[
A^*A\,\varphi(g)
=A^*\psi(g)A
=\varphi(g)A^*A,
\]
so $A^*A$ commutes with the $G$-action on $V$.

The operator $A^*A$ is positive semidefinite Hermitian. Let its eigenvalues be
\[
\sigma_1^2\ge\sigma_2^2\ge\cdots\ge0.
\]
For $v\in V$,
\[
\|Av\|^2=\langle A^*Av,v\rangle.
\]
By the spectral theorem,
\[
\|Av\|=\sigma_1\|v\|
\]
if and only if $v$ lies in the eigenspace
\[
E_{\sigma_1^2}(A^*A)=\ker(A^*A-\sigma_1^2I).
\]
Hence
\[
V_1=E_{\sigma_1^2}(A^*A),
\]
which is a linear subspace. Since $A^*A$ commutes with every $\varphi(g)$, this eigenspace is $G$-stable. Thus $V_1$ is a subrepresentation of $V$.
:::
