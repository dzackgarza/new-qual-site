---
schema: qual/card@1
id: PR-EMFAN
kind: proposition
title: "Holomorphic functions are continuous."
classification:
  areas:
  - complex-analysis
  topics:
  - holomorphic-functions
  - continuity
relations: []
review: draft
---
:::{.proposition title="Holomorphic functions are continuous."}
$f$ is holomorphic at $z_0$ iff there exists an $a\in \CC$ such that
\[
f(z_0 + h) - f(z_0) - ah = h \psi(h), \quad \psi(h) \converges{h\to 0}\to 0
.\]
In this case, $a = f'(z_0)$.
:::
