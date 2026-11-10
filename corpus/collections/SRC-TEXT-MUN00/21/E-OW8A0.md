---
schema: qual/card@1
id: E-OW8A0
kind: problem
title: The subspace metric
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 1, printed p. 133, with the subspace
    topology and the definition of a metric for a topology; the stored statement is the
    printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.1, PDF p. 23. The subspace topology and the
    metric topology of the restricted metric contain each other: a metric ball of a subspace
    point inside a trace is a restricted ball, and every restricted ball is a trace of a
    ball of the big space. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $A \subset X$.
If $d$ is a metric for the topology of $X$, show that $d \mid A \times A$ is a metric for the subspace topology on $A$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.1, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs.

Let $A\subset X$ and $d'=d\restrict_{A\times A}$, clearly a metric on $A$. Write $A_{s}$ for $A$ with the subspace topology and $A_{d'}$ for $A$ with the metric topology of $d'$.

$A_{d'}$ is finer than $A_{s}$: a subspace basis element is $U=B_{d}(x,\varepsilon)\cap A$ with $a\in U$; then $\delta=\varepsilon-d(x,a)>0$ and
$$
a\in B_{d'}(a,\delta)=\{b\in A\mid d(a,b)<\varepsilon\}\subset U,
$$
because $d(a,b)<\delta$ gives $d(x,b)\le d(x,a)+d(a,b)<\varepsilon$.

$A_{s}$ is finer than $A_{d'}$: a metric basis element of $A_{d'}$ is
$$
B_{d'}(a,\varepsilon)=\{b\in A\mid d(a,b)<\varepsilon\}=B_{d}(a,\varepsilon)\cap A,
$$
the trace on $A$ of an open ball of $X$, hence open in the subspace topology.

So the two topologies coincide: $d\restrict_{A\times A}$ is a metric for the subspace topology.
:::
