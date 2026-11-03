---
schema: qual/card@1
id: E-HAT-4.3-18
kind: problem
title: "Long exact sequence for $\\langle X, - \\rangle$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 18; the stored statement matches.
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

::: {.problem}
Show that a fibration sequence $\cdots \to \Omega B \to F \to E \to B$ induces a long exact sequence $\cdots \to \langle X, \Omega B \rangle \to \langle X, F \rangle \to \langle X, E \rangle \to \langle X, B \rangle$, with groups and group homomorphisms except for the last three terms, abelian groups except for the last six terms.
:::

::: {.solution}
For a fibration
$$
F\to E\xrightarrow p B,
$$
the sequence of pointed sets
$$
\langle X,F\rangle\longrightarrow\langle X,E\rangle
\longrightarrow\langle X,B\rangle
$$
is exact: if $pf$ is nullhomotopic, lift a chosen nullhomotopy of $pf$ to homotope $f$ into the fiber. Applying this to every looped fibration in the fibration sequence
$$
\cdots\to\Omega B\to F\to E\to B
$$
gives the long exact sequence
$$
\cdots\to\langle X,\Omega B\rangle
\to\langle X,F\rangle
\to\langle X,E\rangle
\to\langle X,B\rangle.
$$

For every space $K$, the set
$$
\langle X,\Omega K\rangle
$$
is a group using pointwise concatenation of loops, and maps induced by loop maps preserve this operation. Thus every term except the last three is a group and every corresponding map is a homomorphism. After two loopings, the loop multiplication is homotopy-commutative by the Eckmann--Hilton argument, so
$$
\langle X,\Omega^rK\rangle
$$
is abelian for $r\ge2$. Reading this along the fibration sequence gives exactly Hatcher's count: all terms except the last six are abelian groups. Hence the sequence has the asserted group and abelian-group structure.
:::
