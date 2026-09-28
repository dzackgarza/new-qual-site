---
schema: qual/card@1
id: P-AGH548IRREDCLASSES
kind: problem
title: Divisor classes on the cubic surface containing an irreducible curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.8*, whose retained companion solution is blank, and
    followed the printed hint through the cubic-surface blowup model, the 27
    (-1)-curves, Castelnuovo contraction, and the lower-degree del Pezzo
    surfaces. The key lemma used below is proved
    directly and does not invoke this exercise circularly: on X_r=Bl_r P^2
    for 2<=r<=6, every integral class nonnegative on all (-1)-curves is
    globally generated. If it has positive square, it has a smooth
    irreducible member. The proof contracts a zero-intersection (-1)-curve;
    if all intersections are positive, subtract -K and induct on
    anticanonical degree. X_2 is handled explicitly from the three
    base-point-free classes h, h-e_1, h-e_2. Necessity follows from adjunction:
    an irreducible curve of negative square is a line, and one of square zero
    is a degree-two rational conic.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete contraction/global-generation induction and the
    necessity argument. Made the anticanonical-degree-zero termination
    explicit, strengthened the positive-square lemma to a general smooth
    irreducible member, and independently enumerated the complementary
    degree-one square-minus-one classes in the conic case.
---

::: {.problem}
Show that a divisor class $D$ on the cubic surface contains an irreducible curve $\iff$ it contains an irreducible nonsingular curve $\iff$ it is either

a. one of the 27 lines, or

b. a conic (meaning a curve of degree 2) with $D^2=0$, or

c. $D . L \geqslant 0$ for every line $L$, and $D^2>0$.

Hint: Generalize (4.11) to the surfaces obtained by blowing up $2,3,4$, or 5 points of $\PP^2$, and combine with our earlier results about curves on $\PP^1 \times \PP^1$ and the rational ruled surface $X_1$, (2.18).
:::

::: {.solution}
Let
$$
S=X_6=\operatorname{Bl}_{P_1,\ldots,P_6}\PP^2
$$
be the cubic surface, with the six points in general position, and let
$$
H=-K_S
$$
be its anticanonical hyperplane class. Thus
$$
H^2=3,
$$
and the $27$ lines are exactly the $(-1)$-curves listed in
[[FE-SRFCUBIC]].

We first prove the linear-system lemma needed for the sufficiency of (c).

<1>1. For $2\le r\le6$, write
$$
X_r=\operatorname{Bl}_{P_1,\ldots,P_r}\PP^2,
\qquad
A_r=-K_{X_r}=3h-\sum_{i=1}^r e_i.
$$
If an integral divisor class $M$ on $X_r$ satisfies
$$
M\cdot E\ge0
$$
for every $(-1)$-curve $E\subseteq X_r$, then
$$
\boxed{\OO_{X_r}(M)\text{ is globally generated}.}
$$

::: {.proof}
We prove this by induction on $r$, and for fixed $r$ by induction on the
nonnegative anticanonical degree
$$
A_r\cdot M.
$$
The nonnegativity of this degree follows from the explicit decompositions of
$A_r$ into $(-1)$-curve classes recorded in step <1>3 below.

The base $r=2$ is proved in step <1>2. Assume $r>2$ and the assertion known
for $X_{r-1}$.

If there is a $(-1)$-curve $E$ with
$$
M\cdot E=0,
$$
contract it:
$$
\sigma:X_r\longrightarrow X_{r-1}.
$$
Because
$$
\Pic X_r=\sigma^*\Pic X_{r-1}\oplus\ZZ E
$$
and $E^2=-1$, the equality $M\cdot E=0$ says precisely that
$$
M=\sigma^*M'
$$
for a divisor class $M'$ on $X_{r-1}$.

