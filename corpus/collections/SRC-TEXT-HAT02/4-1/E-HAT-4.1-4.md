---


schema: qual/card@1
id: E-HAT-4.1-4
kind: problem
title: "Deck transformation action on $\\pi_n$ of universal cover"
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
    Every citation now names its source's text version or says that the source has none. Hatcher is
    read in `tmp/sources/hatcher-2002-algebraic-topology.md`, named at the definition of the action
    on printed p. 342; Proudfoot's sheet is cited by its path
    `tmp/sources/uoregon-proudfoot-634-hw6.pdf`, with the card now saying that this source has no
    text version in the repository and was read from the PDF text layer. The reader raised no other
    finding on the card: the sheet's heading, its coverage line "Exercises from Hatcher: 4.1,
    Problems 4, 11, 12, 14, 15", and the formula it prints are as the card quotes them. The
    mathematics is unchanged.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line. Correct in substance and careful about the two conventions that make this
    exercise error-prone: the deck transformation for `gamma` is fixed by the *endpoint* of the lifted
    path, so `(T_gamma)_*` lands in `pi_n(X~, T_gamma x~_0)` and must be followed by the
    change-of-basepoint isomorphism along `gamma~`; and the choice of `beta_{gamma~}` versus its inverse
    is exactly the convention the card flags. With `p T_gamma = p`, projecting the corrected class gives
    `gamma . p_*(alpha) = p_*(beta_{gamma~} (T_gamma)_*(alpha))`, i.e. under `p_*` the `pi_1`-action is
    the deck action with basepoint correction.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.1 Exercise 4, printed p. 358, together with
    the definition of the action on p. 342 ($\gamma\cdot\alpha=\beta_\gamma(\alpha)$, with
    $\beta_\eta([f])=[\eta f]$ given by shrinking the cube and inserting the path on the radial shell)
    and the classification of covering spaces for the identification $\gamma\mapsto T_\gamma$. The    step the card asserted — "the defining construction of the $\pi_1(X)$-action gives the commutative
    formula" — is now derived: naturality $\varphi_*\beta_\eta=\beta_{\varphi\eta}\varphi_*$ of the
    construction, proved in one line from $\varphi(\eta f)=(\varphi\eta)(\varphi f)$, applied to
    $\varphi=p$ and $\eta=\tilde\gamma$, together with $pT_\gamma=p$, which makes
    $p_*(T_\gamma)_*\alpha=p_*\alpha$. The card also now says why the basepoint change along
    $\tilde\gamma$ cannot be dropped: $T_\gamma$ moves $\tilde x_0$ whenever $\gamma\neq1$. No
    published solution of this exercise is in the retained sets — Sam's §4.1 covers 2, 3, 5, 10-15 and
    19, DeMason's covers 2, 8 and 11 — recorded in COMPLAINTS.md.
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    The complete published solution is Nicholas Proudfoot, *Math 634: Algebraic Topology I*
    (University of Oregon, Fall 2015), Solutions to Homework #6, §4.1 Exercise 4, printed p. 1,
    `https://pages.uoregon.edu/njp/hw6solutions.pdf`, read 2026-11-11; it was found by searching
    outside the retained sets, as recorded in COMPLAINTS.md. Its argument is the one on this card:
    naturality $f_*\beta_h=\beta_{fh}f_*$ of the change-of-basepoint maps, applied to
    $f=p$, $h=\tilde\gamma$ and $\delta=(T_\gamma)_*\alpha$, with $p\circ T_\gamma=p$. Checked against
    Hatcher (2002) p. 342 for the definition of $\beta_\eta$ and the action, Proposition 4.1 (p. 342)
    for $p_*$ being an isomorphism, and printed p. 358 for the exercise. The published solution
    writes the naturality input in one line; the card proves it, and it says why the factor
    $\beta_{\tilde\gamma}$ cannot be dropped. Not checked: nothing in the source is left unread, but
    the source's page numbering is its own (the sheet is one page) and the file carries no date
    beyond the sheet's own heading.
- event: solution-reviewed
  by: claude
  date: 2026-11-13
  note: >-
    Re-read for the published-solution obligation. The complete published solution is Nicholas Proudfoot, *Math 634: Algebraic Topology I* (University of Oregon, Fall 2015), Solutions to Homework #6, Hatcher §4.1 Exercise 4, printed p. 1: the two-line naturality computation $p_*\beta_{\tilde\gamma}\gamma_*(\alpha)=\beta_\gamma p_*\gamma_*(\alpha)=\beta_\gamma p_*(\alpha)$, with $p\gamma=p$ used for the second equality. Checked against the book: the printed exercise on p. 358, the definition of the action on p. 342 and the formulas (1)--(3) on p. 341. The card writes out the naturality step and the basepoint bookkeeping that the published solution compresses.
