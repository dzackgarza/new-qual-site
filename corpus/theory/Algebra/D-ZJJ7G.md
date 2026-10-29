---
schema: qual/card@1
id: D-ZJJ7G
kind: definition
title: Torsion elements, torsion modules, and torsion-free modules
prompts:
- What does it mean for a module to be torsion-free?
- What is the torsion submodule $M_t$ of a module $M$?
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
Let $R$ be a commutative [[D-GURUB|ring]] and $M$ an $R$-module.

- An element $m\in M$ is a \dfn{torsion element} if there exists a nonzero $r\in R$ with $rm=0$.

- Write $M_t\coloneqq\theset{m\in M \st rm=0 \text{ for some nonzero } r\in R}$ for the set of torsion elements of $M$.

- $M$ is \dfn{torsion-free} if no nonzero element of $M$ is a torsion element, that is, $M_t\subseteq\theset{0}$.

- $M$ is a \dfn{torsion module} if $M_t=M$.

When $R$ is an [[D-QJ3QL|integral domain]], $M_t$ is a submodule of $M$, the \dfn{torsion submodule}.
:::

::: {.remark}
Over a domain, $M_t$ is a submodule: if $rm=0$ and $sn=0$ with $r,s\neq0$, then $rs\neq0$, $rs(m+n)=0$, and $r(am)=a(rm)=0$ for every $a\in R$. Without the domain hypothesis it can fail: in the $\ZZ/6$-module $\ZZ/6$, the torsion elements $2$ and $3$ sum to $5$, which is not torsion.
:::

::: {.remark}
Dummit and Foote write $\operatorname{Tor}(M)$ for $M_t$ [@DF04, Section 10.1, Exercise 8]; problems that follow that text keep its notation, which is unrelated to the functor $\operatorname{Tor}^R_i$.
:::
