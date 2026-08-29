---
schema: qual/card@1
id: S-U3H2D
kind: solution
title: Solution to P-NIC7C
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
relations:
- kind: solves
  target: P-NIC7C
review: draft
---

:::{.solution}
By open mapping theorem, $\phi\circ T^{-1}$ is a well-defined linear bounded functional on $T(X)$. Then, by Hahn-Banach Thm, it can be extent to some $\psi$ on $Y$, say, $y\in T(X)$ implies that $\phi\circ T^{-1}(y)=\psi(y)$. It implies that $\psi(T(x))=\phi(x)$ for all $x\in X$.
:::
