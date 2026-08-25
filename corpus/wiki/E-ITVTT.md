---
schema: qual/card@1
id: E-ITVTT
kind: exercise
title: Residue of $1/z^n+1$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Poles
relations: []
review: draft
---

:::{.exercise title="Residue of $1/z^n+1$"}
Find the residue at $\omega_n \da e^{\pi i \over n}$ of
\[
f(z) = {1\over z^n + 1}
.\]

:::

:::{.solution}
Check that $\dd{}{z} z^n+1 = nz^{n-1}\neq 0$ for $z\neq 0$, so this has no repeated roots since $z=0$ is not a root.
Thus all of the poles are simple, so apply the rational function formula:
\[
\Res_{z=\zeta_{m}} {1\over z^n + 1} 
&= {1 \over nz^{n-1}}\evalfrom_{z=\omega_n} \\
&= {1\over n\omega_n^{n-1}} \\
&= {\omega_n^{1-n}\over n} \\
&= -{\omega_n \over n}
,\]
which follows from expanding 
\[
\omega_n^{1-n} = e^{i\pi (1-n) \over n} =  e^{i\pi\over n}e^{-i\pi n \over n} = e^{i\pi \over n}\cdot (-1) = -\omega_n
.\].
:::

