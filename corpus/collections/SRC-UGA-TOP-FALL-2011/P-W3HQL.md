---
schema: qual/card@1
id: P-W3HQL
kind: problem
title: The genera $g$ for which there is a covering $\Sigma_5\to\Sigma_g$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Replaced the unsupported existence assertion by explicit index-d surface-cover constructions.
---

::: problem
For any natural number $g$ let $\Sigma_g$ denote the (compact, orientable) surface of genus $g$.

Determine, with proof, all numbers $g$ with the property that there exists a covering space $\pi : \Sigma_5 \to \Sigma_g$ .

> Hint: How does the Euler characteristic behave for covering spaces?
:::

::: {.solution}
<1>1. Any covering
\[
\pi:\Sigma_5\to\Sigma_g
\]
has a finite, constant number \(d\ge1\) of sheets.
::: {.proof}
A fiber of a covering map is discrete.
Since \(\Sigma_g\) is Hausdorff, a point \(y\in\Sigma_g\) is closed, so
\[
\pi^{-1}(y)
\]
is a closed subset of the compact space \(\Sigma_5\), hence compact.
A compact discrete space is finite.
The cardinality of the fiber is locally constant for a covering map, and \(\Sigma_g\) is connected, so it is the same finite integer \(d\) over every point.
:::

<1>2. For a \(d\)-sheeted covering of finite CW complexes,
\[
\chi(\Sigma_5)=d\,\chi(\Sigma_g).
\]
::: {.proof}
Give \(\Sigma_g\) a finite CW structure and lift it through the covering.
Every open cell has exactly \(d\) disjoint lifts, each mapped homeomorphically onto that cell.
Thus the lifted CW structure on \(\Sigma_5\) has \(d\) times as many cells in every dimension.
Taking the alternating sum of cell counts gives the displayed identity.
:::

<1>3. A necessary condition for such a covering is
\[
-8=d(2-2g),
\]
so
\[
d=\frac4{g-1}.
\]
Consequently
\[
g\in\{2,3,5\}.
\]
::: {.proof}
For a closed orientable surface of genus \(h\),
\[
\chi(\Sigma_h)=2-2h.
\]
Applying <1>2 gives
\[
2-2\cdot5=d(2-2g),
\]
hence
\[
-8=-2d(g-1).
\]
Thus \(d(g-1)=4\). Since \(d\) is a positive integer, \(g-1\) must be a positive divisor of \(4\), namely \(1,2\), or \(4\). Therefore \(g=2,3\), or \(5\). This also excludes \(g=0,1\).
:::

<1>4. For every \(g\ge1\) and every \(d\ge1\), there exists a connected \(d\)-sheeted covering of \(\Sigma_g\).
::: {.proof}
Use the standard presentation
\[
\pi_1(\Sigma_g)
=
\left\langle
 a_1,b_1,\dots,a_g,b_g
\ \middle|\
 [a_1,b_1]\cdots[a_g,b_g]=1
\right\rangle.
\]
Define
\[
q:\pi_1(\Sigma_g)\to\mathbb Z/d\mathbb Z
\]
by
\[
q(a_1)=1,
\qquad
q(b_1)=q(a_2)=q(b_2)=\cdots=q(a_g)=q(b_g)=0.
\]
The defining relation maps to \(0\), since every commutator maps to \(0\) in the abelian group \(\mathbb Z/d\mathbb Z\). Hence \(q\) is a well-defined surjection.
Its kernel
\[
H=\ker q
\]
has index \(d\) in \(\pi_1(\Sigma_g)\).

By the classification of connected covering spaces, the subgroup \(H\) determines a connected covering
\[
p:\widetilde\Sigma\to\Sigma_g
\]
with exactly \(d\) sheets.
:::

<1>5. If the covering in <1>4 has degree \(d\), then \(\widetilde\Sigma\) is a closed orientable surface of genus
\[
1+d(g-1).
\]
::: {.proof}
A finite-sheeted cover of a compact surface is compact, and a covering of a surface is again a surface.
The orientation of \(\Sigma_g\) lifts through the local homeomorphism \(p\), so \(\widetilde\Sigma\) is orientable.
It is connected by construction and has no boundary, hence
\[
\widetilde\Sigma\cong\Sigma_h
\]
for some \(h\ge0\). By <1>2,
\[
2-2h=d(2-2g).
\]
Solving gives
\[
h=1+d(g-1).
\]
:::

<1>6. Each of \(g=2,3,5\) actually occurs as the target genus of a covering from \(\Sigma_5\).
::: {.proof}
For \(g=2\), take \(d=4\) in <1>4. By <1>5, the covering surface has genus
\[
1+4(2-1)=5,
\]
so it is a \(4\)-sheeted covering
\[
\Sigma_5\to\Sigma_2.
\]
For \(g=3\), take \(d=2\). Its covering surface has genus
\[
1+2(3-1)=5,
\]
so there is a \(2\)-sheeted covering
\[
\Sigma_5\to\Sigma_3.
\]
For \(g=5\), the identity map is a \(1\)-sheeted covering
\[
\Sigma_5\to\Sigma_5.
\]
:::

<1>7. Therefore the complete answer is
\[
\boxed{g=2,3,5}.
\]
::: {.proof}
Necessity is <1>3 and existence is <1>6.
:::
:::
