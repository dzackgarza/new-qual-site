---
schema: qual/card@1
id: P-SQUAL1-05
kind: problem
title: Fundamental group of a torus punctured at three points
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $x,y,z$ be three distinct points of the $2$-torus $T^2$.
Compute
$$\pi_1\bigl(T^2\setminus\{x,y,z\}\bigr).$$
:::

::: {.solution}
Let
\[
X=T^2\setminus\{x,y,z\}.
\]

<1>1. Choose pairwise disjoint embedded closed disks
\[
D_x,D_y,D_z\subset T^2
\]
with
\[
x\in\operatorname{int}D_x,\qquad
y\in\operatorname{int}D_y,\qquad
z\in\operatorname{int}D_z.
\]

::: {.proof}
The three points are distinct, and the torus is Hausdorff and locally Euclidean, so sufficiently small coordinate disks around them can be chosen pairwise disjoint.
:::

<1>2. Set
\[
\Sigma
=
T^2\setminus
\left(
\operatorname{int}D_x
\cup
\operatorname{int}D_y
\cup
\operatorname{int}D_z
\right).
\]
Then \(\Sigma\) is a compact orientable surface of genus \(1\) with three boundary components.

::: {.proof}
Removing three disjoint open disks from a torus preserves genus and creates one boundary circle for each removed disk.
:::

<1>3. The punctured torus \(X\) deformation retracts onto \(\Sigma\).

::: {.proof}
Inside each punctured disk
\[
D_x\setminus\{x\},
\]
use radial coordinates centered at \(x\) and push every point radially outward to \(\partial D_x\), fixing the boundary. Do the same independently in \(D_y\setminus\{y\}\) and \(D_z\setminus\{z\}\), and fix every point outside the three disks. Because the disks are disjoint, these three radial homotopies paste together to a deformation retraction
\[
X\to\Sigma.
\]
:::

<1>4. Therefore
\[
\boxed{
\pi_1(X)\cong\pi_1(\Sigma)}.
\]

::: {.proof}
Deformation retracts are homotopy equivalences and hence induce isomorphisms on fundamental groups.
:::

Choose a basepoint on \(\Sigma\). Let
\[
a,b
\]
be the two standard handle loops, and let
\[
c_1,c_2,c_3
\]
be positively oriented loops around the three boundary components.

<1>5. The standard polygon decomposition of \(\Sigma\) gives
\[
\boxed{
\pi_1(\Sigma)
\cong
\left\langle
a,b,c_1,c_2,c_3
\ \middle|\
[a,b]c_1c_2c_3=1
\right\rangle}.
\]

::: {.proof}
Cut \(\Sigma\) along the handle loops \(a,b\) and along arcs from the basepoint to the three boundary components. The result is a disk. Reading the oriented boundary of this disk yields the word
\[
aba^{-1}b^{-1}c_1c_2c_3
=
[a,b]c_1c_2c_3.
\]
Equivalently, the resulting CW structure has one \(0\)-cell, five \(1\)-cells \(a,b,c_1,c_2,c_3\), and one \(2\)-cell attached by that word. Seifert--van Kampen gives the displayed presentation.
:::

<1>6. The relator is equivalent to
\[
\boxed{
c_3
=
c_2^{-1}c_1^{-1}[a,b]^{-1}}.
\]

::: {.proof}
From
\[
[a,b]c_1c_2c_3=1,
\]
multiply on the left by
\[
c_2^{-1}c_1^{-1}[a,b]^{-1}.
\]
:::

<1>7. Hence the generator \(c_3\) can be eliminated from the presentation.

::: {.proof}
The single defining relation expresses \(c_3\) uniquely as a word in \(a,b,c_1,c_2\). A Tietze transformation therefore removes both \(c_3\) and the relator.
:::

<1>8. Thus
\[
\boxed{
\pi_1(\Sigma)
\cong
\langle a,b,c_1,c_2\mid\ \rangle
\cong
F_4}.
\]

::: {.proof}
After eliminating \(c_3\), the presentation has four generators and no relations, which is the free group of rank \(4\).
:::

<1>9. Consequently,
\[
\boxed{
\pi_1\bigl(T^2\setminus\{x,y,z\}\bigr)
\cong
F_4}.
\]

::: {.proof}
Combine steps <1>4 and <1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required computation.
:::
:::
