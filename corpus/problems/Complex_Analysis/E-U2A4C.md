---
schema: qual/card@1
id: E-U2A4C
kind: problem
title: Residues at $\infty$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Singularities
  - Laurent Series
relations: []
review: draft
---

::: {.exercise}
Compute
\[
\Res_{z=\infty}e^z,
\qquad
\Res_{z=\infty}{z-1\over z+1}.
\]
:::

::: {.solution}
Recall
\[
\Res_{z=\infty}f(z)
=-\Res_{w=0}\frac{f(1/w)}{w^2}.
\]

For $f(z)=e^z$,
\[
\frac{e^{1/w}}{w^2}
=\sum_{k=0}^\infty {w^{-k-2}\over k!}.
\]
There is no $w^{-1}$ term, hence
\[
\Res_{z=\infty}e^z=0.
\]

For
\[
f(z)={z-1\over z+1},
\]
we have
\[
\frac{f(1/w)}{w^2}
={1\over w^2}{1-w\over1+w}
={1\over w^2}\qty{1-2w+2w^2-2w^3+\cdots}.
\]
Thus
\[
\Res_{w=0}\frac{f(1/w)}{w^2}=-2,
\]
so
\[
\Res_{z=\infty}{z-1\over z+1}=2.
\]
Equivalently, the only finite pole is at $z=-1$ with residue $-2$, and the sum of all residues on $\CP^1$ is zero.
:::
