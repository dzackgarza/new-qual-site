---
schema: qual/card@1
id: E-RZLC7
kind: problem
title: Connected metric spaces with more than one point are uncountable
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §27 Exercise 4, printed p. 178, with Exercise
    20.3(a); the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 27.4, PDF p. 17. The continuous function z -> d(x,
    z) has connected image in R containing 0 and a positive value, hence uncountably many
    values. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed and the citations are by number
    --- §27 Exercise 4, §20 Exercise 3(a), §18 Exercise 4 and Theorem 24.3, each read in
    `tmp/sources/munkres-2000-topology.md`, and positron0802's Exercise 27.4 by its number. The
    earlier events keep their text (QUAL-11); these numbered citations supersede their page
    locators. No step changes.

---

::: {.exercise}

Show that a connected metric space having more than one point is uncountable.
:::

::: {.solution}

The argument is **"positron0802"**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 27.4 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the step from connectedness of the image to the containment $[0,\delta]\subset d_{x}(X)$ is here replaced by the intermediate value theorem. The statement was checked against Munkres, *Topology* (2000), §27 Exercise 4, with §20 Exercise 3(a) and the intermediate value theorem, Theorem 24.3.

::: pf

::: {.pf-step #distance-continuous}
For fixed $x\in X$ the map $d_{x}\colon X\to\RR$, $d_{x}(z)\coloneqq d(x,z)$ is continuous.

::: pf-proof
The metric $d\colon X\times X\to\RR$ is continuous by §20 Exercise 3(a). The map $z\mapsto x\times z$ is an imbedding of $X$ into $X\times X$ (§18 Exercise 4), hence continuous, so the composite $d_{x}=d\circ(z\mapsto x\times z)$ is continuous.
:::

:::

::: {.pf-step #interval-in-image}
For $x\neq y$ in $X$ and $\delta\coloneqq d(x,y)>0$ one has $[0,\delta]\subset d_{x}(X)$.

::: pf-proof
$d_{x}(x)=d(x,x)=0$ and $d_{x}(y)=\delta$, and $X$ is connected; so for each $t$ with $0\leq t\leq\delta$ the intermediate value theorem (Theorem 24.3) applied to the continuous map $d_{x}\colon X\to\RR$ and the points $x,y$ gives a point $z\in X$ with $d_{x}(z)=t$. Note $\delta>0$ because $d$ is a metric and $x\neq y$.
:::

:::

::: pf-step
Therefore $X$ is uncountable.

::: pf-proof
Suppose $X$ has at least two points $x\neq y$. By step [](#interval-in-image){.pf-ref} the image of $d_{x}$ contains $[0,\delta]$ with $\delta>0$, an uncountable set; a map onto an uncountable set has uncountable domain, so $X$ is uncountable.
:::

:::

:::

:::
