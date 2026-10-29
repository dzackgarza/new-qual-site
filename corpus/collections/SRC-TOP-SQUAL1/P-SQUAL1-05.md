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
$$
X=T^2\setminus\{x,y,z\}.
$$

::: pf

::: pf-step

Choose pairwise disjoint embedded closed disks
$$
D_x,D_y,D_z\subset T^2
$$
with
$$
x\in\operatorname{int}D_x,\qquad
y\in\operatorname{int}D_y,\qquad
z\in\operatorname{int}D_z.
$$


::: pf-proof

The three points are distinct, and the torus is Hausdorff and locally Euclidean, so sufficiently small coordinate disks around them can be chosen pairwise disjoint.

:::

:::

::: pf-step

Set
$$
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
$$
Then $\Sigma$ is a compact orientable surface of genus $1$ with three boundary components.


::: pf-proof

Removing three disjoint open disks from a torus preserves genus and creates one boundary circle for each removed disk.

:::

:::

::: pf-step

The punctured torus $X$ deformation retracts onto $\Sigma$.


::: pf-proof

Inside each punctured disk
$$
D_x\setminus\{x\},
$$
use radial coordinates centered at $x$ and push every point radially outward to $\partial D_x$, fixing the boundary. Do the same independently in $D_y\setminus\{y\}$ and $D_z\setminus\{z\}$, and fix every point outside the three disks. Because the disks are disjoint, these three radial homotopies paste together to a deformation retraction
$$
X\to\Sigma.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\pi_1(X)\cong\pi_1(\Sigma)}.
$$


::: pf-proof

Deformation retracts are homotopy equivalences and hence induce isomorphisms on fundamental groups.

:::

:::

::: pf-step

The standard polygon decomposition of $\Sigma$ gives
$$
\boxed{
\pi_1(\Sigma)
\cong
\left\langle
a,b,c_1,c_2,c_3
\ \middle|\
[a,b]c_1c_2c_3=1
\right\rangle}.
$$


::: pf-proof

Cut $\Sigma$ along the handle loops $a,b$ and along arcs from the basepoint to the three boundary components. The result is a disk. Reading the oriented boundary of this disk yields the word
$$
aba^{-1}b^{-1}c_1c_2c_3
=
[a,b]c_1c_2c_3.
$$
Equivalently, the resulting CW structure has one $0$-cell, five $1$-cells $a,b,c_1,c_2,c_3$, and one $2$-cell attached by that word. Seifert--van Kampen gives the displayed presentation.

:::

:::

::: pf-step

The relator is equivalent to
$$
\boxed{
c_3
=
c_2^{-1}c_1^{-1}[a,b]^{-1}}.
$$


::: pf-proof

From
$$
[a,b]c_1c_2c_3=1,
$$
multiply on the left by
$$
c_2^{-1}c_1^{-1}[a,b]^{-1}.
$$

:::

:::

::: pf-step

Hence the generator $c_3$ can be eliminated from the presentation.


::: pf-proof

The single defining relation expresses $c_3$ uniquely as a word in $a,b,c_1,c_2$. A Tietze transformation therefore removes both $c_3$ and the relator.

:::

:::

::: {.pf-step #s1-8}

Thus
$$
\boxed{
\pi_1(\Sigma)
\cong
\langle a,b,c_1,c_2\mid\ \rangle
\cong
F_4}.
$$


::: pf-proof

After eliminating $c_3$, the presentation has four generators and no relations, which is the free group of rank $4$.

:::

:::

::: {.pf-step #s1-9}

Consequently,
$$
\boxed{
\pi_1\bigl(T^2\setminus\{x,y,z\}\bigr)
\cong
F_4}.
$$


::: pf-proof

Combine steps [](#s1-4){.pf-ref} and [](#s1-8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is the required computation.

:::

:::

:::