- event: source-corrected
  by: claude
  date: 2026-11-14
  note: >-
    The sheet's title is its own, and the card now gives it: read from the text layer of
    `tmp/sources/uoregon-proudfoot-634-hw6.pdf`, printed p. 1, the heading is "Math 634: Algebraic
    Topology I, Fall 2015" over "Partial Solutions to Homework #6", followed by the coverage line
    "Exercises from Hatcher: 4.1, Problems 4, 11, 12, 14, 15". The earlier events on this card call
    it "Solutions to Homework #6", which drops the sheet's own word "Partial" and overstates what it
    is; the citation in the solution is corrected and the coverage line is now quoted there, which
    also confirms that §4.1 Exercise 4 is on the sheet. The mathematics of the card is unchanged by
    this event.
- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    The owner's acceptance rule applied at paragraph level: the solution opens with the provenance
    convention for a prose proof; the two paragraphs carrying the transport and the naturality of
    $\beta$ apply Proudfoot's solution, printed p. 1, to Hatcher's definition, printed p. 342, and
    are covered by the convention. Checked: Proudfoot's page and Hatcher's definition page.

- event: source-corrected
  by: claude
  date: 2026-11-18
  note: >-
    A false record corrected: the remark said Proudfoot's set has no text version in the repository
    and was read from the PDF text layer. It does have one,
    `tmp/sources/uoregon-proudfoot-634-hw6.md`, whose exercise 4 is the paragraph the card
    transcribes, and the remark now cites it. Checked: the file's presence and its content at
    exercise 4. Not changed: the cited page, the exercise's identity, or the proof.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the comparison of the two actions, which is what Queue D asks for on this card. The lifted loop and the deck transformation, the naturality of the change-of-basepoint maps, the displayed formula and the conclusion are separate steps; the prose's two italicised paragraphs are gone, and the point that the basepoint change is not removable is inside the last step where it belongs. The argument is Proudfoot's (Homework #6, §4.1 Exercise 4, printed p. 1), with its naturality step proved rather than quoted; Hatcher's definition of the action is on printed p. 342 and the exercise on printed p. 358, both checked against the book. No statement repair.
---

::: {.problem}
Let $p: \tilde{X} \to X$ be the universal cover of a path-connected space $X$.
Show that under the isomorphism $\pi_n(X) \approx \pi_n(\tilde{X})$, which holds for $n \geq 2$, the action of $\pi_1(X)$ on $\pi_n(X)$ corresponds to the action of $\pi_1(X)$ on $\pi_n(\tilde{X})$ induced by the action of $\pi_1(X)$ on $\tilde{X}$ as deck transformations.
More precisely, prove a formula like $\gamma p_*(\alpha) = p_*\bigl(\beta_{\tilde{\gamma}}(\gamma_*(\alpha))\bigr)$ where $\gamma \in \pi_1(X, x_0)$, $\alpha \in \pi_n(\tilde{X}, \tilde{x}_0)$, and $\gamma_*$ denotes the homomorphism induced by the action of $\gamma$ on $\tilde{X}$.
:::

::: {.solution}
The proof is **Nicholas Proudfoot, *Math 634: Algebraic Topology I* (University of Oregon, Fall 2015), Partial Solutions to Homework #6, §4.1 Exercise 4, printed p. 1** (`tmp/sources/uoregon-proudfoot-634-hw6.pdf`, text version `tmp/sources/uoregon-proudfoot-634-hw6.md`), whose coverage line reads "Exercises from Hatcher: 4.1, Problems 4, 11, 12, 14, 15". The sheet obtains the formula in two lines from the naturality of the change-of-basepoint maps; the naturality step and the basepoint bookkeeping are written out below, and the statement is Hatcher, *Algebraic Topology* (2002), §4.1 Exercise 4, printed p. 358.

Let $\tilde x_0\in p^{-1}(x_0)$ and let $\gamma$ be a loop at $x_0$. For a path $\eta$ from $x_0$ to $x_1$ and a map $f:(I^n,\partial I^n)\to(X,x_1)$, Hatcher's $\eta f$ is obtained by shrinking the domain of $f$ to a concentric cube and inserting $\eta$ on each radial segment of the shell (printed p. 342), and $\beta_\eta([f])=[\eta f]$ defines $\beta_\eta:\pi_n(X,x_1)\to\pi_n(X,x_0)$; for loops at $x_0$ the association $[\gamma]\mapsto\beta_\gamma$ is the action $\gamma\cdot\alpha=\beta_\gamma(\alpha)$ of $\pi_1(X,x_0)$ on $\pi_n(X,x_0)$.

::: pf

