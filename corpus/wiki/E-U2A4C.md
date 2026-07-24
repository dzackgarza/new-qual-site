---
schema: qual/card@1
id: E-U2A4C
kind: exercise
title: "Residues at $\\infty$"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Residues at $\infty$"}
Compute
\[
&\Res_{z=\infty}e^z\\
&\Res_{z=\infty}{z-1\over z+1}
.\]

:::

:::{.solution}
In parts:

- For $e^z$:
  - Integral formula: $\Res_{z=\infty}f(z) = -{1\over 2\pi }\int_\gamma f(z)\dz$ where $\gamma$ encloses all singularities of $f$, but $e^z$ is entire, so this integral is zero and thus the residue is zero.
  - Inversion formula: expand $z^{-2}f(1/z)$ about $z=0$ to obtain
  \[
  {1\over z^2}e^{1\over z} = z^{-2}\sum_{k\geq 0}z^{-k}/k! = \sum_{k\geq 0}z^{-k-2}/k! = z^{-2} + z^{-3} + {1\over 2!}z^{-4} + \bigo(z^{-5}) 
  ,\]
  so the residue is zero.

- For ${z+1\over z-1}$:
  - Integral formula:
  \[
  \Res_{z=\infty} &= -{1\over 2\pi}\int_{\abs{z} = 2} {z-1\over z+1}\dz \\
  &= - \Res_{z=-1} {z-1\over z+1} \\
  &= - (-2) \\
  &= 2
  .\]
  - Inversion formula:
  \[
  {1\over z^2}{ z\inv - 1 \over z\inv + 1} 
  &= z^{-2}{1 - z \over 1 + z} \\
  &= z^{-2}(z-1)\sum_{k\geq 0} (-z)^k \\
  &= z^{-2} + 2z\inv -2 + 2z - \bigo(z^2)
  ,\]
  which has residue 2.

:::

