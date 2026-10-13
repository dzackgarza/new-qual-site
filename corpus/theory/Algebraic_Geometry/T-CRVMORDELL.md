---
schema: qual/card@1
id: T-CRVMORDELL
kind: theorem
title: Mordell's theorem, and $E(\QQ)$ as a finitely generated abelian group
slogan: 'For an elliptic curve over $\QQ$, the rational points form $\ZZ^r$ plus a finite torsion subgroup.'
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
- Why is the set of rational points a subgroup?
- State Mordell's theorem and say what its two summands are.
- Give a curve with rank $0$ and nontrivial torsion, and one with rank $1$ and no torsion.
---

::: {.theorem title="Mordell"}
Let $E/\QQ$ be an elliptic curve. Then $E(\QQ)$ is a finitely generated abelian group, so
$$
E(\QQ)\cong\ZZ^r\oplus E(\QQ)_{\mathrm{tors}}
$$
for a uniquely determined integer $r\geq0$, and $E(\QQ)_{\mathrm{tors}}$ is finite. The integer $r$ is the rank of $E(\QQ)$.
:::

::: {.example}
**Rank $0$, torsion $C_3$.** The Fermat cubic $x^3 + y^3 = z^3$ has
$$
E(\QQ) = \theset{ \thevector{1:-1:0},\ \thevector{1:0:1},\ \thevector{0:1:1} } \cong C_3 ,
$$
with $\thevector{1:-1:0}$ chosen as the identity. These are the three rational inflection points. The assertion that there are no further rational points is equivalent, after clearing denominators, to Fermat's last theorem for exponent $3$.

**Rank $1$, no torsion.** For $y^2 + y = x^3 - x$ with $p_0 = \thevector{0:1:0}$,
$$
E(\QQ) = \generators{P} \cong \ZZ, \qquad P = (0,0) .
$$
A descent and height computation proves that $P$ generates and that the torsion subgroup is trivial. Its first multiples include
$$
2P = (1, 0), \quad
3P = (-1,-1), \quad
4P = (2,-3), \quad
5P = \qty{ \tfrac{1}{4}, -\tfrac{5}{8} }, \quad
6P = (6, 14), \quad
7P = \qty{ -\tfrac{5}{9}, \tfrac{8}{27} } .
$$
:::

::: {.remark}
The multiplication, inverse, and identity maps of the elliptic-curve group scheme are morphisms over $\QQ$. Therefore they preserve $\QQ$-points, so $E(\QQ)$ is a subgroup of $E(\overline{\QQ})$.

Finite generation is proved by combining descent with a height argument.
The weak Mordell theorem gives $E(\QQ)/2E(\QQ)$ finite. Choose finitely many representatives for these cosets. After subtracting a representative, every point is twice another rational point; the canonical height decreases under this descent except on a bounded set, and there are only finitely many rational points of bounded height. This yields a finite generating set. Over $\overline{\QQ}$, multiplication by every nonzero integer is surjective, so this finite-generation phenomenon is arithmetic rather than geometric over the algebraic closure.

What the theorem does not give is the rank.
Mazur's theorem classifies $E(\QQ)_{\mathrm{tors}}$ into fifteen possible groups. No unconditional algorithm is known that is proved to terminate with the rank for every elliptic curve over $\QQ$, and no uniform upper bound for ranks over $\QQ$ is known.
:::
