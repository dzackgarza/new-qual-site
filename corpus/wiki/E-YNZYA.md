---
schema: qual/card@1
id: E-YNZYA
kind: exercise
title: "Residue of $1/z^2 + 1$"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - poles
relations: []
review: draft
---
:::{.exercise title="Residue of $1/z^2 + 1$"}
Use the rational function formula to compute the residues at $z=\pm i$ of
\[
f(z) \da {1\over z^2 + 1}
.\]

:::

:::{.solution}
Applying the rational function formula:
\[
\Res_{z=z_0}{1\over 1+z^2} &= {1\over 2z}\evalfrom_{z= z_0} \implies\\
\Res_{z=i}f(z) &= {1\over 2i} = -{i\over 2} \\
\Res_{z=-i}f(z) &= -{1\over 2i} = {i\over 2}
.\]

:::

