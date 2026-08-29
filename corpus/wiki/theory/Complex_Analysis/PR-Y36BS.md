---
schema: qual/card@1
id: PR-Y36BS
kind: proposition
title: Holomorphic implies continuous.
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Continuity
relations: []
review: draft
---

:::{.proposition}
$f$ is holomorphic at $z_0$ iff there exists an $a\in \CC$ such that
\[  
f(z_0 + h) - f(z_0) - ah = h \psi(h), \quad \psi(h) \converges{h\to 0}\to 0
.\]
In this case, $a = f'(z_0)$.
:::
