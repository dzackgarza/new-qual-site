---
schema: qual/card@1
id: E-T7M5R
kind: problem
title: The identity component of a topological group is normal
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 9, printed p. 162, with
    Supplementary Exercise TG.4 and the hint; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.9, PDF p. 10. Translations are homeomorphisms,
    so xC and Cx are both the component of x and hence equal, which is normality.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $G$ be a topological group; let $C$ be the component of $G$ containing the identity element $e$.
Show that $C$ is a normal subgroup of $G$.
[Hint: If $x \in G$, then $xC$ is the component of $G$ containing $x$.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.9, PDF p. 10** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

Let $G$ be a topological group, $e$ its identity and $C$ the component of $e$. For $x\in G$ the left translation $y\mapsto xy$ is a homeomorphism (Exercise TG.4), so $xC$ is the component of $x$; likewise $Cx$ is the component of $x$. Hence $xC=Cx$ for every $x$, that is, $C$ is normal. (It is a subgroup by Exercise TG.3 and contains $e$.)
:::
