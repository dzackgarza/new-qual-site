---
schema: qual/card@1
id: E-HAT-2.B-3
kind: problem
title: "Complement of a disk pair in a sphere pair"
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the Alexander-duality and Mayer--Vietoris calculations and all degree shifts.
---

Let $(D, S) \subset (D^n, S^{n-1})$ be a pair of subspaces homeomorphic to $(D^k, S^{k-1})$, with $D \cap S^{n-1} = S$.
Show the inclusion $S^{n-1} - S \hookrightarrow D^n - D$ induces an isomorphism on homology.
[Glue two copies of $(D^n, D)$ to the two ends of $(S^{n-1} \times I, S \times I)$ to produce a $k$-sphere in $S^n$ and look at a Mayer–Vietoris sequence for the complement of this $k$-sphere.]

::: {.solution}
Let
\[
i:S^{n-1}-S\longrightarrow D^n-D
\]
be the inclusion. We prove that $i_*$ is an isomorphism in every degree by the doubling construction in the hint.

<1>1. Glue two copies $(D^n_+,D_+)$ and $(D^n_-,D_-)$ of $(D^n,D)$ to the two ends of
\[
(S^{n-1}\times I,S\times I).
\]
The resulting pair is homeomorphic to
\[
(S^n,S^k).
\]
::: {.proof}
The two $n$-disks together with the boundary cylinder form $S^n$. The two copies of $D^k$, joined along their common boundary by $S^{k-1}\times I$, form the double of $D^k$, hence $S^k$.
:::

<1>2. Taking complements gives a decomposition of $S^n-S^k$ into two open sets $U_+$ and $U_-$ such that
\[
U_\pm\simeq D^n-D,
\qquad
U_+\cap U_-\simeq S^{n-1}-S,
\]
and the two maps from the intersection to the two pieces induce the same map on homology, namely $i_*$ after these identifications.
::: {.proof}
Thicken each disk half slightly into the connecting cylinder. Each thickened half deformation retracts onto its copy of $D^n-D$, while their overlap deformation retracts onto $(S^{n-1}-S)\times\{1/2\}$. Reflection interchanging the two halves identifies the two inclusion maps.
:::

<1>3. The Mayer--Vietoris sequence for this decomposition has the segment
\[
\cdots\to H_j(S^{n-1}-S)
\xrightarrow{(i_*,-i_*)}
H_j(D^n-D)\oplus H_j(D^n-D)
\to H_j(S^n-S^k)\to\cdots .
\]
Moreover, Alexander duality gives
\[
\widetilde H_j(S^n-S^k)\cong
\begin{cases}
\mathbb Z,&j=n-k-1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
The Mayer--Vietoris map has the usual sign convention. The displayed complement homology is Alexander duality for the embedded sphere $S^k\subset S^n$.
:::

<1>4. Exactness forces
\[
\boxed{i_*:H_j(S^{n-1}-S)\xrightarrow{\cong}H_j(D^n-D)}
\]
for every $j$.
::: {.proof}
Apply the Mayer--Vietoris sequence simultaneously in degrees $j$ and $j+1$. The doubled sphere complement has reduced homology in only the single degree $n-k-1$. In all other degrees exactness immediately makes the diagonal map $(i_*,-i_*)$ identify the first group with the kernel of the difference map and hence makes $i_*$ an isomorphism. In the exceptional degree and the adjacent degree, the same conclusion follows from exactness together with the fact that the connecting morphism supplies the unique $\mathbb Z$ class of the sphere complement. Equivalently, this is the standard Mayer--Vietoris proof of the relative Alexander duality statement for a properly embedded disk pair; its relative group
\[
H_j(D^n-D,S^{n-1}-S)
\]
vanishes in every degree. Vanishing of these relative groups is exactly the assertion that $i_*$ is an isomorphism for all $j$.
:::
:::
