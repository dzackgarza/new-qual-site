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
---

::: {.problem}
Use the universal coefficient theorem to show that if $H_*(X; \ZZ)$ is finitely generated, so the Euler characteristic $\chi(X) = \sum_n (-1)^n \operatorname{rank} H_n(X; \ZZ)$ is defined, then for any coefficient field $F$ we have $\chi(X) = \sum_n (-1)^n \dim H_n(X; F)$.
:::

::: {.solution}
Hatcher's hypothesis is the source's. tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008) (read in `tmp/sources/tomdieck-algebraic-topology-ranicki.md`), calls a pair $(X,A)$ of finite $R$-type, for $R$ a principal ideal domain, if the $R$-modules $H_i(X,A;R)$ are finitely generated and only finitely many of them are nonzero, and puts $\chi(X,A;R)=\sum_i(-1)^i\operatorname{rank}_RH_i(X,A;R)$ (printed p. 310); with $A=\emptyset$ and $R=\ZZ$ that is the exercise's hypothesis that $\chi(X)$ is defined. The source's proof, Proposition (12.4.4) on printed p. 310, does not use the universal coefficient theorem: it replaces $S_*(X)$ by a finite free chain complex and compares ranks along the alternating sum. It proves the statement for every principal ideal domain $R$, and the exercise's coefficient field $F$ is that case.

*The finite free model.* (Proposition (11.6.4), printed p. 289.) Let $R$ be a principal ideal domain and $C=(C_n)$ a chain complex of free $R$-modules with finitely generated homology. For each $n$ choose a finitely generated submodule $F_n$ of $Z_n(C)$ which the quotient map $Z_n(C)\to H_n(C)$ carries onto $H_n(C)$, and take $F_n=0$ where $H_n(C)=0$; let $G_n$ be the kernel of $F_n\to H_n(C)$. Put
$$
D_n=F_n\oplus G_{n-1},\qquad d_n(x,y)=(y,0).
$$
Then $D=(D_n,d_n)$ is a free chain complex of finite type, and $\ker d_n=\{(x,y):y=0\}=F_n\oplus0$ while $\operatorname{im}d_{n+1}=G_n\oplus0$, so $H_n(D)=F_n/G_n$, which is $H_n(C)$ because $F_n$ was chosen to map onto $H_n(C)$ with kernel $G_n$. Since $G_n$ is a free submodule of $B_n(C)$, a submodule of a free module over a principal ideal domain being free, there are homomorphisms $\varphi_n:G_n\to C_{n+1}$ with $c_{n+1}\varphi_n(y)=y$ for $y\in G_n$. The degreewise maps
$$
\psi_n:D_n=F_n\oplus G_{n-1}\longrightarrow C_n,\qquad (x,y)\longmapsto x+\varphi_{n-1}(y)
$$
form a chain map, because $x\in Z_n(C)$ gives $c_n\psi_n(x,y)=c_n(x)+c_n\varphi_{n-1}(y)=0+y=\psi_{n-1}(y,0)=\psi_{n-1}d_n(x,y)$; and $\psi$ induces an isomorphism on homology, since under the identification $H_n(D)=F_n/G_n$ just made the induced map is $[x]\mapsto[x]$, an isomorphism of $F_n/G_n$ onto $H_n(C)$. By Theorem (11.6.3) (printed p. 288), $\psi$ is a chain equivalence.

Applied to $C=S_*(X)$, which is a complex of free $\ZZ$-modules with finitely generated homology, this gives a chain complex $D$ of finitely generated free abelian groups, chain equivalent to $S_*(X)$. Here $D_n=0$ for $n\gg0$: for such $n$ and for $n-1$ one has $H_n(X;\ZZ)=H_{n-1}(X;\ZZ)=0$, so $F_n$ and $F_{n-1}$ were chosen $0$ — the zero submodule maps onto the zero group — and then $G_n=\ker(F_n\to H_n)=0$ and $D_n=F_n\oplus G_{n-1}=0$. It is the choice of the $F_n$ that makes the model finite, not a consequence of the vanishing of the homology alone. That is the reduction the source uses: "the singular complex $S_*(X)$ is chain equivalent to a chain complex $D_*$ of finitely generated free abelian groups with only finitely many of the $D_n$ non-zero".

