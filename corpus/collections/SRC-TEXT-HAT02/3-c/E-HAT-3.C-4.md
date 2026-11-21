---
schema: qual/card@1
id: E-HAT-3.C-4
kind: problem
title: Lifting H-space structure to universal covers
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 4; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: $\mu\circ(p\times p)$ lifts uniquely to $\widetilde\mu$ because
    $\widetilde X\times\widetilde X$ is simply connected, and the given unit homotopies lift
    uniquely with the prescribed starting point, ending at the identity map. For the group case the
    inversion lifts the same way and associativity follows from uniqueness of lifts: the two triple
    products are lifts of the same map agreeing at $(\widetilde e,\widetilde e,\widetilde e)$. Read
    at the level of the lifting arguments, which are stated rather than expanded.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the lifted H-space and group structures, which is what Queue D asks for on this card. The multiplication, the identity laws, associativity and the inverse law are separate steps; the prose asserted that "the homotopies expressing the left and right identity laws lift uniquely" without saying why the lifted homotopy ends at the identity rather than at some other lift of the identity map, and that is now the content of the identity step (the two lifts agree at the basepoint, and the domain is connected). Associativity was stated before the identity laws in the prose; the steps now follow the order in which the laws are used. No retained set covers this exercise; the card says so. No statement repair: Hatcher §3.C Exercise 4, printed p. 291.
---

::: {.problem}
Show that an H-space or topological group structure on a path-connected, locally path-connected space can be lifted to such a structure on its universal cover.
[For the group $SO(n)$ considered in the next section, the universal cover for $n > 2$ is a 2-sheeted cover, a group called $\operatorname{Spin}(n)$.]
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §3.C only in Li and Sam, each of which solves exercise 5 there and nothing else. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.C Exercise 4, and uses only the lifting criterion for covering spaces and the uniqueness of lifts.

Let $p:\widetilde X\to X$ be the universal cover of the path-connected, locally path-connected space $X$, and choose $\widetilde e\in p^{-1}(e)$ for a basepoint $e\in X$. The spaces $\widetilde X$, $\widetilde X\times\widetilde X$ and $\widetilde X\times\widetilde X\times\widetilde X$ are simply connected, a product of simply connected spaces being simply connected, and every map from a simply connected space into $X$ with a prescribed lift of one point has a unique lift.

::: pf

::: {.pf-step #multiplication}
An H-space multiplication $\mu:X\times X\to X$ lifts to $\widetilde\mu:\widetilde X\times\widetilde X\to\widetilde X$ with $\widetilde\mu(\widetilde e,\widetilde e)=\widetilde e$, and $p\circ\widetilde\mu=\mu\circ(p\times p)$.

::: pf-proof
The composite $\mu\circ(p\times p):\widetilde X\times\widetilde X\to X$ has simply connected domain, so the lifting criterion applies to the cover $p$ and gives a lift; among the lifts, exactly one takes $(\widetilde e,\widetilde e)$ to the chosen point $\widetilde e$ above $\mu(e,e)=e$, by the uniqueness of lifts from a connected space. The equation $p\circ\widetilde\mu=\mu\circ(p\times p)$ is what it means to lift.
:::

:::

::: {.pf-step #identities}
The left and right identity laws hold strictly for $\widetilde\mu$ at $\widetilde e$.

::: pf-proof
Since $\mu$ is an H-space multiplication there are homotopies $H^L:\mu(e,-)\simeq\mathrm{id}_X$ and $H^R:\mu(-,e)\simeq\mathrm{id}_X$, that is maps $X\times I\to X$. Consider $H^L\circ(p\times\mathrm{id}_I):\widetilde X\times I\to X$; its domain is simply connected and its value at $(\widetilde e,0)$ is $\mu(e,e)=e$, so it lifts uniquely to $\widetilde X\times I\to\widetilde X$ starting at $\widetilde\mu(\widetilde e,-)$. At the other end of the homotopy the lift is a map $\widetilde X\to\widetilde X$ covering $\mathrm{id}_X$, and the identity of $\widetilde X$ is such a map; the two agree at $\widetilde e$, so by uniqueness of lifts they are equal. Hence $\widetilde\mu(\widetilde e,-)=\mathrm{id}_{\widetilde X}$, and the same argument with $H^R$ gives $\widetilde\mu(-,\widetilde e)=\mathrm{id}_{\widetilde X}$. An H-space structure is a multiplication with a two-sided identity up to homotopy, which $\widetilde\mu$ therefore has.
:::

:::

::: {.pf-step #associativity}
If $X$ is a topological group with multiplication $\mu$, then $\widetilde\mu$ is strictly associative.

::: pf-proof
Both $\widetilde\mu\bigl(\widetilde\mu(-,-),-\bigr)$ and $\widetilde\mu\bigl(-,\widetilde\mu(-,-)\bigr)$ are maps $\widetilde X^3\to\widetilde X$ covering the same map $\widetilde X^3\to X$, namely $\mu\bigl(\mu(p\times p)\times p\bigr)=\mu\bigl(p\times(\mu(p\times p))\bigr)$ by the associativity of $\mu$ on $X$; and both take $(\widetilde e,\widetilde e,\widetilde e)$ to $\widetilde e$, since $\widetilde\mu(\widetilde e,\widetilde e)=\widetilde e$. The domain $\widetilde X^3$ is simply connected, so uniqueness of lifts gives the two maps equal.
:::

:::

::: {.pf-step #inverse}
If $X$ is a topological group with inversion $\iota$, then $\iota$ lifts to $\widetilde\iota:\widetilde X\to\widetilde X$ with $\widetilde\iota(\widetilde e)=\widetilde e$, and $\widetilde\iota$ is a two-sided inverse for $\widetilde\mu$; moreover $p$ is a homomorphism.

::: pf-proof
$\iota\circ p:\widetilde X\to X$ has simply connected domain, so it lifts, and the lift can be chosen to send $\widetilde e$ to $\widetilde e$ because $\iota(e)=e$. Then $\widetilde\mu\bigl(\widetilde\iota(-),-\bigr)$ and $\widetilde\mu\bigl(-,\widetilde\iota(-)\bigr)$ cover the composites $\mu(\iota(p\times p))$ and $\mu(p\times\iota(p\times p))$, which are the constant map at $e$; the constant map $\widetilde X\to\widetilde X$ at $\widetilde e$ is a lift of it, and at $\widetilde e$ the two agree because $\widetilde\mu(\widetilde e,\widetilde e)=\widetilde e$ and $\widetilde\iota(\widetilde e)=\widetilde e$. So both composites are constant at $\widetilde e$, which is the strict inverse law. Finally $p\bigl(\widetilde\mu(a,b)\bigr)=\mu(pa,pb)$ by step [](#multiplication){.pf-ref}, so $p$ is a homomorphism, and $\widetilde X$ with $\widetilde\mu,\widetilde e,\widetilde\iota$ is a topological group. An H-space structure being a multiplication with a two-sided identity, this finishes both cases.
:::

:::

:::
:::
