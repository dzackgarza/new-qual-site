---
schema: qual/card@1
id: D-MQSFD
kind: definition
title: Quasicompact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
---

::: {.definition}
A topological space $X$, not necessarily Hausdorff, is \dfn{quasicompact} if every open [[D-AOJG3|cover]] of $X$ has a finite subcover.
A quasicompact space is \dfn{compact} if it is also [[D-ZFRV4|Hausdorff]].
:::

::: {.remark}
Requiring compact spaces to be Hausdorff is the convention of Bourbaki and of algebraic geometry, where the Zariski topology on the [[D-CXXCG|spectrum]] $\Spec A$ of a commutative ring $A$ is always quasicompact and is Hausdorff if and only if every prime ideal of $A$ is maximal.
In [@Mun00] a space is [[D-EILKJ|compact]] under the open-cover condition alone, so compact in that sense means quasicompact in the Bourbaki convention.
:::

::: {.example}
A two-point set with the indiscrete topology is quasicompact, since its only open cover by nonempty sets is the whole space.
It is not Hausdorff, so it is not compact in the Bourbaki convention, although it is [[D-EILKJ|compact]] in the open-cover sense.
:::
