---
schema: qual/card@1
id: P-AGH5414SPACECURVES
kind: problem
title: Existence of space curves of degree at most ten with prescribed genus
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Adjunction
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.14 as transcribed here, the retained Andrew Egbert
    companion sketch, and the cubic-surface existence machinery in V.4.7--4.9.
    The companion identifies which degree-genus pairs remain after V.4.7 but
    stops at the numerical equations for the multiplicities. The solution
    below completes that calculation by giving an explicit divisor class for
    every requested pair and checks each class against all 27 lines before
    applying the V.4.8 smooth-irreducible-member criterion.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read all nine coefficient vectors against the intersection form.
    Checked their sums and sums of squares, the adjunction genus calculation,
    and intersections with the three families of 27 lines. In particular the
    only row with d-a<0 is D_(8,7), where every multiplicity is at least 3,
    so the residual-conic line intersections remain positive. Thus every row
    satisfies the V.4.8 existence criterion.
---

::: {.problem}
Using the method of (4.13.1), verify that there are nonsingular curves in $\PP^3$ with $d=8, g=6,7$; $d=9, g=7,8,9$; $d=10, g=8,9,10,11$.
Combining with (IV, §6), this completes the determination of all possible $g$ for curves of degree $d \leqslant 10$ in $\PP^3$.
:::

::: {.solution}
Let
$$
S=\operatorname{Bl}_{P_1,\ldots,P_6}\PP^2
$$
be a nonsingular cubic surface, with the six points in general position.
Write
$$
h=\pi^*\OO_{\PP^2}(1),
\qquad
e_1,\ldots,e_6
$$
for the usual basis of $\Pic S$. Its hyperplane class is
$$
H=-K_S=3h-e_1-\cdots-e_6.
$$

::: pf

::: {.pf-step #degree-genus-formula}
If
$$
D=ah-\sum_{i=1}^6b_i e_i,
$$
then a nonsingular member $C\in|D|$ has
$$
\boxed{
\deg C=3a-\sum_i b_i,
\qquad
g(C)=1+\frac{a^2-\sum_i b_i^2-\deg C}{2}.}
$$

::: pf-proof
The intersection form is
$$
h^2=1,
\qquad
e_i^2=-1,
\qquad
h\cdot e_i=e_i\cdot e_j=0
\quad(i\ne j).
$$
Hence
$$
H\cdot D=3a-\sum_i b_i
$$
and
$$
D^2=a^2-\sum_i b_i^2.
$$
Since $H$ is the hyperplane class, $H\cdot D$ is the degree of $C$ in
$\PP^3$. Adjunction, using $K_S=-H$, gives
$$
2g(C)-2
=
D\cdot(D+K_S)
=
D^2-H\cdot D,
$$
which is the stated genus formula.
:::

:::

::: {.pf-step #nine-divisor-classes}
The following nine divisor classes have exactly the requested
degree-genus pairs:
$$
\begin{aligned}
D_{8,6}
&=8h-4e_1-3e_2-3e_3-2e_4-2e_5-2e_6,\\
D_{8,7}
&=9h-4e_1-3e_2-3e_3-3e_4-3e_5-3e_6,\\
D_{9,7}
&=8h-4e_1-3e_2-3e_3-2e_4-2e_5-e_6,\\
D_{9,8}
&=8h-4e_1-3e_2-2e_3-2e_4-2e_5-2e_6,\\
D_{9,9}
&=9h-4e_1-3e_2-3e_3-3e_4-3e_5-2e_6,\\
D_{10,8}
&=8h-4e_1-3e_2-3e_3-2e_4-e_5-e_6,\\
D_{10,9}
&=8h-4e_1-3e_2-2e_3-2e_4-2e_5-e_6,\\
D_{10,10}
&=8h-4e_1-2e_2-2e_3-2e_4-2e_5-2e_6,\\
D_{10,11}
&=9h-4e_1-3e_2-3e_3-3e_4-2e_5-2e_6.
\end{aligned}
$$

::: pf-proof
For these classes, respectively,
$$
\begin{aligned}
\left(\sum b_i,\sum b_i^2\right)
&=(16,46),(19,61),(15,43),(15,41),(18,56),\\
&\qquad(14,40),(14,38),(14,36),(17,51).
\end{aligned}
$$
Step [](#degree-genus-formula){.pf-ref} therefore gives
$$
\begin{aligned}
(H\cdot D,D^2)
&=(8,18),(8,20),(9,21),(9,23),(9,25),\\
&\qquad(10,24),(10,26),(10,28),(10,30).
\end{aligned}
$$
Applying the genus formula in step [](#degree-genus-formula){.pf-ref} gives, in the same order,
$$
(d,g)
=
(8,6),(8,7),(9,7),(9,8),(9,9),
(10,8),(10,9),(10,10),(10,11).
$$
:::

:::

::: {.pf-step #positive-line-intersections}
Every class in step [](#nine-divisor-classes){.pf-ref} intersects each of the 27 lines on $S$
positively.

::: pf-proof
The 27 line classes on the cubic surface are
$$
E_i=e_i,
\qquad
L_{ij}=h-e_i-e_j,
\qquad
Q_i=2h-\sum_{j\ne i}e_j
$$
for $1\le i<j\le6$ and $1\le i\le6$.

For a class
$$
D=ah-\sum_i b_i e_i
$$
from step [](#nine-divisor-classes){.pf-ref}, every $b_i$ is positive, so
$$
D\cdot E_i=b_i>0.
$$
In every displayed class the sum of the two largest multiplicities is at
most $7$, while $a\ge8$. Hence
$$
D\cdot L_{ij}
=
a-b_i-b_j
>0.
$$

Finally, if $d=H\cdot D$, then
$$
\sum_i b_i=3a-d,
$$
so
$$
\begin{aligned}
D\cdot Q_i
&=2a-\sum_{j\ne i}b_j\\
&=2a-(3a-d-b_i)\\
&=d-a+b_i.
\end{aligned}
$$
For eight of the nine classes one has $d-a\ge0$. The only exception is
$D_{8,7}$, where $d-a=-1$ but every $b_i\ge3$. Thus
$$
D\cdot Q_i>0
$$
for every $i$ in every case.
:::

:::

::: {.pf-step #nonsingular-irreducible-member}
Each class in step [](#nine-divisor-classes){.pf-ref} contains a nonsingular irreducible curve.

::: pf-proof
Step [](#nine-divisor-classes){.pf-ref} shows that every one of the nine classes has positive
self-intersection. Step [](#positive-line-intersections){.pf-ref} shows that it has nonnegative intersection with
every line on the cubic surface. Therefore alternative (c) of
[[P-AGH548IRREDCLASSES|Exercise V.4.8]] applies: each class contains a
nonsingular irreducible curve.

For such a curve, step [](#nine-divisor-classes){.pf-ref} computes its degree and genus. Since the cubic
surface is already embedded in $\PP^3$ by $|H|$, these are nonsingular curves
in $\PP^3$ with precisely the degree-genus pairs requested in the problem.
:::

:::

::: pf-qed
Step [](#nine-divisor-classes){.pf-ref} constructs a divisor class for each requested pair, step [](#positive-line-intersections){.pf-ref}
checks the line-intersection hypotheses needed for the cubic-surface
existence criterion, and step [](#nonsingular-irreducible-member){.pf-ref} supplies the required nonsingular curves.
:::

:::
:::
