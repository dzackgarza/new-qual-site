---
schema: qual/card@1
id: FD-SK4ON
kind: definition
title: Annihilator of a module
prompts:
- What is the annihilator $\mathrm{ann}_R(M)$ of a module?
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-GURUB|ring]] and $M$ an $R$-module.
The \dfn{annihilator} of $M$ is
$$
\Ann_R(M) \coloneqq \theset{r\in R\st rm=0 \text{ for every } m\in M}.
$$
:::

::: {.remark}
$\Ann_R(M)$ is a two-sided [[D-GOFWL|ideal]] of $R$: it is an additive subgroup, and if $r\in\Ann_R(M)$ and $s\in R$, then $(sr)m=s(rm)=0$ and $(rs)m=r(sm)=0$ for every $m\in M$.
:::
