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
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked for issue #121 against the printed exercise, Hartshorne V.4.15,
    printed pp. 423-424 (its parts (a)-(e), the starred (e) last). Rechecked
    the decisive computations of the card's own proof. degree-bound-nonneg-square:
    with c = b_3, at most six of the b_i are at least 3 in index, so
    sum b_i^2 <= (a-2c)^2 + 7c^2 = a^2 - 4ac + 11c^2, and 3c <= a gives
    11c < 4a; verified. r7-classes-fifty-six: (3a-1)^2 <= 7(a^2+1) gives
    a^2-3a-3 <= 0, so a <= 3, and the three rows give 7 + 21 + 21 + 7 = 56.
    r8-classes-two-forty: a <= 6 with the Cauchy-Schwarz equality case excluded
    because 5/2 is not an integer, and the seven rows give
    8+28+56+56+56+28+8 = 240; both sums and each row's multinomial count were
    recomputed. negative-curve-is-minus-one-curve: the descent
    a' = 2a-b_1-b_2-b_3 < a with b_i+b_j <= a is the standard quadratic
    transformation of an irreducible plane curve, and the process stops at
    plane degree 0, an exceptional divisor. r7-classes-realized-unique: two
    distinct irreducible curves in one class would have intersection -1, which
    is impossible on a smooth surface. Parts (a) and (c) were read but not
    re-derived: their steps are six-points-general-position-iff,
    six-point-condition-preserved, uncountable-field-lemma,
    bad-locus-proper-closed and dense-general-position-extension. Published
    sources read for this card and what each has: Egbert, printed p. 294,
    parts (a)-(d) with (d) as a list of eight families and no proof that no
    other negative curves exist, and (e) as a citation of Nagata; Dolgachev,
    Proposition 8.2.15, printed pp. 261-262, the count of (-1)-classes only;
    Yang Pi-Yeh, printed p. 112, (a)-(c) sketched, (d) the same two sums
    without the negative-curve assertion, (e) argued. No source has all five.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Checked for issue #121 against the printed exercise, Hartshorne V.4.15,
    printed p. 409, all five parts including the starred (e) on that one page
    (PDF p. 424). The line case is correct: the class h-e_1-e_2 has square
    1-1-1 = -1, and the pair bound b_i+b_j <= a is dropped only for it, which is
    what negative-curve-is-minus-one-curve says. The remark on published
    solutions gave Egbert's (d) as "seven and seven" families and Yang's (d) as
    seven rows for r=7; both counts are wrong. Egbert, printed p. 295, finds 7
    exceptional curves, 21 lines, 21 conics through 5 points and 7 cubics
    through 7 points with one doubled, and writes "Thus we have 14+42=56"; for
    r=8 he lists eight exceptional curves, 28 lines, 56 conics, 8 cubics, 56
    quartics, 28 quintics and the sextics as "the rest", which is 56 to make
    240. That is four families for r=7 and seven for r=8. Yang, printed p. 112,
    lists the same four rows for r=7 --- the tuples (0,1,0,0,0,0,0,0),
    (2,1,1,0,0,0,0,0), (2,1,1,1,1,1,0,0) and (3,2,1,1,1,1,1,1) at 7, 21, 21 and
    7, totalling 7+21+21+7=56 --- and seven rows for r=8, totalling
    8+28+56+56+56+28+8=240. Both sentences of the remark now say so. An
    undated sentence recording what an earlier version of
    negative-curve-is-minus-one-curve asserted is removed; the mathematics of
    the sentence it qualified, that the pair bound fails precisely in the line
    case, is kept. Part (c) is unchanged and stays unproved here: the
    properness in bad-locus-proper-closed is asserted and not derived, and that
    step and the qed remark say so. Not checked: the card's own 56 and 240
    tables were not re-enumerated, Dolgachev's Proposition 8.2.15 was not
    re-read, and nothing was searched for a published proof of the properness
    in (c). The event of 2026-11-16 above had been rewritten in place; it is
    restored to the text it was dated with, and the pages it gives there, 423
    and 424, are PDF pages. This note is its correction.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    Under issue #121 the solution is now a transcription, one step per printed
    statement, of what the listed sources prove about the five parts. Read at
    the printed places: M. Nagata, On rational surfaces II, Section 2(c)
    (non-special points), printed p. 279, Lemma 2.2 (corresponding base points),
    p. 278, Lemma 2.5 (independent generic points are non-special), p. 279,
    Proposition 3 (the criterion for special points), p. 279, Theorem 2a
    (bijection between pre-exceptional types and irreducible exceptional curves
    of the first kind), pp. 280--281, Theorem 4a (finitely many for r at most 8,
    infinitely many for r = 9), pp. 283--284, Theorem 3a, p. 282, and
    Proposition 12 (no irreducible negative curve that is not of the first kind
    unless the points are special), p. 293; I. Dolgachev, Topics in Classical
    Algebraic Geometry, Proposition 8.2.15 with its proof and its table,
    printed pp. 261--262, and Section 8.2.6, printed p. 263. The paper's text
    version marks pages only in ten-page blocks; every printed page above was
    read off the paper's own folios in the PDF, which give PDF 1 = printed 271
    and so PDF 7 = 277 for Lemma 2.1, PDF 8 = 278 for Lemma 2.2, PDF 9 = 279 for
    Lemma 2.5 and Proposition 3, PDF 12 = 282 for Theorem 3a, PDF 14 = 284 for
    Theorem 4a, and PDF 21--23 = 291--293 for Propositions 9 to 12. What the
    transcription proves: (b) from the definition and Lemma 2.2, (d) from
    Proposition 12 with Theorem 2a and Dolgachev's count, and (e) from the
    second half of Theorem 4a with Theorem 2a. What it does not prove, and does
    not supply, is named on the card and recorded in COMPLAINTS.md this day:
    part (a) beyond its printed criterion, and part (c) in full. This card's own
    proofs of the parts the sources do not cover --- the six-point class
    computation, the countable-union lemma, the closedness and properness of
    the bad locus, the density argument, and the 56 and 240 tables --- are
    removed from the solution rather than kept beside the transcription, and the
    arithmetic they carried was rechecked against Dolgachev's table and against
    Nagata's r = 8 list before it was dropped.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Checked against the book before the transcription: the exercise is printed
    on p. 409 (PDF p. 424) with parts (a)--(e) and the starred (e) last, the
    hint for (c) being the countable-union lemma and the hint for (e) being the
    line P_1P_2 whose strict transform is made to rise in degree, with the
    attribution to Kodaira and "Nagata [5, II, p. 283]"; Nagata's Theorem 4a,
    the reference the book's own note points at, is the theorem printed at
    pp. 283--284 of the paper. Also checked: Nagata's "Cremona transformation
    with centers within P_i" is by his Section 2(2) a product of
    F-admissible quadratic transformations, which is the class of sequences
    Hartshorne's definition quantifies over, so "general position" and
    "non-special with respect to Cremona transformations" are the same
    condition on ordinary configurations with no three collinear. Not checked:
    the printed pages of Nagata's Lemma 2.1, cited on the card for the formula
    relating the degree, the multiplicities and the invariants, since the text
    version fixes only the ten-page block.

