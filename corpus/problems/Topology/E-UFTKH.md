---
schema: qual/card@1
id: E-UFTKH
kind: problem
title: $\mathrm{cl}_X(\bigcup_i A_i)=\bigcup_i\mathrm{cl}_X(A_i)$
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
---

::: exercise
Show that if $A_i \subseteq X$, then $\cl_X(\union_i A_i) = \union_i \cl_X(A_i)$.
:::

::: {.solution}
<1>1. The displayed assertion is true for finite unions but false for arbitrary indexed unions.
::: {.proof}
For two sets, $\overline{A\cup B}=\overline A\cup\overline B$: the right side is closed and contains $A\cup B$, while monotonicity of closure gives the reverse inclusion. Induction handles finite unions.
:::

<1>2. For an infinite counterexample in $\mathbb R$, take $A_n=\{1/n\}$ for $n\ge1$.
::: {.proof}
Each $A_n$ is closed, so $\bigcup_n\overline{A_n}=\{1/n:n\ge1\}$. But $0$ is a limit point of the union, hence
$$0\in\overline{\bigcup_nA_n}\setminus\bigcup_n\overline{A_n}.$$
:::

<1>3. Thus the correct general relation is only
$$\boxed{\bigcup_i\overline{A_i}\subseteq\overline{\bigcup_iA_i}},$$
with equality guaranteed for finite index sets.
::: {.proof}
Each $A_i\subseteq\bigcup_jA_j$, so monotonicity gives $\overline{A_i}\subseteq\overline{\bigcup_jA_j}$; take the union over $i$.
:::
:::
