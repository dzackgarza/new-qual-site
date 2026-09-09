---
schema: qual/card@1
id: P-HCAX1
kind: problem
title: A continuous isolated singularity is removable
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
---

::: problem
Let $f$ be continuous on a disk and holomorphic away from its center.
Prove that $f$ is holomorphic on the entire disk.
:::

::: solution
Let $a$ be the center of the disk. Since $f$ is continuous at $a$, it is bounded in some neighborhood of $a$.

Define
\[
h(z)=(z-a)^2f(z).
\]
Away from $a$, the function $h$ is holomorphic. At $a$,
\[
\frac{h(z)-h(a)}{z-a}=(z-a)f(z)\longrightarrow 0,
\]
so $h$ is also holomorphic at $a$ and $h'(a)=0$. Thus $h$ has a zero of order at least two at $a$. Hence there is a holomorphic function $g$ on the whole disk such that
\[
h(z)=(z-a)^2g(z).
\]
For $z\ne a$ we may cancel $(z-a)^2$ and obtain $g(z)=f(z)$. By continuity of both functions at $a$,
\[
g(a)=\lim_{z\to a}g(z)=\lim_{z\to a}f(z)=f(a).
\]
Therefore $g=f$ on the entire disk, so $f$ is holomorphic there.
:::
