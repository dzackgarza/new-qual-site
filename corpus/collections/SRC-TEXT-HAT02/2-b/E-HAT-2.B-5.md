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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.B Exercise 5, printed page
    176; the statement matches word for word. Checked: Alexander duality gives
    H̃_i(S^n − S) ≅ H̃^{n−i−1}(S^k) = Z exactly in degree r = n−k−1, matching
    H̃_*(S^r); the normal disk D^{n−k} meets S in one transverse point of the
    coordinate disk, so the Alexander-duality coordinate of the image of [S^r] is
    ±1 and the inclusion is an isomorphism in degree r and hence in all degrees,
    with the r = 0 case read on reduced H_0. No defect.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Added the omitted case k = n. Then the embedded n-sphere is all of S^n by
    invariance of domain, so S^{n-k-1} = S^{-1} and S^n - S are both empty and the
    inclusion is an isomorphism on homology. Alexander duality for a proper subsphere
    is now invoked only after reducing to k < n. The previous r = -1 calculation did
    not cover this case.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Rechecked all cases against Hatcher p.176 and Corollary 2B.4: k = n holds
    trivially, while for k < n the normal disk meets S in one transverse point, giving
    Alexander-duality coordinate plus or minus one for the image of the normal-sphere
    fundamental class. The r = 0 reduced-H_0 interpretation remains included.
---

::: {.problem}
Let $S$ be an embedded $k$-sphere in $S^n$ for which there exists a disk $D^n \subset S^n$ intersecting $S$ in the disk $D^k \subset D^n$ defined by the first $k$ coordinates of $D^n$.
Let $D^{n-k} \subset D^n$ be the disk defined by the last $n-k$ coordinates, with boundary sphere $S^{n-k-1}$.
Show that the inclusion $S^{n-k-1} \hookrightarrow S^n - S$ induces an isomorphism on homology groups.
:::

::: {.solution}
If $k=n$, then $S$ is an embedded $n$-sphere in $S^n$. By invariance of domain it is all of $S^n$. Hence both $S^{n-k-1}=S^{-1}$ and $S^n-S$ are empty, and the inclusion in the statement is an isomorphism on homology.

Now suppose $k<n$ and put $r=n-k-1\ge0$. Alexander duality for the embedded proper subsphere $S\cong S^k$ gives
$$
\widetilde H_i(S^n\setminus S)\cong\widetilde H^{\,n-i-1}(S)
\cong
\begin{cases}\ZZ,&i=r,\\0,&i\ne r.\end{cases}
$$
The source sphere $S^r$ has the same reduced homology groups. It remains to check that its generator maps to a generator in degree $r$.

Inside the coordinate disk $D^n$, the normal disk $D^{n-k}$ meets $S\cap D^n=D^k$ at its center and nowhere else. The boundary of the normal disk is the sphere in the statement. Under Alexander duality, evaluation of the image of its oriented fundamental class on the fundamental class of $S$ is the intersection number of this normal disk with $S$. Excision restricts that intersection calculation to the coordinate disk, where the two coordinate disks meet in one transverse point with local intersection number $+1$ or $-1$. Thus the image has Alexander-duality coordinate $\pm1$ and generates $\widetilde H_r(S^n\setminus S)$.

For $r=0$, the oriented fundamental class of $S^0$ is the difference of its two points, so the same local intersection calculation applies in reduced $H_0$. Hence the inclusion is an isomorphism on reduced homology in every degree, and also on ordinary $H_0$.
:::
