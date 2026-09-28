---
schema: qual/card@1
id: P-AMH-ALG-SG16-23
kind: problem
title: The kernel of a ring homomorphism restricted to an ideal is an ideal
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 2008) Let $\varphi:R\to S$ be a ring homomorphism.
Let $I\subseteq R$ be an ideal of $R$, and set
\[
J=\{x\in I\mid \varphi(x)=0_S\},
\]
where $0_S$ denotes the zero element of $S$.
Prove that $J$ is an ideal of $R$.
:::

::: {.solution}
Proof.
(Nonempty) We have 0 R∈I and φ(0R) = 0S, so 0 R∈J. Thus, J⁄= ∅. (Closure under−) Given x,y∈J, we have x,y∈I and hence x−y∈I. Moreover, φ(x−y) =φ(x)−φ(y) = 0S− 0S = 0S, so x−y∈J. (Sticky) Given x∈J and r∈R, we have x∈I, and hence rx,xr ∈I. Moreover, φ(rx) =φ(r)φ(x) =φ(r)0S = 0S, and φ(xr) =φ(x)φ(r) = 0Sφ(r) = 0S, so rx,xr ∈J. The Fundamental Theorem of Ring Homomorphisms, Also called the First Homomorphism Theorem for Rings or the Basic Homomorphism Theorem for Rings , this theorem says that if φ : R→ S is a ring homomorphism, then there is a ring isomorphism ~φ :R/Ker(φ)≃ Im(φ) deﬁned by ~φ(Ker(φ) +r) =φ(r). 12 Quotient Rings and Fields Criteria for R to be a Field.
Know that a commutive ring with unit is a ﬁeld if and only if its only ideals are{0} and the whole ring.
Be prepared to prove this.
For example, here is a problem asking to prove one direction of this statement:
:::
