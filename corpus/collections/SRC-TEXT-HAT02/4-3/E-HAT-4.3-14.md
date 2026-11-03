---
schema: qual/card@1
id: E-HAT-4.3-14
kind: problem
title: "Fibration classes bijection with map classes"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 14; the stored statement matches.
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
For a space $B$, let $\mathcal{M}(B)$ denote the set of equivalence classes of maps $f: A \to B$ where $f_1: A_1 \to B$ is equivalent to $f_2: A_2 \to B$ if there exists a homotopy equivalence $g: A_1 \to A_2$ such that $f_1 \simeq f_2 g$.
Show the natural map $\mathcal{F}(B) \to \mathcal{M}(B)$ is a bijection. [See Exercises 11 and 13.]
:::

::: {.solution}
Send a fibration $p:E\to B$ to its class as a map in $\mathcal M(B)$. A fiber homotopy equivalence is in particular a homotopy equivalence of total spaces commuting with the projections up to homotopy, so this gives a well-defined map
$$
\mathcal F(B)\to\mathcal M(B).
$$

It is surjective. Given any map $f:A\to B$, its mapping-path replacement
$$
p_f:E_f\to B
$$
is a fibration, and the inclusion
$$
A\to E_f,
\qquad
a\mapsto(a,\text{constant path at }f(a))
$$
is a homotopy equivalence with $f\simeq p_fi$. Hence $f$ and $p_f$ define the same element of $\mathcal M(B)$.

For injectivity, suppose fibrations $p_1:E_1\to B$ and $p_2:E_2\to B$ represent the same element of $\mathcal M(B)$. Then there is a homotopy equivalence
$$
g:E_1\to E_2
$$
with
$$
p_1\simeq p_2g.
$$
Exercises 12 and 13 imply
$$
E_{p_1}\simeq_f E_{p_2g}\simeq_f E_{p_2}.
$$
Each fibration $p_i$ is fiber homotopy equivalent to its mapping-path replacement $E_{p_i}\to B$. Hence $p_1$ and $p_2$ are fiber homotopy equivalent. Therefore
$$
\boxed{\mathcal F(B)\xrightarrow{\cong}\mathcal M(B).}
$$
:::
