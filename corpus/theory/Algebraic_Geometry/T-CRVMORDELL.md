---
schema: qual/card@1
id: T-CRVMORDELL
kind: theorem
title: Mordell's theorem, and $E(\QQ)$ as a finitely generated abelian group
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Number Theory
  - Rational Points
relations:
- kind: uses
  target: PR-CRVGRP
- kind: related-to
  target: T-CRVJINV
review: draft
prompts:
- What does it mean for $(E, p_0)$ to be defined over a subfield?
- Why is the set of rational points a subgroup?
- State Mordell's theorem and say what its two summands are.
- Give a curve with rank $0$ and nontrivial torsion, and one with rank $1$ and no torsion.
---

::: {.definition title="Defined over a subfield"}
Let $k = \bar k$, let $(E, p_0)$ be elliptic, and embed $E \embeds \PP^2_{/k}$ by $\abs{3p_0}$, so $E = V(f)$ for a cubic $f$.
Say $(E, p_0)$ is **defined over** a subfield $k_0 \subseteq k$ when $f$ can be taken with coefficients in $k_0$ and $p_0 \in E(k_0)$.
Then $E(k_0) \leq E(k)$ is a subgroup.
:::

::: {.theorem title="Mordell"}
If $(E,p_0)$ is defined over $\QQ$, then $E(\QQ)$ is a finitely generated abelian group:
\[
E(\QQ) \iso \ZZ^r \oplus E(\QQ)_{\mathrm{tors}} ,
\]
with $r$ the **rank** and the torsion subgroup finite.
:::

::: {.example}
**Rank $0$, torsion $C_3$.** The Fermat cubic $x^3 + y^3 = z^3$ has
\[
E(\QQ) = \ts{ \tv{1:-1:0},\ \tv{1:0:1},\ \tv{0:1:1} } \iso C_3 ,
\]
these being its three rational inflection points.
That the list stops there is Fermat's last theorem for $n=3$, so this example is a restatement of a genuine theorem and not a computation.

**Rank $1$, no torsion.** For $y^2 + y = x^3 - x$ with $p_0 = \tv{0:1:0}$,
\[
E(\QQ) = \gens{P} \iso \ZZ, \qquad P = (0,0) \text{ in affine coordinates} .
\]
Repeatedly adding $P$ to itself by the chord-and-tangent rule produces infinitely many distinct rational points with rapidly growing numerators and denominators, which is the concrete face of "infinite order".
:::

::: {.remark}
Two things make this statement land, and both are about which structure survives restriction to $\QQ$.

The subgroup claim is not automatic and is the reason the definition insists that $p_0$ be rational.
Addition is defined by "three collinear points sum to zero", and a line through two rational points of a rational cubic meets it in a third point whose coordinates are rational, because the cubic in one variable already has two rational roots.
Clearing denominators then turns the group law into a Diophantine operation: rational solutions compose to give rational solutions.

Finite generation is the part with content, and the shape of the proof is worth knowing even when the proof is not.
It is a descent: the weak Mordell theorem gives $E(\QQ)/2E(\QQ)$ finite, and a height function measuring the arithmetic size of a point turns that finiteness into generation by a bounded set.
Neither half is formal, and neither is visible from the geometry over $\bar\QQ$, where $E$ is divisible and nothing is finitely generated.

What the theorem does not give is the rank.
Torsion is completely understood --- by Mazur's theorem, $E(\QQ)_{\mathrm{tors}}$ is one of fifteen groups --- while $r$ has no known algorithm and no proven bound, which is the honest answer when an examiner pushes past the statement.
:::
