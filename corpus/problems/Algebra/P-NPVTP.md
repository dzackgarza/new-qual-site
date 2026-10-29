---
schema: qual/card@1
id: P-NPVTP
kind: problem
title: Nilpotent groups have nontrivial centers
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: The source is a bullet item reading "Show that nilpotent groups have nontrivial centers.", which fails for the trivial group; the statement restricts to nontrivial nilpotent groups.
---

::: {.problem}
Show that nontrivial nilpotent groups have nontrivial centers.
:::

::: {.solution}
Let $G\neq1$ be nilpotent, with lower central series $\gamma_1(G)=G$, $\gamma_{i+1}(G)=[\gamma_i(G),G]$.

::: pf

::: {.pf-step #class}
There is $c\ge1$ with $\gamma_c(G)\ne1$ and $\gamma_{c+1}(G)=1$.

::: pf-proof
Since $G$ is nilpotent, some $\gamma_i(G)$ is trivial, and $\gamma_1(G)=G\ne1$; take $c+1$ to be the least such $i$.
:::

:::

::: pf-step
$Z(G)\ne1$.

::: pf-proof
By step [](#class){.pf-ref}, $[\gamma_c(G),G]=1$, so every element of $\gamma_c(G)$ commutes with every element of $G$, and $1\ne\gamma_c(G)\le Z(G)$.
:::

:::

:::

:::
