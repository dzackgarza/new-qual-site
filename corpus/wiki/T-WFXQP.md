---
schema: qual/card@1
id: T-WFXQP
kind: theorem
title: "Residue formula: poles at infinity"
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - singularities
relations: []
review: draft
---
:::{.theorem title="Residue formula: poles at infinity"}
\[
\Res_{z=\infty}f(z) = \Res_{z=0} g(z) && g(z) \da -{1 \over z^2}f\qty{1\over z} 
.\]

Note on where this weird formula comes from: residues are associated not to function $f$ but to *differential forms* $f(z)\dz$, and inversion sends $f(z) \dz\to f(1/z)d(1/z) = f(1/z)\cdot -{1\over z^2}\dz$.
This residue can alternatively be calculated for $f$ by taking $\gamma$ a contour enclosing all singularities of $f$ and computing
\[
\Res_{z=\infty}f(z) = -{1\over 2\pi}\int_\gamma f(z) \dz
.\]

:::
