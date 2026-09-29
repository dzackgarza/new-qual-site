---
schema: qual/card@1
id: P-B4N3X
kind: problem
title: A map continuous on each of two closed sets covering $X$ is continuous
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the statement against problem 3 of the official UGA Fall 2014 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Verified the closed-set pasting argument; each restricted preimage is closed in its closed piece and hence closed in X, and the two pieces form a finite closed union.
---

::: {.problem}
Let $X$ and $Y$ be topological spaces and let $f : X \to Y$ be a function.

Suppose that $X = A \cup B$ where $A$ and $B$ are closed subsets, and that the restrictions $f \mid_A$ and $f \mid_B$ are continuous (where $A$ and $B$ have the subspace topology).

Prove that $f$ is continuous.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every closed $C\subseteq Y$, the sets $A\cap f^{-1}(C)$ and $B\cap f^{-1}(C)$ are closed in the subspaces $A$ and $B$, respectively.

::: pf-proof

Since the restrictions are continuous,
\[
(f|_A)^{-1}(C)=A\cap f^{-1}(C)
\]
is closed in the subspace $A$, and
\[
(f|_B)^{-1}(C)=B\cap f^{-1}(C)
\]
is closed in the subspace $B$.

:::

:::

::: {.pf-step #s2}

The two sets in step [](#s1){.pf-ref} are closed in $X$.

::: pf-proof

Because $A$ is closed in $X$, every subset closed in $A$ is closed in $X$.
Hence $A\cap f^{-1}(C)$ is closed in $X$.
The same argument applies to $B\cap f^{-1}(C)$ because $B$ is closed in $X$.

:::

:::

::: {.pf-step #s3}

For every closed $C\subseteq Y$, the set $f^{-1}(C)$ is closed in $X$.

::: pf-proof

Using $X=A\cup B$,
\[
f^{-1}(C)
=\bigl(A\cap f^{-1}(C)\bigr)
 \cup\bigl(B\cap f^{-1}(C)\bigr).
\]
By step [](#s2){.pf-ref}, both sets on the right are closed in $X$, so their finite union is closed.

:::

:::

::: pf-step

$f$ is continuous.

::: pf-proof

By step [](#s3){.pf-ref}, the inverse image under $f$ of every closed subset of $Y$ is closed in $X$.
This is the closed-set criterion for continuity.

:::

:::

:::

:::
