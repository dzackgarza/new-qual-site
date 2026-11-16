---
schema: qual/card@1
id: P-AGH5111FINITEAUT
kind: problem
title: Finiteness of effective classes of fixed degree, and finiteness of the automorphism group of a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Adjunction
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.11, the retained Egbert companion sketch, and the local
    Hodge-index, Nakai--Moishezon, adjunction, and diagonal calculations. The
    companion sketch does not supply the required boundedness argument in
    Num(X). The proof below decomposes numerical classes into the ample
    direction and its negative-definite orthogonal complement; adjunction makes
    the orthogonal component of every irreducible curve of bounded H-degree
    uniformly bounded, after which lattice discreteness and the bounded number
    of effective components give finiteness.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.1,
    exercise 1.11, printed page 368 (PDF page 383 of the extraction), with the
    printed hint. Checked the proof step by step: Hodge index on H^perp is
    V.1.9, with the printed hint of V.1.9 giving the signature; H^2 > 0 and
    H.C > 0 for an irreducible C are Nakai-Moishezon; adjunction is V.1.3,
    printed page 361; Num X is free abelian of finite rank by Remark V.1.7.1,
    so it is a lattice in Num X tensor R. Located two published treatments
    outside the twelve retained sets. Algebraic Geometry II, National Taiwan
    University, 2020 Spring, Chapter V homework, Exercise 11 (Shuang-Yen Lee),
    PDF p. 4, downloaded to tmp/sources/ntu-ag2-chapter5.pdf, proves (a) and
    (b) by the same route, but its displayed estimate for the sum of the
    c_i^2 does not follow from its adjunction line, so steps s1 to s3 are the
    corrected bookkeeping rather than a transcription. Yang Pi-Yeh,
    Hartshorne Solutions, exercise 5.1.11, printed p. 101
    (tmp/sources/lfwin-hartshorne-solutions.pdf), never bounds the
    coefficients. Not checked: whether the NTU set's constant A is uniform in
    h; the card does not use that constant.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the printed exercise at Hartshorne (1977), V.1, exercise 1.11, printed
    p. 368 (PDF p. 383), and the National Taiwan University set's Exercise 11
    (Shuang-Yen Lee) in the text version tmp/sources/ntu-ag2-chapter5.md, printed
    p. 4 of that set, on 2026-11-16. The published argument is the card's route:
    Hodge index gives a basis in which the form is diag(1,-1,...,-1) with h =
    H/sqrt(H^2); an irreducible curve has c_0 at least 1/sqrt(H^2) because it meets
    H positively; adjunction gives c_0(c_0+k_0) - sum c_i(c_i+k_i) = 2p_a - 2 at
    least -2; and the conclusion is that D_d is contained in a bounded set with
    v_0 fixed. Its displayed intermediate inequality, sum c_i^2 at most
    c_0^2 + c_0k_0 + 2 + k_0^2/2, does not follow from the adjunction identity,
    which bounds sum(c_i^2 + c_ik_i) and reaches sum c_i^2 only through
    2|c_ik_i| at most c_i^2 + k_i^2, costing a factor two and adding sum k_i^2, so
    steps s1 to s3 remain the card's corrected bookkeeping and are not a
    transcription. Yang Pi-Yeh, exercise 5.1.11, never bounds the coefficients of
    the curves occurring in D + sum a_iR_i, as recorded above. Not checked: the
    argument over a base field that is not algebraically closed.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Re-read the National Taiwan University set's Exercise 11 in its text version
    on 2026-11-16 and corrected what the remark says it proves. Its part (a) is
    the route of steps s1 to s3 in the corrected bookkeeping. Its part (b) is the
    printed hint alone: from Gamma equivalent Delta it derives
    Gamma.Delta = Delta^2 = 2-2g < 0, hence Gamma = Delta, and then applies (a)
    to the graphs with Gamma.(l+m) = 2. It never shows that distinct
    automorphisms have numerically inequivalent graphs, which is step s8; that
    step is what turns finitely many numerical classes into finitely many
    automorphisms, and it is supplied here by the surface automorphism
    id x tau^{-1}. The set's (b) therefore proves only that no automorphism other
    than the identity has a graph numerically equivalent to the diagonal. Not
    checked: whether some other published set supplies step s8; none in
    tmp/sources does.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Restored the event of 2026-11-11 above to its text of that date, undoing the
    naming of a text version that a later commit of 2026-11-16 inserted into it;
    that naming belongs in the citations, and every source cited in the remark
    names its text version. Re-read the National Taiwan University set in its
    text version on 2026-11-16 for its pagination: the printed pages of that set
    are its PDF pages, Exercise 4 on p. 2, Exercise 11 on p. 4, Exercise 12 with
    the two Exercises 1 and 2 of section 2 on p. 5, and Exercise 3 of section 2
    on p. 6. Nothing else in the events above changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Transcribed part (a) from Math StackExchange answer 4775583 by KReiser
    (2023-09-26) to question 4449474, read in its text version
    tmp/sources/mse-4449474-hart-v111a-finite-automorphisms.md, and part (b) from
    Proof 2 of Dan Bragg, "Automorphisms of curves" (2015-11-20), read in
    tmp/sources/bragg-2015-automorphisms-of-curves.md, and re-read the printed
    exercise at Hartshorne, Algebraic Geometry (1977), V.1, exercise 1.11,
    printed p. 368 (PDF p. 383), with its hint. Steps s1, s2 are the answer's
    first three displays, with the book's adjunction (Theorem V.1.3, printed
    p. 361), Hodge index (Theorem V.1.9, printed p. 364) and Nakai--Moishezon
    (Theorem V.1.10, printed p. 365) named where they enter. Checked the
    answer's two closing displays and found that neither follows: the step from
    minus the sum of b_i^2(D_i.K+2) to -d D.K - 2d^2 needs D_i.K at most 0 for
    every component, and the final sentence bounds (D-E)^2 by an expression
    linear in D, so no ellipsoid and no uniformity. Step s3 therefore carries
    the bound as the card's, and part (a) stays without a complete published
    proof; COMPLAINTS.md records it on this date. Part (b) is Bragg's Proof 2
    in steps s6 to s10: the injection Aut C to Num(C x C) through
    nonnegativity of intersections of distinct irreducible curves, and the
    fixed intersection 4g-4 of every graph with the canonical divisor, which
    step s8 proves ample by Nakai--Moishezon since Bragg only says "a fixed
    ample divisor". Bragg asserts Gamma^2 = 2-2g for every graph without
    argument and step s6 supplies the normal-bundle reason. Not checked: whether
    a published treatment of part (a) exists outside the sources named for this
    batch.

- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the card against a reading of the sources on 2026-11-16, after the
    events above of the same date. Three statements are withdrawn. First, the
    direction of the inequality: replacing b_i^2 by b_id under D_i.K_X follows
    from b_i at most d when D_i.K_X is at least 0, not at most 0, so the display
    is reached when K_X is nef, and the event above stating the opposite is
    wrong. Second, the closing display of Math StackExchange answer 4775583 does
    confine D-E: the right hand side is, for fixed E, an affine function of
    D-E, so with the intersection form negative definite on H^perp the
    inequality bounds its norm, and the record calling it no ellipsoid is wrong.
    Third, part (a) is not wholly a transcription: step s3 is the answer's bound
    under the sign condition, step s4 is the card's own bound and holds without
    it, and the qed now says which step is which. Two citations are corrected:
    adjunction for a possibly singular effective divisor is Exercise V.1.3(a),
    printed p. 366, read in the text version, and for a nonsingular curve it is
    Proposition V.1.5, printed p. 361, not Theorem V.1.3, which is the
    definition of C.D on printed p. 358. Bragg's Proof 2 has two paragraphs, so
    the locators in steps s9 to s11 are the first and the second of them, and
    "both degrees being at least one" is corrected to their sum being at least
    one, since the projection to the base of a ruling is constant on a slice.
    Not checked: whether some published treatment bounds D^2 uniformly for a
    surface whose K_X is not nef; the card's step s4 does, as its own argument.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Restored steps s4 and s5 on 2026-11-16 to the argument the card carried
    before this batch, on the reader's report, and left every event above as
    written. Step s4 is the ball estimate on the class of one irreducible curve
    C with 1 at most C.H at most d: adjunction C^2 + K.C at least -2, the
    decomposition of C and of K_X along H, and Cauchy-Schwarz on H^perp bound
    the H^perp-component, and the coefficient of H is bounded by d. Step s5 is
    the count: for D = sum n_iC_i, every C_i.H is between 1 and d and sum n_i
    is at most d, so [D] is a finite sum of elements of the finite set of step
    s4. Both steps are the card's own and need no sign condition. The two
    pieces this batch's repair had written in their place are withdrawn: the
    claim that D^2 is bounded below by a constant -C_d, and a step that ran the
    answer's ball argument on that bound; its sentence "Adding the inequalities
    of step s3, or the bound -C_d of step s4, ... gives [the display]" was
    false, since only step s3 gives that display, the bound -C_d giving instead
    (D-E)^2 at least -2v.E - C_d - E^2 with v = D-E, a different affine bound.
    Part (a) for a surface with a component of negative K_X-degree therefore
    rests again on the card's steps s4 and s5 and on no published argument. In
    step s10 the reason "D maps finitely to both factors" is withdrawn: it is
    false for the rulings, whose projection to the second factor is constant,
    and the sentence now says that D is not a point under both projections, so
    the two degrees sum to at least one. Not checked: whether a published
    treatment of part (a) covers a component of negative K_X-degree.

