---
schema: qual/card@1
id: E-GO24I
kind: problem
title: The rationals are not locally compact
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
    Read against Munkres, Topology (2000), §29 Exercise 1, printed p. 186, with the
    definition of local compactness printed there.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 29.1, PDF p. 21. No rational interval with
    irrational endpoints is compact, by the increasing-union cover; and a compact
    neighbourhood of a rational point would contain such an interval as a closed subset.
    (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Show that the rationals $\QQ$ are not locally compact.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 29.1, PDF p. 21** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the argument is theirs.

First, if $a<b$ are irrational then $\QQ\cap[a,b]$ is not compact: it is countable, say $\{q_{1},q_{2},\dots\}$, and the sets $U_{i}=\QQ\cap[a,q_{i})$ form an open cover of it in which no finite subcollection covers, since $q_{i}\in U_{j}$ only for $j>i$.

Now let $x\in\QQ$ and suppose $\QQ$ locally compact at $x$; then some compact $C\subset\QQ$ contains a neighbourhood $U$ of $x$. Being a neighbourhood in $\QQ$, $U$ contains a set $\QQ\cap[a,b]$ with $a<b$ irrational. That set is closed in $\QQ$ and contained in the compact $C$, hence compact — contradicting the first paragraph. So $\QQ$ is not locally compact.
:::
