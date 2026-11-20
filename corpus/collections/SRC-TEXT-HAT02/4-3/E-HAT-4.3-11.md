---
schema: qual/card@1
id: E-HAT-4.3-11
kind: problem
title: "Fibration classes and homotopy equivalence"
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
  date: 2026-11-21
  note: >-
    Citation convention. Every locator of the form "printed page N" or "PDF page N" written into
    this card before today, here and in the events below, is superseded: sources are cited by
    chapter, section and numbered statement only. The events below are left as their sessions wrote
    them, as QUAL-11 requires, so their locators stand as a historical record; the statement and the
    solution above are the current text and cite by number. This event records the convention and no
    further reading: the mathematics of the card is as the events below describe it.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 11, printed p. 420,
    and Proposition 4.62, printed p. 406. The pullback, functoriality and two-sided
    inverse steps are correct. Step #homotopy proved the homotopy-invariance by asserting
    that a pullback along a homotopy equivalence is a fibre homotopy equivalence and
    deriving it in one clause --- which is the special case of the very proposition the
    exercise rests on, so the card was giving a compressed proof of 4.62 rather than
    citing it. Repaired to cite Proposition 4.62, with a parenthetical recording that
    this is what 4.62 says and why quoting it is legitimate. An independent report from
    the swarm flagged the same circularity. Statement unchanged. Not checked: nothing
    outside this exercise.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 11; the stored statement matches.
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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. The three claims are now separate:
    pullback of a fibration is a fibration with the expected fiber (proved from the homotopy
    lifting property of the original); pullback preserves fiber-preserving maps and fiber
    homotopies, hence induces a map on fiber homotopy classes, with (fg)^* = g^* f^* from the
    universal property of pullbacks; and homotopy invariance, which is the one step the prose
    asserted in a sentence, is now proved by pulling back along the homotopy and using that a
    pullback along the inclusion of an end of B_1 x I is a fiber homotopy equivalence, the inverse
    coming from lifting the deformation retraction. The bijection for a homotopy equivalence then
    follows by functoriality and homotopy invariance. Statement unchanged; no retained solution set
    covers this exercise.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The card said no retained solution set covers this exercise, and that is false: Sam's set,
    retained as `tmp/sources/hatcher-solutions-sam-2008.pdf`, solves it at §4.3 Exercise 11 on
    printed p. 26. The rendered sentence now cites it and says what the card adds. Found by
    screening the residue's absence claims against the solution sets inventoried in
    `wiki/topology/resources/solutions.md`; no step of the proof changed.
---

::: {.problem}
For a space $B$, let $\mathcal{F}(B)$ be the set of fiber homotopy equivalence classes of fibrations $E \to B$.
Show that a map $f: B_1 \to B_2$ induces $f^*: \mathcal{F}(B_2) \to \mathcal{F}(B_1)$ depending only on the homotopy class of $f$, with $f^*$ a bijection if $f$ is a homotopy equivalence.
:::

::: {.solution}
Everything follows from the pullback construction: pulling a fibration back along $f$ gives a fibration over $B_1$, and pullback respects fiber-preserving maps and fiber homotopies, so it induces a map on fiber homotopy classes; a homotopy $f_0\simeq f_1$ is handled by pulling back along the homotopy and using fiber transport along the interval, and functoriality plus the homotopy invariance then make $f^*$ invertible when $f$ is a homotopy equivalence. The argument is that of the retained solution set: **Steven V. Sam, *Solutions to Algebraic Topology* (2008), §4.3 Exercise 11** of `tmp/sources/hatcher-solutions-sam-2008.pdf`, where the pullback and its universal property give well-definedness on fiber homotopy classes and the composition law for $f^*$, Proposition 4.62 gives homotopy invariance, and functoriality gives the bijection for a homotopy equivalence. The steps below follow that route.

::: pf

