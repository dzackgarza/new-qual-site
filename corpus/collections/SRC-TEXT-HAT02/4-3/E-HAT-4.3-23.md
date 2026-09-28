---
schema: qual/card@1
id: E-HAT-4.3-23
kind: problem
title: "Uniqueness of Quillen plus construction"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 23; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Prove the following uniqueness result for the Quillen plus construction: Given a connected CW complex $X$, if there is an abelian CW complex $Y$ and a map $X \to Y$ inducing an isomorphism $H_*(X; \mathbb{Z}) \approx H_*(Y; \mathbb{Z})$, then such a $Y$ is unique up to homotopy equivalence.
:::

::: {.solution}
Suppose
\[
i:X\to Y,
\qquad
i':X\to Y'
\]
are homology isomorphisms and \(Y,Y'\) are connected abelian CW complexes. Replace \(i\) by the inclusion of \(X\) into its mapping cylinder \(W=M_i\). Then \(W\simeq Y\), and since \(i\) is a homology isomorphism,
\[
H_*(W,X;\mathbb Z)=0.
\]
The universal coefficient theorem therefore gives, for every abelian group \(A\),
\[
H^{n+1}(W,X;A)=0
\qquad\text{for all }n.
\]
In particular this holds for
\[
A=\pi_n(Y').
\]

Because \(Y'\) is an abelian CW complex, Corollary 4.73 applies: all obstruction groups to extending
\[
i':X\to Y'
\]
over \(W\) vanish. Hence there is a map
\[
F:W\to Y'
\]
extending \(i'\). Restricting along the deformation retract \(Y\simeq W\) gives a map
\[
f:Y\to Y'
\]
with
\[
fi\simeq i'.
\]
Since both \(i\) and \(i'\) induce homology isomorphisms, so does \(f\). Proposition 4.74, the homology Whitehead theorem for connected abelian CW complexes, therefore gives
\[
\boxed{f:Y\xrightarrow{\simeq}Y'.}
\]
Thus the abelian target of the Quillen plus construction is unique up to homotopy equivalence.
:::
