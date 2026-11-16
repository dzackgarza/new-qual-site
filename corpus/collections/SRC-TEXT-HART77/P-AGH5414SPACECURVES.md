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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    A complete published solution located, on a third pass over issue #121, and
    the card's obligation under it discharged. Algebraic Geometry II, National
    Taiwan University, 2020 Spring (course of Chin-Lung Wang), Chapter V
    Surfaces homework, Exercise 14 of section 4 (by Ping-Hsun Chuang), printed
    p. 18 of tmp/sources/ntu-ag2-chapter5.pdf, whose printed folio is the PDF
    page number, read also in its MinerU text version
    tmp/sources/ntu-ag2-chapter5.md. It states only the very-ampleness
    criterion of Corollary 4.13 and then writes "we only need to find such a
    and b_i", so its use of 4.13(b), the irreducible nonsingular member, is
    implicit; it exhibits one class for each of the nine printed pairs. Each
    row was recomputed here:
    (8,6) a=8 b=(4,3,3,2,2,2); (8,7) a=8 b=(3,3,3,3,2,2); (9,7) a=9
    b=(4,4,4,2,2,2); (9,8) a=9 b=(4,4,3,3,2,2); (9,9) a=9 b=(4,3,3,3,3,2);
    (10,8) a=10 b=(6,3,3,3,3,2); (10,9) a=12 b=(5,5,5,5,3,3); (10,10) a=11
    b=(5,5,4,3,3,3); (10,11) a=10 b=(5,3,3,3,3,3). For every row deg D = 3a - sum
    b_i and p_a(D) = (a-1)(a-2)/2 - sum b_i(b_i-1)/2 give the printed pair, and
    b_i > 0, a > b_i + b_j for every pair and 2a > sum_{j != i} b_j for every i
    hold, so each class is very ample and by 4.13(b) contains an irreducible
    nonsingular curve. The set's two slips are that the third condition is
    printed with b_i inside the sum over j and that Corollary 4.13 is called the
    theorem V.4.13; neither affects the argument. Yang Pi-Yeh, printed p. 112,
    gives the same nine pairs without showing any member nonsingular, so it does
    not close the exercise. The card's own proof is unchanged.
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
then a nonsingular member $C\in\linearsystem{D}$ has
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
surface is already embedded in $\PP^3$ by $\linearsystem{H}$, these are nonsingular curves
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

::: {.remark title="Published solutions"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.14, printed p. 294, read in
`tmp/sources/hartshorne-solutions-egbert.pdf` and in its MinerU text version
`tmp/sources/hartshorne-solutions-egbert.md`, records which pairs remain after (4.7), sets up the $d=8$, $g=6$
adjunction equation and does not solve it, deferring the other cases to his V.4.9.

**The exercise is closed by a complete published solution**: Algebraic Geometry II, National Taiwan University,
2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework, Exercise 14 of §4 (by Ping-Hsun Chuang),
printed p. 18 of `tmp/sources/ntu-ag2-chapter5.pdf`, whose printed folio is the PDF page number, read also in its
MinerU text version `tmp/sources/ntu-ag2-chapter5.md`. It states the very-ampleness criterion of Corollary 4.13
--- a class $D\sim a\ell-\sum_ib_ie_i$ is very ample if and only if $b_i>0$ for all $i$, $a>b_i+b_j$ for all
$i,j$ and $2a>\sum_{j\ne i}b_j$ for all $i$ --- and then writes "we only need to find such $a$ and $b_i$": the
half turning a class that satisfies the criterion into a linear system with an irreducible nonsingular member
is 4.13(b), which the set uses without stating it. It exhibits one class for each of the nine printed pairs,
computing $\deg D=3a-\sum_ib_i$ and
$p_a(D)=\frac12(a-1)(a-2)-\frac12\sum_ib_i(b_i-1)$:

| $(d,g)$ | $a$ | $(b_1,\dots,b_6)$ | $\deg D=3a-\sum b_i$ | $p_a(D)$ |
|---|---|---|---|---|
| $(8,6)$ | $8$ | $(4,3,3,2,2,2)$ | $24-16=8$ | $21-15=6$ |
| $(8,7)$ | $8$ | $(3,3,3,3,2,2)$ | $24-16=8$ | $21-14=7$ |
| $(9,7)$ | $9$ | $(4,4,4,2,2,2)$ | $27-18=9$ | $28-21=7$ |
| $(9,8)$ | $9$ | $(4,4,3,3,2,2)$ | $27-18=9$ | $28-20=8$ |
| $(9,9)$ | $9$ | $(4,3,3,3,3,2)$ | $27-18=9$ | $28-19=9$ |
| $(10,8)$ | $10$ | $(6,3,3,3,3,2)$ | $30-20=10$ | $36-28=8$ |
| $(10,9)$ | $12$ | $(5,5,5,5,3,3)$ | $36-26=10$ | $55-46=9$ |
| $(10,10)$ | $11$ | $(5,5,4,3,3,3)$ | $33-23=10$ | $45-35=10$ |
| $(10,11)$ | $10$ | $(5,3,3,3,3,3)$ | $30-20=10$ | $36-25=11$ |

Every row was checked here against the criterion: $\deg D$ and $p_a(D)$ reproduce the printed pair, $b_i>0$,
$a>b_i+b_j$ for every pair and $2a>\sum_{j\ne i}b_j$ for every $i$; so each of the nine classes is very ample
on the cubic surface and contains a nonsingular curve of the requested degree and genus. Its two slips are
typographical: the third condition is printed with $b_i$ where the summand runs over $j$, and Corollary 4.13 is
called "the theorem V.4.13". Yang Pi-Yeh, *Hartshorne Solutions*, printed p. 112 of
`tmp/sources/lfwin-hartshorne-solutions.pdf`, read also in its MinerU text version
`tmp/sources/lfwin-hartshorne-solutions.md`, gives the same nine pairs as a table of classes, and
that entry does not close the exercise, since it shows no member of any class to be nonsingular; the
National Taiwan University argument does, through 4.13(b).
:::
