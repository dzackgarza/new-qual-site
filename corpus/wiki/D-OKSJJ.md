---
schema: qual/card@1
id: D-OKSJJ
kind: definition
title: Inverse Limit
classification:
  areas:
  - topology
  topics:
  - Category Theory
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
For an inverse system $\ts{A_\alpha}$ with maps $f_{\beta\alpha}: A_\beta \to A_\alpha$ whenever $\alpha \leq \beta$, the **inverse limit** is the subgroup of compatible tuples
\[
\varprojlim_\alpha A_\alpha \da \ts{ (a_\alpha) \in \prod_\alpha A_\alpha \st f_{\beta\alpha}(a_\beta) = a_\alpha \text{ whenever } \alpha \leq \beta }
.\]
Unlike the direct limit it is only left exact; the failure of exactness is measured by the derived functor $\varprojlim^1$.
:::

::: {.concept}
See Hatcher, p. 312.
:::
