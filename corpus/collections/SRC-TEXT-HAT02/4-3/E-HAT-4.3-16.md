---
schema: qual/card@1
id: E-HAT-4.3-16
kind: problem
title: "Whitehead theorem via homotopy fiber"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 16; the stored statement matches.
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
Show that a map $f: X \to Y$ of connected CW complexes is a homotopy equivalence if it induces an isomorphism on $\pi_1$ and its homotopy fiber $F_f$ has $\tilde{H}_*(F_f; \ZZ) = 0$.
:::

::: {.solution}
Replace $f:X\to Y$ by its mapping-path fibration
$$
F_f\longrightarrow E_f\xrightarrow{p}Y,
$$
where $E_f\simeq X$. The hypothesis on $\pi_1$ says
$$
\pi_1(E_f)\xrightarrow{\cong}\pi_1(Y).
$$
The long exact sequence therefore shows that
$$
\pi_1(F_f)\to\pi_1(E_f)
$$
is the zero homomorphism.

By Exercise 10, the usual action of $\pi_1(F_f)$ on every $\pi_n(F_f)$, including conjugation on $\pi_1(F_f)$, factors through $\pi_1(E_f)$. Hence this action is trivial. In particular $\pi_1(F_f)$ is abelian. Since
$$
\widetilde H_1(F_f;\ZZ)=0,
$$
its abelianization is zero, so
$$
\pi_1(F_f)=0.
$$

Now $F_f$ is simply connected and acyclic. If $\pi_n(F_f)\ne0$ for a least $n\ge2$, Hurewicz would give
$$
\pi_n(F_f)\cong H_n(F_f)=0,
$$
a contradiction. Thus all homotopy groups of $F_f$ vanish. The homotopy fiber has CW type, so Whitehead gives
$$
F_f\simeq *.
$$
The fibration long exact sequence now shows that $f$ induces isomorphisms on every homotopy group. Since $X,Y$ are connected CW complexes,
$$
\boxed{f\text{ is a homotopy equivalence}.}
$$
:::
