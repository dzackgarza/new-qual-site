---
schema: qual/card@1
id: D-NODFN
kind: definition
title: Direct Limit
classification:
  areas:
  - topology
  topics:
  - Category Theory
  - Homological Algebra
  - Homology
relations: []
review: draft
---

::: {.definition title="Direct Limit"}
For a directed system $\ts{A_\alpha}$ with maps $f_{\alpha\beta}: A_\alpha \to A_\beta$ whenever $\alpha \leq \beta$, the **direct limit** is
\[
\varinjlim_\alpha A_\alpha \da \qty{ \Disjoint_\alpha A_\alpha } / \qty{ a \sim f_{\alpha\beta}(a) }
,\]
the colimit of the system.
Direct limits are exact, and homology commutes with them: $H_n\qty{\varinjlim X_\alpha} \cong \varinjlim H_n(X_\alpha)$ for a directed system of subcomplexes.
:::

::: {.concept}
See Hatcher, p. 243.
:::
