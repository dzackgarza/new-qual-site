---
schema: qual/card@1
id: P-IBLLK
kind: problem
title: Homology of $S^2$ with equatorial antipodes identified
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
  - Quotient Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Fall 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the quotient CW structure with one 0-cell, one 1-cell, and two 2-cells, and checked that each 2-cell attaching map has degree 2 up to orientation.
---

::: problem
Let $X$ be the topological space obtained as the quotient of the sphere $S^2 = \theset{\vector x \in \RR^3 \suchthat \norm{\vector x} = 1}$ under the equivalence relation $\vector x \sim -\vector x$ for $\vector x$ in the equatorial circle, i.e. for $\vector x = (x_1, x_2, 0)$.

Calculate $H_* (X; \ZZ)$ from a CW complex description of $X$.
:::

::: {.solution}
Write
\[
E=\{(x_1,x_2,0)\in S^2\}
\cong S^1
\]
for the equator, and let $D_+$ and $D_-$ be the closed upper and lower hemispheres.

<1>1. The image of the equator in $X$ is
\[
E/(x\sim -x)\cong\RP^1\cong S^1.
\]
Give it a CW structure with one $0$-cell $v$ and one $1$-cell $e$.
::: {.proof}
The antipodal action on the circle is free, and the quotient map
\[
q_E:S^1\longrightarrow S^1/(z\sim -z)
\]
is the standard two-sheeted covering.
Identifying the quotient circle with $S^1$ via
\[
[z]\longmapsto z^2,
\]
the quotient map becomes
\[
z\longmapsto z^2.
\]
Thus the quotient equator is a circle and has the stated one-vertex CW structure.
:::

<1>2. The interiors of $D_+$ and $D_-$ descend to two open $2$-cells $e_+^2$ and $e_-^2$ of $X$.
Hence $X$ has a CW structure with
\[
\#\{0\text{-cells}\}=1,
\qquad
\#\{1\text{-cells}\}=1,
\qquad
\#\{2\text{-cells}\}=2.
\]
::: {.proof}
The equivalence relation identifies points only on the equator.
Therefore the quotient map is injective on each open hemisphere, so each hemisphere interior maps homeomorphically onto an open disk in $X$.

The characteristic map of either $2$-cell is the quotient map
\[
D_\pm\longrightarrow X.
\]
Its boundary lands in the quotient equator from <1>1.
Together with the cells $v,e$, these two hemisphere interiors exhaust $X$.
:::

<1>3. After choosing orientations of the two $2$-cells suitably, both attaching maps have degree $2$ on the $1$-skeleton.
Thus
\[
d_2:\ZZ e_+^2\oplus\ZZ e_-^2\longrightarrow\ZZ e
\]
is given by
\[
d_2(a,b)=2a+2b.
\]
::: {.proof}
The boundary circle of either hemisphere is the original equator $E$.
By <1>1, its attaching map is exactly the antipodal quotient
\[
S^1\longrightarrow E/(x\sim -x)\cong S^1,
\]
which, under the coordinate $z\mapsto z^2$, has degree $2$.

The cellular boundary formula says that the coefficient of the unique $1$-cell is this degree.
Reversing the chosen orientation of a $2$-cell reverses the sign of its coefficient, so we may orient both cells so that the two coefficients are $+2$.
Therefore
\[
d_2=(2\ \ 2).
\]
:::

<1>4. The cellular differential
\[
d_1:\ZZ e\longrightarrow\ZZ v
\]
is zero.
::: {.proof}
The unique $1$-cell is a loop whose two endpoints are both the unique $0$-cell $v$.
Hence its cellular boundary is
\[
v-v=0.
\]
:::

<1>5. The cellular chain complex is therefore
\[
0
\longrightarrow
\ZZ^2
\xrightarrow{\ (2\ \ 2)\ }
\ZZ
\xrightarrow{\ 0\ }
\ZZ
\longrightarrow0.
\]
::: {.proof}
This is immediate from the cell counts in <1>2 and the boundary computations in <1>3 and <1>4.
:::

<1>6. The second homology group is
\[
\boxed{H_2(X;\ZZ)\cong\ZZ.}
\]
::: {.proof}
There are no $3$-cells, so
\[
H_2(X)=\ker d_2.
\]
From <1>5,
\[
\ker d_2
=\{(a,b)\in\ZZ^2:2a+2b=0\}
=\{(a,-a):a\in\ZZ\}
\cong\ZZ.
\]
:::

<1>7. The first homology group is
\[
\boxed{H_1(X;\ZZ)\cong\ZZ/2\ZZ.}
\]
::: {.proof}
Since $d_1=0$,
\[
H_1(X)
=\frac{\ker d_1}{\operatorname{im}d_2}
=\frac{\ZZ}{2\ZZ}.
\]
Indeed,
\[
\operatorname{im}d_2
=\{2a+2b:a,b\in\ZZ\}
=2\ZZ.
\]
:::

<1>8. Finally,
\[
\boxed{
H_i(X;\ZZ)
\cong
\begin{cases}
\ZZ, & i=0,2,\\
\ZZ/2\ZZ, & i=1,\\
0, & i\ge3.
\end{cases}}
\]
::: {.proof}
The space has one $0$-cell and $d_1=0$, so
\[
H_0(X)\cong\ZZ.
\]
Steps <1>6 and <1>7 compute the remaining nonzero groups.
There are no cells in dimensions at least $3$, so the higher homology groups vanish.
:::
:::
