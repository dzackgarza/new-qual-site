---
schema: qual/card@1
id: P-IT3OF
kind: problem
title: Fundamental group and homology of a $2$-cell attached to $S^1$ by $z\mapsto
  z^n$, and which $X_n$ is a surface
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Fundamental Group
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked van Kampen, the cellular boundary, the surface-classification exclusion, and the explicit RP2 quotient model.
---

::: problem
For any integer $n \geq 2$ let $X_n$ denote the space formed by attaching a 2-cell to the circle $S^1$ via the attaching map
\[
\begin{aligned}
a_n:S^1&\longrightarrow S^1,\\
e^{i\theta}&\longmapsto e^{in\theta}.
\end{aligned}
\]

Compute the fundamental group and the homology of $X_n$.

Exactly one of the $X_n$ (for $n \geq 2$) is homeomorphic to a surface.
Identify, with proof, both this value of $n$ and the surface that $X_n$ is homeomorphic to (including a description of the homeomorphism).
:::

::: {.solution}
<1>1. The space \(X_n\) has a CW structure with one cell in each of dimensions \(0,1,2\), where the \(2\)-cell is attached to the \(1\)-skeleton \(S^1\) by a degree-\(n\) map.
::: {.proof}
Start with the usual CW structure
\[
S^1=e^0\cup e^1.
\]
The definition of \(X_n\) attaches one \(2\)-cell along
\[
a_n(z)=z^n,
\]
whose degree is \(n\). Hence
\[
X_n=e^0\cup e^1\cup_{a_n}e^2.
\]
:::

<1>2. The fundamental group is
\[
\boxed{\pi_1(X_n)\cong\mathbb Z/n\mathbb Z}.
\]
::: {.proof}
The \(1\)-skeleton is \(S^1\), so
\[
\pi_1(S^1)\cong\langle a\rangle\cong\mathbb Z.
\]
Attaching a \(2\)-cell along a loop kills the normal closure of the homotopy class of its attaching map.
Since \(a_n\) has degree \(n\), its class in \(\pi_1(S^1)\) is \(a^n\). Seifert--van Kampen therefore gives
\[
\pi_1(X_n)
\cong
\langle a\mid a^n=1\rangle
\cong
\mathbb Z/n\mathbb Z.
\]
:::

<1>3. The cellular chain complex is
\[
0
\longrightarrow
\mathbb Z
\xrightarrow{\;n\;}
\mathbb Z
\xrightarrow{\;0\;}
\mathbb Z
\longrightarrow0.
\]
::: {.proof}
By <1>1, the cellular chain groups are
\[
C_2(X_n)\cong C_1(X_n)\cong C_0(X_n)\cong\mathbb Z.
\]
The \(1\)-cell begins and ends at the unique \(0\)-cell, so \(\partial_1=0\). For a single \(2\)-cell attached to \(S^1\), the cellular boundary \(\partial_2\) is multiplication by the degree of the attaching map.
Since
\[
\deg(a_n)=n,
\]
one has \(\partial_2(m)=nm\).
:::

