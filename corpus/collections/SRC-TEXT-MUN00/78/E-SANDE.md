---
schema: qual/card@1
id: E-SANDE
kind: problem
title: Classification of compact connected triangulable surfaces with boundary
classification:
  areas:
  - topology
  topics:
  - Classification of Surfaces
relations: []
review: draft
---

::: {.exercise}

Prove the following.

Theorem.
Given a compact connected triangulable 2-manifold $Y$ with boundary, such that $\partial Y$ has $k$ components, then $Y$ is homeomorphic to X-with-$k$-holes, where $X$ is either $S^2$ or the $n$-fold torus $T_n$ or the $m$-fold projective plane $P_m$.

[Hint: Each component of $\partial Y$ is homeomorphic to a circle.]
:::

::: {.solution}
Let the boundary components of \(Y\) be
\[
C_1,\dots,C_k.
\]
By [[E-RKSXA]], \(\partial Y\) is a compact 1-manifold. Each connected compact 1-manifold is homeomorphic to \(S^1\), so choose homeomorphisms
\[
\phi_i:S^1\longrightarrow C_i.
\]

Attach a closed disk \(D_i^2\) to each \(C_i\) by \(\phi_i\), and call the resulting space
\[
X=Y\cup_{\phi_1}D_1^2\cup\cdots\cup_{\phi_k}D_k^2.
\]
We verify the needed properties.

The space is compact because it is a quotient of the compact space
\[
Y\sqcup D_1^2\sqcup\cdots\sqcup D_k^2.
\]
It is Hausdorff because the attaching subsets and their graphs are closed in this compact Hausdorff disjoint union, so the induced equivalence relation is closed. It is connected because \(Y\) is connected and each disk meets \(Y\) along its whole boundary circle.

At points away from the seams \(C_i\), the old surface charts or disk-interior charts suffice. At a seam point, a collar half-disk from \(Y\) and a collar half-disk from the attached \(D_i^2\) glue along their diameter to form an ordinary disk. Hence \(X\) is a 2-manifold without boundary.

Because \(Y\) is triangulable, after subdividing its triangulation we may assume each boundary component is a subcomplex. Triangulate each added disk so that its boundary triangulation agrees with that on \(C_i\). Thus \(X\) is triangulable.

The closed-surface classification theorem therefore gives
\[
X\cong S^2,\qquad T_n\ (n\ge1),\qquad\text{or}\qquad P_m\ (m\ge1).
\]

Finally, in each attached disk choose a smaller concentric open disk \(E_i\) whose closure is contained in its interior. The annulus \(D_i^2-E_i\) is homeomorphic, relative to its outer boundary, to a collar of \(C_i\) in \(Y\). Radially pushing this annulus into the boundary collar gives a homeomorphism
\[
X-\bigcup_{i=1}^k E_i\cong Y.
\]
Thus \(Y\) is precisely \(X\)-with-\(k\)-holes for one of the classified closed surfaces \(X\).
:::
