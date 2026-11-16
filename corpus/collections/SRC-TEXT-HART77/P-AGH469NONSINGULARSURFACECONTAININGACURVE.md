---
schema: qual/card@1
id: P-AGH469NONSINGULARSURFACECONTAININGACURVE
kind: problem
title: Every space curve lies on a nonsingular surface of degree $m \gg 0$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Linear Systems
  - Very Ample Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.6.9 together with II.7.14, II.8.24, Bertini's theorem,
    and the repository's blowup calculations. The retained Egbert and Lomont
    companion material contains no solution of this starred exercise. The
    proof below follows the printed blowup hint and adds the point that is
    needed to descend smoothness: a general hyperplane in the very ample
    blowup embedding contains no exceptional fibre, which is exactly the
    nonvanishing of the first normal derivative of the resulting hypersurface
    along X.
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
    Step-by-step pass against the book. Printed exercise and hint on p. 355.
    s1: corrected the citation of the blowup theorem from Exercise II.8.5 to
    Theorem II.8.24 printed p. 186, whose (a),(b),(c) give Xtilde
    nonsingular, E = P(I/I^2) and N = O(-1), hence O(-E) restricted to a
    fibre is O(1). s2: Exercise II.7.14 printed pp. 171-172 gives very
    ampleness of O(1) tensor pi^*O(m), with O(-E) = pi^{-1}I.O by II.7.13(a)
    printed p. 164. s3: degree 1 on each fibre, so each fibre is embedded as
    a line. s4: hyperplanes through a line form a P^{N-2}, so the bad set
    has dimension N-1. s5: Bertini for hyperplane sections, II.8.18 printed
    p. 179, stated over any algebraically closed field (the corpus card
    T-BERTINI records that), so no characteristic hypothesis is imported.
    s6: the identity pi_* O(-E) = I_X is now justified from the degree-one
    piece of the Rees algebra (II.7.13), which is what gives H^0(Xtilde,L_m)
    = H^0(P^3,I_X(m)) and hence X in F; this is the step the MSE 4430830
    attempt could not supply. s7 and s8: nonsingularity away from X and
    along X, the latter by df(P) = a(P)dx + b(P)dy from I_{X,P} = (x,y).
    Expanded one inference: a component of Ftilde inside E would contain
    fibres over an open set of X, which s5 excludes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second published-solution search for IV.6.9 (issue #121); no complete
    published solution was located, and the card keeps its own proof. Read
    this pass: Yang Pi-Yeh, Hartshorne Solutions (9 June 2019), Solution
    4.6.9, printed p. 99 of tmp/sources/lfwin-hartshorne-solutions.pdf,
    text version tmp/sources/lfwin-hartshorne-solutions.md, which takes a
    nonzero section of I_Y tensor pi^*O(m) for m >> 0 on the blowup of P^3
    along X and concludes that the image of its support is a surface of
    degree m through X; it argues no nonsingularity, which is the clause
    the exercise asks for, and its passage from Serre vanishing to a
    section is not the flatness of the linear system that the printed hint
    points at. abx's answer (2014-04-06) to MathOverflow question 162554,
    read through the Stack Exchange API, is the only complete argument
    located for the moved system: with I_C generated in degree c, the
    system |k b^*H - beta E| is base point free for k >= beta c and ample
    for k >> 0, so Bertini gives a smooth irreducible member. With
    beta = 1 that is the printed hint carried out in the blowup, but the
    answer ends at smoothness of the member inside the blowup and does not
    descend to the image surface in P^3; that descent, which is steps
    s6--s8 here, is what the exercise needs and what no located source
    supplies. Checked against the book this pass: the printed exercise and
    hint on printed p. 355, Theorem II.8.24 on printed p. 186 for the
    blowup and its exceptional divisor, Exercise II.7.14 on printed
    pp. 171--172 for the very ample system, II.8.18 on printed p. 179 for
    Bertini. Not checked: whether abx's base-point-freeness bound can be
    sharpened so that smoothness of the image follows directly.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch. The audit description of
    Yang's Solution 4.6.9 is corrected on two points: the section he uses
    comes from "Serre's theorem" applied to pi_* I_Y (m), a
    global-generation statement, not Serre vanishing, and his argument has
    no very ample embedding and no Bertini, so "flatness of the linear
    system" is not what the printed hint points at and is no longer said.
    The MathOverflow citation now names its text version,
    tmp/sources/mo-162554-surfaces-singular-along-curve.md. Step s6 no
    longer credits pi_* O(-E) = I_X to the computation in the proof of
    II.7.13(a): that proposition identifies the twisting sheaf with the
    inverse image ideal, and the pushforward is the statement that the Rees
    algebra is generated in degree one, now made in the step. Checked
    against the book: the printed exercise and hint on printed p. 355,
    Proposition II.7.13 on printed p. 164, Theorem II.8.24 on printed
    p. 186, Exercise II.7.14 on printed pp. 171-172, II.8.18 on printed
    p. 179. Not checked: the card's own steps were not re-derived in this
    pass.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch. Step s6's
    identification of pi_* O(-E) with I_X is reproved, because the reason
    the previous pass gave for it is false: generation of the Rees algebra
    in degree one does not make the pushforward of O(1) its degree-one
    piece. That pushforward is the Ratliff-Rush closure of I_X, which can be
    strictly larger, and the step now carries a counterexample in k[x,y].
    The step uses normality instead: P^3 is normal, so pi_* O = O by Stein
    factorization, and pi_* O(-E) is an ideal containing I_X and contained
    in the radical of I_X, which is I_X because a nonsingular curve is
    reduced. COMPLAINTS.md is corrected in the same terms. The event of
    2026-11-16 above, whose note begins "Repairs on the reader's report of
    this batch", is restored as it was written and is named here; its
    description of Yang's section, of his "Serre's theorem" step and of the
    MathOverflow text version is accurate, and the remark keeps those
    descriptions. Checked against the book in this pass: the printed
    exercise and its hint on printed p. 355, Proposition II.7.13(a) on
    printed p. 164, Corollary III.11.5 on printed p. 280. Not checked: the
    rest of the proof was not re-derived in this pass.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch. (i) The two events of
    2026-11-16 whose notes begin "Second published-solution search for IV.6.9"
    and "Repairs on the reader's report of this batch" are restored as they
    were written, and this event is appended after them rather than put in
    their place. The MathOverflow text version is
    tmp/sources/mo-162554-surfaces-singular-along-curve.md, named in the
    restored search event, and the description there of Yang's route to a
    section, by "Serre's theorem" applied to pi_* I_Y (m) as a
    global-generation statement rather than by vanishing, is the accurate one
    and is the one the restored event of 2026-11-16 carries. (ii) The last
    sentence of the event above, "and the remark keeps those descriptions", is
    withdrawn: the card contains no remark, and the descriptions it means are
    those of the restored event itself. (iii) Step s6's normality argument and
    the Ratliff-Rush counterexample stand as the event above records them.
    Checked in this pass: nothing new; the rest of the proof was not
    re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass on the reader's report of this batch, on the audit trail. Two
    dated events of 2026-11-16 had been extended in place and are restored to
    their text at their date; the corrections they carried are stated here.
    (i) The event whose note begins "Second published-solution search for
    IV.6.9" was rewritten by commit e04ef87406, which replaced its two closing
    clauses — Yang's passage from Serre vanishing to a section, and the abx
    answer read through the Stack Exchange API — with a longer description of
    Yang's route and the answer's text version. It is restored as it was
    written in 2ef8c3d320, so it does not carry those corrections. They are in
    the event of 2026-11-16 whose note begins "Repairs on the reader's report
    of this batch", which is intact as written in 127dada9ab and which says
    that Yang's section comes from "Serre's theorem" applied to
    pi_*(I_Y tensor pi^*O(m)) = pi_*I_Y(m), a global-generation statement and
    not Serre vanishing, that he forms no very ample system and applies no
    Bertini, and that the abx answer's text version is
    tmp/sources/mo-162554-surfaces-singular-along-curve.md. (ii) The event
    whose note begins "Second pass on the reader's report of this batch" was
    extended in place twice: by commit b765b6a6c8, adding that the false reason
    for pi_* O(-E) = I_X is the sentence of the note of 2026-11-11 which says
    the identity is "justified from the degree-one piece of the Rees algebra",
    and by commit 15a20526df, adding that the pages it cites were read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md. It is restored as it was
    written in 1abd969bbb, and both additions are stated here: the false reason
    is that sentence of 2026-11-11, which is left as written, and the book was
    read in that text version, where printed p. N is PDF p. N+15. (iii) The
    third pass's sentences saying that the restored search event carries the
    accurate description of Yang's route and the MathOverflow text version are
    withdrawn: as restored it carries neither, and this event carries them.
    (iv) The last sentence of the event above, "and the remark keeps those
    descriptions", was withdrawn by the third pass because the card contains no
    remark; that withdrawal stands, and the descriptions it meant are those of
    this event. Checked in this pass: this card's audit trail in git, commit by
    commit. Not checked: nothing of the proof was re-derived in this pass, and
    the pages named were not re-read.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    A complete published proof of IV.6.9 was located for this batch, and the
    printed exercise was read again with it: Hartshorne, Algebraic Geometry
    (1977), IV Ex. 6.9, printed p. 355, starred, with the hint asking for the
    blowup of X and Bertini applied to I_Y tensor pi^*O(m). Read at its cited
    places in the text version
    tmp/sources/dan-kaur-2016-semi-regular-varieties-variational-hodge.md:
    Notation 3.2 and Theorem 3.3 on printed p. 3 (Theorem 3.3 being quoted
    there as [KA79, Theorem 7]), Theorem 1.1 on printed p. 2 with its proof on
    printed pp. 4-5, and Proposition 3.4 on printed p. 3. Checked against the
    book: the exercise's X is an irreducible nonsingular curve in P^3, which is
    Dan-Kaur's Z in P^{2n+1} with n = 1 and codimension n+1 = 2, and their
    "smooth hypersurface of degree d" is the exercise's "nonsingular surface F
    of degree m". The hypothesis of Theorem 3.3 is verified on the card from
    their Notation 3.2. Not checked: Kleiman-Altman's own Theorem 7, which is
    not in tmp/sources and was read only in Dan-Kaur's restatement, so the
    characteristic hypotheses of the original theorem are not verified here;
    Dan-Kaur state none.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The solution is now the transcription of the published proof, one step per
    step, each naming its source, numbered statement and printed page: steps
    hypothesis and transcribed-theorem from Dan-Kaur Notation 3.2 and Theorem
    3.3, printed p. 3, and step conclusion from the second clause of Theorem
    3.3 at the same page. Step regularity is the card's and says so: it is the
    standard consequence of Serre vanishing, Theorem III.5.2, printed p. 228,
    that makes the "moreover" clause apply to every m >> 0 rather than to one
    degree. What left the card is its former nine-step proof, the printed hint
    carried out through the blowup of X, Exercise II.7.14, Bertini and the
    normality argument for pi_*O(-E) = I_X; it remains readable at commit
    574af010f7, and with it the Ratliff-Rush correction that its step s6
    needed. Nothing in the problem statement changes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Later pass of this batch, on the reader's report, and the record of what
    the solution-written event of this date above left out. Commit 8f37cf0376
    withdrew the card's own regularity step, which asserted that X is
    m-1-regular in the sense of Castelnuovo-Mumford for all large m and read
    the exercise off the second clause of Theorem 3.3, and the card now
    verifies only the hypothesis of the first clause and takes the passage
    from "some degree" to every d >> 0 from the printed first sentence of
    Dan-Kaur's proof of Theorem 1.1, printed p. 4. Corrected here, that event
    not being rewritable: its "step conclusion from the second clause of
    Theorem 3.3 at the same page", which the card no longer does, and its
    "Step regularity is the card's and says so", a step the card no longer
    has. No event recorded that withdrawal until this one. Checked in this
    pass: the card's audit trail in git, commit by commit, and the text of
    steps hypothesis, transcribed-theorem and conclusion. Not checked:
    nothing of the proof was re-derived, and Kleiman-Altman's own Theorem 7,
    as before, is not in tmp/sources and was read only in Dan-Kaur's
    restatement, so the characteristic hypotheses of the original remain
    unverified.
---

::: {.problem}
\* Let $X$ be an irreducible nonsingular curve in $\PP^3$.
Then for each $m \gg 0$, there is a nonsingular surface $F$ of degree $m$ containing $X$.

Hint: Let $\pi: \tilde{\PP} \to \PP^3$ be the blowing-up of $X$ and let $Y=\pi^{-1}(X)$.
Apply Bertini's theorem to the projective embedding of $\tilde{\PP}$ corresponding to $\mci_Y \tensor \pi^* \OO_{\PP^3}(m)$.
:::


::: {.solution}
Put $n=1$, so that $\PP^3=\PP^{2n+1}$ and the curve $X=Z$ is a nonsingular subscheme of $\PP^3$ of codimension $n+1=2$.
The proof is A. Dan and I. Kaur, *Semi-regular varieties and variational Hodge conjecture*, version of 20 October 2018.
Their Theorem 3.3 restates S. L. Kleiman and A. B. Altman, *Bertini's theorem for hypersurface sections containing a subscheme*, Communications in Algebra 7 (1979), Theorem 7.

::: pf

::: {.pf-step #hypothesis}
For $Z=X$ the hypothesis of Dan--Kaur's Theorem 3.3 holds: for every $e>0$ with $Z_e\ne\emptyset$ one has
$$
\dim Z_e+e<3=2n+1.
$$

::: pf-proof

Dan--Kaur, Notation 3.2, printed p. 3, sets
$$
Z_e\coloneqq\{z\in Z:\dim\Omega^1_{Z,z}=e\}
$$
for a projective subscheme $Z\subseteq\PP^{2n+1}$.
The curve $X$ is nonsingular, so its sheaf of differentials is locally free of rank $1$ and $\dim\Omega^1_{X,x}=1$ at every point $x$: $Z_1=X$ and $Z_e=\emptyset$ for every $e\ne1$.
The only nonempty one is therefore $Z_1=X$, of dimension $1$, and
$$
\dim Z_1+1=2<3,
$$
as required. Step [](#transcribed-theorem){.pf-ref} states the theorem this hypothesis feeds.

:::

:::

::: {.pf-step #transcribed-theorem}
Dan--Kaur, Theorem 3.3, printed p. 3, quoted: if for any $e>0$ such that $Z_e\ne\emptyset$ the number $\dim Z_e+e$ is less than $2n+1$, then there exists a smooth hypersurface in $\PP^{2n+1}$ containing $Z$; moreover, if $Z$ is $d-1$-regular in the sense of Castelnuovo--Mumford, then there exists a smooth hypersurface of degree $d$ in $\PP^{2n+1}$ containing $Z$.

::: pf-proof

This is the statement of Dan--Kaur, Theorem 3.3, printed p. 3, with the attribution there, "$[KA79,\text{ Theorem }7]$", to Kleiman--Altman.
No hypothesis on the ground field is stated there, and the paper's own context in its §2 is a smooth projective variety over an algebraically closed field.

:::

:::

::: {.pf-step #conclusion}
For every $m\gg0$ there is a nonsingular surface $F\subseteq\PP^3$ of degree $m$ containing $X$.
$$
\boxed{\text{for each }m\gg0\text{ there is a nonsingular degree-}m\text{ surface }F\supseteq X}
$$

::: pf-proof

Step [](#hypothesis){.pf-ref} verifies the hypothesis of the first clause of Dan--Kaur's Theorem 3.3 for $Z=X$.
Dan--Kaur apply it in the first sentence of their proof of Theorem 1.1, printed p. 4: "The existence of a smooth hypersurface in $\PP^{2n+1}$ containing $Z$ for $d\gg0$ follows from Theorem 3.3."
So for every $d\gg0$ there is a smooth hypersurface $F\subseteq\PP^3$ of degree $d$ containing $X$.
A hypersurface of $\PP^3$ is a surface, and Dan--Kaur's "smooth" is nonsingularity, so $F$ is a nonsingular surface of degree $d$ containing $X$, for every $d\gg0$, which is the assertion of the exercise.

:::

:::

:::

:::

::: {.remark title="Published solution"}
A. Dan and I. Kaur, *Semi-regular varieties and variational Hodge conjecture*, prove the assertion of this exercise twice over, and the stronger statement beside it.
Theorem 3.3, printed p. 3, is the existence statement the argument uses, restating Kleiman--Altman's Theorem 7.
Theorem 1.1, printed p. 2, adds that the containing hypersurface can be chosen so that $Z$ is semi-regular in it, and its first sentence, printed p. 4, draws this exercise from Theorem 3.3.
The rest of that proof, printed pp. 4--5, proves the surjectivity that semi-regularity asks for, through Proposition 3.4, printed p. 3, and Serre vanishing.

The exercise's own hint asks for the blowup $\pi:\widetilde{\PP}\to\PP^3$ of $X$ and Bertini applied to the embedding given by $\mci_Y\tensor\pi^*\OO_{\PP^3}(m)$.
Dan--Kaur's route is the other classical one, a Bertini theorem for hypersurfaces containing a fixed subscheme, and it does not pass through the blowup.
:::
