---
schema: qual/card@1
id: P-PDJ5S
kind: problem
title: Transitive subgroups of $S_4$ are $S_4$, $A_4$, $D_4$, $\ZZ_2^2$, and $\ZZ_4$
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Subgroups
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
- Show that the transitive subgroups of $S_4$ are $S_4, A_4, D_4, \ZZ_2^2, \ZZ_4$.
:::

::: {.solution}
Let $G\le S_4$ be transitive. Orbit-stabilizer gives $4\mid |G|$, while Lagrange gives $|G|\mid24$. Hence
\[
|G|\in\{4,8,12,24\}.
\]
If $|G|=24$, then $G=S_4$. If $|G|=12$, then $G$ has index $2$, hence is the kernel of a nontrivial homomorphism $S_4\to C_2$; since $S_4^{\mathrm{ab}}\cong C_2$, this subgroup is $A_4$.

If $|G|=8$, then $G$ is a Sylow $2$-subgroup of $S_4$. All Sylow $2$-subgroups are conjugate, and one is the symmetry group of a square on the four letters, hence isomorphic to $D_8$ (dihedral of order $8$).

If $|G|=4$, transitivity makes the action regular. The two groups of order $4$ both occur regularly: $C_4=\langle(1234)\rangle$ and
\[
V_4=\{1,(12)(34),(13)(24),(14)(23)\}.
\]
Therefore the transitive subgroups of $S_4$, up to conjugacy/isomorphism as appropriate, are
\[
S_4,\quad A_4,\quad D_8,\quad C_4,\quad V_4.
\]
:::
