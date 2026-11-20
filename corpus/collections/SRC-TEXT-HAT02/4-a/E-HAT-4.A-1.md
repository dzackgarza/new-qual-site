---
schema: qual/card@1
id: E-HAT-4.A-1
kind: problem
title: "Homotopies of maps to topological groups are basepoint-preserving"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    Three statements are corrected, all raised by a local reader. (1) The two events of 2026-11-14
    and 2026-11-16 said that Davis--Kirk add "non-degeneracy of the basepoint of $Z$" as a hypothesis
    the exercise does not make, and that "the exercise as printed assumes nothing of $Z$". The
    second is false of the section: Hatcher states on printed p. 421 that $Z$ is a CW complex with
    basepoint a $0$-cell, which is Davis--Kirk's $K_*$ condition on the source of maps (printed
    p. 156), so the published argument covers the exercise as printed, and the card now says so.
    (2) Those events also dropped the path-connectedness hypothesis of Davis--Kirk Theorem 6.57:
    the quotient statement needs the target path connected, while the step the exercise uses,
    $\Phi[f_0]=\Phi[f_1]\Rightarrow[u][f_0]=[f_1]$, is printed without it (p. 158). The card now
    states both hypotheses where they belong. (3) The solution's description of Hatcher's Example
    4A.3 is corrected: it does not normalise a homotopy by the track of the basepoint; it gives the
    homotopy $f_s(z)=f(z)\gamma(s)$, which carries the basepoint along $\gamma$ and ends at a map
    homotopic to $f$. The `pf` block is unchanged and the card's own derivation still covers every
    based space. Checked in the text versions `tmp/sources/hatcher-2002-algebraic-topology.md` and
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md` and in the PDF text layer of
    `tmp/sources/davis-kirk-lecture-notes-algebraic-topology.pdf`. Not checked: the pagination of
    the 2001 bound volume of Davis--Kirk.
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.A Exercise 1, printed p. 426; the statement
    matches the print. The proof is correct and complete as it stands and needed no repair:
    $F(z,t)=H(z,t)\gamma(t)^{-1}$ with $\gamma(t)=H(z_0,t)$ is continuous because multiplication and
    inversion in a topological group are, has $F(z,0)=f(z)x_0^{-1}=f(z)$ and
    $F(z,1)=g(z)x_0^{-1}=g(z)$, and is basepoint-preserving because
    $F(z_0,t)=\gamma(t)\gamma(t)^{-1}=x_0$. The $L_\gamma R_{\gamma^{-1}}$ normalisation used here is
    the same device Hatcher uses in Example 4A.3 (p. 421) to show that an H-space has trivial action
    of $\pi_1$; the group case does not need the H-space machinery since inverses are available. No
    published solution of this exercise is in the retained sets — none of them covers §4.A at all —
    recorded in COMPLAINTS.md.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Page correction to the note above: Example 4A.3 is printed on p. 422, not p. 421. Checked in
    `tmp/sources/hatcher-2002-algebraic-topology.pdf`, where printed p. 421 (PDF p. 430) carries the
    §4.A heading and the display before Example 4A.1, and printed p. 422 (PDF p. 431) carries
    Example 4A.3; the exercise is Exercise 1 of the §4.A exercise list on printed p. 426 (PDF p. 435),
    which is where its statement was re-read. The solution now carries those two citations in its own
    text, so the proof rests on a numbered, paged reference rather than on the audit record. Searched
    for a published solution outside the retained sets — Proudfoot's Math 634 sets, MA3403 (NTNU, 2018)
    exercise sheets with solutions, Hutchings' Math 215a sets, Riemannian Hunger, hat-sols.com — none
    covers §4.A; COMPLAINTS.md records the search.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    The exercise is on printed p. 426. The published argument is Hatcher's Example 4A.3, printed p. 422: for an H-space $X$ with identity $x_0$ the action of $\pi_1(X,x_0)$ on $\pi_n(X,x_0)$ is trivial, because the multiplication moves the basepoint along $x_0\cdot\gamma$ while leaving the map $f$ fixed. A topological group is an H-space with a two-sided identity and an inverse, so the same homotopy applies; the card's proof is that argument with the multiplication and the inverse written out, converting the unbased homotopy $f\simeq g$ into the based one through $f\cdot(g^{-1})$ evaluated at the moving basepoint. Checked against the book: the printed statement of Example 4A.3, the definition of the action in Proposition 4A.1 on p. 422, and the printed exercise on p. 426 which asks exactly for the basepoint-preserving conclusion. Not claimed: that Hatcher prints the exercise.
- event: source-checked
  by: claude
  date: 2026-11-14
  note: >-
    The published instance of this card's argument is now on the card: tom Dieck, *Algebraic
    Topology* (EMS Textbooks in Mathematics, 2008), Lemma (2.7.4) with its proof, printed **p. 49**,
    which for $Z=X=S^1$ (the unit circle as a group) proves the normalisation
    $(x,t)\mapsto H(x,t)\cdot H(1,t)^{-1}$ of a homotopy between pointed maps into a pointed homotopy
    between the same maps, and whose surjectivity half uses a path from $1$ to $f(1)^{-1}$. The
    source's case is stated on the card, and the card states what is not sourced: the lemma treats
    $Z=X=S^1$, while the exercise asks for an arbitrary topological group $X$ and an arbitrary
    pointed space $(Z,z_0)$, and no published source for that generality has been located; the
    derivation for it is the card's, the loop $\gamma(t)=H(z_0,t)$ replacing $H(1,t)$. The proof
    already on the card needed no repair and its `pf` block is unchanged. Checked against Hatcher
    (2002), §4.A Exercise 1 on printed p. 426 and Example 4A.3 on printed p. 422. Not claimed: that
    tom Dieck states the general form, or that Hatcher prints the exercise.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    One sentence of the paragraph on tom Dieck's Lemma (2.7.4) was wrong and is corrected. It called
    "the surjectivity half of the same lemma ... the other half of the construction here", but this
    card's construction is the injectivity half only: it normalises a given homotopy between pointed
    maps and produces nothing else. The lemma's other half is the different statement that every
    unbased homotopy class of maps $S^1\to S^1$ contains a pointed map, proved by the path $w$ from
    $1$ to $f(1)^{-1}$ and the homotopy $(x,t)\mapsto f(x)w(t)$; the exercise asks only for the
    injectivity half, and the card now says that the other half is a different statement which it
    does not use. Checked in the text version
    `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, Lemma (2.7.4) with its proof, and against
    Hatcher (2002), §4.A Exercise 1 on printed p. 426 and Example 4A.3 on printed p. 422.
