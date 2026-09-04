---
schema: qual/card@1
id: P-MXUIS
kind: problem
title: Fundamental group and classification of a sphere with $k$ Möbius bands attached
classification:
  areas:
  - topology
  topics:
  - van Kampen
  - Fundamental Group
  - Surfaces
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 3 of the official UGA Fall 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the boundary-loop presentation of the punctured sphere, the degree-two boundary inclusion of each Mobius band, the van Kampen elimination, and the nonorientable-surface classification.
---

::: problem
Let $S_k$ be the space obtained by removing $k$ disjoint open disks from the sphere $S^2$.
Form $X_k$ by gluing $k$ Möbius bands onto $S_k$ , one for each circle boundary component of $S_k$ (by identifying the boundary circle of a Möbius band homeomorphically with a given boundary component circle).

Use van Kampen's theorem to calculate $\pi_1 (X_k)$ for each $k > 0$ and identify $X_k$ in terms of the classification of surfaces.
:::

::: {.solution}
Fix $k\ge1$ and a basepoint in $S_k$.
For each boundary component choose an arc from the basepoint to that component, and let $c_i$ denote the resulting based boundary loop.

<1>1. The punctured sphere has presentation
\[
\pi_1(S_k)
\cong
\left\langle c_1,\dots,c_k
\mathrel{\Big|}
c_1c_2\cdots c_k=1
\right\rangle.
\]
In particular, $\pi_1(S_k)$ is free of rank $k-1$.
::: {.proof}
Cut $S_k$ along the chosen arcs joining the basepoint to the boundary circles.
The result is a disk, whose oriented boundary reads
\[
c_1c_2\cdots c_k
\]
after the paired arc segments cancel.
Equivalently, a standard van Kampen decomposition gives one generator for each boundary loop and the single relation that their product is trivial.
Eliminating $c_k$ leaves a free group on $c_1,\dots,c_{k-1}$.
:::

<1>2. Let $M_i$ be the Möbius band glued to the $i$th boundary component, and let $x_i$ be its core loop.
Then
\[
\pi_1(M_i)=\langle x_i\rangle\cong\ZZ,
\]
and the boundary circle of $M_i$ represents $x_i^2$, up to replacing $x_i$ by $x_i^{-1}$.
::: {.proof}
A Möbius band deformation retracts onto its core circle, so its fundamental group is infinite cyclic.
In the usual rectangle model
\[
M=[0,1]\times[-1,1]/(0,t)\sim(1,-t),
\]
one circuit around the boundary passes twice around the core before closing.
Thus the homomorphism induced by the boundary inclusion is multiplication by $2$ on $\pi_1\cong\ZZ$.

The attaching homeomorphism of the boundary circle may reverse the chosen orientation, changing $x_i^2$ to $x_i^{-2}$.
Replacing $x_i$ by its inverse removes this sign, so we may write the attaching relation as
\[
c_i=x_i^2.
\]
:::

<1>3. Van Kampen's theorem gives
\[
\pi_1(X_k)
\cong
\left\langle
c_1,\dots,c_k,x_1,\dots,x_k
\mathrel{\Big|}
c_1\cdots c_k=1,\ c_i=x_i^2\ (1\le i\le k)
\right\rangle.
\]
::: {.proof}
Attach the Möbius bands one at a time, thickening each gluing circle by collars so that van Kampen applies to open sets.
At the $i$th attachment, the intersection deformation retracts onto the common boundary circle.
By <1>2, its generator maps to $c_i$ on the $S_k$ side and to $x_i^2$ on the Möbius-band side.
Van Kampen therefore adds the generator $x_i$ and the relation $c_i=x_i^2$.
Doing this for all $i$ yields the displayed presentation together with the relation from <1>1.
:::

<1>4. Eliminating the generators $c_i$ gives
\[
\boxed{
\pi_1(X_k)
\cong
\left\langle x_1,\dots,x_k
\mathrel{\Big|}
x_1^2x_2^2\cdots x_k^2=1
\right\rangle.}
\]
::: {.proof}
Substitute $c_i=x_i^2$ from <1>3 into the single relation
\[
c_1c_2\cdots c_k=1.
\]
The generators $c_i$ can then be removed by Tietze transformations, leaving exactly the displayed presentation.
:::

<1>5. The surface $X_k$ is the closed nonorientable surface of genus $k$:
\[
\boxed{X_k\cong N_k=\#^k\mathbb{RP}^2.}
\]
::: {.proof}
All $k$ boundary circles of $S_k$ are filled by Möbius bands, so $X_k$ is a closed connected surface.
It is nonorientable because it contains the core of any attached Möbius band with its Möbius neighborhood.

Moreover,
\[
\chi(S_k)=2-k,
\qquad
\chi(M_i)=0,
\qquad
\chi(S^1)=0.
\]
Euler characteristic is unchanged when a Möbius band is glued along a boundary circle, so
\[
\chi(X_k)=2-k.
\]
By the classification of closed connected surfaces, the unique nonorientable surface with Euler characteristic $2-k$ is the connected sum of $k$ projective planes.
This also agrees with the standard presentation in <1>4.

Thus $X_1\cong\mathbb{RP}^2$, $X_2$ is the Klein bottle, and in general $X_k\cong N_k$.
:::
:::
