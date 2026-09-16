---
schema: qual/card@1
id: D-TPTOG
kind: definition
title: Mapping path space
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Function Spaces
relations: []
review: draft
---

::: {.definition}
Let $f\colon X\to Y$ be a continuous map, $I=[0,1]$, and $Y^I$ the space of paths $I\to Y$ with the compact-open topology.
The \dfn{mapping path space} of $f$ is the subspace
$$
E_f\coloneqq\ts{(x,\gamma)\in X\times Y^I \st \gamma(0)=f(x)}
$$
of $X\times Y^I$ [@Hat02, p. 407].
:::

::: {.proposition}
Let $\iota\colon X\to E_f$ be $x\mapsto(x,c_{f(x)})$, where $c_y$ is the constant path at $y$, and let $p\colon E_f\to Y$ be $(x,\gamma)\mapsto\gamma(1)$.
Then $f=p\circ\iota$, the space $E_f$ [[D-UH3L5|deformation retracts]] onto $\iota(X)$, so $\iota$ is a [[D-HFR32|homotopy equivalence]], and $p$ is a fibration.
Thus every continuous map factors as a homotopy equivalence followed by a fibration [@Hat02, p. 407].
:::

::: {.remark}
The mapping path space is the Eckmann--Hilton dual of the [[D-RMQ7W|mapping cylinder]], which factors a map as an embedding followed by a homotopy equivalence.
:::
