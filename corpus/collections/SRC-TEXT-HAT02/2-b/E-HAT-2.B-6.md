---
schema: qual/card@1
id: E-HAT-2.B-6
kind: problem
title: "Alexander horned sphere with non-simply-connected complement"
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
  note: Checked against Hatcher, Algebraic Topology, Section 2.B, Exercise 6; the stored statement matches and the construction was compared with Hatcher's preceding Alexander-horned-sphere example.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the local van Kampen injections and the free-group bonding maps for the horned constructions.
---

::: {.problem}
Modify the construction of the Alexander horned sphere to produce an embedding $S^2 \hookrightarrow \mathbb{R}^3$ for which neither component of $\mathbb{R}^3 - S^2$ is simply-connected.
:::

::: {.solution}
The standard Alexander construction can be localized in a small $3$-ball meeting an otherwise tame sphere in a disk. We use two disjoint such balls, one on each side of the sphere.

<1>1. Start with a round sphere $S_0\subset\mathbb R^3$ and choose two disjoint closed disks
\[
D_+,D_-\subset S_0.
\]
Choose disjoint small $3$-balls $N_+,N_-$ with
\[
N_\pm\cap S_0=D_\pm,
\]
where $N_+$ lies mainly on the exterior side of $S_0$ and $N_-$ mainly on the interior side.
::: {.proof}
Take two small disjoint coordinate balls centered at distinct points of the sphere and shrink them so that each meets the sphere in a single tame disk.
:::

<1>2. Inside $N_+$ replace the disk $D_+$ by a localized Alexander horned disk whose horns accumulate from the exterior side. Inside $N_-$ make the mirror-image replacement, with horns accumulating from the interior side. Leave the sphere unchanged outside $D_+\cup D_-$.
::: {.proof}
Delete from the standard Alexander horned sphere a small tame disk disjoint from the horn accumulation set. The remainder is a disk with the same wild horn structure, embedded in a $3$-ball and agreeing with a standard disk near its boundary. This is the required localized horned disk. Reflecting the construction interchanges its two sides.
:::

<1>3. The resulting surface $S$ is homeomorphic to $S^2$.
::: {.proof}
Each replacement is a topological disk attached along the same boundary circle as the disk it replaces, and it agrees with the old disk in a collar of that boundary. Thus replacing $D_+$ and $D_-$ does not change the abstract surface: we have removed two disks from $S^2$ and glued back two disks along their boundary circles. Hence the result is again $S^2$.
:::

<1>4. The exterior component of $\mathbb R^3-S$ is not simply-connected.
::: {.proof}
Inside $N_+$ the exterior-side complement contains exactly the localized complement used in Hatcher's Alexander-horned-sphere argument. Let $\alpha_+$ be a meridian loop linking the first-stage handle. Hatcher's van Kampen calculation identifies the successive stage groups with free groups and sends each old meridian injectively to a commutator of two new meridians. Hence $\alpha_+$ is nontrivial in the local exterior complement.

Choose $N_+$ so that its intersection with the rest of the exterior component is a collar of a disk, hence simply-connected. Van Kampen then expresses the fundamental group of the full exterior as a free product with the local exterior group as a factor. In particular the inclusion of the local exterior complement is injective on $\pi_1$, so $[\alpha_+]$ remains nontrivial globally.
:::

<1>5. The bounded component of $\mathbb R^3-S$ is also not simply-connected.
::: {.proof}
Apply the same argument to the reflected horned disk in $N_-$. A meridian $\alpha_-$ linking its first-stage inward handle is nontrivial in the local interior complement by the identical free-group/commutator calculation. The local piece meets the rest of the bounded component through a simply-connected collar, so van Kampen again makes the local fundamental group inject into the global one. Thus $[\alpha_-]\ne1$.
:::

Therefore
\[
\boxed{\text{neither component of }\mathbb R^3-S\text{ is simply-connected}.}
\]
:::
