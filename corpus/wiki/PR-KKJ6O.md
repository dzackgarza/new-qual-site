---
schema: qual/card@1
id: PR-KKJ6O
kind: proposition
title: "Continuity of Measure"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="Continuity of Measure"}
\[
\text{Continuity from below:} \quad 
E_{n} \nearrow E &\implies m(E_{n}) \converges{n\to\infty}\too m(E) \\
\text{Continuity from above:} \quad 
m(E_{1}) < \infty \text{ and } E_{n} \searrow E &\implies m(E_{n}) \converges{n\to\infty}\too m(E)
.\]

Mnemonic: $\lim_n \mu(E_n) = \mu(\lim E_n)$ where $\lim_n E_n = E\da \union_N E_n$ for $E_n \increasesto E$ and $\lim_n E_n = E \da \intersect_n E_n$ for $E_n\decreasesto E$.
:::
