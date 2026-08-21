---
schema: qual/card@1
id: P-KXSW3
kind: problem
title: A subgroup of a finite $p$-group generating $H/[H,H]$ equals $H$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Commutators
  - Subgroups
relations: []
review: draft
solved: false
---

::: problem
- Let $G\leq H$ where $H$ is a finite $p\dash$group, and suppose $\phi: G\to H / [H, H]$ be defined by composing the inclusion $G\injects H$ with the natural quotient map $H \to H/[H, H]$.

  Prove that $G= H$ by induction on $\size H$ in the following way:

  - Letting $N\normal H$ be any nontrivial normal subgroup of $H$, use the inductive hypothesis to show that $H = GN$.

  - Let $Z = Z(H)$ be the center of $H$.
    Using that $GZ = H$ by (1), show that $G \intersect Z \neq \emptyset$.
    Set $N \da G \intersect Z$ and apply (1) to conclude.
:::
