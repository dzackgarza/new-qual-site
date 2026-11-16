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
---

::: {.problem}
\* Let $X$ be an irreducible nonsingular curve in $\PP^3$.
Then for each $m \gg 0$, there is a nonsingular surface $F$ of degree $m$ containing $X$.

Hint: Let $\pi: \tilde{\PP} \to \PP^3$ be the blowing-up of $X$ and let $Y=\pi^{-1}(X)$.
Apply Bertini's theorem to the projective embedding of $\tilde{\PP}$ corresponding to $\mci_Y \tensor \pi^* \OO_{\PP^3}(m)$.
:::

::: {.solution}
Let
$$
\pi:\widetilde{\PP^3}=\Bl_X\PP^3\longrightarrow\PP^3
$$
be the blowup of $X$, and write
$$
E=\pi^{-1}(X)
$$
for its exceptional divisor.

::: pf

::: {.pf-step #s1}

The threefold $\widetilde{\PP^3}$ is nonsingular, and
$$
E\cong\PP_X(\mci_X/\mci_X^2).
$$
For every $P\in X$, the fibre
$$
E_P=\pi^{-1}(P)
$$
is a projective line and
$$
\OO_{\widetilde{\PP^3}}(-E)\restrict_{E_P}\cong\OO_{\PP^1}(1).
$$

::: pf-proof

The center $X$ is nonsingular of codimension $2$ in the nonsingular threefold $\PP^3$.
The blowup theorem for a nonsingular center, Theorem II.8.24 (printed p. 186), gives
$$
\widetilde{\PP^3}\text{ nonsingular},
\qquad
E\cong\PP_X(\mci_X/\mci_X^2),
$$
which is (a) and (b) of that theorem, and in (c) it identifies the normal sheaf $\mathcal N_{E/\widetilde{\PP^3}}=\OO_{\widetilde{\PP^3}}(E)\restrict_E$ with $\OO_{\PP(\mci_X/\mci_X^2)}(-1)$. Hence
$$
\OO_{\widetilde{\PP^3}}(-E)\restrict_E\cong\OO_E(1).
$$
Here $E$ is the subscheme $Y'$ of the theorem: by II.7.13(a) (printed p. 164) the inverse image ideal $\pi^{-1}\mci_X\cdot\OO$ is invertible, and it is $\OO_{\widetilde{\PP^3}}(-E)$, so $E$ is the subscheme that ideal defines.
Since the conormal bundle $\mci_X/\mci_X^2$ has rank $2$, every fibre of $E\to X$ is $\PP^1$, and restriction of the last identity gives the claimed $\OO_{\PP^1}(1)$.

:::

:::

::: {.pf-step #s2}

For every sufficiently large integer $m$, the invertible sheaf
$$
L_m
=
\OO_{\widetilde{\PP^3}}(-E)
\tensor
\pi^*\OO_{\PP^3}(m)
$$
is very ample.

::: pf-proof

By the Rees-algebra construction,
$$
\widetilde{\PP^3}
=
\Proj_{\PP^3}\bigoplus_{q\ge0}\mci_X^q,
$$
and its relative twisting sheaf is
$$
\OO_{\widetilde{\PP^3}}(1)
\cong
\mci_X\OO_{\widetilde{\PP^3}}
\cong
\OO_{\widetilde{\PP^3}}(-E).
$$
The identification $\OO_{\widetilde{\PP^3}}(1)=\OO_{\widetilde{\PP^3}}(-E)$ is Proposition II.7.13(a) with its proof (printed p. 164), where the twisting sheaf of the blowup is computed to be the inverse image ideal $\pi^{-1}\mci_X\cdot\OO$.
Apply Exercise II.7.14 (printed pp. 171--172) to this relative $\Proj$, with the ample sheaf $\OO_{\PP^3}(1)$ on the base and $\mathcal L=\OO_{\PP^3}(1)$.
Its last part says that
$$
\OO_{\widetilde{\PP^3}}(1)
\tensor
\pi^*\OO_{\PP^3}(m)
$$
is very ample on $\widetilde{\PP^3}$ relative to $\Spec k$ for every $m\gg0$, the base being a point, that is, very ample.
This is exactly $L_m$.

:::

:::

::: {.pf-step #s3}

Fix such an $m$ and let
$$
\iota_m:\widetilde{\PP^3}\hookrightarrow\PP^N
$$
be the embedding defined by $L_m$.
Each exceptional fibre $E_P$ is mapped isomorphically to a line in $\PP^N$.

::: pf-proof

On the fibre $E_P$, the pullback
$$
\pi^*\OO_{\PP^3}(m)\restrict_{E_P}
$$
is trivial.
Step [](#s1){.pf-ref} therefore gives
$$
L_m\restrict_{E_P}\cong\OO_{\PP^1}(1).
$$
The restriction of a projective embedding remains a closed immersion.
Its image therefore has degree
$$
\deg L_m\restrict_{E_P}=1,
$$
so it is a line in $\PP^N$.

:::

:::

::: {.pf-step #s4}

The hyperplanes in $\PP^N$ containing at least one exceptional fibre form a proper closed subset of $\dualof{(\PP^N)}$.

::: pf-proof

Consider the incidence variety
$$
\mathcal B
=
\{(P,H)\in X\times\dualof{(\PP^N)}:
\iota_m(E_P)\subseteq H\}.
$$
By step [](#s3){.pf-ref}, $\iota_m(E_P)$ is a line.
Hyperplanes containing a fixed line form a projective subspace of codimension $2$ in $\dualof{(\PP^N)}$.
Consequently
$$
\dim\mathcal B
=
1+(N-2)
=
N-1.
$$
The projection
$$
\mathcal B\longrightarrow\dualof{(\PP^N)}
$$
is proper because $X$ is projective, so its image is closed.
Its dimension is at most $N-1$, strictly smaller than the dimension $N$ of the dual projective space.
Hence the image is proper.

:::

:::

::: {.pf-step #s5}

There is a hyperplane $H\subseteq\PP^N$ such that
$$
\widetilde F
=
\iota_m^{-1}(H)
$$
is nonsingular and $H$ contains no exceptional fibre.

::: pf-proof

By step [](#s1){.pf-ref}, $\widetilde{\PP^3}$ is nonsingular.
Bertini's hyperplane theorem [[T-BERTINI]] says that the hyperplanes whose inverse image under $\iota_m$ is nonsingular form a dense open subset of $\dualof{(\PP^N)}$.

Step [](#s4){.pf-ref} says that the hyperplanes containing an exceptional fibre form a proper closed subset.
The complement of that subset is therefore another nonempty open subset.
Since $\dualof{(\PP^N)}$ is irreducible, the two open sets meet.
Choose $H$ in their intersection.

:::

:::

::: {.pf-step #s6}

The divisor $\widetilde F$ of step [](#s5){.pf-ref} is the strict transform of a degree-$m$ surface
$$
F\subseteq\PP^3
$$
containing $X$.

::: pf-proof

The line bundle of $\widetilde F$ is
$$
L_m
=
\OO_{\widetilde{\PP^3}}(-E)
\tensor
\pi^*\OO_{\PP^3}(m).
$$
The isomorphism $\OO(-E)\cong\OO(1)$ is Proposition II.7.13(a) with its proof (printed p. 164), where the twisting sheaf of the blowup $\widetilde{\PP^3}=\Proj\bigoplus_{q\ge0}\mci_X^q$ is identified with the inverse image ideal $\pi^{-1}\mci_X\cdot\OO$, which is invertible. The pushforward is a separate matter, and it does not follow from generation in degree one: the degree-one piece of a Rees algebra is $\mci_X$ by construction, whereas $\pi_*\OO(1)=\bigcup_{k\ge0}(\mci_X^{k+1}:\mci_X^k)$, the Ratliff--Rush closure, which can be strictly larger. With $\mci=(x^4,x^3y,xy^3,y^4)$ in $k[x,y]$, for instance, $x^2y^2\mci\subseteq\mci^2$, so $x^2y^2$ lies in the closure and not in $\mci$. What holds here is the following.

The variety $\PP^3$ is normal. By Stein factorization (Corollary III.11.5, printed p. 280) the birational projective morphism $\pi$ factors as $g\circ\pi'$ with $\pi'$ projective with connected fibres and $g$ finite; $g$ is birational, and a finite birational morphism onto a normal variety is an isomorphism, its coordinate rings being finite extensions of a normal domain inside its fraction field. Hence
$$
\pi_*\OO_{\widetilde{\PP^3}}=\OO_{\PP^3}.
$$
Since $E$ is effective, $\OO(-E)\subseteq\OO_{\widetilde{\PP^3}}$, so $\pi_*\OO(-E)$ is an ideal sheaf $\mci'\subseteq\OO_{\PP^3}$. For $f\in\mci_X$ one has $\pi^*f\in\pi^{-1}\mci_X\cdot\OO=\OO(-E)$, so $\mci_X\subseteq\mci'$. Conversely, for $f\in\mci'$ the pullback $\pi^*f$ lies in $\OO(-E)$, hence vanishes on $E$, whose image under $\pi$ is all of $X$; so $f$ vanishes on $X$ set-theoretically and $f\in\sqrt{\mci_X}$. The curve $X$ is nonsingular, so $\mci_X$ is radical, and $\mci'\subseteq\mci_X$. Therefore
$$
\pi_*\OO(-E)=\mci_X .
$$
The projection formula therefore identifies
$$
H^0(\widetilde{\PP^3},L_m)
\cong
H^0(\PP^3,\mci_X(m)).
$$
Thus the section cutting out $\widetilde F$ corresponds to a degree-$m$ homogeneous form vanishing on $X$.
Let $F$ be its zero surface in $\PP^3$.
Then
$$
X\subseteq F,
$$
and away from $E$ the blowup is an isomorphism.
Step [](#s5){.pf-ref} says that $\widetilde F$ contains no exceptional fibre. A component of $\widetilde F$ contained in $E$ would be a divisor in $E=\PP(\mci_X/\mci_X^2)$, and such a divisor meets the fibre $E_P$ over every $P$ in a nonempty open subset of $X$, so $\widetilde F$ would contain those fibres. Hence $\widetilde F$ has no component contained in $E$ either.
It is therefore the closure of
$$
\pi^{-1}(F\setminus X).
$$
Hence it is the strict transform of $F$.

:::

:::

::: {.pf-step #s7}

The surface $F$ is nonsingular away from $X$.

::: pf-proof

The morphism
$$
\pi:\widetilde{\PP^3}\setminus E
\xrightarrow{\sim}
\PP^3\setminus X
$$
is an isomorphism.
By step [](#s6){.pf-ref} it identifies
$$
\widetilde F\setminus E
$$
with
$$
F\setminus X.
$$
Step [](#s5){.pf-ref} says that $\widetilde F$ is nonsingular, so the open subset $F\setminus X$ is nonsingular.

:::

:::

::: {.pf-step #s8}

The surface $F$ is nonsingular at every point of $X$.

::: pf-proof

Fix a point $P\in X$.
Because $X$ is a nonsingular codimension-two subvariety of the nonsingular threefold $\PP^3$, choose regular local parameters
$$
x,y,z
$$
at $P$ such that
$$
\mci_{X,P}=(x,y).
$$
Let $f$ be a local equation for $F$.
Since $X\subseteq F$, write
$$
f=ax+by
$$
for some
$$
a,b\in\OO_{\PP^3,P}.
$$

On the blowup of the ideal $(x,y)$, the exceptional fibre over $P$ is the projective line of normal directions $[u:v]$.
The strict transform of $F$ meets this fibre in the zero locus of the linear form
$$
a(P)u+b(P)v.
$$
If
$$
a(P)=b(P)=0,
$$
that linear form vanishes identically, so the whole exceptional fibre $E_P$ is contained in $\widetilde F$.
Step [](#s5){.pf-ref} excludes this.
Therefore
$$
(a(P),b(P))\ne(0,0).
$$

Modulo the maximal ideal at $P$, differentiation of
$$
f=ax+by
$$
gives
$$
df(P)=a(P)\,dx+b(P)\,dy\ne0.
$$
By the Jacobian criterion, the hypersurface $F$ is nonsingular at $P$.
Since $P$ was arbitrary, $F$ is nonsingular along all of $X$.

:::

:::

::: {.pf-step #s9}

For every sufficiently large $m$, there is a nonsingular degree-$m$ surface containing $X$.

::: pf-proof

Step [](#s2){.pf-ref} gives one threshold beyond which $L_m$ is very ample for every $m$.
For each such $m$, steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} construct a degree-$m$ surface $F$ containing $X$.
Steps [](#s7){.pf-ref} and [](#s8){.pf-ref} prove that $F$ is nonsingular both away from and along $X$.
Therefore
$$
\boxed{
\text{for every }m\gg0\text{ there is a nonsingular degree-}m
\text{ surface }F\supseteq X.
}
$$

:::

:::

::: pf-qed

Step [](#s9){.pf-ref} is exactly the required assertion.

:::

:::

:::
