---
schema: qual/card@1
id: P-KM66S
kind: problem
title: Solvable groups, a nonabelian example, solvability of $A_4$, and normality
  of its index-$3$ subgroup
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Permutations
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "Source printed 'this index 3 subgroup of A_4' with no subgroup introduced; changed to 'the index-3 subgroup of A_4', which is unique (the Klein four-group)."
---

::: {.problem}
(a) Define a solvable group.

(b) Give an example of a solvable nonabelian group.

(c) Show $A_4$ is solvable.

(d) Do the Sylow theorems tell you anything about whether the index-$3$ subgroup of $A_4$ is normal?
:::

::: {.solution}
Let $V_4=\{e,(12)(34),(13)(24),(14)(23)\}\le A_4$ be the Klein four-group.

::: pf

::: pf-step
(a) A group $G$ is solvable if it has a finite subnormal series $\{e\}=G_0\trianglelefteq G_1\trianglelefteq\cdots\trianglelefteq G_k=G$ with every quotient $G_{i+1}/G_i$ abelian.

::: pf-proof
Equivalently, the derived series $G^{(0)}=G$, $G^{(n+1)}=[G^{(n)},G^{(n)}]$ reaches $\{e\}$ after finitely many steps.
:::

:::

::: pf-step
(b) $S_3$ is solvable and nonabelian.

::: pf-proof
It is nonabelian since $(12)(23)\ne(23)(12)$. The series $\{e\}\trianglelefteq A_3\trianglelefteq S_3$ has quotients $A_3\cong\ZZ/3\ZZ$ and $S_3/A_3\cong\ZZ/2\ZZ$, both abelian.
:::

:::

::: {.pf-step #v4-normal}
(c) $A_4$ is solvable.

::: pf-proof
Conjugation in $S_4$ preserves cycle type, and $V_4$ consists of the identity and all double transpositions, so $V_4\trianglelefteq S_4$ and hence $V_4\trianglelefteq A_4$. In the series $\{e\}\trianglelefteq V_4\trianglelefteq A_4$ the quotients are $V_4\cong\ZZ/2\ZZ\times\ZZ/2\ZZ$ and $A_4/V_4$, of order $12/4=3$, hence $\cong\ZZ/3\ZZ$; both are abelian.
:::

:::

::: pf-step
(d) The Sylow theorems alone leave $n_2\in\{1,3\}$ and so do not decide normality; combined with an element count they show that the index-$3$ subgroup $V_4$ is the unique Sylow $2$-subgroup and is normal.

::: pf-proof

::: pf-step
The index-$3$ subgroups of $A_4$ are exactly its Sylow $2$-subgroups, and $n_2\in\{1,3\}$.

::: pf-proof
Since $\abs{A_4}=12=2^2\cdot3$, a subgroup of index $3$ has order $4$ and is a Sylow $2$-subgroup. The Sylow theorems give $n_2\mid3$ and $n_2\equiv1\pmod2$.
:::

:::

::: pf-step
$n_2=1$, so $V_4$ is the unique index-$3$ subgroup and it is normal.

::: pf-proof
The elements of $A_4$ are the identity, the eight $3$-cycles, and the three double transpositions. A subgroup of order $4$ has no element of order $3$, so it consists of the identity and three elements of order $2$; the only choice is $V_4$. A Sylow subgroup is normal exactly when it is unique, which agrees with step [](#v4-normal){.pf-ref}.
:::

:::

:::

:::

:::

:::
