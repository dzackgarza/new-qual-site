---

schema: qual/card@1
id: E-HAT-3.A-1
kind: problem
title: "Euler characteristic is independent of coefficient field"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 1; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 1, printed p. 267. The statement
    matches the print word for word, including the hypothesis that $H_*(X;\ZZ)$ be finitely generated
    and the phrase "for any coefficient field $F$". Repaired in three places where the proof was
    incomplete rather than false: the finiteness of the two alternating sums is now stated rather
    than assumed; the characteristic-$p$ case runs Theorem 3A.3 over $F$ directly through
    Proposition 3A.5(2), (4) and (5), instead of asserting that it suffices to compute over $\FF_p$
    and extend scalars; and Theorem 3A.3 (p. 264) and Proposition 3A.5(3) (p. 265) are cited where
    the proof had said only "the universal coefficient theorem". Checked against Hatcher's
    definitions on pp. 261-266: $C_*(X;G)=C_*(X)\otimes G$, $\operatorname{Tor}_n=0$ for $n>1$, and
    Tor as defined from a free resolution. No published solution of this exercise is in the
    retained sets; recorded in COMPLAINTS.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 267. Its published proof is Hatcher's own: Theorem 3A.3 (universal coefficients for homology with coefficients), printed p. 264 with its complete proof, and Proposition 3A.5, printed pp. 265--266 with its complete proof, which gives the two facts the deduction needs (that $\operatorname{Tor}(\ZZ^{r},F)=0$ and that $\operatorname{Tor}(T,F)$ has dimension equal to the number of $p$-power summands killed by the characteristic). The card's proof is that deduction written out: the UCT splits $H_n(X;F)$ into $H_n(X;\ZZ)\otimes F$ plus $\operatorname{Tor}(H_{n-1}(X;\ZZ),F)$, and the alternating sum of the dimensions telescopes because the torsion correction appears with a compensating sign in the neighbouring degree. Checked against the book: the printed statement, the finite-generation hypothesis, and the two coefficient cases (characteristic zero and characteristic $p$). Not claimed: that the book prints this exercise; it prints the two theorems the exercise applies.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    The proof is now the source's: tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics,
    2008), Proposition (11.6.4) on printed **p. 289** for the finite free model, Theorem (11.6.3) on
    printed p. 288 for the chain equivalence, Proposition (12.4.1) on printed p. 309 for the
    alternating sum, and Proposition (12.4.4) on printed **p. 310**, all transcribed with the two
    verifications the source compresses into "one verifies that $\psi$ is a chain map" and "some
    elementary algebra". The route is the one this card now states: a finite free chain complex
    replaces $S_*(X)$, ranks are compared along the alternating sum, and **the universal coefficient
    theorem is not used**. The source's statement is the pair version for every principal ideal
    domain, so the exercise's field case follows and the card says the source is stronger. The
    previous proof was the universal coefficient theorem route, which is what the printed exercise
    tells the reader to use; it is kept as the closing paragraph and labelled as Hatcher's route with
    its printed inputs (Theorem 3A.3, p. 264; Proposition 3A.5, pp. 265--266), so the card answers the
    exercise as printed while resting on the source for the proof. Page check: (11.6.4) is on p. 289,
    not 288 — the extracted page marker for 289 precedes it and the table of contents puts the start
    of §11.7 on p. 289 — and (12.4.1) is on p. 309, with (12.4.2)--(12.4.4) on p. 310. Checked
    against Hatcher (2002), §3.A Exercise 1, printed p. 267, quoted on the card. Not claimed: that
    tom Dieck states Hatcher's exercise or names the universal coefficient theorem.
