---
schema: qual/card@1
id: E-20CHL
kind: problem
title: Continuity implies separate continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 11, printed p. 112; the definition
    of continuity in each variable separately is stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.11, PDF p. 13. Each slice map is the composite
    of F with an imbedding x -> x x y_0 (Exercise 18.4), hence continuous.
    (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $F: X \times Y \to Z$.
We say that $F$ is continuous in each variable separately if for each $y_0$ in $Y$, the map $h: X \to Z$ defined by $h(x) = F(x \times y_0)$ is continuous, and for each $x_0$ in $X$, the map $k: Y \to Z$ defined by $k(y) = F(x_0 \times y)$ is continuous.
Show that if $F$ is continuous, then $F$ is continuous in each variable separately.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.11, PDF p. 13** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the composition argument is theirs. Whitman, printed p. 188, proves the same by chasing a neighbourhood through a product basis element.

Fix $y_{0}\in Y$. By Exercise 18.4 the map $j:X\to X\times Y$, $j(x)=x\times y_{0}$, is an imbedding, in particular continuous. The map $h:X\to Z$ of the exercise is $h=F\circ j$, a composite of continuous maps, hence continuous. So $F$ is continuous in its first variable.

Fix $x_{0}\in X$. The same argument with $k(y)=F(x_{0}\times y)=F\circ j'$ for the imbedding $j'(y)=x_{0}\times y$ shows that $F$ is continuous in its second variable.

Hence a continuous $F$ is continuous in each variable separately; the converse fails, by Exercise 18.12.
:::
