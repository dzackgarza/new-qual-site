---
schema: qual/card@1
id: E-SS8.EX-22
kind: problem
title: "If  is a simply connected region bounded by a polygon with vertices  and angles "
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
22. If $P$ is a simply connected region bounded by a polygon with vertices $a _ { 1 } , \ldots , a _ { n }$ and angles $\alpha _ { 1 } \pi , \ldots , \alpha _ { n } \pi$ , and $F$ is a conformal map of the disc D to $P ,$ then there exist complex numbers $B _ { 1 } , \ldots , B _ { n }$ on the unit circle, and constants $c _ { 1 }$ and $c _ { 2 }$ so that

$$
F (z) = c _ {1} \int_ {1} ^ {z} \frac {d \zeta}{(\zeta - B _ {1}) ^ {\beta_ {1}} \cdots (\zeta - B _ {n}) ^ {\beta_ {n}}} + c _ {2}.
$$

[Hint: This follows from the standard correspondence between H and D and an argument similar to that used in the proof of Theorem 4.7.]
:::

::: solution
Put $\beta_j=1-\alpha_j$. Choose a Möbius map
\[
\phi:\mathbb H\longrightarrow\mathbb D
\]
whose inverse sends real points $x_j$ to the boundary points $B_j\in\partial\mathbb D$ that correspond under $F$ to the polygon vertices $a_j$.

Then $G=F\circ\phi$ maps $\mathbb H$ conformally onto $P$. By the Schwarz--Christoffel formula,
\[
G'(w)=C\prod_{j=1}^n(w-x_j)^{-\beta_j}.
\tag{1}
\]
Now write $w=\phi^{-1}(z)=(az+b)/(cz+d)$. For each $j$,
\[
w-x_j=\frac{(a-cx_j)(z-B_j)}{cz+d},
\qquad
\frac{dw}{dz}=\frac{ad-bc}{(cz+d)^2}.
\]
Because the angles of a polygon satisfy
\[
\sum_{j=1}^n\alpha_j=n-2,
\]
we have
\[
\sum_{j=1}^n\beta_j
=n-(n-2)=2.
\]
Therefore all powers of $cz+d$ cancel when (1) is transformed back to the disk, and
\[
F'(z)=C_1\prod_{j=1}^n(z-B_j)^{-\beta_j}
\]
for a nonzero constant $C_1$. Integrating from any fixed base point (in particular from $1$, interpreted with a path in the disk when $1$ is not itself a prevertex) gives
\[
F(z)=c_1\int_1^z
\frac{d\zeta}{(\zeta-B_1)^{\beta_1}\cdots(\zeta-B_n)^{\beta_n}}
+c_2,
\]
with suitable branch choices and constants $c_1\ne0,c_2\in\mathbb C$.
:::
