---
schema: qual/card@1
id: P-7LMGJ
kind: problem
title: A group is solvable iff its derived series terminates
classification:
  areas:
  - algebra
  topics:
  - Solvable Groups
  - Subgroup Series
  - Commutators
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
- Show that $G$ is solvable iff its derived series terminates.
:::


::: {.solution}
Write
\[
G^{(0)}=G,\qquad G^{(i+1)}=[G^{(i)},G^{(i)}]
\]
for the derived series.

<1>1. If the derived series terminates at the identity, then $G$ is solvable.
::: {.proof}
Suppose
\[
G=G^{(0)}\trianglerighteq G^{(1)}\trianglerighteq\cdots\trianglerighteq G^{(r)}=1.
\]
Each $G^{(i+1)}$ is characteristic in $G^{(i)}$, hence normal there. Moreover,
\[
G^{(i)}/G^{(i+1)}
\]
is abelian because the commutator subgroup of $G^{(i)}$ is exactly $G^{(i+1)}$. Thus the derived series itself is a finite normal series with abelian factors, so $G$ is solvable.
:::

<1>2. Conversely, suppose $G$ is solvable. Then its derived series terminates.
::: {.proof}
Choose a finite normal series
\[
1=G_r\trianglelefteq G_{r-1}\trianglelefteq\cdots\trianglelefteq G_0=G
\]
whose factors $G_i/G_{i+1}$ are abelian. Since $G_i/G_{i+1}$ is abelian,
\[
[G_i,G_i]\subseteq G_{i+1}.
\]
We prove by induction that
\[
G^{(i)}\subseteq G_i.
\]
It is true for $i=0$. If $G^{(i)}\subseteq G_i$, then
\[
G^{(i+1)}=[G^{(i)},G^{(i)}]\subseteq [G_i,G_i]\subseteq G_{i+1}.
\]
Hence $G^{(r)}\subseteq G_r=1$, so $G^{(r)}=1$.
:::

Therefore $G$ is solvable if and only if its derived series reaches the identity after finitely many steps.
:::
