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
---

::: {.problem}
This is Exercise 1 of Section 4.A of Hatcher, *Algebraic Topology* (2002), printed p. 421, read in the copy retained on this machine as `tmp/sources/hatcher-2002-algebraic-topology.pdf` (printed page = PDF page - 9); the statement below is its wording.

Show directly that if $X$ is a topological group with identity element $x_0$, then any two maps $f, g: (Z, z_0) \to (X, x_0)$ which are homotopic are homotopic through basepoint-preserving maps.
:::

::: {.solution}
The exercise is §4.A Exercise 1, printed p. 426, Hatcher read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`. The device is Hatcher's: on printed p. 422, Example 4A.3 shows that for an H-space with identity $x_0$ the action of $\pi_1(X,x_0)$ on $\langle Z,X\rangle$ is trivial, by the homotopy $f_s(z)=f(z)\gamma(s)$ that multiplies by the loop and carries the basepoint along $\gamma$. Hatcher's own words are that this homotopy "starts and ends with a map homotopic to $f$", and the reason is not that the loop is unconstrained but that in an H-space the identity element is an identity only up to homotopy: $f_s(z)$ at $s=0$ is $f(z)x_0$, which is homotopic to $f(z)$ and need not equal it. The homotopy $f_s$ is not itself basepoint-preserving: $f_s(z_0)=f(z_0)\gamma(s)=\gamma(s)$ need not be $x_0$. What Hatcher records as basepoint-preserving are the two auxiliary homotopies: the homotopies from $f_0$ and from $f_1$ to $f$, which exist because $f(z)x_0\simeq f(z)$, and the homotopy from the loop $f_s(z_0)$ to $\gamma$. Here the space is a group, so the normalisation is $H(z,t)\gamma(t)^{-1}$ with $\gamma(t)=H(z_0,t)$, which ends at $g$ itself, and continuity of $F$ is continuity of the multiplication and of inversion, which are part of the definition of a topological group Hatcher works with in §4.A.

::: pf

::: pf-step
Track of the basepoint under the unbased homotopy:

::: pf-proof

::: pf-step
Let $H: Z \times I \to X$ be an unbased homotopy between $f$ and $g$, so $H(z, 0) = f(z)$ and $H(z, 1) = g(z)$ for all $z \in Z$.
:::

::: pf-step
Define the path $\gamma: I \to X$ traced by the basepoint $z_0$:
$$
\gamma(t) = H(z_0, t).
$$
Because $f, g: (Z, z_0) \to (X, x_0)$ are pointed maps, the endpoints of $\gamma$ satisfy:
$$
\gamma(0) = H(z_0, 0) = f(z_0) = x_0, \qquad \gamma(1) = H(z_0, 1) = g(z_0) = x_0.
$$
Thus $\gamma$ is a loop in $X$ based at the identity element $x_0$.
:::

:::

:::

::: pf-step
Construction of the basepoint-preserving homotopy:

::: pf-proof

::: pf-step
Since $X$ is a topological group, multiplication $m: X \times X \to X$ and inversion $i: X \to X$ are continuous.
Define $F: Z \times I \to X$ by:
$$
F(z, t) = H(z, t) \cdot (\gamma(t))^{-1}.
$$
As a composition of continuous functions, $F$ is continuous.
:::

::: pf-step
Check the initial and final time slices:
$$
F(z, 0) = H(z, 0) \cdot (\gamma(0))^{-1} = f(z) \cdot x_0^{-1} = f(z),
$$
$$
F(z, 1) = H(z, 1) \cdot (\gamma(1))^{-1} = g(z) \cdot x_0^{-1} = g(z).
$$
:::

::: pf-step
Check basepoint preservation for all $t \in [0, 1]$:
$$
F(z_0, t) = H(z_0, t) \cdot (\gamma(t))^{-1} = \gamma(t) \cdot (\gamma(t))^{-1} = x_0.
$$
Thus $F(z_0, t) = x_0$ for every $t \in I$.
:::

:::

:::

::: pf-step
Conclusion:
$F: (Z \times I, \{z_0\} \times I) \to (X, x_0)$ is a pointed homotopy between $f$ and $g$.
:::

:::

:::

*The published instance of this argument.* (tom Dieck, Lemma (2.7.4), printed p. 49.) The source proves exactly this normalisation, for $Z=X=S^1$ with the multiplication of the unit circle: "Let $H:S^1\times I\to S^1$ be a homotopy between pointed maps; then $(x,t)\mapsto H(x,t)\cdot H(1,t)^{-1}$ is a pointed homotopy between the same maps", which is the injectivity half of the statement that the map $[S^1,S^1]_0\to[S^1,S^1]$ forgetting the base point is a bijection. The lemma's surjectivity half — that every unbased homotopy class of maps $S^1\to S^1$ contains a pointed map — is a different statement, which the exercise does not ask for: a path $w$ from $1$ to $f(1)^{-1}$ gives the homotopy $(x,t)\mapsto f(x)w(t)$ from $f$ to the pointed map $x\mapsto f(x)f(1)^{-1}$. The derivation above is that computation with an arbitrary topological group $X$ in place of the unit circle and an arbitrary pointed space $(Z,z_0)$ in place of the circle, the loop $\gamma(t)=H(z_0,t)$ playing the role of $H(1,t)$. The source proves the case $Z=X=S^1$ only. For the statement itself there is a complete published argument, and it is not restricted to the circle: J. F. Davis and P. Kirk, *Lecture Notes in Algebraic Topology* (Graduate Studies in Mathematics 35, American Mathematical Society 2001), read in `tmp/sources/davis-kirk-lecture-notes-algebraic-topology.md` (the printed page numbers quoted are those of its running heads; the PDF is `tmp/sources/davis-kirk-lecture-notes-algebraic-topology.pdf`), Lemma 6.56 on printed pp. 156--157 and Theorem 6.57 on printed p. 158. The standing hypothesis of that section, stated on printed p. 156, is that the source of the maps is a based space with non-degenerate basepoint ("Let $X$ be in $K_*$, that is, it is a based space with a non-degenerate base point $x_0$"); Hatcher's §4.A works throughout with $Z$ a CW complex whose basepoint is a $0$-cell, stated on printed p. 421, and such a space is in $K_*$, so the theorem applies to the exercise's $Z$. Theorem 6.57 states that $[X,Y]$ is the quotient set of $[X,Y]_0$ by the action of $\pi_1(Y,y_0)$ if $Y$ is path connected; the path-connectedness is used only for the surjectivity of the forgetful map, in the proof's last sentence, and the step the exercise needs is the one printed on p. 158: if $\Phi[f_0]=\Phi[f_1]$ then there is a $u\in\pi_1(Y,y_0)$ with $[u][f_0]=[f_1]$, which needs no hypothesis on $Y$, $Y$ being the target of the maps in the source's notation. Hatcher's Example 4A.3, printed p. 422, proves that the action is trivial when $X$ is an H-space, which a topological group is, so that $[u][f_0]=[f_0]$ and the two maps are based homotopic. The derivation above reaches the same conclusion without using the section's convention: the formula $F(z,t)=H(z,t)\gamma(t)^{-1}$ needs only the continuity of multiplication and of inversion, so the card's proof covers every based space $(Z,z_0)$, and the published argument covers the exercise as printed.

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), Lemma (2.7.4) with its proof, printed p. 49, read in the text version `tmp/sources/tomdieck-algebraic-topology-ranicki.md`, for $Z=X=S^1$: the normalisation $(x,t)\mapsto H(x,t)\cdot H(1,t)^{-1}$ of a homotopy between pointed maps, and the path from $1$ to $f(1)^{-1}$ that makes the forgetful map $[S^1,S^1]_0\to[S^1,S^1]$ surjective as well as injective. Hatcher, *Algebraic Topology* (2002), Example 4A.3, printed p. 422, read in the text version `tmp/sources/hatcher-2002-algebraic-topology.md`, is the H-space statement: the action is trivial because multiplication gives the homotopy $f_s(z)=f(z)\gamma(s)$, with the action defined in Proposition 4A.1 on the same page.

J. F. Davis and P. Kirk, *Lecture Notes in Algebraic Topology* (Graduate Studies in Mathematics 35, American Mathematical Society 2001), read in `tmp/sources/davis-kirk-lecture-notes-algebraic-topology.md`, Lemma 6.56 on printed pp. 156--157 and Theorem 6.57 on printed p. 158, give the statement through the $\pi_1$-action: freely homotopic based maps differ by the action of an element of $\pi_1(X,x_0)$, and — when the target is path connected — free homotopy classes are the quotient of the based ones by that action. With Hatcher's Example 4A.3 (trivial action for an H-space) the step that decides the exercise, $\Phi[f_0]=\Phi[f_1]\Rightarrow[u][f_0]=[f_1]$ for some $u$, gives two freely homotopic based maps into a topological group based homotopic. That section's standing hypothesis is a non-degenerate basepoint on the source of the maps (printed p. 156); Hatcher's §4.A states on printed p. 421 that $Z$ is a CW complex with basepoint a $0$-cell, which satisfies it, so the published argument covers the exercise as printed. The exercise is Exercise 1 of §4.A, printed p. 426; the normalisation written out in the solution covers every based space and does not use the convention at all.
:::
