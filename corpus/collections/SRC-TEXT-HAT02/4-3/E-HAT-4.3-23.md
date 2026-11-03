---
schema: qual/card@1
id: E-HAT-4.3-23
kind: problem
title: "Uniqueness of Quillen plus construction"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 23; the stored statement matches.
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
Prove the following uniqueness result for the Quillen plus construction: Given a connected CW complex $X$, if there is an abelian CW complex $Y$ and a map $X \to Y$ inducing an isomorphism $H_*(X; \ZZ) \approx H_*(Y; \ZZ)$, then such a $Y$ is unique up to homotopy equivalence. [Use Corollary 4.73 with $W$ the mapping cylinder of $X \to Y$.]
:::

::: {.solution}
Suppose
$$
i:X\to Y,
\qquad
i':X\to Y'
$$
are homology isomorphisms and $Y,Y'$ are connected abelian CW complexes. Replace $i$ by the inclusion of $X$ into its mapping cylinder $W=M_i$. Then $W\simeq Y$, and since $i$ is a homology isomorphism,
$$
H_*(W,X;\ZZ)=0.
$$
The universal coefficient theorem therefore gives, for every abelian group $A$,
$$
H^{n+1}(W,X;A)=0
\qquad\text{for all }n.
$$
In particular this holds for
$$
A=\pi_n(Y').
$$

Because $Y'$ is an abelian CW complex, Corollary 4.73 applies: all obstruction groups to extending
$$
i':X\to Y'
$$
over $W$ vanish. Hence there is a map
$$
F:W\to Y'
$$
extending $i'$. Restricting along the deformation retract $Y\simeq W$ gives a map
$$
f:Y\to Y'
$$
with
$$
fi\simeq i'.
$$
Since both $i$ and $i'$ induce homology isomorphisms, so does $f$. Proposition 4.74, the homology Whitehead theorem for connected abelian CW complexes, therefore gives
$$
\boxed{f:Y\xrightarrow{\simeq}Y'.}
$$
Thus the abelian target of the Quillen plus construction is unique up to homotopy equivalence.
:::
