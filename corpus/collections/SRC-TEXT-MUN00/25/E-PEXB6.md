---
schema: qual/card@1
id: E-PEXB6
kind: problem
title: A rational fan and a nowhere locally connected path-connected set
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
    Read against Munkres, Topology (2000), §25 Exercise 5, printed p. 162; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.5, PDF p. 9. The fan is a union of segments
    through p, hence path connected and locally connected only at p; adjoining a second fan
    at another point gives a path-connected set locally connected nowhere.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $X$ denote the rational points of the interval $[0, 1] \times 0$ of $\RR^2$.
Let $T$ denote the union of all line segments joining the point $p = 0 \times 1$ to points of $X$.

(a) Show that $T$ is path connected, but is locally connected only at the point $p$.

(b) Find a subset of $\RR^2$ that is path connected but is locally connected at none of its points.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.5, PDF p. 9** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both parts are theirs.

(a) $T=\bigcup_{x\in X}\overline{px}$ is a union of path-connected segments with the common point $p$, hence path connected (Exercise 24.8(d)). It is not locally connected at any $q\in T-\{p\}$: such a $q$ lies on one segment and is a limit point of the others, so every sufficiently small neighbourhood of $q$ meets infinitely many distinct segments and has infinitely many components. At $p$ the space is locally connected, since the segments are the components of small neighbourhoods and each is connected with $p$.

(b) Let $Y=\QQ\cap([0,1]\times\{1\})$ and let $R$ be the union of the segments joining $1\times0$ to the points of $Y$. Then $R$ is path connected, so $R\cup T$ is path connected because $1\times0\in R\cap T$; but at every point, including $p$ and $1\times0$, small neighbourhoods meet infinitely many of the segments and are disconnected, so $R\cup T$ is locally connected at none of its points.
:::