::: {.pf-step #lift}
The lift $\widetilde\gamma$ of $\gamma$ starting at $\tilde x_0$ ends at $T_\gamma(\tilde x_0)$, where $T_\gamma$ is the deck transformation attached to $\gamma$, and $\gamma\mapsto T_\gamma$ identifies $\pi_1(X,x_0)$ with the deck group.

::: pf-proof
Paths lift uniquely to the universal cover once a starting point is fixed, so $\widetilde\gamma$ is determined by $\gamma$ and $\tilde x_0$; its endpoint $\widetilde\gamma(1)$ lies over $\gamma(1)=x_0$, and the endpoint depends only on the class of $\gamma$, because a homotopy of loops rel endpoints lifts rel endpoints. Sending $\gamma$ to the deck transformation carrying $\tilde x_0$ to $\widetilde\gamma(1)$ is the standard identification of the deck group of the universal cover with $\pi_1(X,x_0)$, and it is a homomorphism.
:::

:::

::: {.pf-step #naturality}
For a based map $\varphi:(\widetilde X,\tilde x_0)\to(X,x_0)$ and a path $\eta$ from $\tilde x_0$ to $\tilde x_1$, one has $\varphi_*\beta_\eta=\beta_{\varphi\eta}\,\varphi_*$ as maps $\pi_n(\widetilde X,\tilde x_1)\to\pi_n(X,x_0)$.

::: pf-proof
At the level of maps of cubes, $\varphi(\eta f)=(\varphi\eta)(\varphi f)$: both sides shrink the domain of $\varphi f$ to a concentric cube and fill the shell with $\varphi\eta$, since $\varphi$ applied to the path $\eta$ inserted on the radial segments is the path $\varphi\eta$ inserted there. Passing to homotopy classes gives the identity.
:::

:::

::: {.pf-step #formula}
$\gamma\cdot p_*(\alpha)=p_*\Bigl(\beta_{\widetilde\gamma}\bigl((T_\gamma)_*\alpha\bigr)\Bigr)$ for $\gamma\in\pi_1(X,x_0)$ and $\alpha\in\pi_n(\widetilde X,\tilde x_0)$, $n\ge2$.

::: pf-proof
Let $\alpha=[f]$ with $f:(I^n,\partial I^n)\to(\widetilde X,\tilde x_0)$. Then $(T_\gamma)_*\alpha\in\pi_n(\widetilde X,T_\gamma\tilde x_0)$, and $\beta_{\widetilde\gamma}$ carries it back to $\pi_n(\widetilde X,\tilde x_0)$ because $\widetilde\gamma$ runs from $\tilde x_0$ to $T_\gamma\tilde x_0$. Apply step [](#naturality){.pf-ref} with $\varphi=p$ and $\eta=\widetilde\gamma$, whose image $p\widetilde\gamma=\gamma$ is a loop at $x_0$:
$$
p_*\beta_{\widetilde\gamma}\bigl((T_\gamma)_*\alpha\bigr)=\beta_{p\widetilde\gamma}\,p_*\bigl((T_\gamma)_*\alpha\bigr)=\beta_\gamma\bigl(p_*(T_\gamma)_*\alpha\bigr).
$$
Since $p\circ T_\gamma=p$ as maps $\widetilde X\to X$, the composite $p\circ T_\gamma\circ f$ equals $p\circ f$, so $p_*(T_\gamma)_*\alpha=p_*\alpha$. Hence the right side is $\beta_\gamma(p_*\alpha)=\gamma\cdot p_*(\alpha)$ by the definition of the action.
:::

:::

::: {.pf-step #conclusion}
Under the isomorphism $p_*:\pi_n(\widetilde X,\tilde x_0)\to\pi_n(X,x_0)$, the action of $\pi_1(X,x_0)$ on $\pi_n(X,x_0)$ corresponds to the action on $\pi_n(\widetilde X,\tilde x_0)$ by deck transformations, up to the basepoint change along $\widetilde\gamma$.

::: pf-proof
$p_*$ is an isomorphism for $n\ge2$ because $p$ is a covering map with $\pi_i$ of the fibre vanishing for $i\le1$, the fibre being discrete (Proposition 4.1, printed p. 342). Step [](#formula){.pf-ref} says that for $\alpha\in\pi_n(\widetilde X,\tilde x_0)$ the class $p_*\alpha$ acted on by $\gamma$ equals $p_*$ of $\beta_{\widetilde\gamma}((T_\gamma)_*\alpha)$; so the transported action is the deck action composed with the change of basepoint along the lifted path. That basepoint change cannot be dropped in general, since $T_\gamma$ moves $\tilde x_0$ whenever $\gamma\ne1$, and the exercise's formula, with $\gamma_*$ the homomorphism induced by the deck transformation, is exactly the displayed identity.
:::

:::

:::
:::
