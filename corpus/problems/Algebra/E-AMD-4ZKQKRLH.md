---
schema: qual/card@1
id: E-AMD-4ZKQKRLH
kind: problem
title: A normal $p$-subgroup is contained in every Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that any normal $p$-subgroup of a finite group $G$ is contained in every Sylow $p$-subgroup of $G$.
:::

::: {.solution}
Let $N\trianglelefteq G$ be a normal $p$-subgroup and let $P\in\Syl_p(G)$.

::: pf

::: {.pf-step #np-p-group}
$NP$ is a $p$-subgroup of $G$ that contains $P$.

::: pf-proof
$NP$ is a subgroup because $N$ is normal, and
$$
\abs{NP}=\frac{\abs N\abs P}{\abs{N\cap P}}
$$
is a power of $p$.
:::

:::

::: pf-step
$N\le P$.

::: pf-proof
$P$ is a $p$-subgroup of maximal order, so step [](#np-p-group){.pf-ref} forces $NP=P$, hence $N\le P$. Since $P$ is arbitrary, $N$ lies in every Sylow $p$-subgroup.
:::

:::

:::

:::
