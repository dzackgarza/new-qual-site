---
schema: qual/card@1
id: P-AGH518COHOMCLASS
kind: problem
title: Cohomology class of a divisor and compatibility with the intersection pairing
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
---

::: problem
For any divisor $D$ on the surface $X$, we define its cohomology class $c(D) \in H^1\left(X, \Omega_X\right)$ by using the isomorphism $\Pic X \cong H^1\left(X, \mathcal{O}_X^*\right)$ of (III, Ex.
4.5) and the sheaf homomorphism $d \log : \mathcal{O}^* \rightarrow \Omega_X$ (III, Ex.
7.4c). Thus we obtain a group homomorphism $c: \Pic X \rightarrow H^1\left(X, \Omega_X\right)$.
On the other hand, $H^1(X, \Omega)$ is dual to itself by Serre duality (III, 7.13), so we have a nondegenerate bilinear map
\[
\langle\quad, \quad\rangle: H^1(X, \Omega) \times H^1(X, \Omega) \rightarrow k .
\]

a. Prove that this is compatible with the intersection pairing, in the following sense: for any two divisors $D, E$ on $X$, we have
\[
\langle c(D), c(E)\rangle=(D . E) \cdot 1
\]
in $k$.

Hint: Reduce to the case where $D$ and $E$ are nonsingular curves meeting transversally.
Then consider the analogous map $c: \Pic D \rightarrow H^1\left(D, \Omega_D\right)$, and the fact (III, Ex.
7.4) that $c(\text{point})$ goes to 1 under the natural isomorphism of $H^1\left(D, \Omega_D\right)$ with $k$.

b. If $\operatorname{char} k=0$, use the fact that $H^1\left(X, \Omega_X\right)$ is a finite-dimensional vector space to show that $\Num X$ is a finitely generated free abelian group.
:::
