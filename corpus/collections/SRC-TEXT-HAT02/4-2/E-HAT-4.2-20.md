---
schema: qual/card@1
id: E-HAT-4.2-20
kind: problem
title: "Trivial $\\pi_1$-action on $\\pi_n$ of products"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 20, printed p. 390, and
    the definition of the action on printed pp. 341-342. The argument is correct: for the
    product, pi_n splits as a direct sum and pi_1 as a product, and the action of a loop
    (gamma_1, gamma_2) inserts each into its factor; the K(G,1) factor contributes nothing
    since pi_n(K(G,1)) = 0 for n > 1, and the X factor contributes nothing since pi_1(X) = 0.
    The card said no retained set solves the exercise; Sam's does, at §4.2 Exercise 20, and
    is now cited. Statement unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained solution set is cited on the card and none was
    located among the retained Hatcher sets, so the argument is the card's own. Checked against
    Hatcher, Section 4.2 Exercise 20, printed p. 359, and the description of the action by deck
    transformations in Section 4.1 (p. 345). Each step re-read: the product of the contractible
    cover of K(G,1) with the simply connected X is the universal cover of the product, with deck
    group G acting on the first factor only; projection to X is a homotopy equivalence because
    the cover is contractible; a deck transformation composed with that projection is the
    projection itself, hence induces the identity on homotopy groups; and the action of pi_1 is
    given by deck transformations. Not claimed: the statement for X not simply connected, where
    the universal cover is not this product and the deck group is larger.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Page correction to the note above, which cited the exercise one page off (or, for the Section 4
    cards, carried over the Section 4.1 page). The exercise is printed on p. 390 of Hatcher,
    Algebraic Topology (2002), checked against the retained PDF text at PDF p. 399, whose running
    folio reads 390. The solution section now states the corrected page; the mathematics is
    unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    One false sentence repaired, from an independent review. The step said the covering $p$ is a
    homotopy equivalence because a covering map induces isomorphisms on all homotopy groups. A
    covering induces isomorphisms only from $\pi_2$ up, and is a homotopy equivalence only when its
    fibre is a point; here the fibre is $\pi_1(K)$. What the argument needs and gets is $\pi_n$ for
    $n\ge2$ (Proposition 4.1), and the conclusion is stated only in that range.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Two corrections, from a referee report. (1) The covering's fibre is the group $G=\pi_1(K)$, not
    $\widetilde K$, and it may be trivial — the case $G=1$ is allowed by the exercise — so the
    assertion that the fibre is a non-trivial group is removed and replaced by that description.
    (2) The card claimed Sam's solution is the argument below; it is not: Sam's is the loop argument,
    and the proof below passes to the universal cover and uses the deck action. The preamble now
    states Sam's argument for what it is and marks the card's proof independent.
---

::: {.problem}
Let $G$ be a group and $X$ a simply-connected space.
Show that for the product $K(G, 1) \times X$ the action of $\pi_1$ on $\pi_n$ is trivial for all $n > 1$.
:::

::: {.solution}
A published solution covers this exercise: **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), §4.2 Exercise 20**, by a different argument — an element of $\pi_n$ of the product is a pair of maps, a loop in the product is a pair of loops, and the action inserts the two loops into the two factors, where the first acts trivially because $\pi_n(K(G,1))=0$ for $n>1$ and the second because $\pi_1(X)=0$. The proof below is the card's own and is independent of that one: it passes to the universal cover, where the action of $\pi_1$ on $\pi_n$ is the deck action, and reduces the claim to the vanishing of that action. It is checked against Hatcher, Section 4.2, and against the description of the action by deck transformations in Section 4.1.

::: pf

::: {.pf-step #cover}
Let $K=K(G,1)$. The projection $p:\widetilde K\times X\to K\times X$ is the universal covering, with deck group $G$ acting by $g\cdot(u,x)=(gu,x)$.

::: pf-proof
$\widetilde K$ is contractible, hence simply connected, and $X$ is simply connected by hypothesis, so $\widetilde K\times X$ is simply connected; the projection onto $K\times X$ is a covering with fibre $\widetilde K$ and deck group $\pi_1(K\times X)\cong\pi_1(K)\cong G$, acting on the first factor only, and its total space is simply connected, so it is the universal covering.
:::

:::

::: {.pf-step #homotopy}
The projection $q:\widetilde K\times X\to X$ is a homotopy equivalence, and consequently $\pi_n(K\times X)\cong\pi_n(X)$ for $n>1$.

::: pf-proof
$\widetilde K$ is contractible, so the projection $\widetilde K\times X\to X$ is a homotopy equivalence, with homotopy inverse $x\mapsto(u_0,x)$ for a chosen basepoint $u_0$. The covering $p$ induces isomorphisms on $\pi_n$ for $n\ge2$ (Proposition 4.1), which is all that is used here; it is not a homotopy equivalence in general, its fibre being the group $G=\pi_1(K)$, which may be trivial — the case $G=1$, where the cover is the identity and the assertion is empty, is allowed by the exercise. Composing, $\pi_n(K\times X)\cong\pi_n(\widetilde K\times X)\cong\pi_n(X)$ for $n\ge2$, in particular for $n>1$.
:::

:::

::: {.pf-step #deck}
Under the identification of step [](#homotopy){.pf-ref}, every deck transformation induces the identity on $\pi_n(X)$, $n>1$.

::: pf-proof
A deck transformation is $g\cdot(u,x)=(gu,x)$. Its composite with $q$ is $q(g\cdot(u,x))=x=q(u,x)$, so on the $X$-factor it is the identity map, and the identification of homotopy groups in step [](#homotopy){.pf-ref} is induced by $q$. Hence the induced automorphism of $\pi_n(X)$ is the identity.
:::

:::

::: {.pf-step #action}
The action of $\pi_1(K\times X)$ on $\pi_n(K\times X)$ is trivial for $n>1$.

::: pf-proof
The action of $\pi_1$ on $\pi_n$ of a space is given, through the universal covering, by the action of the deck group: an element $\gamma\in\pi_1$ sends a class represented by a map of $S^n$ to the class of the same map conjugated by the deck transformation $\gamma$, basepoints being moved along chosen paths. By step [](#deck){.pf-ref} each deck transformation acts as the identity on $\pi_n$, so every $\gamma$ acts trivially. This is the assertion of the exercise:
$$
\boxed{\pi_1(K(G,1)\times X)\text{ acts trivially on }\pi_n(K(G,1)\times X)\text{ for }n>1.}
$$
The two hypotheses are used in different places: $G$ arbitrary makes $\pi_1(K\times X)=G$, whose action is what is being trivialised, and simple connectivity of $X$ is used to make $\widetilde K\times X$ the universal cover, with deck group $G$ alone.
:::

:::

:::
:::
