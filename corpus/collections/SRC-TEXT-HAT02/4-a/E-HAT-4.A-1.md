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
---

::: {.problem}
Show directly that if $X$ is a topological group with identity element $x_0$, then any two maps $f, g: (Z, z_0) \to (X, x_0)$ which are homotopic are homotopic through basepoint-preserving maps.
:::

::: {.solution}
The exercise is §4.A Exercise 1, printed p. 426. The device is Hatcher's: on printed p. 422, Example 4A.3 normalises a homotopy $H$ by the track $\gamma(t)=H(x_0,t)$ of the basepoint to produce a basepoint-preserving homotopy, in the H-space case, where the normalisation is by the translations $L_\gamma$ and $R_{\gamma^{-1}}$ rather than by an inverse. Here the space is a group, so the normalisation is $H(z,t)\gamma(t)^{-1}$, and continuity of $F$ is continuity of the multiplication and of inversion, which are part of the definition of a topological group Hatcher works with in §4.A.

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

*The published instance of this argument.* (tom Dieck, Lemma (2.7.4), printed p. 49.) The source proves exactly this normalisation, for $Z=X=S^1$ with the multiplication of the unit circle: "Let $H:S^1\times I\to S^1$ be a homotopy between pointed maps; then $(x,t)\mapsto H(x,t)\cdot H(1,t)^{-1}$ is a pointed homotopy between the same maps", which is the injectivity half of the statement that the map $[S^1,S^1]_0\to[S^1,S^1]$ forgetting the base point is a bijection. The lemma's surjectivity half — that every unbased homotopy class of maps $S^1\to S^1$ contains a pointed map — is a different statement, which the exercise does not ask for: a path $w$ from $1$ to $f(1)^{-1}$ gives the homotopy $(x,t)\mapsto f(x)w(t)$ from $f$ to the pointed map $x\mapsto f(x)f(1)^{-1}$. The derivation above is that computation with an arbitrary topological group $X$ in place of the unit circle and an arbitrary pointed space $(Z,z_0)$ in place of the circle, the loop $\gamma(t)=H(z_0,t)$ playing the role of $H(1,t)$. The source proves the case $Z=X=S^1$ only; the statement for arbitrary $Z$ and $X$ has no located published source, and on this card it rests on the derivation above together with Hatcher's H-space form of the same normalisation in Example 4A.3.

::: {.remark title="Published solution"}
tom Dieck, *Algebraic Topology* (EMS Textbooks in Mathematics, 2008), Lemma (2.7.4) with its proof, printed p. 49, for $Z=X=S^1$: the normalisation $(x,t)\mapsto H(x,t)\cdot H(1,t)^{-1}$ of a homotopy between pointed maps, and the path from $1$ to $f(1)^{-1}$ that makes the forgetful map $[S^1,S^1]_0\to[S^1,S^1]$ surjective as well as injective. Hatcher, *Algebraic Topology* (2002), Example 4A.3, printed p. 422, is the H-space form of the same normalisation, with the action defined in Proposition 4A.1 on the same page. The exercise is Exercise 1 of §4.A, printed p. 426, and a topological group is an H-space in the sense of the example.
:::
