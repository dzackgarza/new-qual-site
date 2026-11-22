---
schema: qual/card@1
id: E-HAT-4.2-9
kind: problem
title: "Contractible mapping cone implies homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 9; the stored statement matches.
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
    Proof read against Hatcher Sec. 4.2 Exercise 9 (AT.txt 19358-19361) and correct as it stands. The
    simply connected half is right: a contractible mapping cone makes the cofibration sequence give an
    isomorphism on reduced homology, and the homology Whitehead theorem for simply connected complexes
    finishes. The counterexample is also right, and I checked the point that could go wrong: for the
    constant map A -> pt the mapping cone is the suspension of A, since the mapping cone of A -> pt is CA
    with A x {0} collapsed to the basepoint, which is (A x I)/(A x {0}, A x {1}) = Sigma A -- and that is
    contractible only when A is acyclic, which is why the preceding exercise is needed rather than
    redundant. Acyclic noncontractible complexes exist (for instance an acyclic K(G,1)). Not checked:
    nothing outside this exercise.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, outside the sections already closed. Read against Hatcher, Exercise 9
    of §4.2, printed p. 389. Checked: the cofibration sequence $X\to Y\to C_f$ with $\widetilde H_*(C_f)=0$
    makes $f_*$ an isomorphism on reduced homology, and the homology Whitehead theorem for simply
    connected CW complexes turns that into a homotopy equivalence; and the counterexample: for the
    constant map $A\to*$ with $A$ acyclic and noncontractible the mapping cone is $CA/A\cong\Sigma A$,
    contractible by Exercise 8, while $f$ is not a homotopy equivalence. The example complex cited
    (Hatcher Example 2.38, printed p. 142) has the stated presentation. No defect; the printed page is
    added.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 9. The proof reads correct. One provenance correction: the
    solution said that no retained set covers the exercise, and the retained sets' actual coverage is
    now recorded — Sam's §4.2 numbering is Hatcher's and Proudfoot's homework 7 covers 1, 2, 30, 31
    and 32, announcing 39 without a solution of it.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 9. One false sentence repaired: the example took $f\colon
    A\to\ast$ the constant map and wrote $C_f\cong\Sigma A$. For Hatcher's $C_f=Y\cup_f CX$ the cone
    of the constant map $A\to\ast$ is the cone $CA$, not the suspension; $\Sigma A$ is the cone of
    the inclusion $A\hookrightarrow CA$. The example's conclusion is unaffected, $CA$ being
    contractible while $A$ is not, and the step now says which cone is which and notes that
    $\Sigma A$ is contractible too for acyclic $A$ (§4.2 Exercise 8).
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Correction of the preceding event, which was itself wrong. For Hatcher's mapping cone
    $C_f=Y\cup_f CX$ with $Y=\ast$, the cone $CA=A\times I/(A\times\{0\})$ is glued to the one-point
    space along $A\times\{1\}$, so both ends of $A\times I$ are collapsed and
    $C_f=(A\times I)/(A\times\{0\}\cup A\times\{1\})=\Sigma A$. The example therefore reads as the
    card originally had it, $C_f=\Sigma A$, with the identification now written out; the argument is
    that $\Sigma A$ is contractible for acyclic $A$ (Exercise 8) while $f$ is not a homotopy
    equivalence.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    The preamble now records the defect in Sam's retained solution, as a referee asked: Sam uses the
    contractibility of $SX$, that is of the mapping cylinder $M_f$, whereas the exercise requires the
    mapping cone $C_f$ to be contractible, and those are different spaces. The card's own argument,
    which shows $C_f=\Sigma X$ contractible, is unchanged and stands.
---

::: {.problem}
Show that a map between simply-connected CW complexes is a homotopy equivalence if its mapping cone is contractible.
Use the preceding exercise to give an example where this fails in the nonsimply-connected case.
:::

::: {.solution}
A retained solution covers this exercise: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.2 Exercise 9** (`tmp/sources/hatcher-solutions-sam-2008.md`). Guanyu Li's set ends with §3.3, DeMason's M382C problem set covers §4.2 Exercises 1, 2, 14 and 27 only, and the Stanford 215C sets cover §3.B and §3.3 exercises. Sam's argument is defective and is not transcribed: he uses the contractibility of the suspension $SX$, that is of the mapping *cylinder* $M_f$, whereas the exercise requires the mapping *cone* $C_f$ to be contractible, and the two are different spaces. The argument below is the card's own, from the cofiber sequence of a map (§4.2), Corollary 4.33, Example 2.38 and §4.2 Exercise 8, and it is $C_f=\Sigma X$ that is shown contractible.

::: pf

::: {.pf-step #homology}
Let $f:X\to Y$ be a map of simply connected CW complexes with $C_f$ contractible. Then $f_*:H_i(X;\ZZ)\to H_i(Y;\ZZ)$ is an isomorphism for every $i$.

::: pf-proof
The cofibration sequence $X\xrightarrow{f}Y\to C_f$ gives the long exact sequence in reduced homology, in which the terms $\widetilde H_i(C_f)$ vanish because $C_f$ is contractible; exactness at $\widetilde H_i(Y)$ and at $\widetilde H_i(X)$ then forces $f_*$ to be injective and surjective in each degree.
:::
:::

::: {.pf-step #whitehead}
$f$ is a homotopy equivalence.

::: pf-proof
$X$ and $Y$ are simply connected CW complexes, so Corollary 4.33 applies: a map between simply connected CW complexes inducing isomorphisms on all homology groups is a homotopy equivalence. Step [](#homology){.pf-ref} supplies the isomorphisms.
:::
:::

::: {.pf-step #counterexample}
Let $A$ be the acyclic noncontractible CW complex of Example 2.38 and $f:A\to *$ the constant map. Then $C_f=\Sigma A$, the suspension of $A$, which is contractible because $A$ is acyclic (Exercise 8), while $f$ is not a homotopy equivalence because $A$ is not contractible. The identification is the one Chapter 0's definition gives: the cone $CA=A\times I/(A\times\{0\})$ is glued to the one-point space $Y=\ast$ along $A\times\{1\}$, so both ends of $A\times I$ are collapsed, and what remains is $(A\times I)/(A\times\{0\}\cup A\times\{1\})=\Sigma A$.

::: pf-proof
In Example 2.38 $A$ is obtained from $S^1\vee S^1$ by attaching two $2$-cells along the words $a^5b^{-3}$ and $b^3(ab)^{-2}$; the boundary matrix has determinant $-1$, so $\widetilde H_i(A)=0$ for all $i$, and $\pi_1(A)$ has the nontrivial presentation $\langle a,b\mid a^5b^{-3},\,b^3(ab)^{-2}\rangle$, so $A$ is not contractible. The mapping cone of $A\to *$ is the cone on $A$ with its base collapsed, which is the suspension $\Sigma A$, and $\Sigma A$ is contractible by §4.2 Exercise 8 because $A$ is acyclic. So the mapping cone is contractible and $f$ is not a homotopy equivalence.
:::
:::

::: {.pf-step #conclusion}
The simply connected hypothesis cannot be dropped.

::: pf-proof
Steps [](#whitehead){.pf-ref} and [](#counterexample){.pf-ref} together give the statement and its sharpness.
:::
:::

:::
:::
