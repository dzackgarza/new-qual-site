---
schema: qual/card@1
id: FF-HRUA3
kind: fact
title: Nowhere dense sets
prompts:
- What does it mean for a set to be nowhere dense?
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Closure
relations: []
review: draft
---

::: {.fact}
Let $X$ be a topological space and $A\subseteq X$.
The following are equivalent:

- $A$ is [[D-2MJRE|nowhere dense]] in $X$, that is, $\qty{\overline{A}}^\circ = \emptyset$;

- every nonempty open set $U\subseteq X$ contains a nonempty open set $V$ with $V\cap A = \emptyset$;

- $A$ is not [[FD-BA2WU|dense]] in any nonempty open subset of $X$.

For $X = \RR$, $A$ is nowhere dense if and only if every open interval $I$ contains an open interval $S\subseteq I$ with $S\cap A = \emptyset$, that is, $\overline{A}$ contains no open interval.
:::
