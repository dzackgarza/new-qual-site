---
schema: qual/card@1
id: P-A3ZPA
kind: problem
title: Presentation of $\pi_1(\Sigma_2)$, a surjection onto $F_2$, and no covering
  $\Sigma_2\to S^1\times S^1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Surfaces
  - Groups
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked all three parts against problem 4 of the official UGA Spring 2018 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified that the free-group quotient respects the surface relator and that covering-space injectivity contradicts nonabelianity.
---

::: problem
(a) Write down (without proof) a presentation for $\pi_1(\Sigma_2,p)$, where $\Sigma_2$ is a closed, connected, orientable genus $2$ surface and $p$ is any point in $\Sigma_2$.

(b) Show that $\pi_1(\Sigma_2,p)$ is not abelian by showing that it surjects onto a free group of rank $2$.

(c) Show that there is no covering space map from $\Sigma_2$ to $S^1\times S^1$.
You may use the fact that $\pi_1(S^1\times S^1)\cong\ZZ^2$ together with the result in part (b).
:::

::: {.solution}
<1>1. A standard presentation is
\[
\pi_1(\Sigma_2,p)
\cong
\left\langle
 a_1,b_1,a_2,b_2
\mathrel{\Big|}
[a_1,b_1][a_2,b_2]=1
\right\rangle.
\]
::: {.proof}
This is the requested presentation in part (a); no proof is required there.
:::

<1>2. There is a surjective homomorphism
\[
\pi_1(\Sigma_2,p)\twoheadrightarrow F(x,y),
\]
where $F(x,y)$ is the free group of rank $2$.
::: {.proof}
Define a map on the generators in <1>1 by
\[
a_1\longmapsto x,
\qquad
b_1\longmapsto y,
\qquad
a_2\longmapsto y,
\qquad
b_2\longmapsto x.
\]
The defining relator maps to
\[
[x,y][y,x]
=[x,y][x,y]^{-1}
=1,
\]
so the assignment descends to a homomorphism
\[
\varphi:\pi_1(\Sigma_2,p)\longrightarrow F(x,y).
\]
Its image contains both $x=\varphi(a_1)$ and $y=\varphi(b_1)$, so $\varphi$ is surjective.
:::

<1>3. The group $\pi_1(\Sigma_2,p)$ is not abelian.
::: {.proof}
Every quotient of an abelian group is abelian.
But $F(x,y)$ is nonabelian, since the reduced words
\[
xy
\qquad\text{and}\qquad
yx
\]
are distinct.
By <1>2, $F(x,y)$ is a quotient of $\pi_1(\Sigma_2,p)$.
Therefore $\pi_1(\Sigma_2,p)$ cannot be abelian.
:::

<1>4. There is no covering map
\[
q:\Sigma_2\longrightarrow S^1\times S^1.
\]
::: {.proof}
Suppose such a covering map existed, and choose the base point $p\in\Sigma_2$ with $q(p)=z_0$.
A covering map induces an injective homomorphism on fundamental groups, so
\[
q_*:\pi_1(\Sigma_2,p)
\hookrightarrow
\pi_1(S^1\times S^1,z_0)
\cong\ZZ^2.
\]
Every subgroup of an abelian group is abelian.
Thus injectivity of $q_*$ would force $\pi_1(\Sigma_2,p)$ to be abelian, contradicting <1>3.
Hence no such covering map exists.
:::
:::