---

::: {.problem}
Let $P_1, \ldots, P_r$ be a finite set of (ordinary) points of $\PP^2$, no 3 collinear.
We define an **admissible transformation** to be a quadratic transformation (4.2.3) centered at some three of the $P_i$ (call them $P_1, P_2, P_3$).

This gives a new $\PP^2$, and a new set of $r$ points, namely $Q_1, Q_2, Q_3$, and the images of $P_4, \ldots, P_r$.

We say that $P_1, \ldots, P_r$ are **in general position** if no three are collinear, and furthermore after any finite sequence of admissible transformations, the new set of $r$ points also has no three collinear.

(a) A set of 6 points is in general position if and only if no three are collinear and not all six lie on a conic.

(b) If $P_1, \ldots, P_r$ are in general position, then the $r$ points obtained by any finite sequence of admissible transformations are also in general position.

(c) Assume the ground field $k$ is uncountable.
Then given $P_1, \ldots, P_r$ in general position, there is a dense subset $V \subseteq \PP^2$ such that for any $P_{r+1} \in V$, $P_1, \ldots, P_{r+1}$ will be in general position.

Hint: Prove a lemma that when $k$ is uncountable, a variety cannot be equal to the union of a countable family of proper closed subsets.

(d) Now take $P_1, \ldots, P_r \in \PP^2$ in general position, and let $X$ be the surface obtained by blowing up $P_1, \ldots, P_r$.
If $r=7$, show that $X$ has exactly 56 irreducible nonsingular curves $C$ with $g=0$, $C^2=-1$, and that these are the only irreducible curves with negative self-intersection.
Ditto for $r=8$, the number being 240.

