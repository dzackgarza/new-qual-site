---
schema: qual/card@1
id: P-AGH5415GENPOSITION
kind: problem
title: Points in general position and exceptional curves on blowups of the plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowups
  - Birational Geometry
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.15 as transcribed here, the retained Andrew Egbert
    companion notes, and the quadratic-transformation formulas in V.4.2.
    The companion gives only a partial r=7,8 count and an abbreviated
    openness argument, and it does not prove the starred r=9 assertion. The
    solution below instead works on the marked blowup: admissible
    transformations give explicit Picard-basis changes, negative curves for
    r<=8 are reduced to exceptional divisors by decreasing plane degree, and
    for r=9 repeated transformations make the degree of a (-1)-class
    unbounded.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the V.4.2 quadratic-transform formulas.
    Checked the six-point pullbacks in part (a), the countable bad-locus
    argument in part (c), the degree-decreasing standard-form argument for all
    negative curves when r=7,8, every multiplicity partition and count in the
    56/240 tables, and the r=9 recurrence
    d'=2d-(m_1+m_2+m_3)>=d+1. The final orbit argument uses actual terminal
    exceptional divisors pulled back to the original blowup, so distinct
    lattice classes give distinct (-1)-curves on the fixed surface.
---

::: {.problem}
Let $P_1, \ldots, P_r$ be a finite set of (ordinary) points of $\PP^2$, no 3 collinear.
We define an **admissible transformation** to be a quadratic transformation (4.2.3) centered at some three of the $P_i$ (call them $P_1, P_2, P_3$).

This gives a new $\PP^2$, and a new set of $r$ points, namely $Q_1, Q_2, Q_3$, and the images of $P_4, \ldots, P_r$.

We say that $P_1, \ldots, P_r$ are **in general position** if no three are collinear, and furthermore after any finite sequence of admissible transformations, the new set of $r$ points also has no three collinear.

a. A set of 6 points is in general position if and only if no three are collinear and not all six lie on a conic.

b. If $P_1, \ldots, P_r$ are in general position, then the $r$ points obtained by any finite sequence of admissible transformations are also in general position.

c. Assume the ground field $k$ is uncountable.
Then given $P_1, \ldots, P_r$ in general position, there is a dense subset $V \subseteq \PP^2$ such that for any $P_{r+1} \in V$, $P_1, \ldots, P_{r+1}$ will be in general position.

Hint: Prove a lemma that when $k$ is uncountable, a variety cannot be equal to the union of a countable family of proper closed subsets.

d. Now take $P_1, \ldots, P_r \in \PP^2$ in general position, and let $X$ be the surface obtained by blowing up $P_1, \ldots, P_r$.
If $r=7$, show that $X$ has exactly 56 irreducible nonsingular curves $C$ with $g=0$, $C^2=-1$, and that these are the only irreducible curves with negative self-intersection.
Ditto for $r=8$, the number being 240.

e. For $r=9$, show that the surface $X$ defined in (d) has infinitely many irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$.

Hint: Let $L$ be the line joining $P_1$ and $P_2$.
Show that there exist finite sequences of admissible transformations such that the strict transform of $L$ becomes a plane curve of arbitrarily high degree.
This example is apparently due to Kodaira -- see Nagata $[5, II, p. 283]$.
:::

::: {.solution}
For a labeled configuration
$$
\mathbf P=(P_1,\ldots,P_r)
$$
with no three points collinear, write
$$
X(\mathbf P)=\operatorname{Bl}_{P_1,\ldots,P_r}\PP^2.
$$
Let $h$ be the pullback of a line and let $e_i$ be the exceptional classes.
Thus
$$
h^2=1,\qquad e_i^2=-1,\qquad
h\cdot e_i=e_i\cdot e_j=0\quad(i\ne j),
$$
and
$$
K_X=-3h+\sum_{i=1}^r e_i.
$$

::: pf

