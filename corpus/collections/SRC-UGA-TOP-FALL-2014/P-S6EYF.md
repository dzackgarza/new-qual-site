---
schema: qual/card@1
id: P-S6EYF
kind: problem
title: Integral homology of the union of the unit sphere and the ellipsoid $x^2+y^2+z^2/4=1$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 6 of the official UGA Fall 2014 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Corrected H_1 from Z to 0; the previous Mayer-Vietoris calculation misread exactness after the map H_1(S^1) to H_1(S^2) plus H_1(S^2). Retained and justified H_2 isomorphic to Z^3.
---

::: problem
Compute the integral homology groups $H_k(X; \mathbb{Z})$ of the space $X = Y \cup Z \subset \mathbb{R}^3$, where $Y$ is the sphere
$$
Y = \{ (x, y, z) \in \mathbb{R}^3 \mid x^2 + y^2 + z^2 = 1 \}
$$
and $Z$ is the ellipsoid
$$
Z = \left\{ (x, y, z) \in \mathbb{R}^3 \;\middle|\; x^2 + y^2 + \frac{z^2}{4} = 1 \right\}.
$$
:::

::: solution
<1>1. The two surfaces are both homeomorphic to $S^2$, and their intersection is the common equatorial circle.
::: {.proof}
The unit sphere
\[
Y=\{x^2+y^2+z^2=1\}
\]
is $S^2$.
The linear map
\[
(x,y,z)\longmapsto(x,y,2z)
\]
maps the unit sphere homeomorphically onto
\[
Z=\left\{x^2+y^2+\frac{z^2}{4}=1\right\},
\]
so $Z\cong S^2$ as well.

If a point lies in $Y\cap Z$, subtracting the two defining equations gives
\[
z^2-\frac{z^2}{4}=0,
\]
hence
\[
z=0.
\]
Substitution then gives
\[
x^2+y^2=1.
\]
Therefore
\[
A:=Y\cap Z
=
\{(x,y,0):x^2+y^2=1\}
\cong S^1.
\]
:::

<1>2. Mayer--Vietoris applies to the decomposition
\[
X=Y\cup Z
\]
with intersection $A\cong S^1$.
::: {.proof}
Give the common equator $A$ its standard CW structure with one $0$-cell and one $1$-cell.
Each of the upper and lower hemispheres of $Y$ is then a $2$-cell attached along $A$, and the same is true for the upper and lower halves of $Z$.
Thus $X$ is a CW complex for which $Y$, $Z$, and $A=Y\cap Z$ are subcomplexes.
The Mayer--Vietoris sequence for a union of CW subcomplexes therefore gives
\[
\cdots
\longrightarrow
\widetilde H_k(A)
\longrightarrow
\widetilde H_k(Y)\oplus\widetilde H_k(Z)
\longrightarrow
\widetilde H_k(X)
\longrightarrow
\widetilde H_{k-1}(A)
\longrightarrow\cdots.
\]
By <1>1,
\[
\widetilde H_k(A)
\cong
\begin{cases}
\mathbb Z,&k=1,\\
0,&k\ne1,
\end{cases}
\]
and
\[
\widetilde H_k(Y)\oplus\widetilde H_k(Z)
\cong
\begin{cases}
\mathbb Z^2,&k=2,\\
0,&k\ne2.
\end{cases}
\]
:::

<1>3. One has
\[
H_k(X;\mathbb Z)=0
\qquad(k\ge3).
\]
::: {.proof}
For $k\ge3$, the relevant Mayer--Vietoris terms from <1>2 are
\[
0
\longrightarrow
\widetilde H_k(X)
\longrightarrow
0.
\]
Hence
\[
\widetilde H_k(X)=0
\]
for every $k\ge3$.
:::

<1>4. The second homology group is
\[
H_2(X;\mathbb Z)\cong\mathbb Z^3.
\]
::: {.proof}
The relevant part of the reduced Mayer--Vietoris sequence is
\[
0
\longrightarrow
\mathbb Z^2
\longrightarrow
\widetilde H_2(X)
\xrightarrow{\partial}
\mathbb Z
\longrightarrow
0.
\]
Exactness gives a short exact sequence
\[
0
\longrightarrow
\mathbb Z^2
\longrightarrow
\widetilde H_2(X)
\longrightarrow
\mathbb Z
\longrightarrow
0.
\]
Because the quotient $\mathbb Z$ is free abelian, this sequence splits.
Therefore
\[
\widetilde H_2(X)
\cong
\mathbb Z^2\oplus\mathbb Z
\cong
\mathbb Z^3.
\]
Since degree $2$ is positive, reduced and unreduced homology agree there.
:::

<1>5. The first homology group is
\[
H_1(X;\mathbb Z)=0.
\]
::: {.proof}
Continuing the same exact sequence from <1>4 gives
\[
\mathbb Z
\longrightarrow
0
\longrightarrow
\widetilde H_1(X)
\longrightarrow
0.
\]
Exactness at $\widetilde H_1(X)$ says
\[
\operatorname{im}\bigl(0\to\widetilde H_1(X)\bigr)
=
\ker\bigl(\widetilde H_1(X)\to0\bigr).
\]
The left-hand side is $0$, while the right-hand side is all of $\widetilde H_1(X)$.
Hence
\[
\widetilde H_1(X)=0.
\]
This is precisely the step that the previous solution misread.
:::

<1>6. Finally,
\[
H_0(X;\mathbb Z)\cong\mathbb Z.
\]
::: {.proof}
Both $Y$ and $Z$ are path connected, and their intersection $A\cong S^1$ is nonempty.
Therefore their union $X$ is path connected, so
\[
H_0(X;\mathbb Z)\cong\mathbb Z.
\]
:::

<1>7. Thus the integral homology groups are
\[
\boxed{
H_k(X;\mathbb Z)
\cong
\begin{cases}
\mathbb Z,&k=0,\\
0,&k=1,\\
\mathbb Z^3,&k=2,\\
0,&k\ge3.
\end{cases}}
\]
::: {.proof}
Combine <1>3--<1>6.
:::
:::
