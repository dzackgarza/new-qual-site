---
schema: qual/card@1
id: D-FULNORMPOLY
kind: definition
title: Normal polytopes, and when dilation forces very ampleness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Polytopes
  - Ample Divisors
relations:
- kind: uses
  target: PR-TORPOS
- kind: uses
  target: D-TORPOLY
review: draft
prompts:
- What is a normal lattice polytope, and how does it relate to very ampleness?
- How large must k be before kP is guaranteed normal?
---

::: {.definition title="Normal"}
A lattice polytope $P \subseteq M_\RR$ is **normal** if
\[
(kP \intersect M) + (\ell P \intersect M) = (k+\ell)P \intersect M \quad \text{for all } k, \ell \geq 1 ,
\]
equivalently $k \cdot (P \intersect M) = (kP) \intersect M$ for all $k \geq 1$, equivalently $(P \intersect M) \times \ts{1}$ generates the semigroup $C(P) \intersect (M \times \ZZ)$, where $C(P) \da \Cone(P \times \ts{1})$.
:::

::: {.proposition title="Two facts to carry"}
1. Normal implies very ample.

2. If $P$ is full-dimensional with $\dim P \geq 2$, then $kP$ is normal for every $k \geq \dim P - 1$.
:::

::: {.remark title="Why this settles the very ample question in practice"}
The three positivity notions can come apart only through the saturation clause at a vertex, and dilating repairs it: whatever $P$ is, some multiple is normal, hence very ample.
So a divisor that is ample but not very ample can only be a low multiple, and the second fact bounds how low.
In dimension two, $k \geq 1$ suffices, which is the reason ample and very ample agree on complete toric surfaces.
In dimension three the bound starts biting at $k \geq 2$, so the counterexample must be a polytope taken at $k = 1$.

The cone $C(P)$ in the definition is the same cone that presents $X_P$ as $\Proj$ of the semigroup ring, so normality of $P$ is exactly the statement that the homogeneous coordinate ring of the embedding by $P \intersect M$ is the full, integrally closed one.
:::
