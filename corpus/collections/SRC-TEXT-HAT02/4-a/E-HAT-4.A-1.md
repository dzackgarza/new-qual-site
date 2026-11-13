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

::: {.remark title="Published solution"}
Hatcher, *Algebraic Topology* (2002), Example 4A.3, printed p. 422 (an H-space acts trivially on its homotopy groups), with the action defined in Proposition 4A.1 on the same page. The exercise is Exercise 1 of §4.A, printed p. 426, and a topological group is an H-space in the sense of the example.
:::
