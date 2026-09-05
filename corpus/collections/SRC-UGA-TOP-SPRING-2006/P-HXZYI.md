---
schema: qual/card@1
id: P-HXZYI
kind: problem
title: Fundamental group, Euler characteristic, and homology of $S^2$ with $k$ points
  identified
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Euler Characteristic
  - Quotient Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked all three requested invariants against problem 8 of the official UGA Spring 2006 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Identified the quotient as S^2/A for a k-point subspace A and used the
    mapping-cone equivalence X/A ≃ X ∨ SA for a nullhomotopic CW subspace.
    Since SA is a graph with two vertices and k parallel edges, it is homotopy
    equivalent to a wedge of k-1 circles. This gives pi_1 = F_{k-1},
    chi = 3-k, H_1 = Z^{k-1}, H_2 = Z, and no higher homology. The quotient
    equivalence is Hatcher, Algebraic Topology, Example 0.14.
---

::: problem
Let $X = S^2 / \theset{p_1 = \cdots = p_k }$ be the topological space obtained from the 2-sphere by identifying $k$ distinct points on it ($k \geq 2$).

Find:

a. The fundamental group of $X$.

b. The Euler characteristic of $X$.

c. The homology groups of $X$.
:::

::: {.solution}
Let
\[
A=\{p_1,\ldots,p_k\}\subset S^2.
\]
Then the given space is the quotient
\[
X=S^2/A,
\]
where all of $A$ is collapsed to one point.

<1>1. There is a homotopy equivalence
\[
X\simeq S^2\vee SA,
\]
where $SA$ denotes the suspension of the $k$-point space $A$.
::: {.proof}
Choose a CW structure on $S^2$ in which the finitely many points $p_1,\ldots,p_k$ are $0$-cells, so $(S^2,A)$ is a CW pair.

The inclusion
\[
A\hookrightarrow S^2
\]
is nullhomotopic.
Indeed, for each $i$ choose a path in $S^2$ from $p_i$ to $p_1$.
Since $A$ is a finite discrete space, these paths together define a homotopy of the inclusion $A\hookrightarrow S^2$ to the constant map with value $p_1$.

For a CW pair $(Y,B)$ whose inclusion $B\hookrightarrow Y$ is nullhomotopic, the quotient $Y/B$ is homotopy equivalent to
\[
Y\vee SB.
\]
Applying this with $(Y,B)=(S^2,A)$ gives the claim.
:::

<1>2. The suspension $SA$ is homotopy equivalent to a wedge of $k-1$ circles.
::: {.proof}
Because $A$ consists of $k$ points, $SA$ is the graph having two suspension vertices and one edge between them for each point of $A$.
Thus it has two vertices and $k$ parallel edges.

Choose one of these edges as a maximal tree and collapse it.
Collapsing a maximal tree in a connected graph is a homotopy equivalence, and the remaining $k-1$ edges become loops at the single vertex.
Hence
\[
SA\simeq\bigvee^{k-1}S^1.
\]
:::

<1>3. Consequently
\[
X\simeq S^2\vee\bigvee^{k-1}S^1.
\]
::: {.proof}
Combine <1>1 and <1>2.
:::

<1>4. The fundamental group is
\[
\boxed{\pi_1(X)\cong F_{k-1}},
\]
the free group on $k-1$ generators.
::: {.proof}
By <1>3 and homotopy invariance of the fundamental group,
\[
\pi_1(X)
\cong
\pi_1\left(S^2\vee\bigvee^{k-1}S^1\right).
\]
The sphere is simply connected, and van Kampen's theorem identifies the fundamental group of the wedge with the free product of the fundamental groups of its summands.
Therefore
\[
\pi_1(X)
\cong
\underbrace{\ZZ*\cdots*\ZZ}_{k-1\text{ factors}}
\cong F_{k-1}.
\]
:::

<1>5. The Euler characteristic is
\[
\boxed{\chi(X)=3-k}.
\]
::: {.proof}
The wedge in <1>3 has a CW structure with one $0$-cell, $k-1$ $1$-cells, and one $2$-cell.
Hence
\[
\chi(X)
=1-(k-1)+1
=3-k.
\]
Euler characteristic is invariant under homotopy equivalence for finite CW complexes.
:::

<1>6. The integral homology groups are
\[
\boxed{
H_n(X;\ZZ)\cong
\begin{cases}
\ZZ,&n=0,\\
\ZZ^{k-1},&n=1,\\
\ZZ,&n=2,\\
0,&n\ge3.
\end{cases}}
\]
::: {.proof}
Use the CW structure from <1>5. Its cellular chain complex is
\[
0\longrightarrow\ZZ
\xrightarrow{0}
\ZZ^{k-1}
\xrightarrow{0}
\ZZ
\longrightarrow0.
\]
The $1$-cells are loops at the unique $0$-cell, so the degree-$1$ cellular boundary is zero.
The $2$-cell is the $2$-cell of the $S^2$ summand and is attached at the wedge point, so its cellular boundary is also zero.
Taking homology gives the displayed groups.
:::
:::
