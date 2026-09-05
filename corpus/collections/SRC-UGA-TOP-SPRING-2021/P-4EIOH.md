---
schema: qual/card@1
id: P-4EIOH
kind: problem
title: Fundamental group and homology of the theta graph and of three disks on a circle
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked both parts against problem 6 of the official UGA Spring 2021 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Verified the theta-graph maximal-tree collapse and the cellular chain
    complex for the three degree-one 2-cell attachments.
---

::: {.problem}
For each of the following spaces, compute the fundamental group and the homology groups.

a. The graph $\Theta$ consisting of two vertices and three edges connecting them.

b. The 2-dimensional cell complex $\Theta_2$ consisting of a closed circle and three 2-dimensional disks each having boundary running once around that circle.
:::

::: {.solution}
<1>1. The theta graph $\Theta$ is homotopy equivalent to $S^1\vee S^1$.
::: {.proof}
Choose one of the three edges of $\Theta$.
Together with the two vertices, this edge is a maximal tree $T\subseteq\Theta$.
Collapsing a maximal tree in a connected graph is a homotopy equivalence, and the quotient collapses the two vertices to one while the two remaining edges become loops.
Hence
\[
\Theta\simeq \Theta/T\cong S^1\vee S^1.
\]
:::

<1>2. Therefore
\[
\pi_1(\Theta)\cong F_2,
\]
the free group on two generators.
::: {.proof}
By <1>1 and homotopy invariance of the fundamental group,
\[
\pi_1(\Theta)
\cong
\pi_1(S^1\vee S^1)
\cong F_2.
\]
:::

<1>3. The homology of $\Theta$ is
\[
H_k(\Theta;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ^2,&k=1,\\
0,&k\ge2.
\end{cases}
\]
::: {.proof}
Give $S^1\vee S^1$ its CW structure with one $0$-cell and two $1$-cells.
Its cellular chain complex is
\[
0\longrightarrow \ZZ^2
\xrightarrow{0}
\ZZ
\longrightarrow0.
\]
Taking homology and using <1>1 gives the displayed groups.
:::

<1>4. Give $\Theta_2$ a CW structure with one $0$-cell, one $1$-cell, and three $2$-cells.
::: {.proof}
Use the given circle as the $1$-skeleton, with one vertex and one open edge.
Each of the three disks is a $2$-cell whose attaching map
\[
S^1\longrightarrow S^1
\]
runs once around the $1$-skeleton, hence has degree $\pm1$.
Orient each $2$-cell so that this degree is $+1$.
Thus the cellular chain groups are
\[
C_2\cong\ZZ^3,
\qquad
C_1\cong\ZZ,
\qquad
C_0\cong\ZZ.
\]
:::

<1>5. In these orientations the cellular boundary maps are
\[
d_2:\ZZ^3\longrightarrow\ZZ,
\qquad
d_2(r,s,t)=r+s+t,
\]
and
\[
d_1=0.
\]
::: {.proof}
For a $2$-cell attached to a single $1$-cell, the cellular boundary coefficient is the degree of its attaching map.
By <1>4 all three degrees are $+1$, giving the formula for $d_2$.
Since the unique $1$-cell begins and ends at the unique $0$-cell, its cellular boundary is zero, so $d_1=0$.
:::

<1>6. The homology of $\Theta_2$ is
\[
H_k(\Theta_2;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
0,&k=1,\\
\ZZ^2,&k=2,\\
0,&k\ge3.
\end{cases}
\]
::: {.proof}
The map $d_2$ in <1>5 is surjective, so
\[
H_1(\Theta_2)
=\ker d_1/\operatorname{im}d_2
=\ZZ/\ZZ
=0.
\]
Also
\[
H_2(\Theta_2)
=\ker d_2
=\{(r,s,t)\in\ZZ^3:r+s+t=0\}
\cong\ZZ^2,
\]
for example with basis
\[
(1,-1,0),
\qquad
(1,0,-1).
\]
The space is connected, so $H_0\cong\ZZ$, and there are no cells above dimension $2$.
:::

<1>7. The fundamental group of $\Theta_2$ is trivial.
::: {.proof}
The $1$-skeleton has fundamental group
\[
\pi_1(S^1)=\langle a\rangle.
\]
Attaching any one of the three $2$-cells along a loop of degree $\pm1$ imposes the relation
\[
a^{\pm1}=1.
\]
By Seifert--van Kampen, after all three attachments
\[
\pi_1(\Theta_2)
\cong
\langle a\mid a,a,a\rangle
=\{e\},
\]
after choosing the orientations from <1>4.
:::
:::
