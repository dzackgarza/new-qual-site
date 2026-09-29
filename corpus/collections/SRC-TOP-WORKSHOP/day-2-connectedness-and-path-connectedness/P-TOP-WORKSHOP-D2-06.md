---
schema: qual/card@1
id: P-TOP-WORKSHOP-D2-06
kind: problem
title: A union of connected subsets with nonempty intersection is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against problem (6) in assets/attachments/Day_2_-_Connectedness_Problems.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a topological space, and $A,B\subseteq X$ be connected subsets of $X$.
Show that if $A\cap B\ne\varnothing$ then $A\cup B$ is a connected subset of $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose for contradiction that $A\cup B$ is disconnected.
Then there are disjoint nonempty sets $U,V$, open in the subspace $A\cup B$, such that
\[
A\cup B=U\cup V.
\]

::: pf-proof

This is the definition of disconnectedness of the subspace $A\cup B$.

:::

:::

::: {.pf-step #s2}

Since $A$ is connected, it is contained entirely in $U$ or entirely in $V$.

::: pf-proof

The sets $A\cap U$ and $A\cap V$ are disjoint and open in the subspace $A$, and
\[
A=(A\cap U)\cup(A\cap V).
\]
If both were nonempty they would separate $A$, contradicting connectedness.
Thus one is empty, so $A$ lies in the other member of the separation.

:::

:::

::: {.pf-step #s3}

Likewise, $B$ is contained entirely in $U$ or entirely in $V$.

::: pf-proof

Apply the argument of step [](#s2){.pf-ref} to the connected subspace $B$.

:::

:::

::: {.pf-step #s4}

The sets $A$ and $B$ must lie in the same member of the separation.

::: pf-proof

Choose $p\in A\cap B$, which exists by hypothesis.
If $A\subseteq U$, then $p\in U$; since $p\in B$ and $B$ lies entirely in one of $U,V$ by step [](#s3){.pf-ref}, disjointness forces $B\subseteq U$.
The case $A\subseteq V$ is identical.

:::

:::

::: {.pf-step #s5}

This contradicts that both $U$ and $V$ are nonempty.

::: pf-proof

By step [](#s4){.pf-ref}, either $A\cup B\subseteq U$ or $A\cup B\subseteq V$.
Since $A\cup B=U\cup V$, the other set would then be empty.

:::

:::

::: pf-step

Therefore $A\cup B$ is connected.

::: pf-proof

The assumption of disconnectedness in step [](#s1){.pf-ref} leads to the contradiction in step [](#s5){.pf-ref}.

:::

:::

:::

:::
