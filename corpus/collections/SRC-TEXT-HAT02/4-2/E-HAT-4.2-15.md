---
schema: qual/card@1
id: E-HAT-4.2-15
kind: problem
title: "Simply-connected closed 3-manifolds are $S^3$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 15; the stored statement matches.
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
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

---

::: {.problem}
Show that a closed simply-connected 3-manifold is homotopy equivalent to $S^3$. [Use Poincaré duality, and also the fact that closed manifolds are homotopy equivalent to CW complexes, from Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected 3-manifold is homeomorphic to $S^3$ is the Poincaré conjecture, finally proved by Perelman. The higher-dimensional analog, that a closed $n$-manifold homotopy equivalent to $S^n$ is homeomorphic to $S^n$, had been proved earlier for all $n \geq 4$.]
:::

::: {.solution}
Let $M$ be a closed simply-connected $3$-manifold. Poincaré duality gives
$$
H_i(M;\ZZ)\cong
\begin{cases}
\ZZ,&i=0,3,\\
0,&i=1,2.
\end{cases}
$$
Thus $M$ is a homology $3$-sphere.

Since $M$ is simply connected and $H_2(M)=0$, the Hurewicz theorem implies $\pi_2(M)=0$: otherwise $\pi_2$ would be the first nonzero higher homotopy group and would map isomorphically to $H_2$. Hence $M$ is $2$-connected. Hurewicz now gives
$$
\pi_3(M)\xrightarrow{\cong}H_3(M)\cong\ZZ.
$$
Choose
$$
f:S^3\to M
$$
representing a generator. Then $f_*$ is an isomorphism on $H_3$, and it is automatically an isomorphism on all other homology groups as well. Both spaces are simply connected CW complexes (or have CW type), so the homology Whitehead theorem implies
$$
\boxed{M\simeq S^3.}
$$
:::
