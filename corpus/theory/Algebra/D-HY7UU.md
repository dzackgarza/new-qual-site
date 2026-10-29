---
schema: qual/card@1
id: D-HY7UU
kind: definition
title: Cyclic modules
prompts:
- When is an $R\dash$module cyclic, and what does it look like as a quotient of $R$?
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Cyclic Groups
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
An [[D-NQZUY|$R$-module]] $M$ is \dfn{cyclic} if there exists $m\in M$ such that
$$
M = Rm \coloneqq \theset{ rm \st r\in R }.
$$
:::

::: {.proposition}
An $R$-module $M$ is cyclic if and only if $M \cong R/I$ for some left ideal $I$ of $R$.
:::

::: {.proof}
If $M=Rm$, the $R$-linear map $\phi\colon R\to M$, $r\mapsto rm$, is surjective, and its kernel $I\coloneqq\theset{r\in R \st rm=0}$ is a left ideal, so $M\cong R/I$ by the first isomorphism theorem.
Conversely, $R/I=R\cdot(1+I)$ is cyclic, and an isomorphism $R/I\to M$ sends the generator $1+I$ to a generator of $M$.
:::