::: {.pf-step #pullback}
For a fibration $p\colon E\to B_2$ and a map $f\colon B_1\to B_2$, the pullback $f^*E=\{(b,e):f(b)=p(e)\}\to B_1$ is a fibration whose fiber over $b$ is the fiber of $p$ over $f(b)$.

::: pf-proof
The projection $f^*E\to B_1$ is a fibration because pullbacks of fibrations are fibrations: given a homotopy $Y\times I\to B_1$ and a lift of its $0$-end, composing with $f$ and applying the homotopy lifting property of $p$ gives a lift into $E$, which with the given map to $B_1$ factors through the pullback. The fiber over $b$ is $\{e:p(e)=f(b)\}$, the fiber of $p$ over $f(b)$.
:::

:::


::: {.pf-step #functor}
Pullback carries fiber-preserving maps to fiber-preserving maps and fiber homotopies to fiber homotopies, so it induces $f^*\colon\mathcal F(B_2)\to\mathcal F(B_1)$; and $(fg)^*=g^*f^*$.

::: pf-proof
A map $u\colon E\to E'$ over $B_2$ gives $f^*u$ over $B_1$ by acting on the second coordinate, and the projection to $B_1$ is respected by construction, so $f^*u$ is fiber-preserving. A fiber homotopy over $B_2$ pulls back to a fiber homotopy over $B_1$, since the square $f^*E\times I\to f^*E'\times I\to B_2$ is the composite through $B_1$ and $f$. Hence $f^*$ is well defined on fiber homotopy classes. For the composite, $(fg)^*E=\{(b,e):f(g(b))=p(e)\}$ is canonically homeomorphic over $B_1$ to $g^*(f^*E)$, by the universal property of pullbacks, and this homeomorphism is natural, so $(fg)^*=g^*f^*$ on classes.
:::

:::


::: {.pf-step #homotopy}
If $f_0\simeq f_1\colon B_1\to B_2$ then $f_0^*=f_1^*$ on $\mathcal F(B_2)$.

::: pf-proof
Let $H\colon B_1\times I\to B_2$ be a homotopy and $p\colon E\to B_2$ a fibration; then $H^*E\to B_1\times I$ is a fibration whose restriction to $B_1\times\{t\}$ is $f_t^*E$. This is the situation of Proposition 4.62: for a fibration $p:E\to B$ and a homotopy $f_t:A\to B$, the pullbacks $f_0^*(E)$ and $f_1^*(E)$ over $A$ are fibre homotopy equivalent. Applying it to the fibration $H^*E\to B_1\times I$ with $A=B_1$ gives a fibre homotopy equivalence $f_0^*E\simeq_f f_1^*E$ over $B_1$; the construction uses only the pullback and the homotopy lifting property, so it is natural in $E$, and $f_0^*=f_1^*$. (Proposition 4.62 is not a consequence of this exercise but its proof: for a fibration over $B\times I$ the restrictions $E_s\to B$ are all fibre homotopy equivalent, by lifting the deformation retraction $B\times I\to B\times\{s\}$. Quoting it avoids arguing the special case as though it were immediate.)
:::

:::


::: {.pf-step #equivalence}
If $f$ is a homotopy equivalence then $f^*$ is a bijection.

::: pf-proof
Let $g$ be a homotopy inverse, so $gf\simeq1_{B_1}$ and $fg\simeq1_{B_2}$. By steps [](#functor){.pf-ref} and [](#homotopy){.pf-ref}, $f^*g^*=(gf)^*=(1_{B_1})^*=\mathrm{id}$ and $g^*f^*=(fg)^*=(1_{B_2})^*=\mathrm{id}$; a map with a two-sided inverse on each side is a bijection.
:::

:::


::: {.pf-step #conclusion}
A map $f\colon B_1\to B_2$ induces $f^*\colon\mathcal F(B_2)\to\mathcal F(B_1)$ depending only on the homotopy class of $f$, and $f^*$ is a bijection when $f$ is a homotopy equivalence.

::: pf-proof
Steps [](#pullback){.pf-ref} and [](#functor){.pf-ref} construct $f^*$, step [](#homotopy){.pf-ref} shows it depends only on the homotopy class, and step [](#equivalence){.pf-ref} gives the bijection for homotopy equivalences.
:::

:::

:::
:::
