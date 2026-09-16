---
schema: qual/card@1
id: E-HAT-4.L-4
kind: problem
title: "No bundle $S^7 \\to S^{23} \\to \\mathbb{OP}^2$ exists"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.L, Exercise 4 and the current corrections; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show there is no fiber bundle $S^7 \to S^{23} \to \mathbb{OP}^2$.
:::

::: {.solution}
Suppose there were a fiber bundle
\[
S^7\longrightarrow S^{23}\xrightarrow{p}\mathbb{OP}^2.
\]
Let
\[
C_p=\mathbb{OP}^2\cup_p CS^{23}
\]
be the mapping cone of the projection.

Coning each fiber \(S^7\) produces a disk \(D^8\). Thus \(C_p\) is the Thom space of the associated cone/disk bundle over \(\mathbb{OP}^2\). Since its boundary is the sphere \(S^{23}\), collapsing this boundary to the cone point gives a closed \(24\)-manifold. The Thom isomorphism (equivalently Poincaré duality in \(C_p\)) gives
\[
H^*(C_p;\mathbb Z)
\cong
\mathbb Z\{1,x,x^2,x^3\},
\qquad |x|=8,
\]
with
\[
x^3\ne0\in H^{24}(C_p;\mathbb Z).
\tag{1}
\]
More explicitly, \(x\) restricts to a generator of \(H^8(\mathbb{OP}^2)\), \(x^2\) generates degree \(16\), and Poincaré duality forces the pairing of degrees \(8\) and \(16\) to be unimodular, so \(x^3\) is a generator up to sign.

Reduce mod \(3\). The instability axiom for reduced powers says that for a degree-eight class,
\[
P^4x=x^3.
\tag{2}
\]
But the mod-3 Adem relation with \(a=1,b=3\) is
\[
P^1P^3=P^4.
\tag{3}
\]
Since
\[
H^{20}(C_p;\mathbb Z_3)=0,
\]
we have
\[
P^3x=0.
\]
Equations (2) and (3) then give
\[
x^3=P^4x=P^1P^3x=0,
\]
contradicting (1). Therefore
\[
\boxed{\text{there is no fiber bundle }S^7\to S^{23}\to\mathbb{OP}^2.}
\]
:::