Every $(-1)$-curve $F'$ on $X_{r-1}$ avoids the point contracted from $E$.
Indeed, if $F'$ passed through that point, its strict transform $F$ would
satisfy
$$
(-K_{X_r})\cdot F
=
(-K_{X_{r-1}})\cdot F'-1
=0,
$$
contradicting ampleness of $-K_{X_r}$. Hence the strict transform of $F'$ is
a $(-1)$-curve on $X_r$, and
$$
M'\cdot F'=M\cdot F\ge0.
$$
The outer induction gives global generation of $M'$, hence of
$M=\sigma^*M'$.

It remains to treat the case
$$
M\cdot E>0
$$
for every $(-1)$-curve $E$. Since all intersections are integers,
$$
M\cdot E\ge1.
$$
Put
$$
N=M-A_r.
$$
Every $(-1)$-curve satisfies
$$
A_r\cdot E=1,
$$
so
$$
N\cdot E=M\cdot E-1\ge0.
$$
Step <1>3 shows that $A_r$ is a positive integral sum of $(-1)$-curve
classes. Hence
$$
A_r\cdot N\ge0.
$$
Also
$$
A_r\cdot N=A_r\cdot M-A_r^2<A_r\cdot M.
$$
The inner induction therefore makes $N$ globally generated. Since $A_r$ is
very ample for the del Pezzo surfaces of degree
$$
A_r^2=9-r\ge3,
$$
Exercise II.7.5(d), [[P-AGH275AMPLEPROPS]], shows that
$$
M=A_r+N
$$
is very ample, in particular globally generated.

This induction is well-founded also at anticanonical degree zero. Indeed, if
$A_r\cdot M=0$ and every intersection $M\cdot E$ with a $(-1)$-curve were
positive, the positive line decomposition of $A_r$ in step <1>3 would force
$A_r\cdot M>0$. Thus at degree zero the zero-intersection contraction case
applies until the explicit $r=2$ base is reached.
:::

<1>2. The global-generation assertion of step <1>1 holds on
$$
X_2=\operatorname{Bl}_{P_1,P_2}\PP^2.
$$

::: {.proof}
Write
$$
M=ah-b_1e_1-b_2e_2.
$$
The three $(-1)$-curves are
$$
E_1=e_1,
\qquad
E_2=e_2,
\qquad
L_{12}=h-e_1-e_2.
$$
The hypotheses give
$$
b_1=M\cdot E_1\ge0,
\qquad
b_2=M\cdot E_2\ge0,
$$
and
$$
c:=a-b_1-b_2=M\cdot L_{12}\ge0.
$$
Hence
$$
M
=
c h
+
b_1(h-e_1)
+
b_2(h-e_2).
$$

The class $h$ is the pullback of the line system on $\PP^2$, while
$h-e_i$ is the base-point-free pencil of lines through $P_i$. Thus all three
summand line bundles are globally generated. Nonnegative tensor products of
globally generated line bundles are globally generated, proving the claim.
:::

<1>3. For every $2\le r\le6$, the anticanonical class $A_r$ is a positive
integral sum of $(-1)$-curve classes.

::: {.proof}
Write
$$
L_{ij}=h-e_i-e_j.
$$
For $r=2$,
$$
A_2=3L_{12}+2e_1+2e_2.
$$
For $r=3$,
$$
A_3=L_{12}+L_{13}+L_{23}+e_1+e_2+e_3.
$$
For $r=4$,
$$
A_4=2L_{12}+L_{34}+e_1+e_2.
$$
For $r=5$, let
$$
G=2h-e_1-e_2-e_3-e_4-e_5,
$$
the strict transform of the conic through the five points; it is a
$(-1)$-curve. Then
$$
A_5=G+L_{12}+e_1+e_2.
$$
Finally,
$$
A_6=L_{12}+L_{34}+L_{56}.
$$
Expanding each right-hand side gives
$$
3h-\sum_{i=1}^r e_i=A_r.
$$
:::

<1>4. Under the hypotheses of step <1>1, if moreover
$$
M^2>0,
$$
then a general member of $|M|$ is a nonsingular irreducible curve.

::: {.proof}
We refine the induction in step <1>1.