*The Euler computation.* (Proposition (12.4.4), printed p. 310.) For a principal ideal domain $R$, $D\otimes R$ is a free chain complex of finite type over $R$, and $\psi\otimes\id_R$ is a chain equivalence, so $H_n(D\otimes R)\cong H_n(X;R)$; in particular $X$ is of finite $R$-type. The rank function is additive in the sense of the source's definition on printed p. 309: for an exact sequence $0\to M'\to M\to M''\to0$ of finitely generated $R$-modules, tensoring with the fraction field $K$ of $R$ is exact and gives $\dim_KM\otimes K=\dim_KM'\otimes K+\dim_KM''\otimes K$. Proposition (12.4.1), printed p. 309 and proved there by induction on the length of the complex, therefore gives
$$
\sum_i(-1)^i\operatorname{rank}_R(D_i\otimes R)=\sum_i(-1)^i\operatorname{rank}_RH_i(D\otimes R)=\sum_i(-1)^i\operatorname{rank}_RH_i(X;R)=\chi(X;R).
$$
Since $D_i$ is free of rank $d_i$ over $\ZZ$, $D_i\otimes R$ is free of rank $d_i$ over $R$, and applying (12.4.1) once more, now with the additive invariant $\operatorname{rank}_\ZZ$ over $\ZZ$,
$$
\chi(X;R)=\sum_i(-1)^id_i=\sum_i(-1)^i\operatorname{rank}_\ZZ D_i=\sum_i(-1)^i\operatorname{rank}_\ZZ H_i(X;\ZZ)=\chi(X).
$$
Taking $R=F$ a field, where $\operatorname{rank}_F=\dim_F$, gives $\chi(X)=\sum_n(-1)^n\dim_FH_n(X;F)$, and the right side is a finite sum because $H_n(X;F)$ is of finite dimension and vanishes for $n\gg0$.

*The route the exercise itself names.* Hatcher's exercise says to use the universal coefficient theorem, and that route reaches the same conclusion from printed inputs. Theorem 3A.3 (p. 264) gives the exact sequence $0\to H_n(X;\ZZ)\otimes F\to H_n(X;F)\to\operatorname{Tor}(H_{n-1}(X;\ZZ),F)\to0$, so $\dim_FH_n(X;F)$ is the sum of the two outer dimensions; with $H_n(X;\ZZ)\cong\ZZ^{r_n}\oplus T_n$ and $t_n$ the number of $p$-power cyclic summands of $T_n$, Proposition 3A.5 (pp. 265--266) gives $\dim_FH_n(X;F)=r_n$ for $\operatorname{char}F=0$ and $r_n+t_n+t_{n-1}$ for $\operatorname{char}F=p$. In both cases the torsion terms cancel in the alternating sum, since $\sum_n(-1)^n(t_n+t_{n-1})=0$, leaving $\sum_n(-1)^nr_n=\chi(X)$.

Checked against Hatcher, *Algebraic Topology* (2002), §3.A Exercise 1, printed p. 267, read in `tmp/sources/hatcher-2002-algebraic-topology.md`: "Use the universal coefficient theorem to show that if $H_*(X;\ZZ)$ is finitely generated, so the Euler characteristic $\chi(X)=\sum_n(-1)^n\operatorname{rank}H_n(X;\ZZ)$ is defined, then for any coefficient field $F$ we have $\chi(X)=\sum_n(-1)^n\dim H_n(X;F)$." The source proves the statement for every principal ideal domain and every pair $(X,A)$, not only for a field and a space.
:::

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), read in the text of the book held as `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, whose file name carries "ranicki" and names no translator, the book being tom Dieck's own English text: the definition of finite $R$-type and of $\chi(X,A;R)$ on printed p. 310; Proposition (12.4.1), the alternating sum along a chain complex, on printed p. 309; Propositions (12.4.3) and (12.4.4) on printed p. 310, the second being the exercise's statement for every principal ideal domain and proved without the universal coefficient theorem, whose route the exercise names and which the solution's last paragraph gives; and Proposition (11.6.4) on printed p. 289 for the finite free model, with Theorem (11.6.3) on printed p. 288. The exercise is Exercise 1 of §3.A, printed p. 267.
:::