- event: solution-written
  by: claude
  date: 2026-11-16
  note: >-
    The statement in the general case now has a published argument, and it is on the card. J. F.
    Davis and P. Kirk, *Lecture Notes in Algebraic Topology*, Graduate Studies in Mathematics 35,
    American Mathematical Society 2001, Lemma 6.56 on printed pp. 156--157 and Theorem 6.57 on
    printed p. 158, prove that free homotopy classes of maps of a based space $Z$ with non-degenerate
    basepoint into a based space $X$ are the quotient of the based classes by the action of
    $\pi_1(X,x_0)$, with the step that matters here printed on p. 158: if the forgetful map
    $\Phi$ carries $[f_0]$ and $[f_1]$ to the same class, then $[u][f_0]=[f_1]$ for some
    $u\in\pi_1(X,x_0)$. Hatcher's Example 4A.3, printed p. 422, proves the action trivial for an
    H-space, and a topological group is one, so $[u][f_0]=[f_0]$ and the two maps are based
    homotopic. The one hypothesis Davis--Kirk add and the exercise does not is non-degeneracy of the
    basepoint of $Z$, which the card states; the card's own derivation needs no hypothesis on $Z$,
    and it remains the proof of the exercise as printed. Checked against Hatcher (2002), §4.A
    Exercise 1 on printed p. 426, Example 4A.3 and Proposition 4A.1 on printed p. 422, and read in
    the text layer of `tmp/sources/davis-kirk-lecture-notes-algebraic-topology.pdf`, whose running
    heads give the printed page numbers quoted, the citation being to the book. Nothing in the
    solution's `pf` block changed.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, second pass: one sentence of the solution explained Hatcher's Example 4A.3 by
    the wrong reason and is corrected. It said that the homotopy $f_s(z)=f(z)\gamma(s)$ "ends at a map
    homotopic to $f$ rather than at $f$ itself" because "the loop is not required to be stationary".
    What Hatcher prints on printed p. 422 is that the homotopy "starts and ends with a map homotopic to
    $f$", and the reason is that in an H-space the identity element is a two-sided identity only up to
    homotopy, so $f(z)x_0$ is homotopic to $f(z)$ and not necessarily equal to it; the basepoint
    condition is a separate matter, and Hatcher records that $f_s(z_0)$ traces $\gamma$ and that both
    of his auxiliary homotopies are basepoint-preserving by the definition of an H-space. The card now
    says that, and the derivation in the `pf` block, which needs no H-space convention, is unchanged.
    Checked in `tmp/sources/hatcher-2002-algebraic-topology.md`, Example 4A.3 on printed p. 422, and
    against the exercise on printed p. 426.