First take $r=2$. The decomposition there writes
$$
M=ch+b_1(h-e_1)+b_2(h-e_2)
$$
with $c,b_1,b_2\ge0$.

If $c>0$, the complete system $|M|$ contains, after multiplying by a section
of the remaining globally generated factor which is nonzero on a dense
open, the ratios of the system $|ch|$. The latter is the blowdown
$X_2\to\PP^2$ followed by the $c$-uple Veronese embedding. Hence the
morphism defined by $|M|$ is generically one-to-one, in particular
separable, and has two-dimensional image.

If $c=0$, then
$$
M^2=2b_1b_2>0
$$
forces
$$
b_1,b_2>0.
$$
The two pencils $|h-e_1|$ and $|h-e_2|$ define a birational morphism
$$
X_2\longrightarrow\PP^1\times\PP^1.
$$
Indeed, after taking
$$
P_1=[1:0:0],
\qquad
P_2=[0:1:0],
$$
it is, on the dense chart $z\ne0$,
$$
[x:y:z]
\longmapsto
([y:z],[x:z]),
$$
which recovers $x/z$ and $y/z$. The positive tensor powers
$b_1,b_2$ followed by the Segre--Veronese embedding remain generically
one-to-one. Thus in this case too the morphism of $|M|$ is separable with
two-dimensional image.

Bertini's theorem for a base-point-free separable system gives a nonsingular
general member, and Bertini irreducibility for a system with
two-dimensional image makes it irreducible.

