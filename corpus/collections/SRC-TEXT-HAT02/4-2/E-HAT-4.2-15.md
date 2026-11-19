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
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, §4.2. Read against Hatcher, Exercise 15 of §4.2, printed p. 390 with
    its bracketed hint — §4.2's exercises are 1--12 on p. 389, 13--23 on p. 390, 24--29 on p. 391
    and 30--39 on p. 392, checked at PDF pages 398--401 of the held book — and the printed page is
    added, the card having had none. Checked: $H_1=0$ by simple connectivity, $H_2\cong H^1=0$ by
    Poincaré duality and the universal coefficient theorem, and $H_0=H_3=\ZZ$, so $M$ is a homology
    3-sphere; then $\pi_2=0$ by Hurewicz (otherwise it would be the first nonzero higher group and
    would map isomorphically to $H_2=0$), $\pi_3\cong H_3=\ZZ$ by Hurewicz applied to the
    2-connected $M$, and a map $S^3\to M$ carrying a generator is an isomorphism on $H_3$ and hence
    on all homology groups, so homology Whitehead applies — both spaces having CW type, which is the
    hint's Corollary A.12. No defect.
---

::: {.problem}
Show that a closed simply-connected 3-manifold is homotopy equivalent to $S^3$. [Use Poincaré duality, and also the fact that closed manifolds are homotopy equivalent to CW complexes, from Corollary A.12 in the Appendix. The stronger statement that a closed simply-connected 3-manifold is homeomorphic to $S^3$ is the Poincaré conjecture, finally proved by Perelman. The higher-dimensional analog, that a closed $n$-manifold homotopy equivalent to $S^n$ is homeomorphic to $S^n$, had been proved earlier for all $n \geq 4$.]
:::

::: {.solution}
The exercise is §4.2 Exercise 15, printed p. 390.

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
