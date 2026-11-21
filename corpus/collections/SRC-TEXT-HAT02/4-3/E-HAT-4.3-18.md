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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Restructured under #2 into numbered steps; the argument is the card's own, since no retained
    solution set covers §4.3 Exercise 18 (Sam's set has 17 and 19-20, not 18). The exactness
    step now names the relative homotopy lifting property for CW pairs, which Hatcher states on
    in §4.3; the iteration of homotopy fibres is in the same section; the group structure on
    <X,Omega K> and the abelian structure on <X,Omega^2 K> are there as well; Exercise 18 is
    §4.3 Exercise 18. Checked against those numbered statements. Not checked: no certificate.
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

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own. The exactness is proved once for an arbitrary fibration and then applied to each consecutive triple of the fibration sequence; the group and abelian bookkeeping is read off from the loopspace structure, by the numbered statements named in the steps.

::: pf

::: {.pf-step #lemma}
Let $q\colon E'\to B'$ be a fibration with fibre $F'=q^{-1}(b'_0)$, and let $X$ be a CW complex with basepoint a $0$-cell. Then $\langle X,F'\rangle\to\langle X,E'\rangle\to\langle X,B'\rangle$ is exact at $\langle X,E'\rangle$, and its composite is the constant map at the basepoint.

::: pf-proof
The composite sends a class represented by $g\colon X\to F'$ to $q\circ g$, which is the constant map at $b'_0$, so it is the basepoint of $\langle X,B'\rangle$. For exactness, let $f\colon X\to E'$ be based with $qf$ based-nullhomotopic, and let $h\colon X\times I\to B'$ be a based nullhomotopy: $h(x,0)=qf(x)$, $h(x,1)=b'_0$ and $h(x_0,t)=b'_0$. On the subcomplex $A=X\times\{0\}\cup\{x_0\}\times I\subset X\times I$ prescribe the lift $\tilde h$ to be $f$ on $X\times\{0\}$ and the constant $e'_0=q^{-1}(b'_0)$ on $\{x_0\}\times I$; the prescription is compatible with $h$ because $qf=qf$ on $X\times\{0\}$ and $q(e'_0)=b'_0=h(x_0,t)$. The relative homotopy lifting property for the CW pair $(X\times I,A)$ extends $\tilde h$ to a lift $H\colon X\times I\to E'$ with $qH=h$. Then $g=H(-,1)$ maps $X$ into $F'$ because $qg=h(-,1)=b'_0$, it is based because $g(x_0)=H(x_0,1)=e'_0$, and $H$ is a based homotopy from $f$ to $g$. So the class of $f$ lies in the image of $\langle X,F'\rangle$.
:::

:::

::: {.pf-step #seq}
The sequence $\cdots\to\langle X,\Omega B\rangle\to\langle X,F\rangle\to\langle X,E\rangle\to\langle X,B\rangle$ is exact at every term.

::: pf-proof
Iterating homotopy fibres of the fibration $F\to E\to B$ gives the sequence $\cdots\to\Omega^2B\to\Omega F\to\Omega E\to\Omega B\to F\to E\to B$ in which each consecutive triple is, up to homotopy equivalence of its maps, a fibration and its fibre: $\Omega B\to F$ is the boundary map, its homotopy fibre is $\Omega E$, and looping repeats the pattern. Step [](#lemma){.pf-ref} applied to each consecutive triple, using that $\langle X,-\rangle$ depends only on homotopy type, gives exactness at the middle term of each triple, which is every term of the displayed sequence.
:::

:::

::: {.pf-step #groups}
For every space $K$, $\langle X,\Omega K\rangle$ is a group, and the map induced by a loop map $\Omega K\to\Omega L$ is a homomorphism.

::: pf-proof
$\Omega K$ is the space of based loops in $K$ with the compact-open topology, and concatenation of loops is a continuous multiplication with a strict identity and inverses up to homotopy; the argument that $\pi_1(K)$ is a group therefore applies verbatim to $\langle X,\Omega K\rangle$. A loop map carries the concatenation of loops in $\Omega K$ to the concatenation of their images, so the induced map on homotopy classes is a homomorphism.
:::

:::

::: {.pf-step #abelian}
$\langle X,\Omega^2K\rangle$ is abelian, and hence $\langle X,\Omega^nK\rangle$ is abelian for every $n\ge2$.

::: pf-proof
$\Omega^2K=\Omega(\Omega K)$ is the space of maps $I^2\to K$ sending $\partial I^2$ to the basepoint, and the argument that $\pi_2(K)$ is abelian, composing in the two coordinates of $I^2$, shows that the group $\langle X,\Omega^2K\rangle$ is abelian. For $n\ge2$, $\Omega^nK=\Omega^2(\Omega^{n-2}K)$.
:::

:::

::: {.pf-step #count}
In the sequence of step [](#seq){.pf-ref} the last three terms are pointed sets, the three terms before them are groups, and every earlier term is an abelian group; the maps between group-valued terms are homomorphisms.

::: pf-proof
Reading from the right, the terms are $\langle X,B\rangle$, $\langle X,E\rangle$, $\langle X,F\rangle$, then $\langle X,\Omega B\rangle$, $\langle X,\Omega E\rangle$, $\langle X,\Omega F\rangle$, then $\langle X,\Omega^2B\rangle$ and its further loopings. The first three carry only the pointed-set structure, since $B$, $E$ and $F$ need not be loop spaces. The next three are groups by step [](#groups){.pf-ref}, and are not asserted to be abelian because $\Omega B$, $\Omega E$ and $\Omega F$ are only loop spaces. From $\langle X,\Omega^2B\rangle$ leftwards the terms are abelian by step [](#abelian){.pf-ref}. The maps between terms that are groups are induced by loop maps, hence are homomorphisms by step [](#groups){.pf-ref}.
:::

:::

::: {.pf-step}
A fibration sequence $\cdots\to\Omega B\to F\to E\to B$ induces a long exact sequence $\cdots\to\langle X,\Omega B\rangle\to\langle X,F\rangle\to\langle X,E\rangle\to\langle X,B\rangle$, with groups and homomorphisms except for the last three terms and abelian groups except for the last six terms.

::: pf-proof
Exactness is step [](#seq){.pf-ref}; the group, abelian-group and homomorphism statements are step [](#count){.pf-ref}.
:::

:::

:::
:::
