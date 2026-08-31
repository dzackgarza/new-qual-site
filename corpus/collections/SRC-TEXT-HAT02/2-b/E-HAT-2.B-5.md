---
schema: qual/card@1
id: E-HAT-2.B-5
kind: exercise
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

Let $S$ be an embedded $k$-sphere in $S^n$ for which there exists a disk $D^n \subset S^n$ intersecting $S$ in the disk $D^k \subset D^n$ defined by the first $k$ coordinates of $D^n$.
Let $D^{n-k} \subset D^n$ be the disk defined by the last $n-k$ coordinates, with boundary sphere $S^{n-k-1}$.
Show that the inclusion $S^{n-k-1} \hookrightarrow S^n - S$ induces an isomorphism on homology groups.

::: {.solution}
<1>1. Homology of the sphere complement $S^n \setminus S$:
<2>1. By Alexander Duality (or the Mayer–Vietoris sphere-complement induction in Hatcher §2.B):
For any embedded sphere $S \cong S^k \subset S^n$ ($0 \le k < n$), the reduced homology of the complement is:
\[
\widetilde{H}_i(S^n \setminus S) \cong \begin{cases} \mathbb{Z} & \text{if } i = n - k - 1, \\ 0 & \text{otherwise.} \end{cases}
\]
Thus the homology of $S^n \setminus S$ matches the homology of the sphere $S^{n-k-1}$ in all dimensions.
::: {.proof}
Alexander Duality $\widetilde{H}_i(S^n \setminus S) \cong \widetilde{H}^{n-1-i}(S^k)$.
:::

<1>2. Local retraction in the coordinate ball $D^n$:
<2>1. In the coordinate disk $D^n \cong D^k \times D^{n-k}$, the intersection with $S$ is $D^k \times \{0\}$.
The complement inside $D^n$ is:
\[
D^n \setminus (D^k \times \{0\}) \cong D^k \times (D^{n-k} \setminus \{0\}).
\]
::: {.proof}
Cartesian product representation.
:::
<2>2. Since $D^k$ is contractible and $D^{n-k} \setminus \{0\}$ deformation retracts radially onto its boundary sphere $\partial D^{n-k} = S^{n-k-1}$:
The inclusion $j: S^{n-k-1} \hookrightarrow D^n \setminus D^k$ is a homotopy equivalence.
::: {.proof}
radial deformation retraction along the last $n-k$ coordinates.
:::

<1>3. Induced isomorphism on homology:
<2>1. Decompose the embedded sphere $S$ into the upper disk $D_1^k = S \cap D^n$ and the lower disk $D_2^k = \overline{S \setminus D_1^k}$, with intersection $\partial D_1^k = S^{k-1}$.
::: {.proof}
decomposition of $S^k$ into two hemispheres.
:::
<2>2. The Mayer–Vietoris sequence for $S^n \setminus S = (S^n \setminus D_1^k) \cap (S^n \setminus D_2^k)$ shows that the inclusion $D^n \setminus D^k \hookrightarrow S^n \setminus S$ induces an isomorphism on reduced homology in dimension $n - k - 1$.
::: {.proof}
Mayer–Vietoris sequence with contractible disk complements.
:::
<2>3. Factoring the inclusion $i: S^{n-k-1} \hookrightarrow S^n \setminus S$ as:
\[
S^{n-k-1} \xrightarrow{j} D^n \setminus D^k \hookrightarrow S^n \setminus S,
\]
the map $i_*$ is the composite of the homotopy equivalence $j_*$ and the Mayer–Vietoris isomorphism.
Therefore $i_*: \widetilde{H}_i(S^{n-k-1}) \xrightarrow{\cong} \widetilde{H}_i(S^n \setminus S)$ is an isomorphism for all $i$.
::: {.proof}
composition of homology isomorphisms.
:::

<1>4. Conclusion:
The inclusion $S^{n-k-1} \hookrightarrow S^n \setminus S$ induces an isomorphism on all homology groups. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
