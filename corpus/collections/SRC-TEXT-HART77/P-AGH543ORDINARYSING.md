---
schema: qual/card@1
id: P-AGH543ORDINARYSING
kind: problem
title: Reduction of a plane curve to ordinary singularities by quadratic transformations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Blowups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.3 and the retained Egbert pointer to Hirschfeld,
    together with the exercise's prescribed V.3.8 resolution input and the
    quadratic-transform formulas of V.4.2. When projection from a chosen bad
    point is separable, a point blowup can be realized inside a quadratic
    transformation by taking the other two base points generally off the
    curve; the three fundamental lines may then be chosen transverse away
    from the chosen centre, so their contractions create only ordinary
    multiple points. In positive characteristic this pencil argument can fail
    at a strange/inseparable centre. The retained source explicitly sends
    that characteristic-free case to Hirschfeld, Algebraic Curves over
    Finite Fields, Theorem 3.27, so the proof below does not silently extend
    the separable argument across that obstruction.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof after separating the separable-pencil argument
    from the positive-characteristic inseparable case. Verified the common
    blowup geometry and ordinary-singularity calculation against V.4.2; the
    inseparable case is attributed only to the Hirschfeld theorem explicitly
    cited by the retained source, rather than extrapolated from Bertini.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.4,
    exercise 4.3, printed page 407. Checked the multiplicity accounting of steps
    s1 to s6 against V.4.2, printed page 406: for a quadratic transformation
    centred at P, A, B with multiplicities m, 0, 0 the strict transform has
    degree 2d-m and the multiplicities at the three points corresponding to the
    fundamental lines PA, PB, AB are d-m, d-m and d, so the three contraction
    points are ordinary d-fold and (d-m)-fold points formed from the d and d-m
    transverse intersection points of those lines with C. Checked that the
    auxiliary choice in step choose-auxiliary-points is made with lines outside
    the tangent cone at P, which is what makes i_P(C,PA) = mu_P(C), and that
    separability of the projection is carried as a hypothesis on that step.
    Searched outside the twelve retained sets: Egbert, PDF p. 286, is the single
    line "See Algebraic Curves over Finite Fields by Hirschfeld, Theorem 3.27",
    and Hirschfeld's book is not in tmp/sources; Algebraic Geometry II,
    National Taiwan University, 2020 Spring, Chapter V homework, Exercise 3 of
    section 4, PDF p. 15 (tmp/sources/ntu-ag2-chapter5.pdf), replaces the
    resolution blowups by quadratic transformations with two auxiliary centres
    and then analyses the multiplicity at P in a single chart, ending "so
    induction on this then we are done" without the case where every tangent
    direction must be separated; Yang Pi-Yeh, Hartshorne Solutions, exercise
    5.4.3, printed p. 109 (tmp/sources/lfwin-hartshorne-solutions.pdf), chooses
    the two points so that P1Pi meets C transversally at P1, notes
    mu(R_i) < mu(P_1), and concludes that the process stops with only ordinary
    singularities, but does not show that the contracted points are ordinary.
    Not checked: Hirschfeld's Theorem 3.27, which the card takes as its source
    for the inseparable case and which is not available here.
---

::: {.problem}
Let $C$ be an irreducible curve in $\PP^2$.
Then there exists a finite sequence of quadratic transformations, centered at suitable triples of points, so that the strict transform $C^{\prime}$ of $C$ has only ordinary singularities, i.e., multiple points with all distinct tangent directions (I, Ex.
5.14). Use (3.8).
:::

::: {.solution}
Call a singular point **bad** if it is not ordinary, i.e. if its tangent cone
does not consist of distinct lines with multiplicity one.

We first give the explicit reduction in the separable case.  The final step
records the positive-characteristic inseparable case separately, using the
source cited for this exercise rather than a false Bertini assertion for an
inseparable pencil.

::: pf

::: pf-step
If $C$ has no bad singularities, there is nothing to prove.

::: pf-proof
In this case every singular point is already an ordinary multiple point, so
the empty sequence of quadratic transformations has the required property.
:::

:::

