---
schema: qual/card@1
id: E-EJN4Q
kind: exercise
title: Open subsets of $\mathbb{R}$ are countable unions of disjoint open intervals
classification:
  areas:
  - real-analysis
  topics:
  - Euclidean Spaces
  - Measure Theory
relations: []
review: draft
solved: true
---

::: exercise
- Show that every open $U \subseteq \RR$ is a countable union of disjoint open intervals.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show every open $U \subseteq \RR$ is a countable union of pairwise disjoint open intervals.

<1>1. The connected components of $U$ are open intervals.
<2>1. Each component $C$ of $U$ is an open interval.
Proof: $C$ is connected in $\RR$ and open in $U$ (components of an open subset of a locally connected space are open), and a nonempty connected subset of $\RR$ is an interval.
Conversely an open interval is connected, so $C$ is exactly an open interval $(a,b)$ with $a,b \in [-\infty, \infty]$.
<2>2. Distinct components are disjoint, and $U$ is their union.
Proof: components are equivalence classes of the relation $x \sim y$ iff $x,y$ lie in a common connected subset of $U$; equivalence classes partition $U$.
<1>2. There are at most countably many components.
Proof: each component is a nonempty open interval and therefore contains a rational $q$; distinct components are disjoint, so the rationals so chosen are distinct; $\QQ$ is countable.
<1>3. Q.E.D. Proof: <1>1 expresses $U$ as a disjoint union of open intervals and <1>2 shows the family is countable.
:::