(e) For $r=9$, show that the surface $X$ defined in (d) has infinitely many irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$.

Hint: Let $L$ be the line joining $P_1$ and $P_2$.
Show that there exist finite sequences of admissible transformations such that the strict transform of $L$ becomes a plane curve of arbitrarily high degree.
This example is apparently due to Kodaira -- see Nagata $[5, II, p. 283]$.
:::

::: {.solution}
Let $X=\operatorname{Bl}_{P_1,\ldots,P_r}\PP^2$ be the blowup, with $h$ the class of the pullback of a line and $e_i$ the exceptional classes, so that $K_X=-3h+\sum_ie_i$. For a class $C=dh-\sum_im_ie_i$ the intersection form gives $C^2=d^2-\sum_im_i^2$, and the virtual genus of the virtual linear system $\mathcal L(d;\sum_im_iP_i)$ is
$$
vg=d^2-3d+2-\sum_i m_i(m_i-1),
$$
a quantity of the numerical type alone (Nagata, Section 1(3) and Section 2, printed pp. 276--277, with Lemma 2.1(iii) and Lemma 2.8). An irreducible curve of $X$ that is not one of the $e_i$ has, in Nagata's language, the class $\mathcal L(d;\sum_im_iP_i)$ with $m_i=m(P_i;C)$; Nagata's "grade" $I$ is the self-intersection and his "virtual genus" is the arithmetic genus (Section 1(3), printed p. 276).

The two conditions the exercise's parts (d) and (e) turn on are Nagata's:

- an irreducible curve of the first kind on $X$ is one with $C\cong\PP^1$ and $C^2=-1$, and by Lemma 2.1(iii) this is exactly $I(C)=-1$ and $vg(C)=0$;
- a numerical type $(d,m_1,\ldots,m_r)$ is *pre-exceptional* when it is similar to $(1,1,1,0,\ldots,0)$ with $r-2$ zeros, and by Theorem 3a (printed p. 282) a virtually connected system with $I=-1$ and $vg=0$ is of pre-exceptional type.

The transcription below proves (b), (d) and (e). Parts (a) and (c) are not proved by the sources listed, and the card says so at the two steps concerned rather than supplying the arguments.

::: pf