- event: solution-written
  by: claude
  date: 2026-11-14
  note: >-
    Two steps of the transcription of tom Dieck (11.6.4) were asserted and are now proved, and one of
    them was stated as if it followed from the vanishing of the homology. (1) "hence $F_n=0$", which
    the card gave as a consequence of $H_n(X;\ZZ)=0$, is a choice: $F_n$ is chosen among the finitely
    generated submodules of $Z_n$ mapping onto $H_n$, and the card now says that it is chosen $0$ where
    $H_n=0$, the zero submodule mapping onto the zero group. The vanishing of $D_n$ also needs
    $F_{n-1}=0$, since $D_n=F_n\oplus G_{n-1}$ and $G_{n-1}=\ker(F_{n-1}\to H_{n-1})$; with both
    chosen $0$ one gets $G_n=0$ and $D_n=0$, which is what the card now says. (2) The isomorphism
    $H_n(D)\cong H_n(C)$ induced by $\psi$ was asserted. Both halves are now computed:
    $\ker d_n=F_n\oplus0$ and $\operatorname{im}d_{n+1}=G_n\oplus0$, so $H_n(D)=F_n/G_n=H_n(C)$; and
    under that identification $\psi_*$ is $[x]\mapsto[x]$, which is an isomorphism by the choice of
    $F_n$ and $G_n$. The chain-map computation was already on the card and is unchanged in substance,
    with the term $c_n(x)=0$ now written out. These are the two places the source covers with "one
    verifies that $\psi$ is a chain map which induces an isomorphism of homology groups", and with
    them written the card's earlier note that both verifications are present is true. Checked against
    tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), Proposition (11.6.4) with
    its proof on printed p. 289 and Theorem (11.6.3) on printed p. 288, and against Hatcher (2002),
    §3.A Exercise 1 on printed p. 267.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Two citation defects. (1) The remark below the solution read "the definition of finite $R$-type,
    Proposition (12.4.1) on printed p. 309", which can be read as putting the definition on p. 309. It
    is on p. 310: the definition of finite $R$-type with the homological Euler characteristic
    $\chi(X,A;R)$ opens the paragraph after (12.4.3), on the page whose folio is 310, which is PDF
    page 323 of `tmp/sources/tomdieck-algebraic-topology-ranicki.pdf`, while (12.4.1), the
    alternating sum along a chain complex, is on the page whose folio is 309 (PDF page 322), together
    with the definition of an additive invariant that it uses. The remark now lists the two pages
    separately and in that order. (11.6.3) and (11.6.4) were checked the same way this pass, on the
    folios 288 and 289 (PDF pages 301 and 302) the card already gave them. (2) No citation named its
    text version. tom Dieck is cited from the text of the Ranicki translation,
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, and Hatcher from
    `tmp/sources/hatcher-2002-algebraic-topology.md`; the sentence naming each now says so, and the
    remark's page list was rewritten to name them. Nothing in the statement or the proof changes. Not
    claimed: a text version for any other source, this card citing none; and nothing was read from a
    rendered page.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass: the source was misnamed, and the record is corrected here as well
    as on the card. tom Dieck's *Algebraic Topology* (EMS Textbooks in Mathematics, 2008) is his own
    English text; the reading copy
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md` carries "ranicki" in its file name only, and
    that word names no translator of the book. The card and the note of this date called it "the Ranicki
    translation", which is withdrawn: both places now say that the file name carries the word and that
    the book is tom Dieck's own. Nothing else changes: the propositions, their folios, the statement of
    Exercise 1 of §3.A on printed p. 267 and every step of the proof stand as they were, and no page was
    re-read for this correction beyond the folios 288, 289, 309 and 310 the card already gives.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card. The `source-corrected` event of this date that
    begins "Two citation defects" was changed in place by commit e945aab1c4, which replaced its
    sentence "tom Dieck is cited from the text of the Ranicki translation,
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md`" with the explanation now standing in that
    event. A dated event records what the session that wrote it found; the original sentence is
    therefore quoted here, and the correction is this event: tom Dieck's *Algebraic Topology* is his
    own English text, and "ranicki" is only in the reading copy's file name and names no translator.
    The card body and the remark were corrected at the same time and already say so; nothing in the
    statement, the pages or the proof changes. Not verified in this pass beyond the folios already on
    the card: nothing was read from a rendered page.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card: the record, not the mathematics. The
    `source-corrected` event of 2026-11-16 beginning "Two citation defects" is restored
    to the text commit 7dd02358ce wrote; e945aab1c4 replaced one of its sentences in
    place, and the third-pass event below quoted that sentence instead of undoing the
    replacement. The restored sentence reads "tom Dieck is cited from the text of the
    Ranicki translation, `tmp/sources/tomdieck-algebraic-topology-ranicki.md`", and the
    correction this event owes it is the one the event below states: tom Dieck's
    *Algebraic Topology* (EMS Textbooks in Mathematics, 2008) is his own English text,
    "ranicki" is in the reading copy's file name only and names no translator, and the
    card body and remark now say so. Nothing in the statement, the pages or the proof
    changes. Not checked in this pass: no page was read from a rendered copy.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied at paragraph level: the solution opens with the provenance
    convention for a prose proof, and the paragraph applying (11.6.4) to $C=S_*(X)$ is of the kind
    that names no source and is the card's own application of the proposition cited above it.
    Checked: that (11.6.4) on printed p. 289 and (12.4.4) on printed p. 310 are named where they are
    used. Not changed: any argument.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured the prose proof into numbered steps under #2, one step per printed input: the finite
    free model (tom Dieck (11.6.4), printed p. 289, with (11.6.3) on p. 288 for the chain
    equivalence), its application to $C=S_*(X)$ with the vanishing of $D_n$ for large $n$, the
    additivity of rank and the alternating-sum formula ((12.4.1), printed p. 309), the Euler
    computation over a principal ideal domain ((12.4.4), printed p. 310), and the field case together
    with the universal coefficient route the exercise names (Hatcher Theorem 3A.3 p. 264 and
    Proposition 3A.5 pp. 265--266, whose torsion terms cancel because
    $\sum_n(-1)^n(t_n+t_{n-1})=0$). Checked against the reads already recorded for this card: that
    each cited proposition is named at the step that uses it, and that the finite-model step really
    produces $D_n=0$ for large $n$ rather than inheriting it from the homology. Re-checked the
    arithmetic of both routes: the torsion cancellation in the UCT route and the two applications of
    additivity in the tom Dieck route. Not claimed: a new reading of tom Dieck or Hatcher in this
    batch, the text versions in `tmp/sources` having been the ones consulted; and no certificate of
    the statement in Lean, which #134 records as open for this card.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 276 carries the running head 267, so
    the printed page is the one the card's earlier event claimed. The durable part of the locator is
    that printed page; the file path names this machine's copy and `tmp/sources` does not survive a VM
    reset. No mathematics changed.