::: {.pf-step #quadratic-transform-basis-change}
An admissible quadratic transformation centered at
$P_1,P_2,P_3$ identifies the two marked blowups and changes the Picard basis
by
$$
\begin{aligned}
h'&=2h-e_1-e_2-e_3,\\
e_1'&=h-e_2-e_3,\\
e_2'&=h-e_1-e_3,\\
e_3'&=h-e_1-e_2,\\
e_i'&=e_i\qquad(i\ge4).
\end{aligned}
$$
Consequently, if
$$
D=ah-\sum_i b_i e_i
=
a'h'-\sum_i b_i'e_i',
$$
then
$$
\boxed{
\begin{aligned}
a'&=2a-b_1-b_2-b_3,\\
b_1'&=a-b_2-b_3,\\
b_2'&=a-b_1-b_3,\\
b_3'&=a-b_1-b_2,\\
b_i'&=b_i\qquad(i\ge4).
\end{aligned}}
$$

::: pf-proof
The common resolution of a quadratic transformation is described in
[[P-AGH542QUADTRANSFORM]]. The pullback of a target line is
$$
2h-e_1-e_2-e_3,
$$
and the target exceptional divisors are the strict transforms of the three
fundamental lines, namely
$$
h-e_2-e_3,\qquad h-e_1-e_3,\qquad h-e_1-e_2.
$$
Because no other $P_i$ lies on a fundamental line, its exceptional divisor
is unchanged. This gives the displayed basis formulas. The quadratic
transformation is an involution, so solving for the coefficients of $D$ in
the target basis gives the same formulas with primed and unprimed
coefficients interchanged, which is the boxed transformation law.
:::

:::

::: {.pf-step #six-point-condition-preserved}
For six points, the condition
$$
\boxed{\text{no three are collinear and the six do not lie on a conic}}
$$
is preserved by every admissible transformation.

::: pf-proof
It suffices to consider a transformation centered at $P_1,P_2,P_3$.
Denote the target base points by $Q_1,Q_2,Q_3$ and the images of
$P_4,P_5,P_6$ by $R_4,R_5,R_6$.

A line through $R_4,R_5,R_6$ has class
$$
h'-e_4'-e_5'-e_6'
=
2h-e_1-e_2-e_3-e_4-e_5-e_6.
$$
Thus these three target points are collinear exactly when the six source
points lie on a conic.

A line through, say, $Q_1,R_4,R_5$ has class
$$
h'-e_1'-e_4'-e_5'
=
h-e_1-e_4-e_5.
$$
Hence such a target collinearity would give three collinear source points.
The same calculation applies after permuting the labels.

A line through two of $Q_1,Q_2,Q_3$ and one $R_j$ would pull back, for
example, to the class
$$
h'-e_1'-e_2'-e_j'=e_3-e_j.
$$
No effective curve has this class: its plane degree is zero, so an effective
divisor of this degree is supported on exceptional curves with nonnegative
coefficients. Finally $Q_1,Q_2,Q_3$ themselves are the three base points of
the inverse quadratic transformation and are noncollinear.

It remains to exclude a conic through all six target points. Its class pulls
back to
$$
2h'-\sum_{i=1}^6e_i'
=
h-e_4-e_5-e_6.
$$
Such a conic would therefore force $P_4,P_5,P_6$ to be collinear.
Thus the displayed source condition implies the same condition on the
target. Since the quadratic transformation is an involution, the converse
holds as well.
:::

:::

::: {.pf-step #six-points-general-position-iff}
Six points are in general position if and only if no three are
collinear and not all six lie on a conic.

::: pf-proof
If the six points satisfy the two stated conditions, step [](#six-point-condition-preserved){.pf-ref} shows that
every successive admissible transformation preserves them. In particular no
three points become collinear after any finite sequence, so the six points
are in general position.

Conversely, general position includes the requirement that the original six
points have no collinear triple. Suppose all six nevertheless lie on a
conic. Choose any three as centers of an admissible transformation. By the
first calculation in step [](#six-point-condition-preserved){.pf-ref}, the images of the other three points are
collinear. This contradicts general position. This proves (a).
:::

:::

::: {.pf-step #general-position-preserved-under-sequence}
General position is preserved after any finite sequence of admissible
transformations.

::: pf-proof
Let $\mathbf Q$ be obtained from a general-position configuration
$\mathbf P$ by a finite admissible sequence $w$. Any further finite
admissible sequence $v$ starting from $\mathbf Q$ gives the concatenated
finite sequence
$$
v\circ w
$$
starting from $\mathbf P$. By general position of $\mathbf P$, the terminal
configuration has no three collinear. Since this holds for every $v$,
$\mathbf Q$ is itself in general position. This proves (b).
:::

:::

::: {.pf-step #uncountable-field-lemma}
Let $k$ be uncountable. A nonempty open subset of $\PP_k^2$ cannot be
covered by countably many proper closed subsets.

::: pf-proof
Let $U\subseteq\PP^2$ be nonempty open and let
$$
Z_1,Z_2,\ldots
$$
be proper closed subsets. Each $Z_n$ has only finitely many one-dimensional
irreducible components. Since $k$ is uncountable, there are uncountably many
lines in $\PP^2$, so one can choose a line $\ell$ which is not a component
of any $Z_n$ and which meets $U$.

For every $n$, the intersection
$$
\ell\cap Z_n
$$
is finite. Hence
$$
\ell(k)\cap\bigcup_nZ_n
$$
is countable. But $\ell(k)\cong\PP^1(k)$ is uncountable, and
$U\cap\ell$ is the complement of finitely many points in $\ell$. Therefore
$U\cap\ell$ contains a point outside every $Z_n$.
:::

:::

::: {.pf-step #bad-locus-proper-closed}
Fix $P_1,\ldots,P_r$ in general position. For every fixed finite word
$w$ of admissible transformations and every fixed triple of labels, the set
of points
$$
P\in\PP^2
$$
for which the word is defined on
$$
(P_1,\ldots,P_r,P)
$$
and the specified terminal triple is collinear is contained in a proper
closed subset of $\PP^2$.

::: pf-proof
Work on the open subset on which the successive centers occurring in $w$
are noncollinear and all quadratic transformations are defined at the
remaining labeled points. The standard quadratic formula
[[P-AGH46CREMONA]] shows inductively that every terminal point has homogeneous
coordinates which are rational functions of the coordinates of $P$.
Collinearity of a specified terminal triple is therefore the vanishing of a
rational determinant. Clearing denominators gives a closed condition on the
initial point $P$.

This determinant is not identically zero. Indeed, cancel the transformations
of $w$ in reverse order, using that each quadratic transformation is
birational and involutive. At the level of function fields, pullback by a
birational map is injective, so a nonzero incidence equation cannot become
the zero equation. Continuing to the initial configuration, an identically
vanishing condition would force either a collinearity among the fixed
$r$-tuple after a finite admissible sequence, contrary to its general
position, or an incidence condition requiring the free point $P$ to lie on
a fixed proper plane curve. The latter is also not an identity on $\PP^2$.
Thus the cleared determinant defines a proper closed subset.
:::

:::

::: {.pf-step #dense-general-position-extension}
If $k$ is uncountable and $P_1,\ldots,P_r$ are in general position,
there is a dense subset
$$
\boxed{V\subseteq\PP^2}
$$
such that every $P_{r+1}\in V$ makes
$P_1,\ldots,P_r,P_{r+1}$ a general-position configuration.

::: pf-proof
There are only finitely many choices of a triple of labels at each stage,
so there are only countably many finite words of admissible transformations.
For each word there are finitely many terminal triples. Step [](#bad-locus-proper-closed){.pf-ref} therefore
produces only countably many proper closed bad subsets of $\PP^2$.

Also exclude the finitely many original lines through pairs of the fixed
points and the finitely many points $P_i$ themselves. Let $B$ be the union
of all these bad subsets and put
$$
V=\PP^2\setminus B.
$$
Step [](#uncountable-field-lemma){.pf-ref}, applied inside every nonempty open subset of $\PP^2$, shows that
$V$ is dense. For $P_{r+1}\in V$, no collinear triple occurs initially or
after any finite admissible word. This is exactly the definition of general
position, proving (c).
:::

:::

::: {.pf-step #degree-bound-nonneg-square}
Let $r\le8$, and let
$$
D=ah-\sum_{i=1}^r b_i e_i
$$
with
$$
a\ge0,
\qquad
b_1\ge b_2\ge\cdots\ge b_r\ge0.
$$
If
$$
a\ge b_1+b_2+b_3,
$$
then
$$
\boxed{D^2\ge0.}
$$

::: pf-proof
If $a=0$, the hypothesis forces every $b_i=0$, so the conclusion is
immediate. Assume $a>0$.

Put $c=b_3$. Since $r\le8$ and $b_i\le c$ for $i\ge3$,
$$
\sum_{i=1}^r b_i^2
\le
b_1^2+b_2^2+6c^2.
$$
Also
$$
b_1+b_2\le a-c
$$
and $b_2\ge c$. For fixed sum, the square sum is maximized by making the two
entries as unequal as the constraint $b_2\ge c$ permits. Hence
$$
b_1^2+b_2^2
\le
(a-2c)^2+c^2.
$$
Because $b_1,b_2\ge c$ and
$b_1+b_2+c\le a$, one has $3c\le a$. Therefore
$$
\begin{aligned}
\sum_i b_i^2
&\le
(a-2c)^2+7c^2\\
&=
a^2-4ac+11c^2\\
&\le a^2.
\end{aligned}
$$
The last inequality follows from $c\le a/3$, since then
$11c\le 11a/3<4a$. Thus
$$
D^2=a^2-\sum_i b_i^2\ge0.
$$
:::

:::

::: {.pf-step #negative-curve-is-minus-one-curve}
For $r=7$ or $8$, every irreducible curve of negative
self-intersection is a nonsingular rational $(-1)$-curve.

::: pf-proof
Let $C\subseteq X(\mathbf P)$ be irreducible with $C^2<0$. If $C$ is an
exceptional divisor, the assertion is immediate. Otherwise its plane image
has positive degree, so after relabeling its class is
$$
C\sim ah-\sum_{i=1}^r b_i e_i,
\qquad
a>0,
\qquad
b_1\ge\cdots\ge b_r\ge0.
$$
By step [](#degree-bound-nonneg-square){.pf-ref}, negativity forces
$$
b_1+b_2+b_3>a.
$$
Perform the admissible quadratic transformation centered at the three points
with these largest multiplicities. Step [](#quadratic-transform-basis-change){.pf-ref} gives the new plane degree
$$
a'=2a-b_1-b_2-b_3<a.
$$
The marked blowup itself is unchanged up to isomorphism, so the transformed
curve remains irreducible and has the same negative self-intersection.
Step [](#general-position-preserved-under-sequence){.pf-ref} says the new point configuration is again in general position.

Repeat. The nonnegative plane degree decreases strictly, so after finitely
many steps it is zero. An irreducible curve of plane degree zero on a
point-blowup is one of the exceptional divisors. Reversing the sequence of
isomorphisms shows that the original $C$ is isomorphic to an exceptional
divisor. Hence
$$
C\cong\PP^1,
\qquad
C^2=-1.
$$
:::

:::

::: {.pf-step #minus-one-curve-numerics}
A nonexceptional $(-1)$-curve
$$
C\sim ah-\sum_{i=1}^r b_i e_i
$$
with $b_i\ge0$ satisfies
$$
\boxed{
\sum_i b_i=3a-1,
\qquad
\sum_i b_i^2=a^2+1.}
$$

::: pf-proof
Step [](#negative-curve-is-minus-one-curve){.pf-ref} gives
$$
C^2=-1
$$
and $p_a(C)=0$. Adjunction gives
$$
-2=C\cdot(C+K_X)=-1+K_X\cdot C,
$$
so
$$
K_X\cdot C=-1.
$$
Using
$$
K_X=-3h+\sum_i e_i
$$
and the intersection form gives
$$
-3a+\sum_i b_i=-1,
$$
which is the first equality. The equation $C^2=-1$ gives the second.
:::

:::

::: {.pf-step #r7-classes-fifty-six}
For $r=7$, the possible $(-1)$-curve classes are exactly
$$
\begin{array}{c|c|c}
a & (b_1,\ldots,b_7)\text{ up to permutation} & \text{number}\\
\hline
0 & \text{exceptional} & 7\\
1 & (1,1,0,0,0,0,0) & \binom72=21\\
2 & (1,1,1,1,1,0,0) & \binom75=21\\
3 & (2,1,1,1,1,1,1) & 7.
\end{array}
$$
Thus there are $56$ such classes.

::: pf-proof
For $a>0$, step [](#minus-one-curve-numerics){.pf-ref} and Cauchy--Schwarz give
$$
(3a-1)^2
\le
7(a^2+1),
$$
hence
$$
a^2-3a-3\le0.
$$
Thus $a\le3$.

For $a=1$ or $2$, subtracting the two equations in step [](#minus-one-curve-numerics){.pf-ref} gives
$$
\sum_i b_i(b_i-1)=(a-1)(a-2)=0.
$$
Thus every $b_i$ is $0$ or $1$, and their sums are respectively $2$ and
$5$, giving the first two nonexceptional rows.

For $a=3$, put $x_i=b_i-1$. The equations become
$$
\sum_i x_i=1,
\qquad
\sum_i x_i^2=1.
$$
Hence exactly one $x_i$ is $1$ and the others are zero. This gives
$(2,1,1,1,1,1,1)$.

Together with the seven exceptional divisors, the total number of classes is
$$
7+21+21+7=\boxed{56}.
$$
:::

:::

::: {.pf-step #r7-classes-realized-unique}
Every class in step [](#r7-classes-fifty-six){.pf-ref} is represented by exactly one irreducible
nonsingular rational curve. Hence for $r=7$ there are exactly $56$ negative
curves, and there are no others.

::: pf-proof
Starting with any nonexceptional row of step [](#r7-classes-fifty-six){.pf-ref}, choose three largest
multiplicities and apply step [](#quadratic-transform-basis-change){.pf-ref}. The plane degree decreases:
$$
3\longmapsto2\longmapsto1\longmapsto0.
$$
The multiplicity patterns become successively the preceding rows, ending in
an exceptional divisor. Because every intermediate point configuration is
general by step [](#general-position-preserved-under-sequence){.pf-ref}, these are admissible transformations. Reversing them
pulls the final exceptional divisor back to an irreducible nonsingular
rational curve in the original class. Thus every listed class is effective.

There cannot be two distinct irreducible curves in the same listed class:
their intersection number would be the self-intersection $-1$, whereas
distinct irreducible curves on a smooth surface have nonnegative
intersection. Hence each class has exactly one representative.
Step [](#negative-curve-is-minus-one-curve){.pf-ref} says every irreducible negative curve must be one of these
$(-1)$-curves. This proves the $r=7$ assertion in (d).
:::

:::

::: {.pf-step #r8-classes-two-forty}
For $r=8$, the possible $(-1)$-curve classes are exactly
$$
\begin{array}{c|c|c}
a & (b_1,\ldots,b_8)\text{ up to permutation} & \text{number}\\
\hline
0 & \text{exceptional} & 8\\
1 & (1,1,0,0,0,0,0,0) & 28\\
2 & (1,1,1,1,1,0,0,0) & 56\\
3 & (2,1,1,1,1,1,1,0) & 56\\
4 & (2,2,2,1,1,1,1,1) & 56\\
5 & (2,2,2,2,2,2,1,1) & 28\\
6 & (3,2,2,2,2,2,2,2) & 8.
\end{array}
$$
Thus there are $240$ such classes.

::: pf-proof
Step [](#minus-one-curve-numerics){.pf-ref} and Cauchy--Schwarz give
$$
(3a-1)^2
\le
8(a^2+1),
$$
so
$$
a^2-6a-7\le0
$$
and hence $a\le7$. Equality in Cauchy--Schwarz would be necessary when
$a=7$, because then
$$
\frac{(3a-1)^2}{8}=a^2+1=50.
$$
It would force all eight integers $b_i$ to equal $20/8=5/2$, impossible.
Thus $a\le6$.

For $a=1,2$, the argument of step [](#r7-classes-fifty-six){.pf-ref} gives respectively two and five
entries equal to $1$.

For $a=3$, writing $x_i=b_i-1$ gives
$$
\sum_i x_i=0,
\qquad
\sum_i x_i^2=2.
$$
Hence one $x_i=1$, one $x_j=-1$, and all others are zero, giving
$(2,1,1,1,1,1,1,0)$.

For $a=4$, again put $x_i=b_i-1$. Then
$$
\sum_i x_i=3,
\qquad
\sum_i x_i^2=3.
$$
Since
$$
\sum_i x_i(x_i-1)=0
$$
and every integer $x_i\ge-1$ has $x_i(x_i-1)\ge0$, each $x_i$ is $0$ or
$1$. Exactly three are $1$, giving $(2,2,2,1,1,1,1,1)$.

For $a=5$, put $y_i=b_i-2$. Then
$$
\sum_i y_i=-2,
\qquad
\sum_i y_i^2=2.
$$
Thus exactly two $y_i$ equal $-1$ and the rest are zero, giving
$(2,2,2,2,2,2,1,1)$.

For $a=6$, the same substitution gives
$$
\sum_i y_i=1,
\qquad
\sum_i y_i^2=1.
$$
Hence exactly one $y_i=1$, giving $(3,2,2,2,2,2,2,2)$.

The numbers of permutations are
$$
8,\ 28,\ 56,\ 56,\ 56,\ 28,\ 8,
$$
whose sum is
$$
\boxed{240}.
$$
:::

:::

::: {.pf-step #r8-classes-realized-unique}
Every class in step [](#r8-classes-two-forty){.pf-ref} is represented by exactly one irreducible
nonsingular rational curve. Hence for $r=8$ there are exactly $240$
negative curves, and there are no others.

::: pf-proof
As in step [](#r7-classes-realized-unique){.pf-ref}, apply an admissible transformation at three points with
largest multiplicities. Direct substitution in step [](#quadratic-transform-basis-change){.pf-ref} gives the degree
reductions
$$
6\longmapsto5\longmapsto4\longmapsto2\longmapsto1\longmapsto0
$$
for the corresponding rows, while the degree-$3$ row maps to the
degree-$2$ row. Thus every listed class reduces to an exceptional divisor.
Reversing the admissible sequence produces a smooth rational representative
of that class on the original surface.

Uniqueness again follows from negative self-intersection: two distinct
irreducible curves in the same class would have intersection $-1$. Finally
step [](#negative-curve-is-minus-one-curve){.pf-ref} excludes every other irreducible curve of negative
self-intersection. This completes (d).
:::

:::

::: {.pf-step #r9-orbit-unbounded-degree}
For $r=9$, the orbit of a line class under admissible
transformations contains classes of arbitrarily large plane degree.

::: pf-proof
Start with the line
$$
L=P_1P_2,
$$
whose strict-transform class is
$$
C_0=h-e_1-e_2.
$$
It is a nonsingular rational $(-1)$-curve. Suppose at some stage its image
has class
$$
C=dh-\sum_{i=1}^9m_i e_i,
\qquad
d>0,
\qquad
m_i\ge0.
$$
Because admissible transformations identify the marked blowups, $C$ remains
a rational $(-1)$-curve. Hence adjunction gives
$$
K_X\cdot C=-1,
$$
or equivalently
$$
\sum_{i=1}^9m_i=3d-1.
$$

Relabel so that
$$
m_1\le m_2\le m_3\le\cdots\le m_9.
$$
The sum of the three smallest multiplicities is at most one third of the
total:
$$
m_1+m_2+m_3
\le
\frac{3d-1}{3}
<
d.
$$
Since it is an integer,
$$
m_1+m_2+m_3\le d-1.
$$
Transform at these three points. Step [](#quadratic-transform-basis-change){.pf-ref} gives the new degree
$$
d'
=
2d-m_1-m_2-m_3
\ge
d+1.
$$
The new multiplicities at the three target base points are
$$
d-m_2-m_3,\qquad
d-m_1-m_3,\qquad
d-m_1-m_2.
$$
Each is positive because each pair sum is at most
$m_1+m_2+m_3\le d-1$; the other six multiplicities are unchanged. Thus the
same argument applies again.

Step [](#general-position-preserved-under-sequence){.pf-ref} guarantees that every successive nine-point configuration remains
in general position. Iterating therefore gives finite admissible sequences
for which the plane degree of the transform of $L$ tends to infinity.
:::

:::

::: {.pf-step #r9-infinitely-many-minus-one-curves}
The surface obtained by blowing up nine points in general position
contains infinitely many irreducible nonsingular rational $(-1)$-curves.

::: pf-proof
An admissible transformation acts on the marked Picard lattice by the
isometry of step [](#quadratic-transform-basis-change){.pf-ref}. Step [](#r9-orbit-unbounded-degree){.pf-ref} shows that the orbit of the line class
$$
h-e_1-e_2
$$
is infinite, because its plane-degree coefficient is unbounded.

This line class lies in the same orbit as an exceptional class: a quadratic
transformation centered at $P_1,P_2,P_3$ contracts the line $P_1P_2$ to the
target exceptional point $Q_3$, so on the blowups its class becomes
$e_3'$. Hence the orbit of an exceptional class is infinite.

For any finite admissible word, take an exceptional divisor on the terminal
marked blowup and pull it back through the induced isomorphism to the original
surface $X$. The result is an irreducible nonsingular rational curve of
self-intersection $-1$, and its Picard class is the corresponding orbit
element. Infinitely many orbit classes therefore give infinitely many
distinct curves on $X$. This proves (e).
:::

:::

::: pf-qed
Steps [](#six-point-condition-preserved){.pf-ref} and [](#six-points-general-position-iff){.pf-ref} prove (a), step [](#general-position-preserved-under-sequence){.pf-ref} proves (b), and steps [](#uncountable-field-lemma){.pf-ref}, [](#bad-locus-proper-closed){.pf-ref} and [](#dense-general-position-extension){.pf-ref}
prove (c). Steps [](#degree-bound-nonneg-square){.pf-ref}, [](#negative-curve-is-minus-one-curve){.pf-ref}, [](#minus-one-curve-numerics){.pf-ref}, [](#r7-classes-fifty-six){.pf-ref}, [](#r7-classes-realized-unique){.pf-ref}, [](#r8-classes-two-forty){.pf-ref} and [](#r8-classes-realized-unique){.pf-ref} classify all negative curves for $r=7,8$ and
give the counts $56$ and $240$, proving (d). Steps [](#r9-orbit-unbounded-degree){.pf-ref} and [](#r9-infinitely-many-minus-one-curves){.pf-ref} prove the
starred $r=9$ assertion (e).
:::

:::
:::
