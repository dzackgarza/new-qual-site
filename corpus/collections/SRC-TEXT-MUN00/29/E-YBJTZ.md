---
schema: qual/card@1
id: E-YBJTZ
kind: problem
title: The one-point compactification of R is the circle
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §29 Exercise 6, printed p. 186, with Theorem 29.1
    on printed p. 183; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.6, PDF p. 22. The line is identified with the
    circle minus one point: t -> (cos 2 pi t, sin 2 pi t) on (-1/2, 1/2) omits (-1,0); the
    circle is then the one-point compactification of the line, unique by Theorem 29.1. The
    aside on this card previously named the omitted point as (1,0) and cited Exercise 29.5
    for uniqueness; both are corrected. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the one-point compactification of $\RR$ is homeomorphic with the circle $S^1$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.6, PDF p. 22** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the map is theirs, with one slip in this card's earlier aside corrected: on the open interval $(-1/2,1/2)$ the map $t\mapsto(\cos 2\pi t,\sin 2\pi t)$ omits $(-1,0)$, not $(1,0)$.

The line is locally compact and Hausdorff. Let $q:\RR\to S^{1}$, $q(t)=(\cos 2\pi t,\ \sin 2\pi t)$, a continuous map; restricted to the open interval $(-\tfrac12,\tfrac12)$ it is injective, and its image is
$$
S^{1}-\{(-1,0)\},
$$
since $q(\pm\tfrac12)=(-1,0)$ and the map is injective on $[-\tfrac12,\tfrac12]$ up to that identification: so $\RR\cong S^{1}-\{(-1,0)\}$, densely contained in the compact Hausdorff space $S^{1}$ whose complement is the single point $(-1,0)$.

By Theorem 29.1 (printed p. 183) a locally compact Hausdorff space has a one-point compactification, unique up to a homeomorphism that is the identity on the space; $S^{1}$ is such a compactification of $\RR$, so $\RR^{+}\cong S^{1}$.
:::
