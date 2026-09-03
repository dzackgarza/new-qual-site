---
schema: qual/card@1
id: E-GMGFS
kind: problem
title: Expansion at an essential singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Essential Singularities
  - Residues
  - Trigonometry
relations: []
review: draft
---

:::{.exercise}
Find a Laurent expansion about $z=0$ of
\[
f(z) \da \cos\qty{1- {1\over z}}
,\]
and compute the "residue" coefficient $c_{-1}$.

:::

:::{.solution}
Write $g(z) \da \cos(1-z)$, so $g(1/z) = f(z)$, and expand:
\[
g(z) 
&= \cos(1-z) \\
&= {1\over 2}\qty{e^{i(1-z)} + e^{-i(1-z)}} \\
&= {1\over 2}\qty{e^i e^{-iz} + e^{-i} e^{iz}}\\
&= {1\over 2}\sum_{k\geq 0} \qty{ (-i)^k e^i + i^k e^{-i} } {z^k \over k!} \\
\implies f(z) 
&= {1\over 2}\sum_{k\geq 0}  \qty{ ( (-i)^k e^i + i^k e^{-i} } {1 \over k!z^k}
.\]

Taking $k=1$ yields
\[
c_{-1} = {-ie^i + ie^{-i} \over 2} = -i\cdot {e^i - e^{-i}\over 2} = {e^i - e^{-i}\over 2i} = \sin(1)
.\]

:::

