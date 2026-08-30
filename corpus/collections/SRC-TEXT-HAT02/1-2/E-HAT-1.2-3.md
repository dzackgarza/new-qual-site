---
schema: qual/card@1
id: E-HAT-1.2-3
kind: exercise
title: Complement of a finite set of points in $\mathbb{R}^n$ is simply-connected for $n \geq 3$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
  - Simply Connected
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

Show that the complement of a finite set of points in $\mathbb{R}^n$ is simply-connected if $n \geq 3$.

::: {.solution}
**Goal.** Show $\RR^n \sm \theset{p_1, \dots, p_k}$ is simply connected for $n \ge 3$.

<1>1. $\RR^n \sm \theset{p_1, \dots, p_k}$ is path-connected for $n \ge 2$.
Proof: any two points can be joined by a path avoiding the finitely many removed points (there is plenty of room in dimension $\ge 2$).

<1>2. It suffices to show $\pi_1(\RR^n \sm \theset{p_1, \dots, p_k}) = 0$.
Proof: simply connected means path-connected and trivial fundamental group.

<1>3. $\RR^n \sm \theset{p_1, \dots, p_k}$ deformation-retracts onto a wedge of $k$ copies of $S^{n-1}$.
Proof: place small disjoint $(n-1)$-spheres around each removed point; the complement deformation-retracts onto the wedge of these spheres (for $n \ge 2$).

<1>4. $\pi_1\qty(\bigvee_{i=1}^k S^{n-1}) = 0$ for $n - 1 \ge 2$.
Proof: $\pi_1(S^{n-1}) = 0$ for $n - 1 \ge 2$, and the fundamental group of a wedge is the free product of the fundamental groups, so $\pi_1 = \ast_{i=1}^k \pi_1(S^{n-1}) = 0$.

<1>5. Hence $\pi_1(\RR^n \sm \theset{p_1, \dots, p_k}) = 0$.
Proof: <1>3 and <1>4 (homotopy invariance of $\pi_1$).

<1>6. Q.E.D. Proof: <1>1 and <1>5 show the complement is simply connected.
:::