---

::: {.problem}
In this problem, we assume that $X$ is a surface for which $\Num X$ is finitely generated (i.e., any surface, if you accept the Néron-Severi theorem (Ex.
1.7)).

(a) If $H$ is an ample divisor on $X$, and $d \in \ZZ$, show that the set of effective divisors $D$ with $D . H=d$, modulo numerical equivalence, is a finite set.

Hint: Use the adjunction formula, the fact that $p_a$ of an irreducible curve is $\geqslant 0$, and the fact that the intersection pairing is negative definite on $H^{\perp}$ in $\Num X$.

(b) Now let $C$ be a curve of genus $g \geqslant 2$, and use (a) to show that the group of automorphisms of $C$ is finite, as follows.
Given an automorphism $\sigma$ of $C$, let $\Gamma \subseteq X=C \times C$ be its graph.
First show that if $\Gamma \equiv \Delta$, then $\Gamma=\Delta$, using the fact that $\Delta^2<0$, since $g \geqslant 2$ (Ex.
1.6). Then use (a). Cf.
(IV, Ex.
2.5).

:::

::: {.solution}
Let
$$
N=\Num X,
\qquad
N_\RR=N\tensor_\ZZ\RR .
$$
Because $N$ is finitely generated and numerical equivalence has no torsion, $N$ is a lattice in $N_\RR$.

::: pf

