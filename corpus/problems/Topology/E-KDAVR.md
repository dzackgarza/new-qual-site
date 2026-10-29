---
schema: qual/card@1
id: E-KDAVR
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
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $X$ is compact and $A\subseteq X$ is closed then $A$ is compact.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}

Let $\theset{U_\alpha}$ be a cover of $A$ by open subsets of $X$.

::: pf-proof

Every open set of the subspace $A$ has the form $U \intersect A$ with $U$ open in $X$, so it suffices to treat covers by open subsets of $X$.

:::

:::

::: {.pf-step #s2}

$X \setminus A$ is open in $X$.

::: pf-proof

This holds because $A$ is closed.

:::

:::

::: {.pf-step #s3}

$\theset{U_\alpha} \cup \theset{X \setminus A}$ is an open cover of $X$.

::: pf-proof

On $A$, the $U_\alpha$ cover; on $X \setminus A$, the set $X \setminus A$ covers.

:::

:::

::: {.pf-step #s4}

There is a finite subcover of $X$: some $U_{\alpha_1}, \ldots, U_{\alpha_n}$ together with (possibly) $X \setminus A$.

::: pf-proof

$X$ is compact and step [](#s3){.pf-ref} is an open cover.

:::

:::

::: pf-step

$\theset{U_{\alpha_1}, \ldots, U_{\alpha_n}}$ is a finite subcover of the cover in step [](#s1){.pf-ref}, so $A$ is compact.

::: pf-proof

Any $a \in A$ lies in a member of the finite subcover from step [](#s4){.pf-ref}, and that member is some $U_{\alpha_j}$ because $a \notin X \setminus A$.

:::

:::

:::

:::
