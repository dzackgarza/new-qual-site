---
schema: qual/card@1
id: P-AGH542QUADTRANSFORM
kind: problem
title: Degree and multiplicities of a strict transform under a quadratic transformation
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Blowups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.2, the retained Egbert coordinate calculation, the
    standard quadratic Cremona transformation, and the blowup intersection
    formulas. The printed/transcribed statement omits the three fundamental
    lines joining pairs of base points: each is contracted by the quadratic
    transformation, so its target strict transform is a point rather than a
    curve. The statement is corrected by excluding those three lines. On the
    common blowup of the three source and target base points, the target line
    class is 2H-E_1-E_2-E_3 and the three target exceptional curves are the
    strict transforms H-E_j-E_k; intersecting with the strict transform of C
    gives the degree and all three target multiplicities without any
    smoothness assumption on C.
- event: source-corrected
  by: chatgpt
  date: 2026-09-19
  note: Excluded the three lines joining pairs of base points, which are contracted rather than transformed to curves.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $\varphi$ be the quadratic transformation of $(4.2.3)$, centered at $P_1, P_2, P_3$.
If $C$ is an irreducible curve of degree $d$ in $\PP^2$, distinct from the three lines joining pairs of $P_1,P_2,P_3$, and with points of multiplicity $r_1, r_2, r_3$ at $P_1, P_2, P_3$, then the strict transform $C^{\prime}$ of $C$ by $\varphi$ has degree
\[
d^{\prime}=2 d-r_1-r_2-r_3
\]
and has points of multiplicity

- $d-r_2-r_3$ at $Q_1$,

- $d-r_1-r_3$ at $Q_2$ and

- $d-r_1-r_2$ at $Q_3$.

The curve $C$ may have arbitrary singularities.

Hint: Use (Ex.
3.2).
:::

::: {.remark title="Erratum"}
The exclusion of the three lines joining pairs of base points is necessary.
Those are precisely the three curves contracted by the quadratic
transformation. For example, the line through $P_2$ and $P_3$ has
$$
d=1,
\qquad
r_1=0,
\qquad
r_2=r_3=1,
$$
so the displayed degree formula gives $d'=0$: its image is the point $Q_1$,
not a plane curve.
:::

::: {.solution}
Let
$$
p:S=\operatorname{Bl}_{P_1,P_2,P_3}\PP^2\longrightarrow\PP^2
$$
be the blowup of the three base points. Write $H$ for the pullback of a
line and $E_i$ for the exceptional curve over $P_i$.

<1>1. The quadratic transformation lifts to a morphism
$$
q:S\longrightarrow\PP^{2\prime}
$$
defined by the complete linear system
$$
|H'|,
\qquad
H'=2H-E_1-E_2-E_3.
$$

::: {.proof}
After choosing coordinates so that the $P_i$ are the three coordinate
vertices, the quadratic transformation is
$$
[x_0:x_1:x_2]
\dashmapsto
[x_1x_2:x_0x_2:x_0x_1]
$$
[[P-AGH46CREMONA]]. Its defining quadrics are exactly the conics through all
three base points, so on the blowup their strict transforms have divisor
class
$$
2H-E_1-E_2-E_3.
$$
The three base points are removed by the blowup, hence this system defines
the morphism $q$ resolving the rational map.
:::

<1>2. Let
$$
L_{23}=H-E_2-E_3,
\qquad
L_{13}=H-E_1-E_3,
\qquad
L_{12}=H-E_1-E_2
$$
be the strict transforms of the three lines joining pairs of base points.
Then $q$ contracts them respectively to three points
$$
Q_1,
\qquad
Q_2,
\qquad
Q_3,
$$
and identifies $S$ with
$$
\operatorname{Bl}_{Q_1,Q_2,Q_3}\PP^{2\prime}.
$$

::: {.proof}
For example,
$$
H'\cdot L_{23}
=
(2H-E_1-E_2-E_3)\cdot(H-E_2-E_3)
=
2-1-1
=0.
$$
The same calculation holds for the other two lines. Each $L_{jk}$ is a
nonsingular rational curve with
$$
L_{jk}^2=1-1-1=-1,
$$
so the resolved quadratic transformation contracts precisely these three
$(-1)$-curves.

The quadratic transformation is an involution [[P-AGH46CREMONA]]. Applying
the same construction on the target therefore blows up the three target
base points $Q_1,Q_2,Q_3$ and recovers $S$. Thus $L_{23},L_{13},L_{12}$ are
the exceptional curves over $Q_1,Q_2,Q_3$, respectively.
:::

