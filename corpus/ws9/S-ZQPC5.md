---
schema: qual/card@1
id: S-ZQPC5
kind: solution
title: Solution to P-HWAMG
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-HWAMG
review: draft
---

:::{.solution}
Define $\text{osc}_f(x)=\inf\{\sup_{z,y\in U}|f(z)-f(y)| : U \text{ is a nbhd of } x\}$. It is not hard to see $\text{osc}_f(x)$ is a continuous function and $\{x:f \text{ is continuous at } x\}=\{x:\text{osc}_f(x)=0\}=\bigcap_{n=1}^\infty\{x:\text{osc}_f(x)<1/n\}$, which is a $G_\delta$ set. It implies that $\{x:f\text{ is discontinuous at }x\}$ is a $F_\sigma$, i.e. a countable union of closed subsets.

For the second part, suppose there is a one. Then $\{x:f \text{ is continuous at } x\}=\mathbb{Q}$ is a dense $G_\delta$ set, say co-meager, which means that the set $Ir$ of all irrationals is meager. Since $\mathbb{Q}$ is also countable, thus meager, $[0,1]=\mathbb{Q}\bigsqcup Ir$ is also a meager set. A contradiction to the Baire category theorem.
:::
