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
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Withdrew the added MSE 4773641 transcription as unverified. Independent review establishes
    that ell is the image of a half-sized open k-disk, not a closed subset, and that the omitted
    definitions of D and D' prevent checking excision and generalized Schoenflies. The previous
    text also repeated the thread's h'(S^k) notation although h' has domain D^n. The earlier
    Alexander-intersection proof and k=n case are unchanged; #105's complete-solution obligation
    for this card remains open.
---

::: {.problem}
Let $S$ be an embedded $k$-sphere in $S^n$ for which there exists a disk $D^n \subset S^n$ intersecting $S$ in the disk $D^k \subset D^n$ defined by the first $k$ coordinates of $D^n$.
Let $D^{n-k} \subset D^n$ be the disk defined by the last $n-k$ coordinates, with boundary sphere $S^{n-k-1}$.
Show that the inclusion $S^{n-k-1} \hookrightarrow S^n - S$ induces an isomorphism on homology groups.
:::

::: {.solution}
Put $r=n-k-1$.

::: pf

::: pf-step
If $k=n$, then the inclusion in the statement is an isomorphism on homology.

::: pf-proof
An embedded $n$-sphere in $S^n$ is all of $S^n$ by invariance of domain. Hence both $S^r=S^{-1}$ and $S^n-S$ are empty.
:::

:::

::: {.pf-step #complement-homology}
For $k<n$, both $S^r$ and $S^n-S$ have reduced homology $\ZZ$ in degree $r$ and zero in every other degree.

::: pf-proof
Now $r\ge0$, and Alexander duality for the embedded proper subsphere $S\cong S^k$ gives
$$
\widetilde H_i(S^n\setminus S)\cong\widetilde H^{\,n-i-1}(S)
\cong
\begin{cases}\ZZ,&i=r,\\0,&i\ne r.\end{cases}
$$
The source sphere $S^r$ has the same reduced homology groups.
:::

:::

::: {.pf-step #normal-generator}
The image of the oriented fundamental class of $S^r$ is a generator of $\widetilde H_r(S^n\setminus S)$.

::: pf-proof
Inside the coordinate disk $D^n$, the normal disk $D^{n-k}$ meets $S\cap D^n=D^k$ at its center and nowhere else. The boundary of the normal disk is the sphere in the statement. Under Alexander duality, evaluation of the image of its oriented fundamental class on the fundamental class of $S$ is the intersection number of this normal disk with $S$. Excision restricts that intersection calculation to the coordinate disk, where the two coordinate disks meet in one transverse point with local intersection number $+1$ or $-1$. Thus the image has Alexander-duality coordinate $\pm1$, so it is a generator.
:::

:::

::: pf-step
Consequently the inclusion induces an isomorphism on reduced homology in every degree, and also on ordinary $H_0$.

::: pf-proof
For $k<n$, step [](#complement-homology){.pf-ref} leaves only degree $r$ to check, and step [](#normal-generator){.pf-ref} shows that the inclusion sends a generator to a generator. For $r=0$, the oriented fundamental class of $S^0$ is the difference of its two points, so the same local intersection calculation applies in reduced $H_0$. Reduced homology determines ordinary homology in positive degrees and determines ordinary $H_0$ here since both spaces are nonempty. The case $k=n$ was already verified directly.
:::

:::

:::
:::
