---
schema: qual/card@1
id: P-AMD-ZO6DF2Q5
kind: problem
title: Fundamental groups of punctured Euclidean spaces, spherical quotients, and
  the Hopf link complement
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Write down the fundamental group of the following spaces:

1. $\mathbb{R}^2 - \{0, 1\}$

2. $\mathbb{R}^2 - I$

3. The symbol $\oplus \in \mathbb{R}^2$

4. $S^2 - \{p_i\}_{i=1}^4$

5. $T - \{p_0\}$

6. $S^2 / \mathbb{Z}_2$ via the antipodal map

7. $S^2/\mathbb{Z}_3$ via a $2\pi/3$ rotation about the $z$-axis.

8. $S_2 \cup \{(0,0,z) \mid -1 \leq z \leq 1 \}$

9. $\mathbb{R}^3 - \{ (x,y,0) \mid x^2 + y^2 = 1\}$

10. $\mathbb{R}^2 - H$, the Hopf link
:::

::: {.solution}
<1>1. Computation of fundamental groups for items 1 through 5:
<2>1. **Item 1: $\mathbb{R}^2 \setminus \{0, 1\}$**
The plane minus 2 points deformation retracts onto a figure-eight space $S^1 \vee S^1$.
Thus $\pi_1(\mathbb{R}^2 \setminus \{0, 1\}) \cong F_2 = \mathbb{Z} * \mathbb{Z}$.
Proof: deformation retraction of $\mathbb{R}^2 \setminus \{2 \text{ points}\}$ onto wedge of 2 circles.
<2>2. **Item 2: $\mathbb{R}^2 \setminus I$ (where $I = [0, 1]$)**
The closed interval $I$ is contractible and can be deformed to a single point $\{0\}$, so $\mathbb{R}^2 \setminus I \simeq \mathbb{R}^2 \setminus \{0\} \simeq S^1$.
Thus $\pi_1(\mathbb{R}^2 \setminus I) \cong \mathbb{Z}$.
Proof: homotopy equivalence of plane minus a segment with punctured plane.
<2>3. **Item 3: The symbol $\oplus \subset \mathbb{R}^2$**
The space $\oplus$ is a 1-dimensional CW complex (graph) consisting of 5 vertices (center $+ 4$ on circle) and 8 edges (4 circle arcs $+ 4$ spokes).
Its Euler characteristic is $\chi = 5 - 8 = -3$.
The fundamental group of any connected graph is free of rank $1 - \chi = 1 - (-3) = 4$.
Thus $\pi_1(\oplus) \cong F_4$.
Proof: fundamental group of finite connected graph.
<2>4. **Item 4: $S^2 \setminus \{p_1, p_2, p_3, p_4\}$**
Stereographic projection from $p_4$ gives a homeomorphism $S^2 \setminus \{p_1, p_2, p_3, p_4\} \cong \mathbb{R}^2 \setminus \{3 \text{ points}\} \simeq \bigvee^3 S^1$.
Thus $\pi_1(S^2 \setminus \{p_i\}_{i=1}^4) \cong F_3 = \mathbb{Z} * \mathbb{Z} * \mathbb{Z}$.
Proof: stereographic projection and deformation retraction.
<2>5. **Item 5: $T \setminus \{p_0\}$ (punctured torus)**
Removing a point from the standard 2-cell representation $T = I^2 / \sim$ deformation retracts the punctured 2-cell onto the 1-skeleton $S^1 \vee S^1$.
Thus $\pi_1(T \setminus \{p_0\}) \cong F_2 = \mathbb{Z} * \mathbb{Z}$.
Proof: deformation retraction onto 1-skeleton.

<1>2. Computation of fundamental groups for items 6 through 10:
<2>1. **Item 6: $S^2 / \mathbb{Z}_2$ via the antipodal map**
The quotient of $S^2$ under the antipodal identification is the real projective plane $\mathbb{RP}^2$, which has universal cover $S^2$.
Thus $\pi_1(S^2 / \mathbb{Z}_2) \cong \mathbb{Z}_2$.
Proof: covering space classification for $\mathbb{RP}^2$.
<2>2. **Item 7: $S^2 / \mathbb{Z}_3$ via rotation by $2\pi/3$ about the $z$-axis**
Viewing $S^2 \cong \Sigma S^1$, the $\mathbb{Z}_3$-action rotates each latitude circle and fixes the north and south poles.
The quotient space is homeomorphic to the suspension $\Sigma(S^1 / \mathbb{Z}_3) \cong \Sigma S^1 \cong S^2$.
Because $S^2$ is simply connected, $\pi_1(S^2 / \mathbb{Z}_3) \cong 0$.
Proof: suspension of a circle is homeomorphic to $S^2$.
<2>3. **Item 8: $S^2 \cup \{(0, 0, z) \mid -1 \le z \le 1\}$**
The space consists of $S^2$ with an interior diameter segment joining the poles.
Collapsing the contractible diameter segment to a point yields the wedge sum $S^2 \vee S^1$.
By the Seifert–van Kampen Theorem:
\[
\pi_1(S^2 \cup \text{segment}) \cong \pi_1(S^2 \vee S^1) \cong \pi_1(S^2) * \pi_1(S^1) \cong 0 * \mathbb{Z} \cong \mathbb{Z}.
\]
Proof: quotient by contractible subcomplex.
<2>4. **Item 9: $\mathbb{R}^3 \setminus \{(x, y, 0) \mid x^2 + y^2 = 1\}$**
The complement of the unknot in $\mathbb{R}^3$ deformation retracts onto $S^2 \vee S^1$ (the $z$-axis plus a 2-sphere enclosing the circle), so:
\[
\pi_1(\mathbb{R}^3 \setminus S^1) \cong \pi_1(S^2 \vee S^1) \cong \mathbb{Z}.
\]
Proof: deformation retraction of unknot complement in $\mathbb{R}^3$.
<2>5. **Item 10: $\mathbb{R}^3 \setminus H$ (Hopf link complement)**
The complement of the Hopf link in $S^3$ is homeomorphic to $T^2 \times (0, 1) \simeq S^1 \times S^1$.
Thus:
\[
\pi_1(\mathbb{R}^3 \setminus H) \cong \pi_1(S^1 \times S^1) \cong \mathbb{Z} \oplus \mathbb{Z}.
\]
Proof: Wirtinger presentation / torus fiber structure of the Hopf link complement.

<1>3. Conclusion:
The fundamental groups are:
1. $F_2$, 2. $\mathbb{Z}$, 3. $F_4$, 4. $F_3$, 5. $F_2$, 6. $\mathbb{Z}_2$, 7. $0$, 8. $\mathbb{Z}$, 9. $\mathbb{Z}$, 10. $\mathbb{Z} \oplus \mathbb{Z}$. Q.E.D.
Proof: <1>1 and <1>2.
:::
