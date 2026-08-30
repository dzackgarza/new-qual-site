---
schema: qual/card@1
id: E-HAT-3.F-3
kind: exercise
title: "$\\operatorname{Ext}(A, \\mathbb{Q}) = 0$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Show that $\operatorname{Ext}(A, \mathbb{Q}) = 0$ for all $A$.
[Consider the homology with $\mathbb{Q}$ coefficients of a Moore space $M(A, n)$.]

::: {.solution}
<1>1. Divisibility and injectivity of $\mathbb{Q}$:
<2>1. An abelian group $D$ is divisible if for every $d \in D$ and non-zero integer $n \in \mathbb{Z}$, there exists $x \in D$ such that $nx = d$.
$\mathbb{Q}$ is divisible because $n(q/n) = q$ for all $q \in \mathbb{Q}$ and $n \in \mathbb{Z} \setminus \{0\}$.
Proof: arithmetic of rational numbers.
<2>2. By Baer’s Criterion, an abelian group (a $\mathbb{Z}$-module) is injective if and only if it is divisible.
Thus $\mathbb{Q}$ is an injective $\mathbb{Z}$-module.
Proof: Baer's Criterion for modules over principal ideal domains.

<1>2. Vanishing of $\operatorname{Ext}(A, \mathbb{Q})$ via free resolutions:
<2>1. Let $A$ be any abelian group, and choose a free presentation (resolution):
\[
0 \longrightarrow F_1 \xrightarrow{\;d\;} F_0 \longrightarrow A \longrightarrow 0,
\]
where $F_0, F_1$ are free abelian groups.
Proof: every abelian group is a quotient of a free abelian group with free kernel.
<2>2. Applying the contravariant functor $\operatorname{Hom}_\mathbb{Z}(-, \mathbb{Q})$ yields the long exact sequence:
\[
0 \longrightarrow \operatorname{Hom}(A, \mathbb{Q}) \longrightarrow \operatorname{Hom}(F_0, \mathbb{Q}) \xrightarrow{\;d^* \;} \operatorname{Hom}(F_1, \mathbb{Q}) \longrightarrow \operatorname{Ext}^1(A, \mathbb{Q}) \longrightarrow 0.
\]
Proof: derived functor long exact sequence for $\operatorname{Ext}$.
<2>3. Because $\mathbb{Q}$ is injective, every homomorphism $\phi: F_1 \to \mathbb{Q}$ extends along the inclusion $d: F_1 \hookrightarrow F_0$ to a homomorphism $\widetilde{\phi}: F_0 \to \mathbb{Q}$ such that $\widetilde{\phi} \circ d = \phi$.
Thus the dual map $d^*: \operatorname{Hom}(F_0, \mathbb{Q}) \to \operatorname{Hom}(F_1, \mathbb{Q})$ is surjective.
Proof: definition of injective module.
<2>4. By exactness:
\[
\operatorname{Ext}^1(A, \mathbb{Q}) \cong \operatorname{coker}(d^*) = \operatorname{Hom}(F_1, \mathbb{Q}) / \operatorname{Im}(d^*) = 0.
\]
Proof: surjectivity of $d^*$.

<1>3. Alternative topological perspective via Moore spaces:
<2>1. Let $X = M(A, n)$ be a Moore space with $\widetilde{H}_n(X) \cong A$ and $\widetilde{H}_i(X) = 0$ for all $i \neq n$.
By the Universal Coefficient Theorem for cohomology with $\mathbb{Q}$ coefficients:
\[
0 \longrightarrow \operatorname{Ext}(H_n(X), \mathbb{Q}) \longrightarrow H^{n+1}(X; \mathbb{Q}) \longrightarrow \operatorname{Hom}(H_{n+1}(X), \mathbb{Q}) \longrightarrow 0.
\]
Proof: Universal Coefficient Theorem for Cohomology.
<2>2. Since $\mathbb{Q}$ is a field, $H_{n+1}(X; \mathbb{Q}) \cong H_{n+1}(X) \otimes \mathbb{Q} = 0 \otimes \mathbb{Q} = 0$, so $H^{n+1}(X; \mathbb{Q}) = 0$.
The exact sequence forces $\operatorname{Ext}(A, \mathbb{Q}) = 0$.
Proof: exactness with vanishing middle group.

<1>4. Conclusion:
$\operatorname{Ext}(A, \mathbb{Q}) = 0$ for every abelian group $A$. Q.E.D.
Proof: <1>1 through <1>3.
:::
