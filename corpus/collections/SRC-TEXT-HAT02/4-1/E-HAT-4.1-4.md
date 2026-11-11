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
---

::: {.problem}
Let $p: \tilde{X} \to X$ be the universal cover of a path-connected space $X$.
Show that under the isomorphism $\pi_n(X) \approx \pi_n(\tilde{X})$, which holds for $n \geq 2$, the action of $\pi_1(X)$ on $\pi_n(X)$ corresponds to the action of $\pi_1(X)$ on $\pi_n(\tilde{X})$ induced by the action of $\pi_1(X)$ on $\tilde{X}$ as deck transformations.
More precisely, prove a formula like $\gamma p_*(\alpha) = p_*\bigl(\beta_{\tilde{\gamma}}(\gamma_*(\alpha))\bigr)$ where $\gamma \in \pi_1(X, x_0)$, $\alpha \in \pi_n(\tilde{X}, \tilde{x}_0)$, and $\gamma_*$ denotes the homomorphism induced by the action of $\gamma$ on $\tilde{X}$.
:::

::: {.solution}
Let $\tilde x_0\in p^{-1}(x_0)$ and let $\gamma$ be a loop at $x_0$. Lift $\gamma$ to the path
$$
\tilde\gamma:I\to\widetilde X,\qquad \tilde\gamma(0)=\tilde x_0,
$$
whose endpoint is $\tilde\gamma(1)=T_\gamma(\tilde x_0)$, where $T_\gamma$ is the deck transformation of the universal cover corresponding to $\gamma$. By the classification of covering spaces the deck transformation group of the universal cover is $\pi_1(X,x_0)$, so $\gamma\mapsto T_\gamma$ is well defined.

This is the published solution of Nicholas Proudfoot, *Math 634: Algebraic Topology I* (University of Oregon, Fall 2015), Solutions to Homework #6, §4.1 Exercise 4, printed p. 1, which obtains the formula in two lines from the naturality of the change-of-basepoint maps; the naturality step and the basepoint bookkeeping are written out below.

Hatcher's definition of the action (p. 342) is this. For a path $\eta$ from $x_0$ to $x_1$ and a map $f:(I^n,\partial I^n)\to(X,x_1)$, the map $\eta f$ is obtained by shrinking the domain of $f$ to a concentric cube and inserting $\eta$ on each radial segment of the shell; then $\beta_\eta([f])=[\eta f]$ defines $\beta_\eta:\pi_n(X,x_1)\to\pi_n(X,x_0)$, and for loops at $x_0$ the association $[\gamma]\mapsto\beta_\gamma$ is the action $\gamma\cdot\alpha=\beta_\gamma(\alpha)$ of $\pi_1(X,x_0)$ on $\pi_n(X,x_0)$.

Take $\alpha=[f]\in\pi_n(\widetilde X,\tilde x_0)$ with $n\ge2$. Then $(T_\gamma)_*(\alpha)\in\pi_n(\widetilde X,T_\gamma\tilde x_0)$, and $\beta_{\tilde\gamma}$ carries it back to $\pi_n(\widetilde X,\tilde x_0)$, since $\tilde\gamma$ runs from $\tilde x_0$ to $T_\gamma\tilde x_0$.

*Naturality of $\beta$.* If $\varphi:(\widetilde X,\tilde x_0)\to(X,x_0)$ is a map of basepointed spaces and $\eta$ is a path from $\tilde x_0$ to $\tilde x_1$, then $\varphi(\eta f)=(\varphi\eta)(\varphi f)$, so
$$
\varphi_*\beta_\eta=\beta_{\varphi\eta}\,\varphi_* .
$$
This is a comparison of the two constructions of the shell: shrinking the domain and inserting $\eta$ commutes with composing by $\varphi$.

*The formula.* Apply naturality with $\varphi=p$ and $\eta=\tilde\gamma$, whose image $p\tilde\gamma=\gamma$ is a loop at $x_0$:
$$
p_*\beta_{\tilde\gamma}\bigl((T_\gamma)_*\alpha\bigr)=\beta_{p\tilde\gamma}\,p_*\bigl((T_\gamma)_*\alpha\bigr)=\beta_\gamma\bigl(p_*(T_\gamma)_*\alpha\bigr).
$$
Since $pT_\gamma=p$ as maps $\widetilde X\to X$, the map $p\circ T_\gamma\circ f$ equals $p\circ f$, so $p_*(T_\gamma)_*\alpha=p_*\alpha$. Therefore
$$
\boxed{\ \gamma\cdot p_*(\alpha)=\beta_\gamma\bigl(p_*\alpha\bigr)=p_*\left(\beta_{\tilde\gamma}\bigl((T_\gamma)_*\alpha\bigr)\right),\ }
$$
which is the formula of the exercise, with $\gamma_*$ the homomorphism induced by the deck transformation $T_\gamma$ attached to $\gamma$. So the action of $\pi_1(X,x_0)$ on $\pi_n(X,x_0)$ is transported by the isomorphism $p_*:\pi_n(\widetilde X,\tilde x_0)\to\pi_n(X,x_0)$ of Proposition 4.1 (p. 342) to the action of $\pi_1(X,x_0)$ on $\pi_n(\widetilde X,\tilde x_0)$ through deck transformations, up to the basepoint change along the lifted path $\tilde\gamma$; that basepoint change is not removable, since $T_\gamma$ moves $\tilde x_0$ when $\gamma\neq1$.
:::