<1>3. The strict transform $\overline C\subseteq S$ of $C$ has class
$$
\boxed{
\overline C
\sim
dH-r_1E_1-r_2E_2-r_3E_3.}
$$

::: {.proof}
The total transform of a plane curve of degree $d$ has class $dH$. At a
blown-up point $P_i$ of multiplicity $r_i$, the exceptional curve occurs in
the total transform with coefficient $r_i$. Therefore the standard
strict-transform formula gives the displayed class. This calculation uses
only the multiplicities at the three chosen points; $C$ may have arbitrary
other singularities.
:::

<1>4. Because $C$ is not one of the three contracted lines, the morphism
$q$ maps $\overline C$ birationally onto the target strict transform
$C'\subseteq\PP^{2\prime}$.

::: {.proof}
The morphism $q$ is an isomorphism away from the three curves
$L_{23},L_{13},L_{12}$. Since $C$ is irreducible and is not one of the
corresponding three lines in the source plane, its strict transform
$\overline C$ is not one of these exceptional curves. Hence its generic
point lies in the locus on which $q$ is an isomorphism. Its image is
therefore an irreducible curve $C'$, and
$$
q|_{\overline C}:\overline C\dashrightarrow C'
$$
is birational.
:::

<1>5. The degree of $C'$ is
$$
\boxed{
d'=2d-r_1-r_2-r_3.}
$$

::: {.proof}
The pullback by $q$ of a line in the target plane is $H'$. Therefore
$$
\deg C'
=
H'\cdot\overline C.
$$
Using steps <1>1 and <1>3 together with
$$
H^2=1,
\qquad
E_i^2=-1,
\qquad
H\cdot E_i=E_i\cdot E_j=0\quad(i\ne j),
$$
gives
$$
\begin{aligned}
d'
&=(2H-E_1-E_2-E_3)
\cdot(dH-r_1E_1-r_2E_2-r_3E_3)\\
&=2d-r_1-r_2-r_3.
\end{aligned}
$$
:::

<1>6. The multiplicity of $C'$ at $Q_1$ is
$$
\boxed{
\mu_{Q_1}(C')=d-r_2-r_3.}
$$

::: {.proof}
Under
$$
q:S=\operatorname{Bl}_{Q_1,Q_2,Q_3}\PP^{2\prime}
\longrightarrow\PP^{2\prime},
$$
the exceptional curve over $Q_1$ is $L_{23}$. For the blowup of a point,
the multiplicity of a curve at the centre equals the intersection of its
strict transform with the exceptional curve. Hence
$$
\mu_{Q_1}(C')
=
\overline C\cdot L_{23}.
$$
By steps <1>2--<1>3,
$$
\begin{aligned}
\overline C\cdot L_{23}
&=(dH-r_1E_1-r_2E_2-r_3E_3)
\cdot(H-E_2-E_3)\\
&=d-r_2-r_3.
\end{aligned}
$$
:::

<1>7. Similarly,
$$
\boxed{
\mu_{Q_2}(C')=d-r_1-r_3,
\qquad
\mu_{Q_3}(C')=d-r_1-r_2.}
$$

::: {.proof}
The exceptional curves over $Q_2$ and $Q_3$ are respectively
$$
L_{13}=H-E_1-E_3
$$
and
$$
L_{12}=H-E_1-E_2.
$$
Intersecting each with the class of $\overline C$ from step <1>3 gives
$$
\overline C\cdot L_{13}=d-r_1-r_3
$$
and
$$
\overline C\cdot L_{12}=d-r_1-r_2.
$$
By the same blowup multiplicity formula as in step <1>6, these are exactly
the target multiplicities at $Q_2,Q_3$.
:::

<1>8. The formulas remain valid when $C$ has arbitrary singularities away
from, or at, the three base points.

::: {.proof}
Every calculation above takes place in the divisor class group of the smooth
common resolution $S$ and uses only the multiplicities $r_i$ entering the
strict-transform class. No step assumes that the germ of $C$ at any $P_i$
is ordinary or nonsingular, nor that $C$ is nonsingular elsewhere. Thus the
degree and target-multiplicity formulas hold for arbitrary singularities.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>5 proves the degree formula, steps <1>6--<1>7 prove the three
multiplicity formulas, and step <1>8 establishes the stated generality.
:::
:::
