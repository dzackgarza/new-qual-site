---
schema: qual/card@1
id: E-SS9.EX-2
kind: problem
title: "Zeros minus poles of an elliptic function lands in the period lattice"
classification:
  areas:
  - complex-analysis
  topics: ['Elliptic Functions', 'Weierstrass P', 'Lattices']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
2. Suppose that $a _ { 1 } , \ldots , a _ { r }$ and $b _ { 1 } , \ldots , b _ { r }$ are the zeros and poles, respectively, in the fundamental parallelogram of an elliptic function $f .$ Show that

$$
a _ {1} + \dots + a _ {r} - b _ {1} - \dots - b _ {r} = n \omega_ {1} + m \omega_ {2}
$$

for some integers n and $m .$

[Hint: If the boundary of the parallelogram contains no zeros or poles, simply integrate $z f ^ { \prime } ( z ) / f ( z )$ over that boundary, and observe that the integral of $f ^ { \prime } ( z ) / f ( z )$ over a side is an integer multiple of $2 \pi i$ . If there are zeros or poles on the side of the parallelogram, translate it by a small amount to reduce the problem to the first case.]
:::

::: solution
Translate the fundamental parallelogram slightly, if necessary, so that its boundary contains no zero or pole of $f$. Let its vertices be
\[
z_0,\quad z_0+\omega_1,\quad z_0+\omega_1+\omega_2,\quad z_0+\omega_2,
\]
and put
\[
g(z)=\frac{f'(z)}{f(z)}.
\]
The function $g$ is elliptic with the same periods as $f$.

By the residue theorem,
\[
\frac1{2\pi i}\int_{\partial P} z g(z)\,dz
=\sum_j a_j-\sum_j b_j,
\tag{1}
\]
where zeros and poles are repeated according to multiplicity.

Pair the bottom side with the oppositely oriented top side. Periodicity under $\omega_2$ gives
\[
\int_{\text{bottom}}zg(z)\,dz+
\int_{\text{top}}zg(z)\,dz
=-\omega_2\int_{\text{bottom}}g(z)\,dz.
\]
Similarly, pairing the left and right sides gives
\[
\int_{\text{right}}zg(z)\,dz+
\int_{\text{left}}zg(z)\,dz
=\omega_1\int_{\text{left}}g(z)\,dz.
\]
Therefore
\[
\frac1{2\pi i}\int_{\partial P}zg(z)\,dz
=m\omega_1+n\omega_2
\tag{2}
\]
for some integers $m,n$, because on either side joining two points differing by a period,
\[
\frac1{2\pi i}\int \frac{f'}f\,dz
\]
is the winding number of the closed curve traced by $f$ and hence is an integer.

Combining (1) and (2),
\[
\sum_j a_j-\sum_j b_j=m\omega_1+n\omega_2.
\]
If the original fundamental parallelogram had zeros or poles on its boundary, a sufficiently small translation avoids them without changing the divisor modulo the period lattice, so the same conclusion holds.
:::
