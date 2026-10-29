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

::: {.problem}
(a) What is a Lie group? Define a unitary representation and state the Peter--Weyl theorem. What is the Lie algebra of a Lie group, the Jacobi identity, and the adjoint representation? What is the commutator of vector fields?

(b) For a finite-dimensional complex representation of $\ZZ$, when is it completely reducible, and what are its indecomposable modules?
:::

::: {.solution}

::: pf

::: pf-step
(a) A Lie group is a smooth manifold $G$ with a group structure for which multiplication and inversion are smooth maps.

::: pf-proof

::: pf-step
The commutator of vector fields $X,Y$ on a manifold is the vector field $[X,Y]$ acting on smooth functions by $[X,Y](f)=X(Yf)-Y(Xf)$.

:::

::: pf-step
The Lie algebra of $G$ is $\mathfrak g=T_eG$, identified with the left-invariant vector fields on $G$, with the commutator of vector fields as bracket. The bracket is bilinear, alternating, and satisfies the Jacobi identity
$$
[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0.
$$

:::

::: pf-step
The adjoint representation of $G$ is $\operatorname{Ad}:G\to\GL(\mathfrak g)$, where $\operatorname{Ad}_g$ is the derivative at $e$ of conjugation $h\mapsto ghg^{-1}$. Its derivative is the adjoint representation of $\mathfrak g$,
$$
\operatorname{ad}:\mathfrak g\to\mathfrak{gl}(\mathfrak g),\qquad \operatorname{ad}_X(Y)=[X,Y].
$$

:::

::: pf-step
A unitary representation of a topological group $G$ is a homomorphism $\pi:G\to U(V)$ into the unitary group of a complex Hilbert space $V$ that is strongly continuous: $g\mapsto\pi(g)v$ is continuous for each $v\in V$.

:::

::: pf-step
The Peter--Weyl theorem: for a compact group $G$, the matrix coefficients of finite-dimensional irreducible unitary representations are dense in $C(G)$; equivalently, the left regular representation on $L^2(G)$ is the Hilbert direct sum of the finite-dimensional irreducible representations, each occurring with multiplicity equal to its dimension.

:::

:::

:::

::: pf-step
(b) Let $\rho:\ZZ\to\GL(V)$ be a finite-dimensional complex representation and $T=\rho(1)$. Then $\rho$ is completely reducible if and only if $T$ is diagonalizable, and its indecomposable summands are the Jordan blocks $J_r(\lambda)$ with $r\ge1$ and $\lambda\in\CC^\times$.

::: pf-proof

::: {.pf-step #operator}
Representations of $\ZZ$ on $V$ are the same as invertible operators on $V$.

::: pf-proof
A representation is determined by $T=\rho(1)\in\GL(V)$ through $\rho(n)=T^n$, and every invertible $T$ defines one this way.
:::

:::

::: pf-step
$\rho$ is completely reducible if and only if $T$ is diagonalizable.

::: pf-proof
By step [](#operator){.pf-ref}, a subrepresentation is a $T$-invariant subspace. The irreducible complex representations of the abelian group $\ZZ$ are one-dimensional, given by the characters $n\mapsto\lambda^n$ with $\lambda\in\CC^\times$, since $T$ has an eigenvector in every nonzero invariant subspace. A direct sum of irreducibles is therefore a basis of eigenvectors of $T$.
:::

:::

::: pf-step
The indecomposable finite-dimensional representations are the Jordan blocks $J_r(\lambda)$, $r\ge1$, $\lambda\in\CC^\times$.

::: pf-proof
A representation is a module over $\CC[\ZZ]\cong\CC[t,t^{-1}]$, a PID, with $t$ acting by $T$. A finite-dimensional module is torsion, and by the structure theorem its indecomposable summands are the primary cyclic modules $\CC[t,t^{-1}]/((t-\lambda)^r)$ with $\lambda\ne0$. On such a module $t$ acts by the Jordan block $J_r(\lambda)$.
:::

:::

:::

:::

:::

:::
