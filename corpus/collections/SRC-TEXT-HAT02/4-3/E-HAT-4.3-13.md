---
schema: qual/card@1
id: E-HAT-4.3-13
kind: problem
title: "Pre-composing with homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.problem}
Given a map $f: A \to B$ and a homotopy equivalence $g: C \to A$, show that the fibrations $E_f \to B$ and $E_{fg} \to B$ are fiber homotopy equivalent. [One approach is to use Corollary 0.21 to reduce to the case of deformation retractions.]
:::

::: {.solution}
Let $g:C\to A$ be a homotopy equivalence with homotopy inverse $h:A\to C$, and choose homotopies
$$
gh\simeq1_A,
\qquad
hg\simeq1_C.
$$
There is an evident fiber-preserving map
$$
\Phi:E_{fg}\to E_f,
\qquad
(c,\gamma)\longmapsto(g(c),\gamma).
$$

For the reverse direction, use a chosen homotopy $K:gh\simeq1_A$. For $(a,\gamma)\in E_f$, the path
$$
t\longmapsto f(K(a,t))
$$
runs from $f(gh(a))$ to $f(a)$. Prepending it to $\gamma$ defines a fiber-preserving map
$$
\Psi:E_f\to E_{fg},
\qquad
\Psi(a,\gamma)=\bigl(h(a),fK_a*\gamma\bigr).
$$
The homotopies $gh\simeq1_A$ and $hg\simeq1_C$, together with contraction of the resulting backtracking paths, give fiber-preserving homotopies
$$
\Phi\Psi\simeq1_{E_f},
\qquad
\Psi\Phi\simeq1_{E_{fg}}.
$$
Thus
$$
\boxed{E_f\to B\simeq_f E_{fg}\to B.}
$$
:::
