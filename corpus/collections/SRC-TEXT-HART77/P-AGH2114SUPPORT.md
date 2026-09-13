---
schema: qual/card@1
id: P-AGH2114SUPPORT
kind: problem
title: The support of a section is closed, but the support of a sheaf need not be
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Support
  - Stalks
relations: []
review: draft
---

::: problem
Let $\mcf$ be a sheaf on $X$ and let $s \in \mcf(U)$ be a section over an open set $U$.
The **support of $s$**, denoted $\supp s$, is defined to be $\ts{P \in U \st s_P \neq 0}$, where $s_P$ denotes the germ of $s$ in the stalk $\mcf_P$.
Show that $\supp s$ is a closed subset of $U$.

Define the support of $\mcf$ to be $\supp \mcf \da \ts{P \in X \st \mcf_P \neq 0}$.
Show that this need not be a closed subset.
:::
