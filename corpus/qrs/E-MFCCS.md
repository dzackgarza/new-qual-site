---
schema: qual/card@1
id: E-MFCCS
kind: exercise
title: "Show that any disjoint intervals is countable."
classification:
  areas:
  - real-analysis
  topics:
  - countability
  - euclidean-spaces
relations: []
review: draft
solved: true
---

::: exercise
- Show that any disjoint intervals is countable.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. A family $\mathcal I$ of pairwise disjoint intervals in $\RR$, each with nonempty interior, is at most countable.
<2>1. Each $I \in \mathcal I$ contains a rational number $q_I$.
Proof: an interval with nonempty interior contains an open subinterval, and $\QQ$ is dense in $\RR$.
<2>2. The assignment $I \mapsto q_I$ is injective.
Proof: if $I \neq J$ are disjoint, then $I \cap J = \emptyset$, so the chosen rationals cannot coincide.
<2>3. Q.E.D. Proof: <2>1 and <2>2 embed $\mathcal I$ injectively into the countable set $\QQ$.

<1>2. The hypothesis of nonempty interior is necessary: the statement is false for arbitrary intervals.
<2>1. Every singleton $\{x\}$ is an interval.
Proof: $[x,x]$ satisfies the interval condition.
<2>2. The family $\{\{x\} : x \in \RR\}$ is pairwise disjoint and uncountable.
Proof: distinct singletons are disjoint, and there are $|\RR|$ of them.
<2>3. Q.E.D. Proof: <2>1 and <2>2 give a family of pairwise disjoint intervals that is not countable.

<1>3. Q.E.D. Proof: <1>1 proves the intended statement (intervals with nonempty interior, in particular open intervals); <1>2 records the necessary hypothesis.
:::
