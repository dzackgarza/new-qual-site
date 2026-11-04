---
schema: qual/card@1
id: E-HAT-4.2-35
kind: problem
title: "Quotient fiber bundle from quaternionic Hopf bundle"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 35; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the fiber bundle $S^3 \to S^{4n+3} \to \quatprojective^n$ gives rise to a quotient fiber bundle $S^2 \to \CP^{2n+1} \to \quatprojective^n$ by factoring out the action of $S^1$ on $S^{4n+3}$ by complex scalar multiplication.
:::

::: {.solution}
View
$$
S^{4n+3}\subset\quaternions^{n+1}.
$$
The quaternionic Hopf bundle is the quotient by right multiplication of unit quaternions:
$$
S^3\longrightarrow S^{4n+3}\longrightarrow\quatprojective^n.
$$
Inside $S^3$ is the subgroup
$$
S^1=\{e^{i\theta}\}\subset\CC\subset\quaternions.
$$
Its action on $S^{4n+3}$ is precisely complex scalar multiplication after identifying
$$
\quaternions^{n+1}\cong\CC^{2n+2}.
$$
Therefore
$$
S^{4n+3}/S^1\cong\CP^{2n+1}.
$$

Although $S^1\subset S^3$ is not a normal subgroup, the quotient is taken fiberwise by the right $S^1$-action: over a quaternionic line $L$, the Hopf fiber is $S^3$, and dividing that fiber by the right $S^1$-action gives
$$
S^3/S^1\cong S^2.
$$
The original local trivializations of the quaternionic Hopf bundle are $S^3$-equivariant, hence descend after quotienting by $S^1$. Thus we obtain a locally trivial bundle
$$
\boxed{S^2\longrightarrow\CP^{2n+1}\longrightarrow\quatprojective^n.}
$$
:::