Now let $r>2$. If $M\cdot E=0$ for some $(-1)$-curve, step <1>1 writes
$$
M=\sigma^*M'
$$
on the contraction $\sigma:X_r\to X_{r-1}$, with
$$
(M')^2=M^2>0.
$$
By induction a general member of $|M'|$ is nonsingular and irreducible.
Since $M'$ is globally generated, the members passing through the contraction
point form a proper hyperplane in $|M'|$; choose the general smooth member
outside that hyperplane. Its pullback is isomorphic to it and is a
nonsingular irreducible member of $|M|$.

If $M\cdot E>0$ for every $(-1)$-curve, step <1>1 proves that $M$ is very
ample. A general hyperplane section of the corresponding embedding is
nonsingular and irreducible by Bertini. This completes the induction.
:::

<1>5. Let $C\subseteq S$ be an irreducible curve and put
$$
d=H\cdot C>0.
$$
Then
$$
\boxed{C^2\ge d-2.}
$$

::: {.proof}
Adjunction and $K_S=-H$ give
$$
2p_a(C)-2=C^2-d.
$$
Because $C$ is an integral projective curve,
$$
p_a(C)=h^1(C,\OO_C)\ge0.
$$
Therefore
$$
C^2-d\ge-2,
$$
which is the displayed inequality.
:::

<1>6. If an irreducible curve $C$ on $S$ has
$$
C^2<0,
$$
then $C$ is one of the $27$ lines.

::: {.proof}
Step <1>5 gives
$$
d-2\le C^2<0.
$$
Since $d$ is a positive integer, this forces
$$
d=1,
\qquad
C^2=-1.
$$
An irreducible degree-one curve in the given embedding
$$
S\subseteq\PP^3
$$
is a projective line. Thus $C$ is one of the $27$ lines on $S$.
:::

<1>7. If an irreducible curve $C$ is not a line and satisfies
$$
C^2=0,
$$
then
$$
\boxed{H\cdot C=2,
\qquad
p_a(C)=0.}
$$
Thus $C$ is a conic.

::: {.proof}
Step <1>5 gives
$$
d\le2.
$$
The adjunction formula becomes
$$
2p_a(C)-2=-d.
$$
If $d=1$, its right-hand side is odd, impossible. Hence
$$
d=2,
$$
and then
$$
p_a(C)=0.
$$
In the anticanonical embedding a degree-two irreducible curve is a conic.
:::

<1>8. If $C$ is an irreducible curve which is neither a line nor a conic of
self-intersection zero, then its class satisfies condition (c):
$$
\boxed{C\cdot L\ge0\text{ for every line }L,
\qquad
C^2>0.}
$$

::: {.proof}
If $L$ is any line and $C\ne L$, the two distinct irreducible curves have
nonnegative intersection number:
$$
C\cdot L\ge0.
$$
Since $C$ is not a line, step <1>6 excludes negative self-intersection; since
it is not a conic of square zero, step <1>7 excludes zero self-intersection.
Therefore
$$
C^2>0.
$$
This proves the necessity of alternatives (a)--(c).
:::

<1>9. Every class in alternative (a) contains an irreducible nonsingular
curve.

::: {.proof}
Alternative (a) is, by definition, one of the $27$ line classes. The
corresponding line
$$
L\cong\PP^1
$$
is itself nonsingular and irreducible.
:::

<1>10. Every class in alternative (b) contains an irreducible nonsingular
conic.

::: {.proof}
Let $D$ satisfy
$$
H\cdot D=2,
\qquad
D^2=0.
$$
Put
$$
E=H-D.
$$
Then
$$
H\cdot E=3-2=1
$$
and
$$
E^2
=
H^2-2H\cdot D+D^2
=
3-4
=-1.
$$
Also
$$
K_S\cdot E=-1.
$$
To identify $E$ without assuming effectivity, write
$$
E=ah-\sum_{i=1}^6 b_i e_i.
$$
The two numerical equalities are
$$
3a-\sum_i b_i=1,
\qquad
a^2-\sum_i b_i^2=-1.
$$
Hence
$$
\sum_i b_i=3a-1,
\qquad
\sum_i b_i^2=a^2+1.
$$
Cauchy--Schwarz gives
$$
(3a-1)^2\le6(a^2+1),
$$
so
$$
3a^2-6a-5\le0.
$$
Thus the integer $a$ is one of
$$
0,1,2.
$$
For $a=0$, the equations force one $b_i=-1$ and the rest zero, giving
$E=e_i$. For $a=1$, they force exactly two $b_i=1$, giving
$E=h-e_i-e_j$. For $a=2$, they force exactly five $b_i=1$, giving
$$
E=2h-\sum_{j\ne i}e_j.
$$
These are precisely the $27$ line classes [[FE-SRFCUBIC]]. Hence
$$
E\sim L
$$
for a line $L\subseteq S$, and
$$
D\sim H-L.
$$

The planes through $L$ cut divisors
$$
L+Q_\Pi\in|H|,
$$
where the residual curves $Q_\Pi$ have class $H-L=D$. As proved directly in
[[P-AGH547GENUSBOUND]], a general residual conic in this pencil is
nonsingular and irreducible. Thus $D$ contains such a conic.
:::

<1>11. Every class in alternative (c) contains an irreducible nonsingular
curve.

::: {.proof}
For the cubic surface $S=X_6$, the lines are exactly its $(-1)$-curves.
Condition (c) says precisely that
$$
D\cdot E\ge0
$$
for every $(-1)$-curve $E$, and that
$$
D^2>0.
$$
Step <1>4, applied with $r=6$ and $M=D$, therefore gives a nonsingular
irreducible member of $|D|$.
:::

<1>12. A divisor class on the cubic surface contains an irreducible curve if
and only if it contains an irreducible nonsingular curve, and this happens
exactly in alternatives (a), (b), and (c).

::: {.proof}
If the class contains an irreducible curve, steps <1>6--<1>8 place it in one
of the three alternatives. Conversely, steps <1>9--<1>11 show that every
class in one of those alternatives contains an irreducible nonsingular
curve. A nonsingular irreducible curve is in particular irreducible, so the
two existence conditions are equivalent and both are equivalent to the
classification (a)--(c).
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 establish the lower-degree del Pezzo linear-system lemma
suggested by the hint. Steps <1>5--<1>8 prove necessity, and steps
<1>9--<1>12 prove sufficiency and the equivalence of the two existence
conditions.
:::
:::
