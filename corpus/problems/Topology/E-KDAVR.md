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
**Goal:** Show that if $X$ is compact and $A \subseteq X$ is closed, then $A$ is compact.

::: pf

::: {.pf-step #s1}

Let $\theset{U_\alpha}$ be an open cover of $A$.

::: pf-proof

Arbitrary open cover of $A$ (by open subsets of $X$).

:::

:::

::: {.pf-step #s2}

$X \setminus A$ is open in $X$.

::: pf-proof

$A$ is closed.

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

::: {.pf-step #s5}

$\theset{U_{\alpha_1}, \ldots, U_{\alpha_n}}$ is a finite cover of $A$.

::: pf-proof

The finite subcover from step [](#s4){.pf-ref} covers $A$ after discarding $X \setminus A$ (which contains no points of $A$); the remaining $U_{\alpha_j}$ still cover $A$ since any $a \in A$ lies in one of the subcover members, which must be a $U_{\alpha_j}$ because $a \notin X \setminus A$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} show every open cover of $A$ has a finite subcover.

:::

:::

:::