---

::: {.problem}
This is Exercise 1 of Section 3.A of Hatcher, *Algebraic Topology* (2002), read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf`; the statement below is its wording.

Use the universal coefficient theorem to show that if $H_*(X; \ZZ)$ is finitely generated, so the Euler characteristic $\chi(X) = \sum_n (-1)^n \operatorname{rank} H_n(X; \ZZ)$ is defined, then for any coefficient field $F$ we have $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$.
:::

::: {.solution}
The proof below is tom Dieck's, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), read in `tmp/sources/tomdieck-algebraic-topology-ranicki.md`: a pair $(X,A)$ is of finite $R$-type for a principal ideal domain $R$ when the modules $H_i(X,A;R)$ are finitely generated and only finitely many are nonzero, with $\chi(X,A;R)=\sum_i(-1)^i\rank_RH_i(X,A;R)$ (printed p. 310); with $A=\emptyset$ and $R=\ZZ$ that is the exercise's hypothesis. The source proves the statement for every principal ideal domain and every pair, by replacing $S_*(X)$ with a finite free model and comparing ranks along the alternating sum, without the universal coefficient theorem; the route the exercise names is given in the last step. The exercise is Exercise 1 of §3.A, read in `tmp/sources/hatcher-2002-algebraic-topology.md`.

::: pf

::: {.pf-step #model}
Let $R$ be a principal ideal domain and $C$ a chain complex of free $R$-modules with finitely generated homology. Then there is a chain complex $D$ of finitely generated free $R$-modules, with $D_n=0$ for $n\gg0$, and a chain equivalence $\psi\colon D\to C$.

::: pf-proof
This is Proposition (11.6.4) on printed p. 289. For each $n$ choose a finitely generated submodule $F_n\subseteq Z_n(C)$ mapping onto $H_n(C)$, taking $F_n=0$ where $H_n(C)=0$, and let $G_n$ be the kernel of $F_n\to H_n(C)$; put $D_n=F_n\oplus G_{n-1}$ and $d_n(x,y)=(y,0)$. Then $\ker d_n=F_n\oplus0$ and $\operatorname{im}d_{n+1}=G_n\oplus0$, so $H_n(D)=F_n/G_n\cong H_n(C)$. Each $G_n$ is a submodule of the free module $B_n(C)=Z_n(C)$, hence free over the principal ideal domain $R$, so there are maps $\varphi_n\colon G_n\to C_{n+1}$ with $c_{n+1}\varphi_n(y)=y$; the degreewise $\psi_n(x,y)=x+\varphi_{n-1}(y)$ satisfies $c_n\psi_n=\psi_{n-1}d_n$ because $x$ is a cycle, so $\psi$ is a chain map, and it induces the isomorphism $F_n/G_n\to H_n(C)$ just computed. By Theorem (11.6.3) on printed p. 288 a chain map inducing isomorphisms on homology is a chain equivalence.
:::

:::

::: {.pf-step #finite-model}
For $C=S_*(X)$ the model $D$ may be taken with $D_n=0$ for $n\gg0$.

::: pf-proof
$S_*(X)$ is a complex of free $\ZZ$-modules whose homology is finitely generated by hypothesis, so step [](#model){.pf-ref} applies. For $n$ large enough both $H_n(X;\ZZ)$ and $H_{n-1}(X;\ZZ)$ vanish, so $F_n=0$ and $F_{n-1}=0$ — the zero submodule mapping onto the zero group — whence $G_n=0$ and $D_n=F_n\oplus G_{n-1}=0$. It is the choice of the $F_n$ that makes the model finite, not the vanishing of the homology alone.
:::

:::

::: {.pf-step #additivity}
For an exact sequence $0\to M'\to M\to M''\to0$ of finitely generated $R$-modules, $\rank_RM=\rank_RM'+\rank_RM''$; hence for a chain complex of finite type $\sum_i(-1)^i\rank_RC_i=\sum_i(-1)^i\rank_RH_i(C)$.

::: pf-proof
Tensoring the exact sequence with the fraction field $K$ of $R$ is exact, since $K$ is flat over a principal ideal domain, and $\rank_RM=\dim_KM\otimes_RK$; dimension is additive on short exact sequences of $K$-vector spaces. The alternating-sum statement is Proposition (12.4.1) on printed p. 309, proved there by induction on the length of the complex, using exactly that additivity.
:::

:::

::: {.pf-step #euler}
$\chi(X;R)=\sum_i(-1)^i\rank_RH_i(X;R)=\sum_i(-1)^i\rank_\ZZ D_i=\chi(X)$ for every principal ideal domain $R$, in particular $X$ is of finite $R$-type.

::: pf-proof
$D\otimes R$ is a free chain complex of finite type over $R$ and $\psi\otimes\id_R$ is a chain equivalence, so $H_n(D\otimes R)\cong H_n(X;R)$ and only finitely many of these vanish. Since $D_i$ is free of rank $d_i$ over $\ZZ$, the module $D_i\otimes R$ is free of rank $d_i$ over $R$. Applying step [](#additivity){.pf-ref} to $D\otimes R$ over $R$, and again to $D$ over $\ZZ$ with the additive invariant $\rank_\ZZ$,
$$
\chi(X;R)=\sum_i(-1)^i\rank_R(D_i\otimes R)=\sum_i(-1)^id_i=\sum_i(-1)^i\rank_\ZZ D_i=\sum_i(-1)^i\rank_\ZZ H_i(X;\ZZ)=\chi(X).
$$
This is Proposition (12.4.4) on printed p. 310.
:::

:::

::: {.pf-step}
$\boxed{\chi(X)=\sum_n(-1)^n\dim_FH_n(X;F)}$ for every coefficient field $F$.

::: pf-proof
Take $R=F$ a field in step [](#euler){.pf-ref}, where $\rank_F=\dim_F$ and $F$ is a principal ideal domain; the right-hand side is a finite sum because $H_n(X;F)$ is finite dimensional and vanishes for $n\gg0$ by the same step. Alternatively, along the route the exercise names: Theorem 3A.3 (p. 264) gives the exact sequence $0\to H_n(X;\ZZ)\otimes F\to H_n(X;F)\to\operatorname{Tor}(H_{n-1}(X;\ZZ),F)\to0$, so $\dim_FH_n(X;F)$ is the sum of the two outer dimensions, and with $H_n(X;\ZZ)\cong\ZZ^{r_n}\oplus T_n$ and $t_n$ the number of cyclic $p$-power summands of $T_n$, Proposition 3A.5 (pp. 265--266) gives $\dim_FH_n(X;F)=r_n$ when $\operatorname{char}F=0$ and $r_n+t_n+t_{n-1}$ when $\operatorname{char}F=p$. In both cases the torsion terms cancel in the alternating sum, because $\sum_n(-1)^n(t_n+t_{n-1})=0$, leaving $\sum_n(-1)^nr_n=\chi(X)$.
:::

:::

:::
:::
::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), read in the text of the book held as `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, whose file name carries "ranicki" and names no translator, the book being tom Dieck's own English text: the definition of finite $R$-type and of $\chi(X,A;R)$ on printed p. 310; Proposition (12.4.1), the alternating sum along a chain complex, on printed p. 309; Propositions (12.4.3) and (12.4.4) on printed p. 310, the second being the exercise's statement for every principal ideal domain and proved without the universal coefficient theorem, whose route the exercise names and which the solution's last paragraph gives; and Proposition (11.6.4) on printed p. 289 for the finite free model, with Theorem (11.6.3) on printed p. 288. The exercise is Exercise 1 of §3.A.
:::