<1>4. The integral homology of \(X_n\) is
\[
\boxed{
H_k(X_n;\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z/n\mathbb Z,&k=1,\\
0,&k\ge2.
\end{cases}}
\]
::: {.proof}
From <1>3,
\[
H_0(X_n)=\mathbb Z/\operatorname{im}\partial_1\cong\mathbb Z,
\]
\[
H_1(X_n)
=
\ker\partial_1/\operatorname{im}\partial_2
\cong
\mathbb Z/n\mathbb Z,
\]
and, because \(n\ne0\), multiplication by \(n\) on \(\mathbb Z\) is injective, so
\[
H_2(X_n)=\ker\partial_2=0.
\]
There are no cells in dimensions above \(2\).
:::

<1>5. The Euler characteristic is
\[
\chi(X_n)=1.
\]
::: {.proof}
The CW structure in <1>1 has one \(0\)-cell, one \(1\)-cell, and one \(2\)-cell.
Therefore
\[
\chi(X_n)=1-1+1=1.
\]
:::

<1>6. If \(X_n\) is homeomorphic to a surface, then that surface is \(\mathbb{RP}^2\).
::: {.proof}
The space \(X_n\) is a finite connected CW complex, hence compact and connected.
Thus any surface homeomorphic to it is a compact connected surface.

Allowing surfaces with boundary, the classification theorem gives
\[
\chi(M)=2-2g-b
\]
for an orientable surface of genus \(g\) with \(b\) boundary components, and
\[
\chi(M)=2-k-b
\]
for a nonorientable surface of genus \(k\ge1\) with \(b\) boundary components.
By <1>5, \(\chi(M)=1\). In the orientable case this forces
\[
2g+b=1,
\]
so \(M\cong D^2\). In the nonorientable case it forces
\[
k+b=1,
\]
so \(M\cong\mathbb{RP}^2\).

But <1>4 gives
\[
H_1(X_n;\mathbb Z)\cong\mathbb Z/n\mathbb Z\ne0,
\]
whereas \(H_1(D^2;\mathbb Z)=0\). Hence the disk is impossible, and the only possible surface is \(\mathbb{RP}^2\).
:::

<1>7. Consequently, if \(X_n\) is a surface, then
\[
n=2.
\]
::: {.proof}
By <1>6, such an \(X_n\) must be homeomorphic to \(\mathbb{RP}^2\). Homology is a homeomorphism invariant, and
\[
H_1(\mathbb{RP}^2;\mathbb Z)
\cong
\mathbb Z/2\mathbb Z.
\]
Comparing with <1>4,
\[
\mathbb Z/n\mathbb Z
\cong
\mathbb Z/2\mathbb Z,
\]
which for \(n\ge2\) forces \(n=2\).
:::

<1>8. The space \(X_2\) is homeomorphic to \(\mathbb{RP}^2\).
::: {.proof}
Use the standard disk model
\[
\mathbb{RP}^2
\cong
D^2/\bigl(z\sim -z\text{ for }z\in\partial D^2=S^1\bigr).
\]
Let
\[
q:S^1\to S^1,
\qquad
q(z)=z^2.
\]
Then
\[
q(z)=q(w)
\quad\Longleftrightarrow\quad
w=z\text{ or }w=-z.
\]
Thus \(q\) is exactly the quotient map of the boundary circle by the antipodal relation, after identifying the quotient circle with \(S^1\).

More explicitly, if \(r:D^2\to D^2/(z\sim-z)\) is the quotient map, define
\[
j:S^1\to r(S^1)
\]
by
\[
j(w)=r(z)
\qquad\text{for any }z\in S^1\text{ with }z^2=w.
\]
This is well-defined because the two square roots are antipodal.
The induced map
\[
S^1/(z\sim-z)\longrightarrow S^1,
\qquad
[z]\longmapsto z^2
\]
is a continuous bijection from a compact space to the Hausdorff circle, hence a homeomorphism; therefore \(j\) is continuous.

Now define a map on the disjoint union used to form \(X_2\): on the disk use \(r\), and on the attached circle use \(j\). For every boundary point \(z\in S^1\),
\[
r(z)=j(z^2)=j(a_2(z)),
\]
so the map is constant on the identifications defining \(X_2\). It therefore descends to a continuous bijection
\[
X_2\longrightarrow D^2/(z\sim-z).
\]
The space $X_2$ is compact, and the disk quotient is the Hausdorff space $\mathbb{RP}^2$, so this continuous bijection is a homeomorphism.
Composing with the standard disk-model homeomorphism gives
\[
\boxed{X_2\cong\mathbb{RP}^2}.
\]
:::

<1>9. Therefore exactly one \(X_n\) is a surface:
\[
\boxed{n=2,\qquad X_2\cong\mathbb{RP}^2}.
\]
::: {.proof}
Necessity is <1>7 and existence, with an explicit homeomorphism, is <1>8.
:::
:::
