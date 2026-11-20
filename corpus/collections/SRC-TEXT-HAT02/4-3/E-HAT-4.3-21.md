---
schema: qual/card@1
id: E-HAT-4.3-21
kind: problem
title: "H-space Postnikov towers"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Restructured under #2 into numbered steps. No retained solution set covers §4.3 Exercise 21
    (Sam's set has 17 and 19-20, not 21), so the argument is the card's own. The functoriality
    that the earlier text asserted in one sentence is now derived from two numbered results:
    Example 4.16, printed p. 354, builds P_nX from X by attaching cells of dimension at least
    n+2, and Lemma 4.7, printed p. 348, extends a map over such a stage into a space with
    pi_i = 0 for i > n and makes the extension unique up to homotopy. The product identification
    and the H-space coherence then follow from that uniqueness rather than from an unproved
    functoriality of P_n. Verified: the Postnikov properties (1) and (2) are Hatcher's printed
    p. 410, and the count of cells in P_nX x P_nX uses the product CW structure. Not checked:
    no certificate, and the k-invariant description of the tower on printed p. 412 is not used.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 21, printed p. 420.
    The step P_n(X x X) = P_n X x P_n X was justified by "both sides have the same
    homotopy groups through degree n and none above", which is not an argument: isomorphic
    homotopy groups give a homotopy equivalence only with a map in hand. Repaired by
    naming the map theta induced by the two projections and concluding with Whitehead's
    theorem, with a parenthetical saying why the original sentence was not enough.
    Independent reports from the swarm flagged the same sentence. Statement unchanged.
    Not checked: the coherence steps of the argument beyond this one.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own. Everything rests on two numbered results: Example 4.16 (printed p.~354) builds the Postnikov stage $P_nX$ from $X$ by attaching cells of dimension at least $n+2$, so that $\pi_i(P_nX)=0$ for $i>n$ and $X\to P_nX$ is an isomorphism on $\pi_i$ for $i\le n$; and Lemma 4.7 (printed p.~348) extends maps from a CW complex over cells of dimension at least $n+2$ into a space whose homotopy vanishes above degree $n$, uniquely up to homotopy.

::: pf

::: {.pf-step #stage}
$P_nX$ is obtained from $X$ by attaching cells of dimension at least $n+2$; hence $\pi_i(P_nX)=0$ for $i>n$ and $X\to P_nX$ induces isomorphisms on $\pi_i$ for $i\le n$.

::: pf-proof
This is Example 4.16, printed p.~354, together with conditions (1) and (2) of the definition of a Postnikov tower on printed p.~410.
:::

:::

::: {.pf-step #extension}
Let $W$ be obtained from a CW complex $A$ by attaching cells of dimension at least $n+2$, and let $Y$ satisfy $\pi_i(Y)=0$ for $i>n$. Then every map $A\to Y$ extends to a map $W\to Y$, and two maps $W\to Y$ whose restrictions to $A$ are homotopic rel the basepoint are homotopic rel $A$.

::: pf-proof
For the extension, apply Lemma 4.7 (printed p.~348) to the CW pair $(W,A)$: a cell of $W-A$ has dimension $k\ge n+2$, so $k-1\ge n+1>n$ and $\pi_{k-1}(Y)=0$. For the uniqueness, let $F\colon A\times I\to Y$ be a homotopy between the two restrictions and consider the subcomplex $B=A\times I\cup W\times\partial I$ of $W\times I$; the given maps on $W\times\partial I$ and $F$ on $A\times I$ define a map $B\to Y$, and the cells of $W\times I$ outside $B$ have dimension at least $n+2$, so Lemma 4.7 extends it to $W\times I$. That extension is the required homotopy rel $A$.
:::

:::

::: {.pf-step #product}
The identity on $X\times X$ extends to maps $\theta\colon P_n(X\times X)\to P_nX\times P_nX$ and $\eta\colon P_nX\times P_nX\to P_n(X\times X)$, and $\theta$ is a homotopy equivalence.

::: pf-proof
$P_n(X\times X)$ is obtained from $X\times X$ by cells of dimension at least $n+2$ by step [](#stage){.pf-ref}. For the product, give $P_nX\times P_nX$ the CW structure whose cells are products of cells; a cell outside $X\times X$ has at least one factor a cell of $P_nX-X$, of dimension at least $n+2$, so it has dimension at least $n+2$. Both targets have vanishing $\pi_i$ for $i>n$ by step [](#stage){.pf-ref}. So step [](#extension){.pf-ref} extends the identity of $X\times X$ in both directions, giving $\theta$ and $\eta$. The composites $\theta\eta$ and $\eta\theta$ restrict to the identity on $X\times X$, and both are maps to spaces with $\pi_i=0$ for $i>n$ from a stage built by cells of dimension at least $n+2$; by the uniqueness in step [](#extension){.pf-ref} they are homotopic to the identity rel $X\times X$.
:::

:::

::: {.pf-step #mult}
There is a multiplication $\mu_n\colon P_nX\times P_nX\to P_nX$ extending $\mu$ up to homotopy.

::: pf-proof
The composite $X\times X\xrightarrow{\mu}X\to P_nX$ extends to a map $\tilde\mu\colon P_n(X\times X)\to P_nX$ by step [](#extension){.pf-ref}, since $P_nX$ has $\pi_i=0$ for $i>n$. Set $\mu_n=\tilde\mu\,\eta$ with $\eta$ as in step [](#product){.pf-ref}. On $X\times X$ this is homotopic to $\mu$, because $\eta$ restricts to the identity there and $\tilde\mu$ extends $\mu$.
:::

:::

::: {.pf-step #hspace}
$\mu_n$ makes $P_nX$ an H-space.

::: pf-proof
Let $e_n$ be the basepoint of $P_nX$. The maps $\mu_n(\id\times e_n)$ and $\id$ of $P_nX$ agree up to homotopy on $X$, where $\mu(x,e)\simeq x$ is the unit homotopy of $\mu$; both source and target are stages over $X$ built by cells of dimension at least $n+2$ and the target has $\pi_i=0$ for $i>n$, so step [](#extension){.pf-ref} makes them homotopic. The same argument applies to $\mu_n(e_n\times\id)$. Associativity: the two maps $P_nX\times P_nX\times P_nX\to P_nX$ agree up to homotopy on $X\times X\times X$, by the associativity homotopy of $\mu$, and the source is a stage over $X\times X\times X$ built by cells of dimension at least $n+2$, so they are homotopic by step [](#extension){.pf-ref}. A homotopy inverse: the map $\iota\colon X\to X$ with $\mu(\id\times\iota)\simeq e$ and $\mu(\iota\times\id)\simeq e$ extends, followed by the inclusion, to a map $P_n\iota\colon P_nX\to P_nX$ by step [](#extension){.pf-ref}; then $\mu_n(\id\times P_n\iota)$ and $e_n$ agree up to homotopy on $X$, and so do $\mu_n(P_n\iota\times\id)$ and $e_n$, so by the same uniqueness $P_n\iota$ is a homotopy inverse for $\mu_n$.
:::

:::

::: {.pf-step #tower}
Every tower map $p\colon P_nX\to P_{n-1}X$ is an H-map.

::: pf-proof
Both $p\,\mu_n$ and $\mu_{n-1}(p\times p)$ are maps $P_nX\times P_nX\to P_{n-1}X$. On $X\times X$ they agree up to homotopy, because both restrict to $\mu$ composed with the inclusion. The source is a stage over $X\times X$ built by cells of dimension at least $n+2$, and $\pi_i(P_{n-1}X)=0$ for $i>n-1$, so step [](#extension){.pf-ref} makes the two maps homotopic.
:::

:::

::: {.pf-step}
In the Postnikov tower of an H-space all stages are H-spaces and all tower maps are H-maps.

::: pf-proof
Step [](#hspace){.pf-ref} gives the H-space structure on each $P_nX$ and step [](#tower){.pf-ref} the multiplicativity of each $P_nX\to P_{n-1}X$ up to homotopy.
:::

:::

:::
:::
