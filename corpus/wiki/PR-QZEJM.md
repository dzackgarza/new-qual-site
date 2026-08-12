---
schema: qual/card@1
id: PR-QZEJM
kind: proposition
title: "Jordan's Lemma"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="Jordan's Lemma"}
Suppose that $f(z) = e^{iaz}g(z)$ for some $g$, and let $C_R \da \ts{ z=Re^{it} \st t\in [0, \pi] }$. Then
\[
\abs{\int_{C_R} f(z) \dz} \leq {\pi M_R \over a}
\]
where $M_R \da \sup_{t\in [0, \pi]} \abs{g(Re^{it})}$.
:::
