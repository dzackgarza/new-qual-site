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
---

::: {.exercise}

(a) Let $A_{1}$ and $A_{2}$ be disjoint sets, well-ordered by $<_{1}$ and $<_{2}$, respectively.
Define an order relation on $A_{1} \cup A_{2}$ by letting $a < b$ either if $a, b \in A_{1}$ and $a <_{1} b$, or if $a, b \in A_{2}$ and $a <_{2} b$, or if $a \in A_{1}$ and $b \in A_{2}$. Show that this is a **well-ordering**.

(b) Generalize (a) to an arbitrary family of pairwise disjoint well-ordered sets $\{A_\alpha\}_{\alpha \in J}$, indexed by a well-ordered set $J$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.8, printed pp. 112--113** (`tmp/sources/munkres-solutions-whitman.pdf`). Whitman omits the verification that the relation is an order on the union, which well-ordering presupposes by the definition of §10; that verification is supplied here, and the rest is his.

(a) Let $A=A_{1}\cup A_{2}$ and define $a<b$ iff $a,b\in A_{1}$ and $a<_{1}b$, or $a,b\in A_{2}$ and $a<_{2}b$, or $a\in A_{1}$ and $b\in A_{2}$.

*The relation is a simple order.* Only comparability and transitivity need checking, since no clause allows $a=b$ for $a,b$ in the same part (the orders $<_{1},<_{2}$ are strict) and no clause allows $a\in A_{2}$, $b\in A_{1}$.

For comparability, let $a\ne b$ in $A$. If $a,b\in A_{1}$ then $a<_{1}b$ or $b<_{1}a$; if $a,b\in A_{2}$ then $a<_{2}b$ or $b<_{2}a$; if $a\in A_{1}$, $b\in A_{2}$ then $a<b$; and if $b\in A_{1}$, $a\in A_{2}$ then $b<a$. So $a$ and $b$ are comparable.

For transitivity, let $a<b$ and $b<c$. If $a,b\in A_{1}$ then either $c\in A_{1}$ with $b<_{1}c$, and $a<_{1}c$ gives $a<c$, or $c\in A_{2}$, and $a\in A_{1},c\in A_{2}$ gives $a<c$. If $a\in A_{1}$ and $b\in A_{2}$, then $b<c$ forces $b,c\in A_{2}$ with $b<_{2}c$, so $a\in A_{1}$ and $c\in A_{2}$, giving $a<c$. There is no case $a,b\in A_{2}$ and $c\in A_{1}$, since the definition has no clause with $b\in A_{2}$ and $c\in A_{1}$. So $a<c$ in every case.

*The order is a well-ordering.* Let $B\subset A$ be nonempty. If $B\cap A_{1}\ne\varnothing$, then $B\cap A_{1}$ is a nonempty subset of $A_{1}$ and has a smallest element $a$ in $<_{1}$. For any $x\in B$: if $x\in A_{1}$ then $a\le_{1}x$ because $x\in B\cap A_{1}$, so $a\le x$; if $x\in A_{2}$ then $a<x$ by the third clause. If $B\cap A_{1}=\varnothing$, then $B\subset A_{2}$ is nonempty and has a smallest element $a$ in $<_{2}$, which is the smallest element of $B$. In either case $B$ has a smallest element.

(b) Let $J$ be well ordered by $<_{J}$ and let $\{A_{\alpha}\}_{\alpha\in J}$ be a family of pairwise disjoint sets, $A_{\alpha}$ well ordered by $<_{\alpha}$. Put $A=\bigcup_{\alpha\in J}A_{\alpha}$; each $x\in A$ lies in a unique $A_{\alpha}$. Define $x<y$ iff ($x,y\in A_{\alpha}$ and $x<_{\alpha}y$ for some $\alpha$) or ($x\in A_{\alpha}$, $y\in A_{\beta}$ and $\alpha<_{J}\beta$).

*The relation is a simple order.* Comparability: for $x\ne y$ with $x\in A_{\alpha}$, $y\in A_{\beta}$, either $\alpha=\beta$ and $x<_{\alpha}y$ or $y<_{\alpha}x$, or $\alpha\ne\beta$ and $\alpha<_{J}\beta$ or $\beta<_{J}\alpha$. Transitivity: if $x\in A_{\alpha}$, $y\in A_{\beta}$, $z\in A_{\gamma}$ with $x<y$ and $y<z$, then $\alpha\le_{J}\beta\le_{J}\gamma$; if $\alpha=\gamma$ then $\alpha=\beta$ and $x<_{\alpha}y<_{\alpha}z$ gives $x<z$, and otherwise $\alpha<_{J}\gamma$ gives $x<z$. No element is below itself, since $x<y$ always forces $x\ne y$.

*The order is a well-ordering.* Let $B\subset A$ be nonempty and let
$$
I=\{\alpha\in J\mid B\cap A_{\alpha}\ne\varnothing\}.
$$
Then $I\ne\varnothing$ because $B\ne\varnothing$, so $I$ has a smallest element $\alpha$ in $<_{J}$. Choose $w\in B\cap A_{\alpha}$; then $B\cap A_{\alpha}$ is a nonempty subset of $A_{\alpha}$ and has a smallest element $a$ in $<_{\alpha}$. For any $x\in B$ with $x\in A_{\beta}$: if $\beta=\alpha$ then $a\le_{\alpha}x$, so $a\le x$; if $\beta\ne\alpha$ then $\beta\in I$ and $\alpha<_{J}\beta$ by minimality of $\alpha$, so $a<x$. Hence $a$ is the smallest element of $B$, and $A$ is well ordered.
:::
