---
schema: qual/card@1
id: P-UCTOP-SU11-8
kind: problem
title: Homology of lens glued with 120-degree twist
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Let $L$ be a solid 3-dimensional lens (a flattened ball).
Identify the top and bottom surfaces via vertical translation and a twist of 120 degrees.
Calculate the integral homology of the resulting space.

::: {.solution}
<1>1. The space $X$ is homeomorphic to the 3-dimensional lens space $L(3, 1)$.
Proof: the standard cell decomposition of the lens space $L(p, q)$ with $p = 3, q = 1$ is obtained by identifying the upper and lower hemisphere disks of the 3-ball via a $2\pi/3 = 120^\circ$ rotation.

<1>2. Build a CW complex structure on $X$.
<2>1. Subdivide the equatorial circle $S^1 = \partial D^2$ into 3 1-cells connecting 3 0-cells at angles $0, 2\pi/3, 4\pi/3$.
Proof: subdivision of the boundary.
<2>2. Under the $120^\circ$ rotation identification, all 3 vertices are identified to a single 0-cell $e^0$, and all 3 boundary edges are identified to a single 1-cell $e^1$.
Proof: the rotation acts transitively on the 3 vertices and 3 edges.
<2>3. The top and bottom 2-dimensional hemispherical disks are identified to a single 2-cell $e^2$.
Proof: gluing map identifies top and bottom faces.
<2>4. The interior of the solid 3-ball forms a single 3-cell $e^3$.
Proof: the 3-ball has dimension 3. <2>5. The cellular chain groups are:
\[
C_3(X) = \mathbb{Z}e^3,\quad C_2(X) = \mathbb{Z}e^2,\quad C_1(X) = \mathbb{Z}e^1,\quad C_0(X) = \mathbb{Z}e^0,\quad C_k(X) = 0 \text{ for } k \ge 4.
\]
Proof: one cell in each dimension $0, 1, 2, 3$.

<1>3. Compute the cellular boundary maps: <2>1. $d_1: C_1(X) \to C_0(X)$ is $d_1(e^1) = e^0 - e^0 = 0$.
Proof: the 1-cell is a closed loop starting and ending at $e^0$.
<2>2. $d_2: C_2(X) \to C_1(X)$ is $d_2(e^2) = 3e^1$.
Proof: the boundary of the 2-cell traverses the equatorial circle, which consists of 3 identified copies of $e^1$ oriented in the same direction.
<2>3. $d_3: C_3(X) \to C_2(X)$ is $d_3(e^3) = 0$.
Proof: $\partial e^3 = D^2_{\text{top}} - D^2_{\text{bot}} = e^2 - e^2 = 0$ (the identification matches the two disks with opposite outward normal orientations).

<1>4. Compute the homology groups $H_k(X) = \ker(d_k)/\operatorname{im}(d_{k+1})$: <2>1. $H_0(X) = \ker(d_0)/\operatorname{im}(d_1) = \mathbb{Z}e^0 / 0 \cong \mathbb{Z}$.
Proof: $\ker(d_0) = \mathbb{Z}$ and $d_1 = 0$.
<2>2. $H_1(X) = \ker(d_1)/\operatorname{im}(d_2) = \mathbb{Z}e^1 / (3\mathbb{Z}e^1) \cong \mathbb{Z}/3\mathbb{Z}$.
Proof: $\ker(d_1) = \mathbb{Z}$ and $\operatorname{im}(d_2) = 3\mathbb{Z}$.
<2>3. $H_2(X) = \ker(d_2)/\operatorname{im}(d_3) = 0 / 0 \cong 0$.
Proof: $\ker(d_2) = \{n \in \mathbb{Z} : 3n = 0\} = 0$.
<2>4. $H_3(X) = \ker(d_3)/\operatorname{im}(d_4) = \mathbb{Z}e^3 / 0 \cong \mathbb{Z}$.
Proof: $\ker(d_3) = \mathbb{Z}$ and $C_4(X) = 0$.
<2>5. $H_k(X) = 0$ for all $k \ge 4$.
Proof: $C_k(X) = 0$ for $k \ge 4$.

<1>5. Conclusion:
\[
H_k(X; \mathbb{Z}) \cong \begin{cases}
\mathbb{Z} & k = 0, \\
\mathbb{Z}/3\mathbb{Z} & k = 1, \\
0 & k = 2, \\
\mathbb{Z} & k = 3, \\
0 & k \ge 4.
\end{cases}
\]
Q.E.D. Proof: <1>4.
:::
