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
That $P$ has infinite order is visible after a few doublings, and the denominators are the thing to watch:
\[
2P = (1, 0), \quad
3P = (-1,-1), \quad
4P = (2,-3), \quad
5P = \qty{ \tfrac{1}{4}, -\tfrac{5}{8} }, \quad
6P = (6, 14), \quad
7P = \qty{ -\tfrac{5}{9}, \tfrac{8}{27} } .
\]
The denominators appear as $d^2$ and $d^3$ in the two coordinates, which is exactly the shape a height function measures.
:::

::: {.remark}
Two things make this statement land, and both are about which structure survives restriction to $\QQ$.

The subgroup claim is not automatic and is the reason the definition insists that $p_0$ be rational.
Addition is defined by "three collinear points sum to zero", and a line through two rational points of a rational cubic meets it in a third point whose coordinates are rational, because substituting the line into the cubic gives a cubic in one variable with rational coefficients and two rational roots, so the third root is rational too.
Inversion is reflection, also rational.
If $p_0$ were irrational the identity would leave the set and nothing would be a subgroup; this is why the base point is part of the data and not an afterthought.

That subgroup is where the geometry turns into arithmetic.
Writing a rational point in lowest terms and clearing denominators converts $E(\QQ)$ into the integral solutions of a homogeneous cubic in three variables, so the chord-and-tangent construction becomes an operation that manufactures new integer solutions from old ones --- the classical secant method, predating any of this language.
Reading it the other way, a Diophantine question about a cubic acquires a group acting on its own solution set, and Mordell's theorem says that group is small enough to describe: finitely many generators account for every solution there is.
This exchange is the entire reason elliptic curves sit in number theory rather than only in geometry.

Finite generation is the part with content, and the shape of the proof is worth knowing even when the proof is not.
It is a descent: the weak Mordell theorem gives $E(\QQ)/2E(\QQ)$ finite, and a height function measuring the arithmetic size of a point turns that finiteness into generation by a bounded set.
Neither half is formal, and neither is visible from the geometry over $\bar\QQ$, where $E$ is divisible and nothing is finitely generated.

What the theorem does not give is the rank.
Torsion is completely understood --- by Mazur's theorem, $E(\QQ)_{\mathrm{tors}}$ is one of fifteen groups --- while $r$ has no known algorithm and no proven bound, which is the honest answer when an examiner pushes past the statement.
:::
