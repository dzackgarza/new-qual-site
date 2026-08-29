---
schema: qual/card@1
id: S-DHPCN
kind: solution
title: Solution to P-7VK5X
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations:
- kind: solves
  target: P-7VK5X
review: draft
---

:::{.solution}
$f:\mathbb{R}^2\to\mathbb{R}$ by $f(x,y)=x-y$ is continuous. Thus, $E=f^{-1}(A)$ is Borel. $E^y=\{x\in\mathbb{R}:(x,y)\in E\}=y+A$ which is a null set since $m(y+A)=m(A)=0$. Thus $m\times m(E)=\int m(E^y)dm(y)=0$.
:::
