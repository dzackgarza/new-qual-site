---
schema: qual/card@1
id: E-O5T9Y
kind: problem
title: The lower limit line is disconnected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 7, printed p. 152, with the lower
    limit topology of §13; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.7, PDF p. 2. The ray (-infinity,0) and the ray
    [0,infinity) are disjoint nonempty open sets of R_l whose union is the space.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Is the space $\RR_\ell$ connected?
Justify your answer.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.7, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the witness pair is theirs.

$\RR_{\ell}$ is **not** connected. The sets $(-\infty,0)$ and $[0,\infty)$ are disjoint, nonempty, and both open in $\RR_{\ell}$ — the first is a union of basis elements $(a,b)$, the second is the basis element $[0,1)$ together with $\bigcup_{n\ge1}[n,n+1)$ — and their union is $\RR$. So they form a separation.
:::
