---
schema: qual/card@1
id: D-TZSG2
kind: definition
title: "Direct Sum"
classification:
  areas:
  - topology
  topics:
  - modules
  - category-theory
relations: []
review: draft
---

::: {.definition title="Direct Sum"}
The submodule
\[
\bigoplus_\alpha M_\alpha \da \ts{ (m_\alpha) \in \prod_\alpha M_\alpha \st m_\alpha = 0 \text{ for all but finitely many } \alpha }
,\]
equipped with the inclusions $\iota_\beta: M_\beta \injects \bigoplus_\alpha M_\alpha$.
It is the categorical coproduct in $R\dash$modules: a map $\bigoplus_\alpha M_\alpha \to N$ is the same as a family of maps $M_\alpha\to N$.
For a finite index set it coincides with the direct product.
:::

::: {.concept}
See Dummit and Foote, §10.3.
:::
