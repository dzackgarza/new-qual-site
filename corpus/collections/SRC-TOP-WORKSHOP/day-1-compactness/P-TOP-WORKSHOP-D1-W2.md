---
schema: qual/card@1
id: P-TOP-WORKSHOP-D1-W2
kind: problem
title: A closed subset of a compact space is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against the first warm-up item after the Hausdorff compact-subset
    exercise in assets/attachments/Day_1_-_Compactness_Problems.pdf. The source
    says X is compact but then writes A subseteq Y; the intended ambient space is X.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Proved the intended statement that a closed subset of a compact space is compact.
---

::: {.problem}
If $X$ is compact, and $A\subseteq Y$ is closed, then $A$ is compact.
:::

::: {.solution}
The statement assumes $X$ is compact but writes $A\subseteq Y$; we prove it with $A\subseteq X$: if $X$ is compact and $A\subseteq X$ is closed, then $A$ is compact.

::: pf

::: {.pf-step #s1}

Let $\mathcal U$ be an open cover of $A$ by sets open in $X$.

::: pf-proof

To prove compactness of $A$, it is enough to show that every open cover of $A$ admits a finite subcover.
Any open cover by sets open in the subspace $A$ can first be written in the form $A\cap U$ with $U$ open in $X$, so it suffices to treat covers by ambient open sets.

:::

:::

::: {.pf-step #s2}

The family $\mathcal U\cup\{X\setminus A\}$ is an open cover of $X$.

::: pf-proof

Because $A$ is closed in $X$, the complement $X\setminus A$ is open.
The family $\mathcal U$ covers $A$, while $X\setminus A$ covers every point of $X$ not in $A$.

:::

:::

::: {.pf-step #s3}

There are finitely many sets $U_1,\dots,U_n\in\mathcal U$ such that
\[
X\subseteq U_1\cup\cdots\cup U_n\cup(X\setminus A).
\]

::: pf-proof

Apply compactness of $X$ to the open cover in step [](#s2){.pf-ref}.
If a finite subcover does not use $X\setminus A$, the same conclusion holds after adjoining it.

:::

:::

::: {.pf-step #s4}

The sets $U_1,\dots,U_n$ cover $A$.

::: pf-proof

Intersect the inclusion in step [](#s3){.pf-ref} with $A$.
Since $A\cap(X\setminus A)=\varnothing$, one obtains
\[
A\subseteq U_1\cup\cdots\cup U_n.
\]

:::

:::

::: pf-step

Therefore $A$ is compact.

::: pf-proof

The open cover $\mathcal U$ in step [](#s1){.pf-ref} was arbitrary, and step [](#s4){.pf-ref} produced a finite subcover.

:::

:::

:::

:::
