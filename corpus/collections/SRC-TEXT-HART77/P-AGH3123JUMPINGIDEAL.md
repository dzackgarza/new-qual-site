---
schema: qual/card@1
id: P-AGH3123JUMPINGIDEAL
kind: problem
title: Jumping cohomology for the ideal sheaf of a degenerating quartic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Semicontinuity
  - Flat Families
  - Ideal Sheaves
  - Rational Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.12.3, Example III.9.8.3, and the twisted-quartic source context.
    The printed untwisted cohomology claim is false; the advertised jump is obtained after twisting by O(1).
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-09
  note: 'Read III.12.3 against Hartshorne pp. 291-292 and Dongryul Kim, Solutions to Hartshorne, p. 215, whose errata list notes that the printed statement seems false. Verified the printed claim: for every t one has h^0(I_t) = 1 - h^0(O_{X_t}) = 0 and H^1(I_t) = 0, since H^1(P^4,O) = 0, so there is no jump. The statement is now kept as printed and the erratum at the start of the solution proves the jump for I(1), where the values are 0 and 1 as displayed. Kims solution stops after the exact sequence and does not treat the cohomology, so the twisted computation here is not taken from him.'
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne III.12.3 prints the jumps for h^0(t, I) and h^1(t, I), which vanish for every t. The statement now asks for the jumps of h^0(t, I(1)) and h^1(t, I(1)).
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Published-solution search for this exercise (issue #121) located no
    complete published argument, and one published claim of a corrected
    jump that does not hold. Printed exercise read: Hartshorne, Algebraic
    Geometry (1977), III.12.3, printed pp. 291--292, with Example
    III.9.8.4, printed pp. 274--275, Example III.12.9.2, printed p. 289,
    and Exercise III.9.3.5(c), printed p. 285. Sources read: Dongryul Kim,
    Solutions to Hartshorne, Chapter III §12, PDF p. 215, which proves the
    flat limit and the flatness of the ideal sheaf and computes no
    cohomology, and whose errata ask whether the statement is false; A.
    Egbert, Solutions, III.12.3, printed p. 204, a typo note with no
    mathematics. MathOverflow question 90260 was read through the Stack
    Exchange API: the answer by S. Kovács (2012-03-05, with addendum)
    claims h^0(O_{X_0}) = 2 and h^1(P^4, I_0) = 1, that is, that the
    printed h^1 line is right, and the answer by J. Böhm (2015-05-15)
    computes the fibre ideal by elimination and reports all
    H^i(P^4, I_0) = 0. Kovács's conclusion fails: in his fibre ideal x_2
    is annihilated by all five coordinates, so x_2 is zero in the
    localization at each x_i and is not a function on X_0, and the card
    now derives those five relations from the family's parametrization.
    Repaired on the card: step s1's Hilbert-polynomial argument, which
    does not exclude a nilpotent because this family's nilpotent
    contributes only in degree one and leaves P(m) = 4m+1, is replaced by
    the annihilator argument; the opening paragraph's claim that
    H^1(I_t) embeds in H^1(P^4, O) = 0 is replaced by the correct
    h^1(I_t) = coker(H^0(O) -> H^0(O_{X_t})) = 0. Statement unchanged in
    substance: the printed h^0 value at t = 0 is false, and the printed
    h^1 value is false as well, for the reason now given. Not checked: no
    machine computation was run in this pass; Böhm's is the only one read,
    and it is reported, not reproduced.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch, checked against the book
    and the text versions. Step s1's proof is restored to the
    Hilbert-polynomial argument, which does exclude a thickening: the
    special fibre Z has P_Z = P_{X_1} = 4m+1 by flatness, the reduced
    quartic X_0 has P_{X_0} = 4m+1 as well, and a nonzero kernel K of
    O_Z -> O_{X_0} is a coherent sheaf on the curve, so K(m) is generated
    by global sections for m >> 0 and its Hilbert polynomial is nonzero.
    The sentence claiming that the Hilbert polynomial does not exclude a
    nilpotent, which stood in this step in the previous pass, was false and
    is withdrawn. The annihilator computation stays, in the remark, where
    it refutes Kovacs: the chart argument is the questioner's on the MO
    thread, x_2/x_0 = x_0x_2/x_0^2 = 0 in the degree-zero localization at
    x_0, and Kovacs's addendum treats x_2 as an affine coordinate of that
    chart, which it is not. The opening paragraph's reference to that
    paragraph is corrected to point at step s1. Also corrected: Kim's
    remark is in his list of problems he has not solved (PDF p. 1), not in
    his list of corrections, and the text versions are now named for Kim,
    Egbert and MathOverflow 90260. Checked against the book in this pass:
    III.12.3 on printed pp. 291-292, Example III.9.8.4 on printed
    pp. 259-260, Theorem II.5.17 on printed p. 121. Not checked: no
    machine computation was run.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch. Step s1's argument is
    completed: for m >> 0 the twist K(m) is generated by global sections
    (Theorem II.5.17, printed p. 121) and H^1(P^4, K(m)) = 0 by Serre
    vanishing (Theorem III.5.2, printed p. 228), so h^0(K(m)) =
    chi(K(m)) = P_K(m) = 0 for those m, which contradicts generation when K
    is nonzero. The earlier form of that sentence read h^0(K(m)) > 0 off
    P_K = 0 without the vanishing step; the same elision stands in the event
    of 2026-11-16 above whose note begins "Repairs on the reader's report of
    this batch", which is named here and left as written. Restored, as the
    report asks: the two passages of the earlier events of 2026-11-16 that
    the previous pass had rewritten in place. The first event of that date
    again reads as it was written, including "whose errata ask whether the
    statement is false", and its description of the pass is corrected here:
    that pass replaced step s1's argument with the annihilator argument, so
    the event cannot say the step kept the Hilbert-polynomial argument.
    Corrected in COMPLAINTS.md: the broken sentence in the 12.3 entry, which
    read "identically zero. the jump occurs", and the same missing vanishing
    step in its 2026-11-16 entry. Checked against the book in this pass:
    III.12.3 on printed pp. 291-292, Theorem II.5.17 on printed p. 121,
    Theorem III.5.2 on printed p. 228, Example III.9.8.4 on printed
    pp. 259-260. Not checked: no machine computation was run.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass on the reader's report of this batch, on the citations and
    the audit trail. (i) The solution-reviewed event of 2026-11-16 whose note
    begins "Repairs on the reader's report of this batch" is restored as it
    was written, and this event is appended after it rather than put in its
    place; the reference in the event above to that event "above" therefore
    has its referent again. (ii) The text
    versions of Egbert's solutions and of MathOverflow 90260 are named here,
    because the event of 2026-11-16 whose note begins "Published-solution
    search for this exercise" was restored to a text written before the
    citations were added: tmp/sources/hartshorne-solutions-egbert.md for
    Egbert and tmp/sources/mo-90260-trouble-with-semicontinuity.md for
    MathOverflow 90260. The Kim text version,
    tmp/sources/hartshorne-solutions-kim.md, is named in the remark on the
    card. (iii) The same event's "whose errata ask whether the statement is
    false" is wrong: Kim's doubt stands in his list of problems he has not
    solved, at the head of the text on PDF p. 1, not in a list of errata, as
    the remark on the card records. Checked against the book in this pass:
    III.12.3 on printed pp. 291-292 and Example III.9.8.4 on printed
    pp. 259-260, read in tmp/sources/hartshorne-1977-algebraic-geometry.md,
    where printed p. N is PDF p. N+15. Not checked: no machine computation was
    run in this pass.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fourth pass, on the audit trail and the rule that a dated event is never
    edited. Three things. (i) The event above whose note begins
    "Published-solution search for this exercise" was edited in place by
    commit 2145766034, which changed its citations of two printed pages: it
    read "Example III.9.8.4, printed pp. 274--275 ... and Exercise
    III.9.3.5(c), printed p. 285" and that commit made it "printed pp.
    259--260 ... Exercise IV.3.5(c), printed p. 315". It is restored as it was
    written in cd28c3bc2b, and the correction is here. The numbers it carried
    were the PDF folios of the text version, not the printed pages: in
    tmp/sources/hartshorne-1977-algebraic-geometry.md Example 9.8.4 stands
    between the markers of PDF pages 274 and 275, which are printed pp.
    259--260; the exercise meant is IV.3.5(c), whose section's exercises open
    on printed p. 315, PDF p. 330. (ii) The event above whose note begins
    "Third pass on the reader's report of this batch" was extended in place by
    commit 15a20526df with the sentence naming
    tmp/sources/hartshorne-1977-algebraic-geometry.md and the printed-to-PDF
    offset; it is restored as it was written in 1abd969bbb, and that sentence
    is here: the pages it cites were read in that text version, where printed
    p. N is PDF p. N+15. (iii) The event of 2026-10-29 above, whose note
    begins "Hartshorne III.12.3 prints the jumps", was shortened in place by
    commit 9979beae9c, which removed its second sentence, "The statement now
    asks for the jumps of h^0(t, I(1)) and h^1(t, I(1))." That edit was made
    on 2026-11-09, before the gate held dated events, and the record is of an
    earlier day, so it stands and is disclosed here rather than restored.
    Checked in this pass: this card's audit trail in git, commit by commit,
    and the two pages of the text version named in (i). Not checked: no other
    page was re-read, and no step was re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Fifth pass, on the one dated event the event above left disclosed. The
    source-checked event of 2026-10-29 is now restored to the text it carried
    at d383f9e9ee, its second sentence included: "The statement now asks for
    the jumps of h^0(t, I(1)) and h^1(t, I(1))." The previous pass read
    QUAL-11 as permitting a disclosed in-place edit to stand and said so; a
    correction to a dated event is a new event of the correcting commit's
    date, and the restoration is allowed precisely because the text it
    restores stands, whole, in an earlier revision of this path, so the event
    above is superseded on this point and is left as written. What the
    restored sentence says is corrected here: it is true of the card's own
    statement as it stood on 2026-10-29, which asked for the jumps of the
    twist, and false of the book, whose III.12.3 asks for h^0(t, I) and
    h^1(t, I) untwisted, as the first sentence of the same event says. The
    card's statement is the printed one, and the twist is discussed in the
    solution as the case in which the printed functions jump. Checked in this
    pass: this card's history at d383f9e9ee, 9979beae9c and HEAD, and the
    printed exercise in tmp/sources/hartshorne-1977-algebraic-geometry.md
    (printed p. N is PDF p. N+15), printed pp. 291-292. Not checked: no step
    was re-derived and no page was read beyond the exercise in this pass.
---

::: {.problem}
Let $X_1 \subseteq \PP_k^4$ be the \dfn{rational normal quartic curve}, the $4\dash$uple embedding of $\PP^1$ in $\PP^4$. Let $X_0 \subseteq \PP_k^3$ be a nonsingular rational quartic curve, such as the one in (I, Ex. 3.18b).

Use (9.8.3) to construct a flat family $\theset{X_t}$ of curves in $\PP^4$, parametrized by $T = \AA^1$, with the given fibres $X_1$ and $X_0$ for $t = 1$ and $t = 0$.

Let $\mci \subseteq \mco_{\PP^4 \times T}$ be the ideal sheaf of the total family $X \subseteq \PP^4 \times T$. Show that $\mci$ is flat over $T$. Then show that
$$
h^0(t, \mci) =
\begin{cases}
0 & t \neq 0 \\
1 & t = 0
\end{cases}
\qquad
h^1(t, \mci) =
\begin{cases}
0 & t \neq 0 \\
1 & t = 0
\end{cases}
.$$

This gives another example of cohomology groups jumping at a special point.
:::

::: {.solution}
The cohomology claim printed in the exercise is false as stated: for every $t$,
$$
h^0(t,\mci_t)=0,
\qquad
h^1(t,\mci_t)=0 .
$$
Indeed $0\to\mci_t\to\OO_{\PP^4}\to\OO_{X_t}\to0$ gives
$h^0(\mci_t)=\ker\bigl(H^0(\OO_{\PP^4})\to H^0(\OO_{X_t})\bigr)=0$, since
$H^0(\OO_{\PP^4})=k$ restricts injectively, and it gives
$h^1(\mci_t)=\operatorname{coker}\bigl(H^0(\OO_{\PP^4})\to H^0(\OO_{X_t})\bigr)
=h^0(\OO_{X_t})-1=0$, since $H^1(\PP^4,\OO)=0$. Here $h^0(\OO_{X_t})=1$ for
every $t$: for $t\ne0$ because $X_t$ is a connected reduced projective curve,
and for $t=0$ because the flat limit is reduced as well, as step s1 shows. So
there is no jump in the
untwisted ideal sheaf, and none can be produced from it by semicontinuity.

The jump the exercise is after appears after twisting by $\OO_{\PP^4}(1)$: the
statements proved below are
$$
h^0(\PP^4,\mci_t(1))=
\begin{cases}0,&t\ne0,\\ 1,&t=0,\end{cases}
\qquad
h^1(\PP^4,\mci_t(1))=
\begin{cases}0,&t\ne0,\\ 1,&t=0.\end{cases}
$$
The flat family and the flatness of $\mci$ are as printed, and are proved first
(steps s1 and s2); the erratum concerns only the two displayed cohomology
statements.

Use homogeneous coordinates
$$
[x_0:x_1:x_2:x_3:x_4]
$$
on $\PP^4$. The rational normal quartic is
$$
\nu_1:\PP^1\longrightarrow\PP^4,
\qquad
[s:u]\longmapsto
[s^4:s^3u:s^2u^2:su^3:u^4].
$$

::: pf

::: {.pf-step #s1}

Hartshorne's projection degeneration (III.9.8.3), applied by scaling
the coordinate $x_2$, gives a flat family
$$
X\longrightarrow T=\AA^1
$$
whose fibres for $a\ne0$ are
$$
X_a=
\left\{
[s^4:s^3u:a s^2u^2:su^3:u^4]
\right\},
$$
and whose special fibre is the reduced twisted quartic
$$
X_0=
\left\{
[s^4:s^3u:0:su^3:u^4]
\right\}
\subseteq V(x_2)\cong\PP^3.
$$

::: pf-proof

Let
$$
P=[0:0:1:0:0].
$$
This point does not lie on $X_1$. For $a\ne0$, let
$$
\sigma_a([x_0:x_1:x_2:x_3:x_4])
=
[x_0:x_1:a x_2:x_3:x_4].
$$
Then $X_a=\sigma_a(X_1)$, so over $\GG_m\subset\AA^1$ the family is
isomorphic to the product $X_1\times\GG_m$. Example III.9.8.3 takes its
flat projective closure over $\AA^1$. Set-theoretically the special fibre
is the projection of $X_1$ from $P$ to the hyperplane $x_2=0$, namely the
displayed twisted quartic.

Flatness makes the Hilbert polynomial of every fibre equal to that of the
rational normal quartic:
$$
P(m)=4m+1.
$$
The reduced projected curve is isomorphic to $\PP^1$ by
[[P-AGH318PROJNORMAL|Exercise I.3.18]], and its hyperplane bundle pulls
back to $\mco_{\PP^1}(4)$, so that reduced curve, call it $X_0$, has the same
Hilbert polynomial $4m+1$.

Let $Z$ be the special fibre, a closed subscheme of $\PP^4$ with
$P_Z(m)=4m+1$ because the family is flat, and let $X_0$ be the reduced curve
just described, which is the underlying reduced scheme of $Z$. The kernel $K$
of $\OO_Z\to\OO_{X_0}$ is a coherent sheaf supported on the curve $X_0$. The
Euler characteristic is additive on the short exact sequence
$0\to K\to\OO_Z\to\OO_{X_0}\to0$, so
$$
P_K(m)=P_Z(m)-P_{X_0}(m)=0
$$
identically. If $K\ne0$, then for $m\gg0$ the twist $K(m)$ is generated by its
global sections (Theorem II.5.17, printed p. 121) and $H^1(\PP^4,K(m))=0$
(Serre vanishing, Theorem III.5.2, printed p. 228). For those $m$ the vanishing
gives
$$
h^0(K(m))=\chi(K(m))=P_K(m)=0,
$$
whereas generation gives $h^0(K(m))>0$ as soon as $K\ne0$. The two are
incompatible, so $K=0$: the special fibre is the reduced curve $X_0$, with no
nilpotent or embedded component.

A nilpotent thickening would give such a $K$, so equal Hilbert polynomials
together with Serre vanishing settle the question. It is not the only route:
Kim reaches the same
conclusion from the closed immersion $\PP^1\times\AA^1\hookrightarrow
\PP^4\times\AA^1$ that the family itself is (see the remark below), and the
collapsed coordinate $x_2$ of this family is annihilated by all five
coordinates at $a=0$, which is what makes the naive reading of it on an affine
chart wrong; that computation is in the remark, where it refutes the published
counterargument.

:::

:::

::: {.pf-step #s2}

The ideal sheaf
$$
\mci\subseteq\mco_{\PP^4\times T}
$$
of the total family is flat over $T$.

::: pf-proof

There is an exact sequence
$$
0
\longrightarrow
\mci
\longrightarrow
\mco_{\PP^4\times T}
\longrightarrow
\mco_X
\longrightarrow0.
$$
The middle term is flat over $T$, and $\mco_X$ is flat over $T$ because
$X\to T$ is flat. In an exact sequence, the kernel of a surjection between
flat modules is flat. Therefore $\mci$ is flat over $T$.

:::

:::

::: {.pf-step #s3}

After twisting by $\mco_{\PP^4}(1)$, for every $a\ne0$ one has
$$
H^0(\PP^4,\mci_a(1))
=
H^1(\PP^4,\mci_a(1))
=
0.
$$

::: pf-proof

Since $\mco_X$ is flat over $T$, restricting the exact sequence of
step [](#s2){.pf-ref} to the fibre over $t$ remains exact, so
$\mci_t$ is the ideal sheaf of $X_t$ in $\PP^4$. Twisting this fibre
sequence by $\mco_{\PP^4}(1)$ gives
$$
0
\longrightarrow
\mci_a(1)
\longrightarrow
\mco_{\PP^4}(1)
\longrightarrow
\mco_{X_a}(1)
\longrightarrow0.
$$
For $a\ne0$, the embedding $X_a\cong\PP^1\hookrightarrow\PP^4$ is the
complete linear series $\linearsystem{\mco_{\PP^1}(4)}$. Therefore the restriction map
$$
H^0(\PP^4,\mco(1))
\longrightarrow
H^0(X_a,\mco_{X_a}(1))
$$
identifies two five-dimensional spaces and sends the five coordinate
linear forms to a basis of $H^0(\PP^1,\mco(4))$. Hence it is an
isomorphism. Since $H^1(\PP^4,\mco(1))=0$, the long exact sequence gives
the claimed vanishing.

:::

:::

::: {.pf-step #s4}

For the special fibre,
$$
h^0(\PP^4,\mci_0(1))
=
h^1(\PP^4,\mci_0(1))
=
1.
$$

::: pf-proof

The pullback of $\mco_{X_0}(1)$ to $\PP^1$ is again
$\mco_{\PP^1}(4)$, so
$$
h^0(X_0,\mco_{X_0}(1))=5.
$$
Under the parametrization
$$
[s:u]\longmapsto[s^4:s^3u:0:su^3:u^4],
$$
the restriction map
$$
H^0(\PP^4,\mco(1))
\longrightarrow
H^0(\PP^1,\mco(4))
$$
sends the coordinate basis to
$$
s^4,\ s^3u,\ 0,\ su^3,\ u^4.
$$
Its kernel is therefore the one-dimensional span of $x_2$, and its image
has codimension one, missing the section $s^2u^2$.

The long exact sequence of
$$
0
\to
\mci_0(1)
\to
\mco_{\PP^4}(1)
\to
\mco_{X_0}(1)
\to0
$$
and the vanishing $H^1(\PP^4,\mco(1))=0$ identify
$$
H^0(\PP^4,\mci_0(1))
$$
with that kernel and
$$
H^1(\PP^4,\mci_0(1))
$$
with that cokernel. Both have dimension one.

:::

:::

::: {.pf-step #s5}

Therefore
$$
h^0(t,\mci(1))
=
h^1(t,\mci(1))
=
\begin{cases}
0,&t\ne0,\\
1,&t=0.
\end{cases}
$$

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give the displayed values.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} construct the required flat family and prove flatness of
its ideal sheaf, and steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove the
cohomology jump.

:::

:::

:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), Chapter III §12, Exercise 12.3, PDF p. 215, text version `tmp/sources/hartshorne-solutions-kim.md`, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: his solution checks that the flat limit at $t=0$ is the reduced quartic $X_0$ inside $V(x_2)\cong\PP^3$, from the closed immersion $\PP^1\times\AA^1\hookrightarrow\PP^4\times\AA^1$ that the family is, and that $\mci$ is flat over $T$ from the exact sequence $0\to\mci\to\OO_{\PP^4\times T}\to\OO_X\to0$, and then stops: it does not compute the two cohomology functions. His list of problems he has not solved, at the head of the text on PDF p. 1, asks "Exercise 3.12.3: The statement seems to be false?"; it is not a list of corrections, and it gives no reason. The printed claim is indeed false, and the erratum and steps s3--s5 above supply the computation the source omits, for $\mci(1)$.

One published answer claims a corrected jump in the printed functions themselves, and it does not hold. MathOverflow question 90260, *Trouble with semicontinuity* (2012-03-05), answer by S. Kovács (2012-03-05, with an addendum), computes $h^0(\OO_{X_0})=2$ from a nilpotent $x_2$ and concludes $h^1(\PP^4,\mci_0)=1$, which would make the printed $h^1$ line right and only the $h^0$ line wrong. His fibre ideal is $\mathcal J+(x_0x_2,x_1x_2,x_2^2,x_3x_2,x_4x_2)$ with $\mathcal J$ the ideal of the quartic in $\PP^3$, and in it $x_2$ is annihilated by every coordinate. That annihilator is decisive, and the questioner on the same thread already says so in the question body ($x_2/x_i=x_2x_i/x_i^2=0$ after the question's own edit): in the degree-zero localization at any $x_i$ the coordinate $x_i$ is invertible, so the class of $x_2$ is $x_2x_i/x_i^2=0$ in the coordinate ring of every standard affine chart, and a section of $\OO(1)$ that vanishes on each chart is the zero section. What the addendum of the answer gets wrong is the chart: for the chart $x_0\ne0$ it writes the coordinate ring of $\mathscr X_0\cap U_0$ as $k[y_1,x_2]/(y_1x_2,x_2^2)$ with $y_1=x_1/x_0$, mixing the degree-zero localization, in which $y_1$ lives, with the degree-one coordinate $x_2$; the element of that chart is $x_2/x_0$, and it satisfies $y_1\cdot(x_2/x_0)=x_1x_2/x_0^2=0$ as well as $(x_2/x_0)^2=0$, so it is zero there too. Hence $x_2$ is not a function on $X_0$, $h^0(\OO_{X_0})=1$, and $h^1(\PP^4,\mci_0)=0$. The annihilating relations are exactly what this family gives, in $\ker(k[a,x_0,\ldots,x_4]\to k[a,s,u])$ with $x_0=s^4$, $x_1=s^3u$, $x_2=as^2u^2$, $x_3=su^3$, $x_4=u^4$: $x_2x_0=ax_1^2$, $x_2x_1=ax_0x_3$, $x_2x_3=ax_1x_4$, $x_2x_4=ax_3^2$, $x_2^2=a^2x_0x_4$, all of which are $0$ at $a=0$. The contrast is Example III.12.9.2, printed p. 289, where the nilpotent $z$ of the cubic family satisfies $z^2=yz=xz=0$ but $zw\ne0$; that single non-vanishing product is why $h^0(\OO)$ is $2$ there and the jump in $h^0,h^1$ of $\OO$ is genuine. A second answer in the same thread, by J. Böhm (2015-05-15), computes the fibre ideal by elimination and reports all $H^i(\PP^4,\mci_0)=0$ for $i=0,\ldots,4$, which agrees with the argument above; he asks for a reconciliation and receives none.
:::