::: {.pf-step #choose-auxiliary-points}
Let $P$ be a bad singular point of a current plane model
$$
C\subseteq\PP^2.
$$
Assume that projection from $P$ on the normalization of $C$ is separable.
There exist two points $A,B\in\PP^2\setminus C$ such that the three lines
$$
PA,
\qquad
PB,
\qquad
AB
$$
have the following properties:

- they contain no singular point of $C$ other than $P$;
- $AB$ meets $C$ transversely in distinct smooth points;
- $PA$ and $PB$ have intersection multiplicity
  $\mu_P(C)$ at $P$ and meet $C$ transversely in distinct smooth points
  away from $P$.

::: pf-proof
The singular locus of the integral plane curve is finite. A general line
avoids this finite set and is not tangent to the smooth locus, so it meets
$C$ transversely in distinct smooth points. This applies directly to the
unconstrained line $AB$.

Among the lines through the fixed point $P$, only finitely many tangent
directions occur in the tangent cone of $C$ at $P$. A line through $P$ whose
direction is not in that tangent cone satisfies
$$
i_P(C,L)=\mu_P(C).
$$
The pencil of lines through $P$ induces the projection morphism from the
normalization of $C$ to $\PP^1$. By hypothesis this map is separable. Hence
it is generically etale, so outside finitely many members of the pencil a
line through $P$ meets $C$ away from $P$ in distinct smooth transverse
points. Choose two such members with directions outside the tangent cone and
avoiding the finitely many other singular points. Pick $A$ and $B$ on these
two lines, off $C$, generally enough that the joining line $AB$ is also a
transverse line avoiding the singular locus. This gives the stated
properties.
:::

:::

::: {.pf-step #quadratic-transform-realizes-blowup}
Let
$$
\varphi:\PP^2\dashrightarrow\PP^{2\prime}
$$
be the quadratic transformation centered at
$$
P,A,B.
$$
On the common resolution
$$
S=\operatorname{Bl}_{P,A,B}\PP^2,
$$
the strict transform of $C$ near the exceptional curve over $P$ is exactly
the strict transform obtained by the ordinary point blowup of $P$.

::: pf-proof
The resolved quadratic transformation is the blowup of the three source
base points followed by the contraction of the three strict transforms of
the joining lines, as in [[P-AGH542QUADTRANSFORM]].

Let $E_P$ be the exceptional curve over $P$. The only two contracted curves
meeting $E_P$ are the strict transforms of $PA$ and $PB$, and they meet
$E_P$ at the two points representing their tangent directions at $P$.
By step [](#choose-auxiliary-points){.pf-ref} neither direction belongs to the tangent cone of $C$ at $P$.
Hence the strict transform of $C$ on $S$ does not meet $E_P$ at either of
those two points.

Consequently the second morphism, which contracts the three fundamental
lines, is an isomorphism in a neighbourhood of every point where the strict
transform of $C$ meets $E_P$. Thus the germs of the new plane curve along
the image of $E_P$ are exactly the germs produced by blowing up $C$ at $P$.
:::

:::

::: {.pf-step #contraction-points-ordinary}
The quadratic transformation in step [](#quadratic-transform-realizes-blowup){.pf-ref} creates only ordinary
singularities at the three contraction points of the fundamental lines.

::: pf-proof
Let
$$
m=\mu_P(C),
\qquad
d=\deg C.
$$
Because $A,B\notin C$, their multiplicities on $C$ are zero. V.4.2 therefore
gives target multiplicities
$$
d,
\qquad
d-m,
\qquad
d-m
$$
at the three contraction points.

More importantly, step [](#choose-auxiliary-points){.pf-ref} describes the branches there. The strict
transform of $AB$ meets the strict transform of $C$ in $d$ distinct points,
all transversely. Contracting $AB$ identifies these points to one target
point; on the inverse blowup they correspond to $d$ distinct points of the
exceptional curve, hence to $d$ distinct tangent directions. Thus the target
point is an ordinary $d$-fold point.

Likewise, Bezout and
$$
i_P(C,PA)=i_P(C,PB)=m
$$
show that after removing the contribution at $P$, each of $PA$ and $PB$
meets $C$ in exactly $d-m$ distinct transverse smooth points. Their
contractions therefore produce ordinary $(d-m)$-fold points. If $d-m$ is
$0$ or $1$, the corresponding target point is not singular, which is even
better.
:::

:::

::: {.pf-step #other-singularities-unchanged}
Every singularity of $C$ away from the three fundamental lines is
unchanged by the transformation.

::: pf-proof
The quadratic transformation is an isomorphism away from its three base
points and the three fundamental lines. By the choice in step [](#choose-auxiliary-points){.pf-ref}, those
lines contain no singular point of $C$ except the chosen point $P$, while
$A,B$ do not lie on $C$. Hence every other singular germ of $C$ lies in the
isomorphism locus and is carried isomorphically to the new plane model.
:::

:::

::: {.pf-step #one-blowup-replaced-safely}
Thus one quadratic transformation can replace one prescribed point
blowup at a bad singularity without introducing any new bad singularity.

::: pf-proof
By step [](#quadratic-transform-realizes-blowup){.pf-ref}, the germs lying over the chosen bad point $P$ are exactly those
obtained from its point blowup. Step [](#contraction-points-ordinary){.pf-ref} says all singularities introduced
by contracting the fundamental lines are ordinary. Step [](#other-singularities-unchanged){.pf-ref} says every
other old singularity is unchanged. Therefore the only possible bad
singularities after the quadratic transformation are precisely the bad
infinitely near singularities which the prescribed blowup of $P$ would
produce.
:::

:::

::: {.pf-step #resolution-sequence-exists}
The resolution result (3.8) cited in the exercise gives a finite
sequence of point blowups after which the strict transform of $C$ is
nonsingular.

::: pf-proof
This is exactly the curve-resolution input requested by the exercise. It
produces finitely many ordinary point blowups, each centered at a singular
point of the current strict transform, such that the final strict transform
is nonsingular. Equivalently, there are only finitely many bad infinitely
near singular germs which need to be eliminated.
:::

:::

::: {.pf-step #separable-case-induction}
Suppose every bad centre encountered in the resolution sequence has
separable projection. Then replacing the successive point blowups by the
quadratic transformations of steps [](#choose-auxiliary-points){.pf-ref}, [](#quadratic-transform-realizes-blowup){.pf-ref}, [](#contraction-points-ordinary){.pf-ref}, [](#other-singularities-unchanged){.pf-ref} and [](#one-blowup-replaced-safely){.pf-ref} gives, after finitely many
steps, a plane strict transform having only ordinary singularities.

::: pf-proof
Proceed through the finite point-blowup sequence of step [](#resolution-sequence-exists){.pf-ref}. At each bad
centre, choose the two auxiliary points generally as in step [](#choose-auxiliary-points){.pf-ref}. In
addition, avoid the finite set of ordinary singularities already present;
the same open conditions allow this.

Step [](#one-blowup-replaced-safely){.pf-ref} shows inductively that the quadratic transformation performs the
required next blowup on the bad germ and creates no new bad germ. Ordinary
singularities already present and away from the chosen fundamental lines are
preserved by step [](#other-singularities-unchanged){.pf-ref}, while the newly contracted-line singularities are
ordinary by step [](#contraction-points-ordinary){.pf-ref}.

After the finitely many prescribed centres have been processed, no bad
infinitely near singularity remains, because the corresponding point-blowup
sequence resolves the original curve. The remaining singularities of the
final plane model are therefore all ordinary multiple points with distinct
tangent directions.
:::

:::

::: {.pf-step #inseparable-case}
The same conclusion holds when an inseparable projection occurs in
positive characteristic.

::: pf-proof
This is the exceptional case for which the retained source of this exercise
does not use the general-pencil argument above.  It explicitly refers to
Hirschfeld, *Algebraic Curves over Finite Fields*, Theorem 3.27.  That
theorem is the characteristic-free quadratic-reduction theorem: an
irreducible plane curve is transformed by a finite sequence of quadratic
transformations to a plane model whose singularities are ordinary.

Thus, if the inductive construction reaches a bad point for which projection
is inseparable, apply Hirschfeld's theorem to the current irreducible plane
model.  It supplies the required finite remaining sequence of quadratic
transformations.  This is exactly the positive-characteristic case for which
the retained solution cites that theorem.
:::

:::

::: pf-qed
Steps [](#choose-auxiliary-points){.pf-ref}, [](#quadratic-transform-realizes-blowup){.pf-ref}, [](#contraction-points-ordinary){.pf-ref}, [](#other-singularities-unchanged){.pf-ref} and [](#one-blowup-replaced-safely){.pf-ref} show how to realize one required resolution blowup by a
quadratic transformation without creating nonordinary singularities whenever
the relevant projection is separable. Steps [](#resolution-sequence-exists){.pf-ref} and [](#separable-case-induction){.pf-ref} iterate this through
the finite resolution sequence in that case, and step [](#inseparable-case){.pf-ref} supplies the
inseparable positive-characteristic case from the source cited for V.4.3.
:::

:::
:::

::: {.remark title="Published solution"}
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise V.4.3, PDF p. 286: the whole of his solution is "See Algebraic Curves over Finite Fields by Hirschfeld, Theorem 3.27", which is not among the retained files, so there is no argument to check. The reduction above is that of the standard proof: (3.8) resolves $C$ by point blowups, and one point blowup at a bad point $P$ is realized by a quadratic transformation whose two other centres are chosen so that the joining lines meet $C$ at $P$ in exactly $\mu_P(C)$ and elsewhere transversely, which makes the three contracted lines ordinary multiple points and leaves every other germ unchanged; the only case it does not cover is an inseparable projection, steps [](#choose-auxiliary-points){.pf-ref} to [](#separable-case-induction){.pf-ref} being the separable one and [](#inseparable-case){.pf-ref} the citation he gives. Recorded in COMPLAINTS.
:::

::: {.remark title="Published solutions searched"}
The published treatments of this exercise are incomplete, so the card's own proof is what was checked against the book. Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework, Exercise 3 of §4 (solution by Shuang-Yen Lee), PDF p. 15, does choose two auxiliary centres through the bad point and analyse the chart $x=(t+\mu)y$, and its intent is the argument of steps [](#quadratic-transform-realizes-blowup){.pf-ref} to [](#one-blowup-replaced-safely){.pf-ref}; but its case analysis of the multiplicity at the image point ends "if there's a $k$ such that $e'_k+k=e$ since we can factor into linear equations such that every direction has multiplicity less than $e$ $…$ induction on this then we are done", and it never shows that the three contracted points are ordinary, which is the content of step [](#contraction-points-ordinary){.pf-ref}.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.4.3, printed p. 109, states the criterion correctly: choose $P_2,P_3$ so that $P_1P_i$ meets $C$ transversally at $P_1$, then $R_i$ is on neither fundamental line and $\mu(R_i)<\mu(P_1)$, so the process terminates. It does not show that the images of $R_i$ at the three contraction points are ordinary, and it does not separate the inseparable projection case.
:::
