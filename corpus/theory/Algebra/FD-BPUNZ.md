---
schema: qual/card@1
id: FD-BPUNZ
kind: definition
title: Torsion submodule
prompts:
- What is the torsion submodule $M_{\mathrm{tors}}$ of a module $M$?
classification:
  areas:
  - algebra
  topics:
  - Torsion
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be an [[D-QJ3QL|integral domain]] and $M$ an $R$-module.
The \dfn{torsion submodule} of $M$ is
$$
M_{\mathrm{tors}} \coloneqq \theset{m \in M \st rm = 0 \text{ for some nonzero } r \in R}.
$$
:::

::: {.remark}
$M_{\mathrm{tors}}$ is a submodule: if $rm=0$ and $sn=0$ with $r,s\neq0$, then $rs\neq0$ because $R$ is a domain, $rs(m+n)=0$, and $r(am)=a(rm)=0$ for every $a\in R$.
:::

::: {.remark}
Dummit and Foote write $\operatorname{Tor}(M)$ for $M_{\mathrm{tors}}$ [@DF04, Section 10.1, Exercise 8]; problems that follow that text keep its notation, which is unrelated to the functor $\operatorname{Tor}^R_i$.
:::