::: {.pf-step #s1}
The intersection form is negative definite on
$$
H^\perp=\qty{v\in N_\RR\st v\cdot H=0},
$$
and
$$
N_\RR=\RR H\oplus H^\perp .
$$

::: pf-proof
Hartshorne, *Algebraic Geometry* (1977), Theorem V.1.9 (Hodge index theorem), printed p. 364, states that $D^2<0$ for every $D\not\equiv0$ with $D\cdot H=0$, which is the negative definiteness named by the printed hint to Exercise V.1.11, printed p. 368. The divisor $H$ is ample, so $H^2>0$ and $H\cdot C>0$ for every irreducible curve $C$ by the Nakai--Moishezon criterion, Theorem V.1.10, printed p. 365, and every $v\in N_\RR$ decomposes as
$$
v=\frac{v\cdot H}{H^2}H+\qty(v-\frac{v\cdot H}{H^2}H)
$$
with the second summand orthogonal to $H$.

:::

:::

::: {.pf-step #s2}
Let $D=\sum_ib_iD_i$ be an effective divisor with distinct prime components $D_i$ and $D\cdot H=d$. Then
$$
b_i\le d,
\qquad
\sum_ib_i^2\le d^2,
\qquad
D^2\ge\sum_ib_i^2D_i^2\ge-\sum_ib_i^2\qty(D_i\cdot K_X+2).
$$

::: pf-proof
The three displays are the first three steps of Math StackExchange answer 4775583 to question 4449474. Each $D_i$ is an integral curve and $H$ is ample, so $D_i\cdot H\ge1$, and $d=D\cdot H=\sum_jb_j(D_j\cdot H)$ gives $b_i\le d$ and $\sum_ib_i^2\le\qty(\sum_ib_i)^2\le d^2$. For the last display, Exercise V.1.3(a), printed p. 366, gives $2p_a(D_i)-2=D_i\cdot(D_i+K_X)$ for the effective divisor $D_i$, with $p_a$ as in III, Exercise 5.3; an integral projective curve has $p_a(D_i)\ge0$, so $D_i^2\ge-D_i\cdot K_X-2$. Two distinct irreducible curves on a surface meet in a finite set of points with positive multiplicities, so $D_i\cdot D_j\ge0$ for $i\ne j$ and
$$
D^2=\sum_ib_i^2D_i^2+2\sum_{i<j}b_ib_jD_i\cdot D_j\ge\sum_ib_i^2D_i^2 .
$$

:::

:::

::: {.pf-step #s3}
When $D_i\cdot K_X\ge0$ for every component,
$$
D^2\ge-d\,D\cdot K_X-2d^2 .
$$

::: pf-proof
This is the display of the same answer. Replacing $b_i^2$ by $b_id$ under $D_i\cdot K_X$ is the inequality
$$
b_i^2D_i\cdot K_X\le db_iD_i\cdot K_X,
$$
which follows from $b_i\le d$ when $D_i\cdot K_X\ge0$, and the constant term uses $\sum_ib_i^2\le d^2$ from step [](#s2){.pf-ref}:
$$
\sum_i-b_i^2\qty(D_i\cdot K_X+2)\ge-\sum_ib_idD_i\cdot K_X-2d^2=-d\,D\cdot K_X-2d^2 .
$$
The condition is satisfied in particular when $K_X$ is nef. For a component with $D_i\cdot K_X<0$ and $b_i<d$ the comparison is reversed, so this derivation does not reach such a surface; steps [](#s4){.pf-ref} and [](#s5){.pf-ref} do.

:::

:::

::: {.pf-step #s4}
For every integer $d\ge1$ the numerical classes of irreducible curves $C$ with
$$
1\le C\cdot H\le d
$$
form a finite set.

::: pf-proof
This bound is the card's own; it uses neither the sign of $D_i\cdot K_X$ nor the coefficients of step [](#s3){.pf-ref}. Put
$$
K_X=\frac{K_X\cdot H}{H^2}H+z,
\qquad z\in H^\perp,
$$
and write $C=\frac{h}{H^2}H+y$ with $h=C\cdot H$ and $y\in H^\perp$, normed by $\norm{v}^2=-v^2$. Exercise V.1.3(a) applied to the integral curve $C$ and $p_a(C)\ge0$ give $C^2+K_X\cdot C\ge-2$, that is
$$
\frac{h^2}{H^2}-\norm{y}^2+\frac{h(K_X\cdot H)}{H^2}+z\cdot y\ge-2,
$$
and Cauchy--Schwarz for the positive definite form $(u,v)_+=-u\cdot v$ on $H^\perp$ bounds $z\cdot y\le\norm{z}\norm{y}$; hence
$$
\norm{y}^2-\norm{z}\norm{y}\le A_h\coloneqq2+\frac{h^2+h(K_X\cdot H)}{H^2}.
$$
The integer $h$ lies in the finite set $\{1,\dots,d\}$, so the left side, which tends to $+\infty$ with $\norm{y}$, bounds $\norm{y}$ by a constant $R_d$ depending on $d$ alone, while the coefficient $h/H^2$ of $H$ is bounded as well. Every class therefore lies in a bounded subset of $N_\RR$, which holds only finitely many lattice points.

:::

:::

::: {.pf-step #s5}
For every integer $d>0$ there are only finitely many numerical classes of effective divisors $D$ with $D\cdot H=d$.

::: pf-proof
Write $D=\sum_in_iC_i$ with $n_i>0$ and distinct irreducible $C_i$. Then
$$
d=D\cdot H=\sum_in_i\qty(C_i\cdot H)
$$
with every $C_i\cdot H$ at least $1$, so every component satisfies $1\le C_i\cdot H\le d$ and its numerical class lies in the finite set of step [](#s4){.pf-ref}, which we call $S_d$, and $\sum_in_i\le d$. Hence $[D]$ is a sum of at most $d$ elements of $S_d$, counted with repetition, and there are only finitely many such sums in the abelian group $N$. This counting is the card's own, and it uses only the bound of step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}
If $d<0$ there is no effective divisor $D$ with $D\cdot H=d$, and if $d=0$ the only one is $D=0$.

::: pf-proof
A nonzero effective divisor is $D=\sum_in_iC_i$ with $n_i>0$ and distinct irreducible $C_i$, and $H\cdot C_i\ge1$ because $H$ is ample, so $D\cdot H=\sum_in_i(H\cdot C_i)>0$. This step is the card's own.

:::

:::

::: {.pf-step #s7}
For every integer $d$, only finitely many numerical classes of effective divisors satisfy $D\cdot H=d$. This proves part (a).

::: pf-proof
Steps [](#s1){.pf-ref} to [](#s5){.pf-ref} prove the case $d>0$, and step [](#s6){.pf-ref} the cases $d\le0$.

:::

:::

::: {.pf-step #s8}
Let $C$ have genus $g\ge2$, let $X=C\times C$, and let $\Gamma_\sigma$ be the graph of an automorphism $\sigma$ of $C$. Then
$$
\Gamma_\sigma^2=\Delta^2=2-2g<0.
$$

::: pf-proof
Bragg, *Automorphisms of curves* (2015), Proof 2, reads $\Delta^2$ off the conormal bundle of the diagonal embedding, computing $\Delta^2=\deg\mathcal N_{C/C\times C}=2-2g$; the same number is Exercise V.1.6, printed p. 367. Bragg asserts $\Gamma^2=2-2g$ for the graph of any automorphism; the reason is that the quotient of $T_C\oplus u^*T_C$ by the graph of $du$ identifies the normal bundle of the graph of a morphism $u$ with $u^*T_C$, and $u$ an automorphism makes $\deg u^*T_C=\deg T_C=2-2g$.

:::

:::

::: {.pf-step #s9}
The map
$$
\Aut C\longrightarrow N=\Num(C\times C),
\qquad
\sigma\longmapsto[\Gamma_\sigma],
$$
is injective.

::: pf-proof
Bragg, Proof 2, the paragraph beginning "We use intersection theory on the surface $X=C\times C$": the graphs of distinct automorphisms are distinct irreducible curves, so they share no irreducible component and their intersection number is nonnegative, a sum of nonnegative local intersection multiplicities. If $\Gamma_\sigma\equiv\Gamma_\tau$, then
$$
\Gamma_\sigma\cdot\Gamma_\tau=\Gamma_\tau^2=2-2g<0
$$
by step [](#s8){.pf-ref}, since $g\ge2$, which contradicts the nonnegativity. Hence $\Gamma_\sigma=\Gamma_\tau$, the two graphs coincide, and $\sigma=\tau$.

:::

:::

::: {.pf-step #s10}
Every graph $\Gamma_\sigma$ meets the divisor
$$
K=K_{C\times C}=\pi_1^*K_C+\pi_2^*K_C
$$
in $4g-4$, and $K$ is ample.

::: pf-proof
Bragg, Proof 2, the paragraph beginning "Next, consider the canonical divisor $K$ of $C\times C$", computes $\Gamma\cdot K=4g-4$ for the graph of an automorphism, independent of $\Gamma$; adjunction, Proposition V.1.5, printed p. 361, with $\Gamma^2=2-2g$ and $p_a(\Gamma)=g$ gives the same number. Bragg takes $K$ as his fixed ample divisor; that it is ample follows from Nakai--Moishezon, Theorem V.1.10, printed p. 365: $K\cdot l=K\cdot m=2g-2>0$ for the rulings, $K^2=2(2g-2)^2>0$, and for an irreducible curve $D\subseteq C\times C$ the projection formula gives
$$
K\cdot D=(2g-2)\qty(\deg\qty(\restrictionof{p_1}{D})+\deg\qty(\restrictionof{p_2}{D}))>0,
$$
whose two degrees sum to at least one: $D$ is a curve, so it is not a point under both projections, and a nonconstant morphism of curves has degree at least one while a constant one has degree $0$.

:::

:::

::: {.pf-step #s11}
Only finitely many numerical classes of effective divisors $D$ on $C\times C$ satisfy $D\cdot K=4g-4$.

::: pf-proof
Part (a), proved in steps [](#s1){.pf-ref} to [](#s7){.pf-ref}, applies to the ample divisor $K$ of step [](#s10){.pf-ref} with $d=4g-4$; this is the use Bragg makes of it in his closing sentence.

:::

:::

::: {.pf-step #s12}
$$
\boxed{\cardinality{\Aut C}<\infty}.
$$

::: pf-proof
Each graph $\Gamma_\sigma$ is an effective divisor with $\Gamma_\sigma\cdot K=4g-4$ by step [](#s10){.pf-ref}, so its class lies in the finite set of step [](#s11){.pf-ref}, and step [](#s9){.pf-ref} makes $\sigma\mapsto[\Gamma_\sigma]$ injective. This proves part (b).

:::

:::

::: pf-qed
Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} are the published component bookkeeping; step [](#s3){.pf-ref} is the published bound under its sign condition; steps [](#s4){.pf-ref} and [](#s5){.pf-ref} are the card's own, a bound on the classes of the components that needs no such condition and the counting over them, and steps [](#s6){.pf-ref} and [](#s7){.pf-ref} close part (a) for $d\le0$ and in general. Steps [](#s8){.pf-ref} to [](#s12){.pf-ref} prove part (b) from (a).

:::

:::

:::

::: {.remark title="Published solution"}
Dan Bragg, *Automorphisms of curves* (2015), Proof 2, "Intersection Theory", proves (b) given (a): the graphs of distinct automorphisms of a curve of genus $g\ge2$ are distinct irreducible curves on $C\times C$, which therefore meet nonnegatively, whereas numerically equivalent graphs would meet in $\Gamma^2=2-2g<0$; so $\sigma\mapsto[\Gamma_\sigma]$ is injective, and every graph meets the canonical divisor of $C\times C$ in the same $4g-4$, which is what part (a) counts. Bragg leaves the ampleness of $K_{C\times C}$ implicit and asserts $\Gamma^2=2-2g$ for the graph of any automorphism without argument; step [](#s8){.pf-ref} gives the normal-bundle reason and step [](#s10){.pf-ref} the Nakai--Moishezon check.

Math StackExchange answer 4775583 by KReiser, to question 4449474, gives (a) in the form of steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}: adjunction bounds the square of each prime component below, distinct components meet nonnegatively, and $b_i\le d$ gives $\sum_ib_i^2\le d^2$. Its display for $D^2$ replaces $b_i^2$ by $b_id$ under $D_i\cdot K_X$, an inequality that follows from $b_i\le d$ when $D_i\cdot K_X\ge0$, as it is when $K_X$ is nef; for a component with $D_i\cdot K_X<0$ and $b_i<d$ the comparison is reversed. Its closing display bounds $(D-E)^2$ below, for fixed $E$, by an affine function of $D-E$, which with negative definiteness confines $D-E$ to a ball. The card reaches finiteness instead through steps [](#s4){.pf-ref} and [](#s5){.pf-ref}, which bound the class of every prime component with $1\le C\cdot H\le d$ and then count the components, and which are its own.

Algebraic Geometry II, National Taiwan University, 2020 Spring (course of Chin-Lung Wang), *Chapter V Surfaces* homework solutions, Exercise 11 (solution by Shuang-Yen Lee), takes the same route for (a) but displays the estimate $\sum_ic_i^2\le c_0^2+c_0k_0+2+\frac12k_0^2$ from an adjunction identity that bounds $\sum_i(c_i^2+c_ik_i)$; reaching $\sum_ic_i^2$ through $2\abs{c_ik_i}\le c_i^2+k_i^2$ costs a factor $2$ and adds $\sum_ik_i^2$. Its (b) is the printed hint, and proves only that no automorphism other than the identity has a graph numerically equivalent to the diagonal.

Yang Pi-Yeh, *Hartshorne Solutions*, exercise 5.1.11, takes an orthogonal basis $R_1,\dots,R_k$ of $H^\perp$ and concludes from $(\sum a_iR_i)^2+(\text{lower terms})>0$ that "the inequality above has only finite solution of $a_i$". The unknown that must be bounded is not $a_i$ but the coefficients of the curves occurring in $D+\sum a_iR_i$, which step [](#s4){.pf-ref} bounds through adjunction.

:::
