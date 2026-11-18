---
schema: qual/card@1
id: E-MUN-10-8
kind: problem
title: Well-ordering unions of disjoint well-ordered sets
classification:
  areas:
  - topology
  topics:
  - Well-Ordered Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §10 Exercise 8, printed p. 67; (a) and (b) are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.8, printed pp.
    112-113. (a) is his, including the two cases for the smallest element of a subset of the
    union; (b) is his generalisation to a family indexed by a well-ordered set, with the
    least index occurring and the least element of its fibre. Whitman skips the check that
    the defined relation is an order on the union, which well-ordering presupposes under the
    definition of §10; the card supplies that check for both parts, together with his
    closing remark that (a) is the addition of ordinal numbers.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 10.8, printed
    pp. 112-113. Checked against Munkres §10 Exercise 8, whose number is read from the collection
    index. The card keeps, and now places in its own step, the verification that the relation is a
    strict simple order, which the earlier prose said Whitman omits: irreflexivity, comparability
    and transitivity are each checked against the three clauses, including the case that cannot
    occur. The well-ordering steps take the least element of the first part meeting B, or of the
    least index whose part meets B, and compare against every element of B. Not claimed: any
    statement about order type or about sums of order types, which the exercise does not ask.
---

::: {.exercise}

(a) Let $A_{1}$ and $A_{2}$ be disjoint sets, well-ordered by $<_{1}$ and $<_{2}$, respectively.
Define an order relation on $A_{1} \cup A_{2}$ by letting $a < b$ either if $a, b \in A_{1}$ and $a <_{1} b$, or if $a, b \in A_{2}$ and $a <_{2} b$, or if $a \in A_{1}$ and $b \in A_{2}$. Show that this is a **well-ordering**.

(b) Generalize (a) to an arbitrary family of pairwise disjoint well-ordered sets $\{A_\alpha\}_{\alpha \in J}$, indexed by a well-ordered set $J$.
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.8, printed pp. 112--113 (`tmp/sources/munkres-solutions-whitman.pdf`); the rest is his, and the verification that the relation is an order on the union, which well-ordering presupposes, is supplied here. It is checked against Munkres, Topology (2000), §10 Exercise 8.

::: pf

::: {.pf-step #parta}
Let $A=A_{1}\sqcup A_{2}$ and define $a<b$ iff ($a,b\in A_{1}$ and $a<_{1}b$) or ($a,b\in A_{2}$ and $a<_{2}b$) or ($a\in A_{1}$, $b\in A_{2}$). This is a well-ordering.

:::: pf-proof

::: {.pf-step #order}
The relation is a strict simple order: irreflexive, transitive, comparable.

::: pf-proof
Irreflexive: no clause has $a=b$ within one part, since $<_{1},<_{2}$ are strict, and no clause puts an element of $A_{2}$ below one of $A_{1}$. Comparable: for $a\ne b$, if both lie in $A_{1}$ use $<_{1}$, if both in $A_{2}$ use $<_{2}$, if $a\in A_{1}$ and $b\in A_{2}$ then $a<b$, and if $a\in A_{2}$ and $b\in A_{1}$ then $b<a$. Transitive: if $a<b$ then either $a,b\in A_{1}$, or $a\in A_{1}$ and $b\in A_{2}$, or $a,b\in A_{2}$. In the first case $b<c$ gives either $c\in A_{1}$ with $b<_{1}c$, whence $a<_{1}c$ and $a<c$, or $c\in A_{2}$, whence $a\in A_{1}$, $c\in A_{2}$ and $a<c$. In the second case $b<c$ forces $b,c\in A_{2}$, so $a\in A_{1}$, $c\in A_{2}$ and $a<c$. The third case with $c\in A_{1}$ cannot occur, because no clause has $b\in A_{2}$ and $c\in A_{1}$; the remaining subcase $a,b,c\in A_{2}$ uses $<_{2}$.
:::

:::

::: {.pf-step #wellorder}
Every nonempty $B\subseteq A$ has a smallest element.

::: pf-proof
If $B\cap A_{1}\ne\varnothing$ then $B\cap A_{1}$ is a nonempty subset of $A_{1}$ and has a smallest element $a$ in $<_{1}$. For $x\in B$: if $x\in A_{1}$ then $a\le_{1}x$ because $x\in B\cap A_{1}$, so $a\le x$; if $x\in A_{2}$ then $a<x$ by the third clause. If $B\cap A_{1}=\varnothing$ then $B\subseteq A_{2}$ is nonempty and has a smallest element in $<_{2}$, which is least in $B$.
:::

:::

:::

:::

::: {.pf-step #partb}
Let $J$ be well ordered by $<_{J}$, let $\{A_{\alpha}\}_{\alpha\in J}$ be pairwise disjoint with $A_{\alpha}$ well ordered by $<_{\alpha}$, let $A=\bigcup_{\alpha}A_{\alpha}$, and define $x<y$ iff ($x,y\in A_{\alpha}$ and $x<_{\alpha}y$ for some $\alpha$) or ($x\in A_{\alpha}$, $y\in A_{\beta}$, $\alpha<_{J}\beta$). This is a well-ordering.

:::: pf-proof

::: {.pf-step #bfamily}
Each element of $A$ lies in a unique $A_{\alpha}$, and the relation is a strict simple order.

::: pf-proof
Uniqueness of $\alpha$ is pairwise disjointness. Irreflexivity: $x<y$ forces $x\ne y$, since the first alternative uses a strict order and the second separates the parts. Comparability: for $x\in A_{\alpha}$, $y\in A_{\beta}$ with $x\ne y$, either $\alpha=\beta$ and $x<_{\alpha}y$ or $y<_{\alpha}x$, or $\alpha\ne\beta$ and $\alpha<_{J}\beta$ or $\beta<_{J}\alpha$. Transitivity: for $x\in A_{\alpha}$, $y\in A_{\beta}$, $z\in A_{\gamma}$ with $x<y<z$ one has $\alpha\le_{J}\beta\le_{J}\gamma$; if $\alpha=\gamma$ then $\alpha=\beta$ and $x<_{\alpha}y<_{\alpha}z$ gives $x<z$, and otherwise $\alpha<_{J}\gamma$ gives $x<z$.
:::

:::

::: {.pf-step #bwellorder}
Every nonempty $B\subseteq A$ has a smallest element.

::: pf-proof
Let $I=\{\alpha\in J:B\cap A_{\alpha}\ne\varnothing\}$, which is nonempty because $B$ is, and let $\alpha$ be its least element under $<_{J}$. Then $B\cap A_{\alpha}$ is a nonempty subset of $A_{\alpha}$, with least element $a$ in $<_{\alpha}$. For $x\in B\cap A_{\beta}$: if $\beta=\alpha$ then $a\le_{\alpha}x$; if $\beta\ne\alpha$ then $\beta\in I$ and $\alpha<_{J}\beta$ by minimality of $\alpha$, so $a<x$. Hence $a$ is least in $B$.
:::

:::

:::

:::

::: {.pf-step}
Part (a) and its generalization (b) hold.

::: pf-proof
Steps [](#order){.pf-ref} and [](#wellorder){.pf-ref} prove (a), and steps [](#bfamily){.pf-ref} and [](#bwellorder){.pf-ref} prove (b):
$$
\boxed{\text{the ordered union of disjoint well-ordered sets is well ordered, for two summands and for a well-ordered family}.}
$$
In (b) the index set must itself be well ordered, and in (a) it is the two-element set $\{1<2\}$, which is the case $J=2$ of (b).
:::

:::

:::
:::
