---
schema: qual/card@1
id: E-UFTKH
kind: problem
title: Closure of a finite union is the union of the closures
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source asks to show cl_X(union_i A_i) = union_i cl_X(A_i) for an arbitrary family, which is false (A_n = {1/n} in R). The statement now takes finitely many sets; the infinite counterexample is a remark."
---

::: {.exercise}
Show that if $A_1,\ldots,A_n \subseteq X$, then $\cl_X\left(\union_{i=1}^n A_i\right) = \union_{i=1}^n \cl_X(A_i)$.
:::

::: {.solution}

Write $\overline{S}$ for $\cl_X(S)$.

::: pf

::: {.pf-step #two-sets}

For $A,B\subseteq X$, $\overline{A\cup B}=\overline A\cup\overline B$.

::: pf-proof

The set $\overline A\cup\overline B$ is closed and contains $A\cup B$, so it contains $\overline{A\cup B}$. Conversely, $A\subseteq A\cup B$ gives $\overline A\subseteq\overline{A\cup B}$ by monotonicity of closure, and likewise for $B$.

:::

:::

::: pf-step

$\overline{\bigcup_{i=1}^nA_i}=\bigcup_{i=1}^n\overline{A_i}$.

::: pf-proof

Induct on $n$: the case $n=1$ is trivial, and $\bigcup_{i=1}^{n}A_i=\left(\bigcup_{i=1}^{n-1}A_i\right)\cup A_n$, so step [](#two-sets){.pf-ref} and the inductive hypothesis give the claim.

:::

:::

:::

:::

::: {.remark}
For an infinite family only $\bigcup_i\overline{A_i}\subseteq\overline{\bigcup_iA_i}$ holds. In $\RR$, take $A_n=\{1/n\}$ for $n\ge1$: each $A_n$ is closed, so $\bigcup_n\overline{A_n}=\{1/n:n\ge1\}$, but
$$0\in\overline{\bigcup_nA_n}\setminus\bigcup_n\overline{A_n}.$$
:::