::: {.pf-step #general-position-is-non-special}
For ordinary points $P_1,\ldots,P_r$ of $\PP^2$ with no three collinear, being in general position is the same condition as being non-special with respect to Cremona transformations.

::: pf-proof
Nagata, Section 2(c), printed p. 279, calls the points non-special when for every Cremona transformation $T$ with centres within the $P_i$ the corresponding base points to the $P_i$ under $T$ are ordinary points of $T(S)$ no three of which are collinear; the corresponding base points are the $r$ points of Lemma 2.2, printed p. 278, which are exactly $r$ in number and satisfy $F=\operatorname{dil}_{(P_1',\ldots,P_r')}(T(S))$. By Section 2(2) of the paper a Cremona transformation with centres within the $P_i$ is by definition a product of $F$-admissible quadratic Cremona transformations, and $F$-admissible here means exactly that the centres are points of the configuration, so these are the finite sequences of admissible transformations of the exercise. The two definitions therefore quantify over the same sequences and require the same thing of the resulting configuration.
:::

:::

::: {.pf-step #general-position-preserved-under-sequence}
General position is preserved by every finite sequence of admissible transformations, which is part (b).

::: pf-proof
Let $\mathbf Q$ be obtained from a general-position configuration $\mathbf P$ by a finite admissible sequence $w$. By step [](#general-position-is-non-special){.pf-ref} the configuration $\mathbf P$ is non-special, so for every Cremona transformation $T$ with centres within its points the corresponding base points are ordinary with no three collinear; $w$ is such a transformation, so $\mathbf Q$ is itself a configuration of ordinary points, no three collinear. Applying the definition to $\mathbf Q$, a further finite sequence $v$ of admissible transformations from $\mathbf Q$ composed with $w$ is a finite sequence from $\mathbf P$ --- the same composition Nagata's Section 2(2) uses to make products of quadratic transformations the objects he quantifies over --- so its terminal configuration has no three collinear. As this holds for every $v$, $\mathbf Q$ is in general position.
:::

:::

::: {.pf-step #six-point-criterion}
Part (a) is not proved by the sources listed: what they print is its criterion, and the passage from that criterion to the two conditions of (a) is where the printed record stops.

::: pf-proof
The two conditions of part (a) are that no three of the six points are collinear and that not all six lie on a conic, which is part (a)'s own hypothesis, printed p. 409.
The criterion the sources print is Proposition 3 of Nagata, printed p. 279: ordinary points are special if and only if there is a numerical type $(d,m_1,\ldots,m_r)$ similar to $(1,1,1,0,\ldots,0)$ such that the effective system $\mathcal L^\oplus(d;\sum_im_iP_i)$ is not empty. For $r=6$ that criterion has to be turned into the two conditions of part (a) by enumerating the class of $(1,1,1,0,\ldots,0)$ with six base points, and no source listed for this card prints that enumeration: Nagata's own printed corollary that lists the conditions for a configuration is the one for eight ordinary points, printed p. 291, whose three conditions are a collinear triple, six points on a conic, and a cubic through all eight with a double point at one of them. Part (a) is therefore not proved here, and it is recorded in the complaints file.
:::

:::

::: {.pf-step #dense-extension-not-proved}
Part (c) is not proved by the sources listed.

::: pf-proof
What those sources print is the generic-point statement, Lemma 2.5 of Nagata, printed p. 279: if $P_1,\ldots,P_r$ are independent generic points of $S$ over the prime field, then they are non-special with respect to Cremona transformations. That is a statement about all $r$ points at once being generic, and it is not the statement of part (c), which fixes a configuration in general position and asks for a dense set of positions of one further point $P_{r+1}$. Neither does Nagata's proof of Lemma 2.5 give it: the proof transforms the finitely many generic points and observes that the transformed points are again generic over the prime field, so it establishes that the bad locus is a proper closed subset of the space of all $r$-tuples, not that it is proper after the first $r$ points are fixed. Hartshorne's hint for (c), printed p. 409, is the countable-union lemma for an uncountable field, and that lemma is not printed in either source. Part (c) is therefore not proved here, and it is recorded in the complaints file.
:::

:::

::: {.pf-step #every-negative-curve-is-exceptional}
Assume $r\le9$ and let the $P_i$ be in general position. Then every irreducible curve $C\subseteq X$ with $C^2<0$ is an irreducible exceptional curve of the first kind: $C\cong\PP^1$ and $C^2=-1$.

::: pf-proof
By step [](#general-position-is-non-special){.pf-ref} the points are non-special, so Proposition 12 of Nagata, printed p. 293, applies: for $r\le9$ the surface $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$ carries only finitely many irreducible curves that are not exceptional curves of the first kind and have negative grade, and the existence of such a curve is equivalent to the points being special. The points are not special, so no such curve exists; every irreducible curve of negative self-intersection is therefore an exceptional curve of the first kind, hence isomorphic to $\PP^1$ with self-intersection $-1$.
:::

:::

::: {.pf-step #classes-are-pre-exceptional}
For $r\le9$ and $P_1,\ldots,P_r$ in general position, the map sending an irreducible exceptional curve of the first kind to its numerical type is a bijection onto the set of pre-exceptional types with $r$ base points.

::: pf-proof
This is Theorem 2a of Nagata, printed pp. 280--281: if $P_1,\ldots,P_r$ are non-special with respect to Cremona transformations, there is a one-one correspondence between all pre-exceptional types $(d,m_1,\ldots,m_r)$ with $r$ base points and all irreducible exceptional curves of the first kind on $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$, in such a way that the curve corresponds to the type of $\operatorname{dil}(\mathcal L(d;\sum_im_iP_i))$. The proof runs by Lemma 2.6, which turns a pre-exceptional type into $\mathcal L(0;-P_1')$ over a Cremona transform with centres within the $P_i$ and so produces the curve, and by induction on the degree for the converse, using that $m_1+m_2+m_3>d$ for a curve of grade $-1$ and virtual genus $0$. Step [](#general-position-is-non-special){.pf-ref} supplies the hypothesis.
:::

:::

::: {.pf-step #count-fifty-six-and-two-forty}
The number of pre-exceptional types with $r$ base points is $56$ for $r=7$ and $240$ for $r=8$.

::: pf-proof
A pre-exceptional type has $I=-1$ and $vg=0$, and by Lemma 2.1(iii) of Nagata, printed p. 277, the invariants of a type satisfy $3d-\sum_im_i=I-2vg+2$, so a pre-exceptional type is a solution of
$$
d^2-\sum_{i=1}^r m_i^2=-1,\qquad 3d-\sum_{i=1}^rm_i=1
$$
up to permutation, and conversely. Dolgachev, Proposition 8.2.15 with its proof, printed pp. 261--262, solves exactly these two equations for the lattice $I^{1,N}$: the Cauchy--Schwarz bound $(3d-1)^2\le N(d^2+1)$ bounds the degree, the solutions are listed degree by degree --- $\mathbf e_i$ at $d=0$, then $\mathbf e_0-\mathbf e_i-\mathbf e_j$, then $2\mathbf e_0-\sum_{j=1}^N\mathbf e_j+\mathbf e_i+\mathbf e_j$, then $-\mathbf k_7-\mathbf e_i$ at $N=7$, and at $N=8$ the two families with $\mathbf k_8$ together with $-\mathbf k_8+2\mathbf e_{i_1}-\cdots-\mathbf e_{i_6}$ --- and Noether's inequality with the reflection $r_{\alpha_{123}}$ puts them in one orbit of $W(\mathbf E_N)$. His table, printed p. 262, gives $56$ for $N=7$ and $240$ for $N=8$, the same numbers as the number of pre-exceptional types by Theorem 2a of step [](#classes-are-pre-exceptional){.pf-ref}; Nagata's own list for $r=8$, in the proof of Theorem 4a, printed p. 284, is the same list. The permutation counts $7+21+21+7$ and $8+28+56+56+56+28+8$ were recomputed here and agree.
:::

:::

::: {.pf-step #part-d}
Part (d) holds: for $r=7$ the surface $X$ carries exactly $56$ irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$, and these are the only irreducible curves of negative self-intersection; for $r=8$ the numbers are $240$ and the same conclusion.

::: pf-proof
By step [](#every-negative-curve-is-exceptional){.pf-ref} every irreducible curve of negative self-intersection is an exceptional curve of the first kind, and by step [](#classes-are-pre-exceptional){.pf-ref} the exceptional curves of the first kind correspond one to one to the pre-exceptional types. Step [](#count-fifty-six-and-two-forty){.pf-ref} counts those types: $56$ for $r=7$ and $240$ for $r=8$. An exceptional curve of the first kind is by definition a nonsingular rational curve of self-intersection $-1$, so the count is the count of the curves the exercise asks for, and the same two steps say that there are no others of negative self-intersection.
:::

:::

::: {.pf-step #part-e}
Part (e) holds: for $r=9$ the surface $X$ carries infinitely many irreducible nonsingular curves $C$ with $g=0$ and $C^2=-1$.

::: pf-proof
This is the second half of Theorem 4a of Nagata, printed pp. 283--284: if $r\ge9$ and the $P_i$ are non-special, then $\operatorname{dil}_{(P_1,\ldots,P_r)}(S)$ carries infinitely many exceptional curves of the first kind. The proof given there is that $3d-\sum_im_i$ is an invariant of the similarity class by Lemma 2.8, so a pre-exceptional type satisfies $3d-\sum_im_i=1$; ordering $m_1\le\cdots\le m_r$ then gives $m_1+m_2+m_3\le(\sum_im_i)/3=(3d-1)/3<d$, so the operator $\mathfrak q$ of Section 2, which sends $(d,m_1,\ldots,m_r)$ to $(d+a,m_1+a,m_2+a,m_3+a,m_4,\ldots,m_r)$ with $a=d-m_1-m_2-m_3>0$, produces a pre-exceptional type of strictly larger degree. Iterating gives infinitely many pre-exceptional types with $r$ base points, and Theorem 2a of step [](#classes-are-pre-exceptional){.pf-ref} turns them into that many distinct irreducible exceptional curves of the first kind on $X$.
:::

:::

::: pf-qed
Steps [](#general-position-is-non-special){.pf-ref} and [](#general-position-preserved-under-sequence){.pf-ref} prove (b). Steps [](#every-negative-curve-is-exceptional){.pf-ref}, [](#classes-are-pre-exceptional){.pf-ref}, [](#count-fifty-six-and-two-forty){.pf-ref} and [](#part-d){.pf-ref} prove (d), and step [](#part-e){.pf-ref} proves the starred (e). Parts (a) and (c) are not proved: step [](#six-point-criterion){.pf-ref} records that the sources print the criterion for (a) but not the enumeration with six base points that turns it into (a), and step [](#dense-extension-not-proved){.pf-ref} records that the generic-point lemma they print is not the dense-extension statement of (c).
:::

:::
:::

::: {.remark title="Published solutions"}
The exercise is Hartshorne, *Algebraic Geometry* (1977), V.4, exercise 4.15, printed p. 409, all five parts on that one page, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`, whose printed page is its marker minus fifteen.

M. Nagata, *On rational surfaces, II*, Mem. Coll. Sci. Univ. Kyoto Ser. A 32 (1960), read in `tmp/sources/nagata-1960-rational-surfaces-ii.md`, is the source the book's own note cites ("see Nagata [5, II, p. 283]"), and its Theorem 4a is the printed theorem at those pages. What it contributes to this exercise: Section 2(c) with Lemma 2.2 for the identification of general position with non-speciality and for (b); Lemma 2.5 for the generic-point statement that (c) is a spreading-out of but is not; Proposition 3 for the printed criterion behind (a); Theorem 2a for the bijection between pre-exceptional types and irreducible exceptional curves of the first kind; Theorem 4a for finiteness at $r\le8$ and for the infinite family at $r=9$, which is the starred part (e); and Proposition 12 for the statement that an irreducible curve of negative self-intersection that is not of the first kind exists only when the points are special, which is the half of (d) that the count of classes does not give. The paper's text version marks pages only in ten-page blocks; the printed page numbers above are read off those blocks, with Lemma 2.5 at p. 279 and Theorem 4a at pp. 283--284 fixing them.

Igor V. Dolgachev, *Topics in Classical Algebraic Geometry*, Proposition 8.2.15 with its proof, printed pp. 261--262, and Section 8.2.6 with Lemma 8.2.18, printed pp. 263--264, read in `tmp/sources/dolgachev-topics-classical-ag.md` at line 9857 and in the PDF. Proposition 8.2.15 classifies and counts the vectors with $\mathbf k_N\cdot v=-1$ and $v^2=-1$, which are the classes with $C\cdot K_X=-1$ and $C^2=-1$, at $56$ for $N=7$ and $240$ for $N=8$; Section 8.2.6 explains why on a Del Pezzo surface the image of each exceptional vector is a $(-1)$-curve, which is Dolgachev's route to the same realization that Theorem 2a gives here. What the printed proof of 8.2.15 does not carry correctly is the degree bound: it writes that $(3d-1)^2\le N(d^2+1)$ gives $0\le d\le4$ for every $N$, whereas the inequality gives $d\le3$ at $N=7$ and $d\le6$ at $N=8$, and its own list for $N=8$ contains a vector of degree $6$, namely $6\mathbf e_0-3\mathbf e_1-2\mathbf e_2-\cdots-2\mathbf e_8$. The list and the count are right; the intermediate bound as printed is not, and it is the count that the card uses.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.15, printed p. 294 for part (a) --- the statement that one curve of order $m$ passes through $m(m+3)/2$ points, by induction on $m$ --- and p. 295 for the rest: (b) is the single line "This is Nagata, Rational Surfaces II, corollary to proposition 9, and use (a) of this problem", (c) is the general-position set as the complement of the vanishing of finitely many determinants, (d) is a list of four families for $r=7$ summing to $56$ and seven for $r=8$ whose counts make $240$, and there is no entry for the starred (e). His (b) cites the corollary at p. 291, which is the eight-point criterion and not the invariance of the definition.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.4.15, printed p. 112, argues four of the five parts and leaves the decisive half of (d): its (a) checks that six points on a conic land on a line after one transformation, (b) is the composability argument, (c) takes the union of the lines $P_iP_j$ and the conics through five points and observes that its complement is dense because $k$ is uncountable --- the printed hint's lemma used and not proved --- (d) lists the four rows for $r=7$ and the seven for $r=8$, and says nothing about which classes are represented by irreducible curves nor about negative curves that are not $(-1)$-curves, and (e) is the degree-increasing argument, labelled by him "the case $r>9$".
:::
