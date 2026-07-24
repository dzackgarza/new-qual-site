---
schema: qual/card@1
id: S-3Q7SE
kind: solution
title: Solution to P-W5XWA
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-W5XWA
review: draft
---

:::{.solution}
$(x_n)$ is bounded. W.L.O.G, we may assume $(x_n)\to 0$ by subtract its' limit. It allows to choose $y_j$ by induction such that $|\langle y_j,\sum_{k=1}^{j-1}y_k\rangle|<2^{-j}$. Now, for $n>m$, $\|\frac1m\sum_{j=1}^m y_j-\frac1n\sum_{j=1}^n y_j\|^2=\langle\frac1m\sum_{j=1}^m y_j-\frac1n\sum_{j=1}^n y_j,\frac1m\sum_{j=1}^m y_j-\frac1n\sum_{j=1}^n y_j\rangle = \langle(\frac1m-\frac1n)\sum_{j=1}^m y_j-\frac1n\sum_{j=m+1}^n y_j,(\frac1m-\frac1n)\sum_{j=1}^m y_j-\frac1n\sum_{j=m+1}^n y_j\rangle$ $(\star)$

Let $\epsilon>0$, by the choice of $y_j$, there is a $m\in\mathbb{N}$, whenever $n\ge m$, $|\langle(\frac1m-\frac1n)\sum_{j=1}^m y_j,\frac1n\sum_{j=m+1}^n y_j\rangle|<\epsilon^2$. Then $(\star)\le(\frac1m-\frac1n)^2\|\sum_{j=1}^m y_j\|^2+2\epsilon^2+\frac1{n^2}\|\sum_{j=m+1}^n y_j\|^2\le \frac1{m^2}(\sum_{j=1}^n\|y_j\|^2+2)+\frac1{n^2}(\sum_{j=m+1}^n\|y_j\|^2+2)+2\epsilon^2\le\frac1{m^2}(m\cdot\sup_{j\in\mathbb{N}}\|y_j\|^2+2)+\frac1{n^2}(n\cdot\sup_{j\in\mathbb{N}}\|y_j\|^2+2)+2\epsilon^2$
:::
