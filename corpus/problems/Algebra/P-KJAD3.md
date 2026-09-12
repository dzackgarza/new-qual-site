---
schema: qual/card@1
id: P-KJAD3
kind: problem
title: Lie groups, Peter–Weyl, and representations of $\ZZ$
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
  - Algebras
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
What is a Lie group? Define a unitary representation and state the Peter--Weyl theorem. What is the Lie algebra of a Lie group, the Jacobi identity, and the adjoint representation? What is the commutator of vector fields?

For a finite-dimensional complex representation of $\ZZ$, when is it completely reducible, and what are its indecomposable modules?
:::

::: {.solution}
<1>1. A **Lie group** is a smooth manifold $G$ equipped with a group structure for which multiplication and inversion are smooth.

Its **Lie algebra** is
\[
\mathfrak g=T_eG,
\]
identified with the left-invariant vector fields on $G$. The bracket is the commutator of vector fields:
\[
[X,Y](f)=X(Yf)-Y(Xf).
\]
It is bilinear, alternating, and satisfies the Jacobi identity
\[
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
\]

The **adjoint representation** of the Lie algebra is
\[
\operatorname{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g),
\qquad
\operatorname{ad}_X(Y)=[X,Y].
\]

<1>2. A **unitary representation** of a topological group $G$ is a continuous homomorphism
\[
\pi:G\to U(V)
\]
for a complex Hilbert space $V$.

For a compact group, the Peter--Weyl theorem says that the matrix coefficients of finite-dimensional irreducible unitary representations are dense in $C(G)$; equivalently, the left regular representation on $L^2(G)$ decomposes as a Hilbert direct sum of finite-dimensional irreducibles, each occurring with multiplicity equal to its dimension.

<1>3. A finite-dimensional complex representation of $\ZZ$ is the same thing as an invertible linear operator.
::: {.proof}
A representation
\[
\rho:\ZZ\to GL(V)
\]
is determined by
\[
T=\rho(1)\in GL(V),
\]
and then $\rho(n)=T^n$. Conversely every invertible $T$ defines such a representation.
:::

<1>4. The representation is completely reducible if and only if $T$ is diagonalizable over $\CC$.
::: {.proof}
The irreducible complex representations of the abelian group $\ZZ$ are one-dimensional characters
\[
n\longmapsto\lambda^n,
\qquad \lambda\in\CC^\times.
\]
Thus a direct sum of irreducibles is exactly a decomposition of $V$ into eigenspaces of $T$, i.e. diagonalizability.
:::

<1>5. The finite-dimensional indecomposable complex representations are the Jordan blocks
\[
J_r(\lambda),
\qquad r\ge1,
\quad \lambda\in\CC^\times.
\]
::: {.proof}
The group algebra is
\[
\CC[\ZZ]\cong\CC[t,t^{-1}],
\]
a PID. Finite-dimensional modules are torsion modules, and the indecomposable primary cyclic modules are
\[
\CC[t,t^{-1}]/((t-\lambda)^r),
\qquad \lambda\ne0.
\]
Under the action of $t$, these are exactly Jordan blocks $J_r(\lambda)$.
:::
:::
