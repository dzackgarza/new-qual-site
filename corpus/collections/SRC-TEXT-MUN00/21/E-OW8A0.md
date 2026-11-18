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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked that the restriction is a metric, that every
    subspace basis element around a point contains a d'-ball around it (with delta = epsilon
    - d(x,a)), and that every d'-ball is the trace of a d-ball, so the two topologies
    coincide. positron0802, Exercise 21.1, PDF p. 23. The printed statement needed no
    repair.
---

::: {.exercise}

Let $A \subset X$.
If $d$ is a metric for the topology of $X$, show that $d \mid A \times A$ is a metric for the subspace topology on $A$.
:::

::: {.solution}
The published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.1, PDF p. 23** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs, with the metric axioms for the restriction stated separately below.

Let $A\subset X$ and $d'=d\restrict_{A\times A}$, and write $A_{s}$ for $A$ with the subspace topology and $A_{d'}$ for $A$ with the topology induced by $d'$.

::: pf

::: {.pf-step #metric}
$d'$ is a metric on $A$.

::: pf-proof
For $a,b,c\in A$: $d'(a,b)=d(a,b)\ge0$; $d'(a,b)=0$ exactly when $a=b$; $d'(a,b)=d(b,a)$; and $d'(a,b)=d(a,b)\le d(a,c)+d(c,b)=d'(a,c)+d'(c,b)$. These are the metric axioms for $d$ restricted to the pairs from $A$.
:::

:::

::: {.pf-step #finer}
$A_{d'}$ is finer than $A_{s}$.

::: pf-proof
A basis element of the subspace topology containing $a\in A$ is $U=B_{d}(x,\varepsilon)\cap A$ with $x\in X$, $\varepsilon>0$ and $a\in U$; put $\delta=\varepsilon-d(x,a)>0$. Then
$$
a\in B_{d'}(a,\delta)=\{b\in A\mid d(a,b)<\delta\}\subset U,
$$
because $d(a,b)<\delta$ gives $d(x,b)\le d(x,a)+d(a,b)<\varepsilon$ and $b\in A$. So every subspace neighbourhood of $a$ contains a $d'$-ball around $a$, and $A_{d'}$ is finer.
:::

:::

::: {.pf-step #coarser}
$A_{s}$ is finer than $A_{d'}$.

::: pf-proof
A basis element of $A_{d'}$ is
$$
B_{d'}(a,\varepsilon)=\{b\in A\mid d(a,b)<\varepsilon\}=B_{d}(a,\varepsilon)\cap A,
$$
the trace on $A$ of the open ball $B_{d}(a,\varepsilon)$ of $X$, which is open in $X$; so it is open in the subspace topology.
:::

:::

::: {.pf-step}
$d\restrict_{A\times A}$ is a metric for the subspace topology on $A$.

::: pf-proof
Steps [](#finer){.pf-ref} and [](#coarser){.pf-ref} show that each of the two topologies is finer than the other, hence that they are equal, and step [](#metric){.pf-ref} shows that $d'$ is a metric.
:::

:::

:::
:::
