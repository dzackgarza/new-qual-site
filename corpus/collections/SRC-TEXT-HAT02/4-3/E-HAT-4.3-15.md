---
schema: qual/card@1
id: E-HAT-4.3-15
kind: problem
title: "Homotopy equivalence fibration is fiber homotopy trivial"
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
  date: 2026-11-20
  note: >-
    Citation convention. Sources on this card are cited by chapter, section and numbered statement
    only, and the statement and solution above cite every source by its numbered statement. The
    events dated before today are left as their sessions wrote them, which QUAL-11 requires, so a
    locator in one of them stands as a historical record and is superseded by the citation now on
    the card. This event records the convention and claims no further reading: the
    mathematics of the card is as those events describe it.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 15; the stored statement matches.
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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewrote the prose solution as a Lamport proof and located a retained set for the exercise:
    Steven V. Sam, solutions to Hatcher (2008), Section 4.3 Exercise 15, PDF p. 29, whose answer is
    "p is fiber-preserving, and a homotopy inverse q of p can be chosen to be fiber-preserving by
    (Ex. 4.3.14)". Re-read Exercises 11 and 14 in the book's text version
    (tmp/sources/hatcher-2002-algebraic-topology.md) before transcribing: M(B) is defined there,
    F(B) is the set of fiber homotopy equivalence classes of fibrations E -> B, and the natural map
    F(B) -> M(B) is asserted to be a bijection. The card now proves that p and 1_B agree in M(B)
    (the constant homotopy, with g = p), invokes the bijection, and then states the criterion that
    the fiber-preserving map p is a fiber homotopy equivalence because it is a homotopy
    equivalence: Hatcher's Exercise 4.H.3, printed p. 466, dual to Proposition 0.19. That is a later
    exercise and the note says so; the Section 4.3 content of the answer is the computation in M(B).
    The section's exercises 11-15 stand on printed p. 420, checked on the PDF.

---

::: {.problem}
If the fibration $p: E \to B$ is a homotopy equivalence, show that $p$ is a fiber homotopy equivalence of $E$ with the trivial fibration $\id: B \to B$.
:::

::: {.solution}
The exercise is solved in the retained set **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), Section 4.3 Exercise 15** (`tmp/sources/hatcher-solutions-sam-2008.pdf`): $p$ is fiber-preserving, and a homotopy inverse of $p$ is fiber-preserving by Exercise 14. The steps below are that answer, with the class computation it leaves implicit written out.

::: pf

::: {.pf-step #class-in-M}
$p:E\to B$ and $1_B:B\to B$ represent the same element of $\mathcal{M}(B)$.

::: pf-proof
By Exercise 14, two maps $f_1:A_1\to B$ and $f_2:A_2\to B$ are equivalent when there is a homotopy equivalence $g:A_1\to A_2$ with $f_1\simeq f_2 g$. Take $A_1=E$, $f_1=p$, $A_2=B$, $f_2=1_B$ and $g=p$: the map $g$ is a homotopy equivalence by hypothesis, and $f_2 g=1_B\circ p=p=f_1$, so the required homotopy is the constant one.
:::

:::

::: {.pf-step #bijection}
The natural map $\mathcal{F}(B)\to\mathcal{M}(B)$ is a bijection, so two fibrations over $B$ with the same class in $\mathcal{M}(B)$ have the same class in $\mathcal{F}(B)$.

::: pf-proof
This is Exercise 14, and only its injectivity is used. In the retained set's solution of that exercise, surjectivity comes from the inclusion $A\hookrightarrow E_f$ being a homotopy equivalence, and injectivity from Exercise 4.3.13 together with Proposition 4.65: if $p_1\simeq p_2 g$ with $g$ a homotopy equivalence, the two fibrations are fiber homotopic, hence $E_1\to B$ and $E_2\to B$ are fiber homotopy equivalent.
:::

:::

::: {.pf-step #fiber-equivalent}
The fibration $p:E\to B$ is fiber homotopy equivalent over $B$ to the trivial fibration $1_B:B\to B$.

::: pf-proof
By Exercise 11 the set $\mathcal{F}(B)$ is the set of fiber homotopy equivalence classes of fibrations $E\to B$. Both $p:E\to B$ and $1_B:B\to B$ are fibrations over $B$: the first by hypothesis, and the identity has the homotopy lifting property trivially, a homotopy being its own lift. Step [](#class-in-M){.pf-ref} puts them in one class in $\mathcal{M}(B)$, and step [](#bijection){.pf-ref} transfers that to one class in $\mathcal{F}(B)$, which is the assertion: there are fiber-preserving maps $E\to B$ and $B\to E$ over $B$ whose two composites are homotopic to the identities through fiber-preserving maps.
:::

:::

::: {.pf-step #answer}
$\boxed{p:E\to B\text{ is a fiber homotopy equivalence of }E\text{ with the trivial fibration }1_B:B\to B.}$

::: pf-proof
The map $p$ is fiber-preserving over $B$, since $1_B\circ p=p$, and it is a homotopy equivalence by hypothesis; a fiber-preserving map between fibrations over $B$ that is a homotopy equivalence is a fiber homotopy equivalence, which is Exercise 4.H.3, dual to Proposition 0.19. With the class computation of step [](#fiber-equivalent){.pf-ref} this is the retained set's answer, and it is the exercise's assertion.
:::

:::

:::
:::
