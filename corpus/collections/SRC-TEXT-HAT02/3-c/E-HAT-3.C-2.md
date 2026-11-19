---
schema: qual/card@1
id: E-HAT-3.C-2
kind: problem
title: Retracts of H-spaces
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 2; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the proof: $\mu_A=r\circ\mu\circ(i\times i)$ with $i,r$ the retract pair, and the unit
    homotopies for $\mu_A$ are the composites of the given homotopies with $i$ and $r$, using
    $r\circ i=\mathrm{id}$. The identity element stays in $A$ by hypothesis, which is what makes
    $\mu_A(e,a)$ and $\mu_A(a,e)$ well formed.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 2 of §3.C, printed p. 291, and the definition of an H-space on
    printed p. 281. Correct. With $i\colon A\to X$, $r\colon X\to A$, $ri=\mathrm{id}_A$ and $e\in A$,
    the multiplication $\mu_A=r\circ\mu\circ(i\times i)$ satisfies $\mu_A(a,e)=r\mu(i(a),e)$ and
    $\mu_A(e,a)=r\mu(e,i(a))$, and composing the basepoint-preserving unit homotopies of the H-space
    structure with $i$ and $r$ gives $\mu_A(a,e)\simeq ri(a)=a$ and the same on the other side.
    These are basepoint-preserving because $r(e)=e$, which follows from $ri=\mathrm{id}_A$ and
    $e\in A$; that is why the hypothesis that the retract contains the identity is needed. Nothing
    changed. Not claimed: a published solution of this exercise, and no certificate.
---

::: {.problem}
Show that a retract of an H-space is an H-space if it contains the identity element.
:::

::: {.solution}
Let $X$ be an H-space with identity $e$, and let $A\subset X$ be a retract containing $e$. Write
$$
i:A\hookrightarrow X,
\qquad
r:X\to A,
\qquad
r\circ i=\operatorname{id}_A.
$$
If
$$
\mu:X\times X\to X
$$
is the H-space multiplication, define
$$
\mu_A=r\circ\mu\circ(i\times i):A\times A\to A.
$$
Then
$$
\mu_A(a,e)=r(\mu(i(a),e)),
\qquad
\mu_A(e,a)=r(\mu(e,i(a))).
$$
The two maps $x\mapsto\mu(x,e)$ and $x\mapsto\mu(e,x)$ are homotopic to $\operatorname{id}_X$ through basepoint-preserving maps. Composing these homotopies with $i$ and $r$ gives basepoint-preserving homotopies
$$
a\longmapsto\mu_A(a,e)\simeq r i(a)=a,
$$
and similarly
$$
a\longmapsto\mu_A(e,a)\simeq a.
$$
Thus $A$ is an H-space with identity $e$.
:::
