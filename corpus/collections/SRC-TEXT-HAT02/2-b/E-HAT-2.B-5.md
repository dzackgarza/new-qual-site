---
schema: qual/card@1
id: E-HAT-2.B-5
kind: problem
title: "Homology of complements of spheres in spheres"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $S$ be an embedded $k$-sphere in $S^n$ for which there exists a disk $D^n \subset S^n$ intersecting $S$ in the disk $D^k \subset D^n$ defined by the first $k$ coordinates of $D^n$.
Let $D^{n-k} \subset D^n$ be the disk defined by the last $n-k$ coordinates, with boundary sphere $S^{n-k-1}$.
Show that the inclusion $S^{n-k-1} \hookrightarrow S^n - S$ induces an isomorphism on homology groups.
:::

::: {.solution}
Put $r=n-k-1$. Alexander duality for the embedded sphere $S\cong S^k$ gives
$$
\widetilde H_i(S^n\setminus S)\cong\widetilde H^{\,n-i-1}(S)
\cong
\begin{cases}\ZZ,&i=r,\\0,&i\ne r.\end{cases}
$$
The source sphere $S^r$ has the same reduced homology groups. It remains to check that its generator maps to a generator in degree $r$.

Inside the coordinate disk $D^n$, the normal disk $D^{n-k}$ meets $S\cap D^n=D^k$ at its center and nowhere else. The boundary of the normal disk is the sphere in the statement. Under Alexander duality, evaluation of the image of its oriented fundamental class on the fundamental class of $S$ is the intersection number of this normal disk with $S$. Excision restricts that intersection calculation to the coordinate disk, where the two coordinate disks meet in one transverse point with local intersection number $+1$ or $-1$. Thus the image has Alexander-duality coordinate $\pm1$ and generates $\widetilde H_r(S^n\setminus S)$.

For $r=0$, the oriented fundamental class of $S^0$ is the difference of its two points, so the same local intersection calculation applies in reduced $H_0$. Hence the inclusion is an isomorphism on reduced homology in every degree, and also on ordinary $H_0$.
:::
