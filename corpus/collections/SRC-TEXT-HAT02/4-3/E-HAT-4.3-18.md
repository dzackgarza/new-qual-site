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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 18, printed p. 420.
    The group and abelian-group bookkeeping is right and already argued: ⟨X, Omega^r K⟩ is
    a group by pointwise concatenation for r >= 1 and abelian for r >= 2 by Eckmann--Hilton,
    which is exactly the printed "except the last three" and "except the last six". The
    exactness at ⟨X,E⟩ was one clause --- "lift a chosen nullhomotopy of pf" --- which
    hides the two points that make it work: the nullhomotopy must be based, and the lift
    needs the relative homotopy lifting property for the CW pair
    (X x I, X x {0} u {x_0} x I), without which the homotopy does not keep the basepoint
    fixed. That is now written out. Independent reports from the swarm flagged the same
    step. Statement unchanged. Not checked: nothing outside this exercise.
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
is exact. Exactness at $\langle X,B\rangle$ is immediate: the composite $pf$ is nullhomotopic. Exactness at $\langle X,E\rangle$ is the assertion: a based map $f:X\to E$ with $pf$ based-nullhomotopic is based homotopic to a map into $F$. Take a based nullhomotopy $h:X\times I\to B$ of $pf$, so $h(x,0)=pf(x)$, $h(x,1)=b_0$ and $h(x_0,t)=b_0$. The map $(x,0)\mapsto f(x)$, $(x_0,t)\mapsto e_0$ on $X\times\{0\}\cup\{x_0\}\times I$ is a lift of $h$ restricted to that subcomplex, and $(X\times I,X\times\{0\}\cup\{x_0\}\times I)$ is a CW pair because $X$ is a CW complex with basepoint a $0$-cell; the homotopy lifting property applied to this cofibration extends the lift to $\tilde h:X\times I\to E$ with $\tilde h(x,0)=f(x)$ and $\tilde h(x_0,t)=e_0$. Then $\tilde h(-,1)$ is based — it lies in $F$ since $p\tilde h(x,1)=h(x,1)=b_0$, and it sends $x_0$ to $e_0$ — and $\tilde h$ is a homotopy through based maps from $f$ to it. Applying this to every looped fibration in the fibration sequence
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
