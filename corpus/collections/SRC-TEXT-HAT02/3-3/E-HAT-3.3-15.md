---
schema: qual/card@1
id: E-HAT-3.3-15
kind: problem
title: "Local homology as sections of a covering"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
For an $n$-manifold $M$ and a compact subspace $A \subset M$, show that $H_n(M, M - A; R)$ is isomorphic to the group $\Gamma_R(A)$ of sections of the covering space $M_R \to M$ over $A$, that is, maps $A \to M_R$ whose composition with $M_R \to M$ is the identity.
:::

::: {.solution}
Write
\[
H_n(M\mid A;R)=H_n(M,M-A;R).
\]
For each $x\in A$, inclusion of pairs gives a homomorphism
\[
H_n(M\mid A;R)\longrightarrow H_n(M\mid x;R).
\]
Thus every class $\alpha\in H_n(M\mid A;R)$ determines a function
\[
x\longmapsto \alpha_x,
\]
where $\alpha_x$ is its image in the local homology group at $x$.

By the local constancy statement built into the orientation covering $M_R\to M$, this function is a section of $M_R$ over $A$. Hence there is a homomorphism
\[
\Phi:H_n(M,M-A;R)\longrightarrow\Gamma_R(A),
\qquad
\Phi(\alpha)(x)=\alpha_x.
\]

Hatcher's Lemma 3.27(a) says precisely that if $A$ is compact and $x\mapsto\alpha_x$ is a section of $M_R\to M$ over $A$, then there exists a unique class
\[
\alpha_A\in H_n(M\mid A;R)
\]
whose image in every $H_n(M\mid x;R)$ is $\alpha_x$. Therefore every section lies in the image of $\Phi$, and uniqueness says that $\Phi$ is injective.

Consequently
\[
\boxed{H_n(M,M-A;R)\cong\Gamma_R(A).}
\]
The isomorphism is the natural one sending a relative homology class to its family of local orientation classes along $A$.
:::