- event: source-corrected
  by: claude
  date: 2026-11-16
  note: >-
    #123 reader's report, third pass on this card: two repairs. (1) The `source-corrected` event of
    this date corrected the reason for Hatcher's "homotopic to $f$", but the body then said that the
    homotopy $f_s$ is itself basepoint-preserving because $f_s(z_0)=\gamma(s)$ traces $\gamma$. The
    two clauses contradict each other, since $\gamma(s)$ need not be $x_0$. Hatcher's printed
    sentence makes $f_0$ and $f_1$ homotopic to $f$ and the loop $f_s(z_0)$ homotopic to $\gamma$,
    and says that those two auxiliary homotopies are basepoint-preserving; $f_s$ itself is not. The
    body now says that, and the `pf` block is unchanged. (2) The body said that the repository holds
    no text version of Davis--Kirk; it holds
    `tmp/sources/davis-kirk-lecture-notes-algebraic-topology.md`, which is now named in the body and
    in the remark, with the printed page numbers taken from its running heads. Checked:
    Hatcher's Example 4A.3 on printed p. 422 in
    `tmp/sources/hatcher-2002-algebraic-topology.md`, and Davis--Kirk's Lemma 6.56 and Theorem 6.57
    in the text version. Nothing else changes.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, the correctness read of this card's own part, which is the normalisation. No defect
    found. Checked: $H$ is continuous at $t=0$ with $F(z,0)=f(z)x_0^{-1}=f(z)$ and at $t=1$ with
    $F(z,1)=g(z)x_0^{-1}=g(z)$, both because $f(z_0)=g(z_0)=x_0$; and
    $F(z_0,t)=\gamma(t)\gamma(t)^{-1}=x_0$, so the single formula is a basepoint-preserving homotopy,
    continuity of $F$ being that of multiplication and inversion. The hypothesis used is exactly that
    $X$ is a topological group with identity $x_0$ and that $f,g$ are pointed; no hypothesis on $Z$
    enters, which is what the card says in comparing itself with the published arguments. Checked the
    statement against Hatcher, Exercise 1 of §4.A on printed p. 426, in
    `tmp/sources/hatcher-2002-algebraic-topology.md`. Not changed: any part of the solution. Not
    claimed: a published solution of the exercise in this generality; tom Dieck's Lemma (2.7.4) and
    Davis--Kirk's Lemma 6.56 and Theorem 6.57 are the published arguments the card records beside
    its own.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    The solution's opening sentence now names the exercise, the printed page and the retained copy.
    Re-confirmed in this pass rather than copied: PDF p. 430 carries the running head 421,
    so the printed page is the one the card's earlier event claimed. The durable part of the locator
    is that printed page; the file path names this machine's copy and `tmp/sources` does not survive a
    VM reset. No mathematics changed.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, the problem block's locator repaired. It named printed p. 421 for the exercise, which
    is where §4.A opens, not where the exercise stands: PDF page 430 of the author's copy carries the
    running head "Basepoints and Homotopy / Section 4.A / 421", while the exercise is on PDF page 435
    = printed p. 426, under the heading "Exercises" that closes the section, and its wording there is
    the card's. The solution's own opening sentence already said printed p. 426, so the two halves of
    the card disagreed and the statement's half was the wrong one. The block now names the text
    version `tmp/sources/hatcher-2002-algebraic-topology.md`, which is present, in place of a PDF that
    is no longer in `tmp/sources`, and gives the PDF page of the author's copy. Nothing in the
    displayed statement changed.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170, referee read of this card's own part, the normalisation of the unbased homotopy.
    Checked: for $H:Z\times I\to X$ an unbased homotopy of the pointed maps $f,g:(Z,z_0)\to(X,x_0)$,
    the path $\gamma(t)=H(z_0,t)$ is a loop at $x_0$ because $\gamma(0)=f(z_0)=x_0=\gamma(1)=g(z_0)$;
    $F(z,t)=H(z,t)\gamma(t)^{-1}$ is continuous, multiplication and inversion being continuous in a
    topological group; $F(z,0)=f(z)x_0^{-1}=f(z)$ and $F(z,1)=g(z)x_0^{-1}=g(z)$; and
    $F(z_0,t)=\gamma(t)\gamma(t)^{-1}=x_0$, so $F$ is a homotopy through based maps. The single
    formula does all three jobs, which is what the exercise asks, and no hypothesis on $Z$ is used.
    Checked that this is the published normalisation in the one case a source proves it: tom Dieck,
    Lemma (2.7.4), printed p. 49, is $(x,t)\mapsto H(x,t)H(1,t)^{-1}$ for pointed maps $S^1\to S^1$,
    the same formula with $Z=X=S^1$; the card says so and does not claim the general statement from
    it. Not claimed: a published proof of the general statement in this form.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, §4.A Exercise 1, and against the published statements the card records:
    Hatcher's Example 4A.3, tom Dieck's Lemma (2.7.4), and Davis--Kirk's Lemma 6.56 and
    Theorem 6.57. The mathematics is correct as it stood: with $\gamma(t)=H(z_0,t)$ a loop at
    $x_0$, $F(z,t)=H(z,t)\gamma(t)^{-1}$ is continuous, starts at $f$, ends at $g$ and carries
    $z_0$ to $x_0$ throughout, which is exactly the printed exercise. Two changes. The card's
    text cited printed pages, PDF pages and the offset between them in the problem block, the
    solution and the remark; by the owner's correction of this date it now cites numbered
    statements only --- Hatcher's exercise and Example 4A.3, tom Dieck's Lemma (2.7.4),
    Davis--Kirk's Lemma 6.56 and Theorem 6.57 --- and no page. And the proof's three top-level
    steps were titled sections rather than claims, the last with no proof block; they are now
    five steps, each a claim with its proof, the same formulas unchanged. No statement changed.
    Not checked: the pagination of the 2001 bound volume of Davis--Kirk, and no certificate.


- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Issue #170's item for this card, the normalisation beyond tom Dieck's circle lemma, read step by step
    and found correct. $H$ is a homotopy of pointed maps, so $\gamma(t)=H(z_0,t)$ is a loop at $x_0$
    because $f(z_0)=g(z_0)=x_0$; $F(z,t)=H(z,t)\gamma(t)^{-1}$ is continuous as the composite of
    $(z,t)\mapsto(H(z,t),\gamma(t))$ with multiplication and inversion, which a topological group has
    continuous; $F(z,0)=f(z)x_0^{-1}=f(z)$ and $F(z,1)=g(z)x_0^{-1}=g(z)$ because $x_0$ is the identity;
    $F(z_0,t)=\gamma(t)\gamma(t)^{-1}=x_0$; so $F$ is the basepoint-preserving homotopy the exercise asks
    for, with no hypothesis on $Z$ beyond that $f$ and $g$ are pointed and homotopic. The statement is
    Hatcher's §4.A Exercise 1 word for word. tom Dieck's Lemma (2.7.4) proves this for the unit circle
    only — the pointed homotopy in its proof is $(x,t)\mapsto H(x,t)H(1,t)^{-1}$ — and its other half,
    surjectivity on unbased classes, is the path $w$ from $1$ to $f(1)^{-1}$ and is not what the exercise
    asks; the card's derivation is that argument for an arbitrary topological group and an arbitrary
    pointed space. Davis--Kirk is stated as their §6.16 states it: the source of the maps is assumed to lie
    in $\kappa_\ast$, a based space with non-degenerate basepoint, which Hatcher's §4.A convention — $Z$ a
    CW complex with basepoint a $0$-cell — supplies; Theorem 6.57's path-connectedness of the target enters
    only its quotient statement, and the implication this card uses is Lemma 6.56's existence clause. No
    step changed. Not claimed: a published solution of the exercise itself, which is not in the retained
    sets, so the #123 source obligation stays open.
---

::: {.problem}
This is Exercise 1 of Section 4.A of Hatcher, *Algebraic Topology* (2002); the statement below is its wording.

Show directly that if $X$ is a topological group with identity element $x_0$, then any two maps $f, g: (Z, z_0) \to (X, x_0)$ which are homotopic are homotopic through basepoint-preserving maps.
:::

::: {.solution}
The exercise is §4.A Exercise 1 of Hatcher. The device is Hatcher's: Example 4A.3 shows that for an H-space with identity $x_0$ the action of $\pi_1(X,x_0)$ on $\langle Z,X\rangle$ is trivial, by the homotopy $f_s(z)=f(z)\gamma(s)$ that multiplies by the loop and carries the basepoint along $\gamma$. Hatcher's own words are that this homotopy "starts and ends with a map homotopic to $f$", and the reason is not that the loop is unconstrained but that in an H-space the identity element is an identity only up to homotopy: $f_s(z)$ at $s=0$ is $f(z)x_0$, which is homotopic to $f(z)$ and need not equal it. The homotopy $f_s$ is not itself basepoint-preserving, since $f_s(z_0)=\gamma(s)$ need not be $x_0$; what Hatcher records as basepoint-preserving are the two auxiliary homotopies, from $f_0$ and from $f_1$ to $f$ and from the loop $f_s(z_0)$ to $\gamma$. Here the space is a group with identity $x_0$, so the normalisation is $H(z,t)\gamma(t)^{-1}$ with $\gamma(t)=H(z_0,t)$, which ends at $g$ itself, and continuity of $F$ is continuity of the multiplication and of inversion.

