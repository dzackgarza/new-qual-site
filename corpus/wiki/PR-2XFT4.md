---
schema: qual/card@1
id: PR-2XFT4
kind: proposition
title: "Residue formula for higher order poles"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - poles
relations: []
review: draft
---
:::{.proposition title="Residue formula for higher order poles"}
If $f$ has a pole $z_0$ of order $n$, then
\[
\Res_{z=z_0} f = \lim_{z\to z_0} {1 \over (n-1)!} \qty{\dd{}{z}}^{n-1} (z-z_0)^n f(z)
.\]
:::
