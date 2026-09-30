---
schema: qual/card@1
id: E-BRPKJ
kind: problem
title: Where a proof about closures of unions fails
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Criticize the following "proof" that $\overline{\bigcup A_\alpha} \subset \bigcup \overline{A}_\alpha$: if $\theset{A_\alpha}$ is a collection of sets in $X$ and if $x \in \overline{\bigcup A_\alpha}$, then every neighborhood $U$ of $x$ intersects $\bigcup A_\alpha$.
Thus $U$ must intersect some $A_\alpha$, so that $x$ must belong to the closure of some $A_\alpha$.
Therefore, $x \in \bigcup \overline{A}_\alpha$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The step "so that $x$ must belong to the closure of some $A_\alpha$" does not follow.

::: pf-proof

The previous step gives, for each neighborhood $U$ of $x$, an index $\alpha(U)$ with $U\cap A_{\alpha(U)}\ne\varnothing$.
By the definition of closure, $x\in\overline{A_\beta}$ requires a single index $\beta$ such that every neighborhood of $x$ meets $A_\beta$.
The index $\alpha(U)$ may change with $U$, so no such $\beta$ is produced.

:::

:::

::: {.pf-step #s2}

The inclusion $\overline{\bigcup A_\alpha}\subseteq\bigcup\overline{A_\alpha}$ is false in general.

::: pf-proof

In $\RR$ let $A_n=\{1/n\}$ for $n\ge1$.
Then $\overline{\bigcup_nA_n}=\{0\}\cup\{1/n:n\ge1\}$, while $\bigcup_n\overline{A_n}=\{1/n:n\ge1\}$ does not contain $0$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} locates the invalid inference, and step [](#s2){.pf-ref} shows that the conclusion itself fails.

:::

:::

:::