::: pf

::: {.pf-step #loop}
The path $\gamma(t)=H(z_0,t)$ is a loop at $x_0$.

::: pf-proof
$\gamma(0)=H(z_0,0)=f(z_0)=x_0$ and $\gamma(1)=H(z_0,1)=g(z_0)=x_0$, because $f$ and $g$ are pointed maps.
:::

:::

::: {.pf-step #continuous}
$F(z,t)=H(z,t)\gamma(t)^{-1}$ is a continuous map $Z\times I\to X$.

::: pf-proof
It is the composite of $(z,t)\mapsto\bigl(H(z,t),\gamma(t)\bigr)$, which is continuous because $H$ and $\gamma$ are, with $(x,y)\mapsto xy^{-1}$, which is continuous because multiplication and inversion in a topological group are.
:::

:::

::: {.pf-step #ends}
$F(z,0)=f(z)$ and $F(z,1)=g(z)$ for every $z\in Z$.

::: pf-proof
$F(z,0)=H(z,0)\gamma(0)^{-1}=f(z)x_0^{-1}=f(z)$ and $F(z,1)=H(z,1)\gamma(1)^{-1}=g(z)x_0^{-1}=g(z)$, using that $\gamma$ is a loop at $x_0$ by step [](#loop){.pf-ref}.
:::

:::

::: {.pf-step #based}
$F(z_0,t)=x_0$ for every $t\in I$.

::: pf-proof
$F(z_0,t)=H(z_0,t)\gamma(t)^{-1}=\gamma(t)\gamma(t)^{-1}=x_0$.
:::

:::

::: {.pf-step}
$F$ is a homotopy from $f$ to $g$ through basepoint-preserving maps.

::: pf-proof
By step [](#continuous){.pf-ref} $F$ is continuous, by step [](#ends){.pf-ref} it starts at $f$ and ends at $g$, and by step [](#based){.pf-ref} it carries $\{z_0\}\times I$ to $x_0$; that is exactly a basepoint-preserving homotopy between the two pointed maps.
:::

:::

:::
:::

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), Lemma (2.7.4), proves this normalisation for $Z=X=S^1$ with the multiplication of the unit circle: $(x,t)\mapsto H(x,t)\cdot H(1,t)^{-1}$ is a pointed homotopy between the same maps. Its other half, that every unbased homotopy class of maps $S^1\to S^1$ contains a pointed map, is a different statement which the exercise does not ask for: a path $w$ from $1$ to $f(1)^{-1}$ gives the homotopy $(x,t)\mapsto f(x)w(t)$ from $f$ to the pointed map $x\mapsto f(x)f(1)^{-1}$. The derivation above is that computation with an arbitrary topological group $X$ and an arbitrary pointed space $(Z,z_0)$ in place of the circle, the loop $\gamma(t)=H(z_0,t)$ playing the role of $H(1,t)$; the source proves the case $Z=X=S^1$ only.

For the statement itself there is a complete published argument that is not restricted to the circle: J. F. Davis and P. Kirk, *Lecture Notes in Algebraic Topology* (Graduate Studies in Mathematics 35, American Mathematical Society 2001), Lemma 6.56 and Theorem 6.57. The standing hypothesis of that section is that the source of the maps is a based space with non-degenerate basepoint; Hatcher's §4.A works throughout with $Z$ a CW complex whose basepoint is a $0$-cell, and such a space satisfies it, so the theorem applies to the exercise's $Z$. Theorem 6.57 states that $[X,Y]$ is the quotient of $[X,Y]_0$ by the action of $\pi_1(Y,y_0)$ when $Y$ is path connected; the path-connectedness is used only for the surjectivity of the forgetful map, and the step the exercise needs is that $\Phi[f_0]=\Phi[f_1]$ gives $[u][f_0]=[f_1]$ for some $u\in\pi_1(Y,y_0)$, which needs no hypothesis on $Y$. Hatcher's Example 4A.3 proves the action trivial when $X$ is an H-space, which a topological group is, so $[u][f_0]=[f_0]$ and the two maps are based homotopic. The derivation above reaches the same conclusion without the section's convention, since $F(z,t)=H(z,t)\gamma(t)^{-1}$ needs only continuity of multiplication and of inversion.
:::
