---
schema: qual/card@1
id: E-0S3OA
kind: problem
title: Subgroups and closures of subgroups are topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 3, printed p. 146,
    with Exercise 17.9 and Theorem 18.1; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.3, printed p. 264.
    His argument: the closure of a subgroup is a subgroup, because f(H x H) lies in H for
    the continuous f(x,y) = x y^{-1} and f(closure H x closure H) lies in the closure of f(H
    x H); both H and its closure are subspaces of a T1 space and the operations are
    restrictions of continuous ones. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Let $H$ be a subspace of the topological group $G$.
Show that if $H$ is also a subgroup of $G$, then both $H$ and $\overline{H}$ are topological groups.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.3, printed p. 264** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his.

Let $H$ be a subspace of the topological group $G$ and a subgroup. Both $H$ and $\overline H$ are $T_{1}$, being subspaces of the $T_{1}$ space $G$.

*$\overline{H}$ is a subgroup.* By the criterion: $\overline H$ is a subgroup of $G$ if $x\cdot y^{-1}\in\overline H$ whenever $x,y\in\overline H$. Let $f:G\times G\to G$, $f(x,y)=x\cdot y^{-1}$, which is continuous (Exercise TG.1). Then
$$
f\big(\overline{H}\times\overline{H}\big)\subset\overline{f(H\times H)}\subset\overline{H},
$$
the first inclusion because $f$ is continuous and $\overline{A\times B}=\overline A\times\overline B$ (Exercise 17.9) with $\overline{H\times H}=\overline H\times\overline H$, the second because $H$ is a subgroup so $f(H\times H)\subset H$. Hence $\overline H$ is a subgroup.

*$H$ is a subgroup* by hypothesis, and $\overline H$ is one by the above. The multiplication of $H$ (respectively $\overline H$) is the restriction of the continuous multiplication of $G$ to $H\times H$ (respectively $\overline H\times\overline H$), hence continuous by Theorem 18.2(d); similarly the inversion is the restriction of the continuous inversion of $G$. So both are topological groups.
:::
