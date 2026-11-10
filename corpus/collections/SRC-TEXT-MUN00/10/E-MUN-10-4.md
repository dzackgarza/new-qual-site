---
schema: qual/card@1
id: E-MUN-10-4
kind: problem
title: Characterizing non-well-ordered sets via $\ZZ_{-}$
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
    Read against Munkres, Topology (2000), §10 Exercise 4, printed p. 67; the stored
    statement is printed (a) and (b), Z_- being the negative integers in the usual order.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.4, printed pp.
    109-110. (a) is his: failing well-ordering gives a nonempty subset with no smallest
    element, from which the axiom of choice and the principle of recursive definition build
    a strictly decreasing sequence, i.e. a subset of order type Z_-; the converse is his
    too. (b) is his reduction of an ill-ordered A to a countable subset of type Z_-, which
    the hypothesis forbids. The recursion in (a) is written out as an application of the
    principle of recursive definition rather than left implicit.
---

::: {.exercise}

(a) Let $\ZZ_{-}$ denote the set of negative integers in the usual order.
Show that a simply ordered set $A$ fails to be well-ordered if and only if it contains a subset having the same order type as $\ZZ_{-}$ .

(b) Show that if $A$ is simply ordered and every countable subset of $A$ is well-ordered, then $A$ is well-ordered.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.4, printed pp. 109--110** (`tmp/sources/munkres-solutions-whitman.pdf`); both parts are his, with the recursion used in (a) spelled out as an application of the principle of recursive definition.

(a) Let $A$ be a simply ordered set.

*If $A$ is not well ordered.* Then some nonempty $B\subset A$ has no smallest element. For $b\in B$ put $X_b=\{x\in B\mid x<b\}$; the set $X_b$ is nonempty, since otherwise $b$ would be the smallest element of $B$. By the axiom of choice there is a choice function $c$ on the collection $\{X_b\mid b\in B\}$ of nonempty subsets of $B$, and we may apply the principle of recursive definition to the formula
$$
f(1)=b_0,\qquad f(n)=c\big(X_{f(n-1)}\big)\ \ (n>1),
$$
where $b_0\in B$ is fixed; the formula is defined on every function from a nonempty section of $\ZZ_{+}$ into $B$, since $X_{b}\ne\varnothing$ for every $b\in B$. This gives $f:\ZZ_{+}\to B$ with $f(n)\in X_{f(n-1)}$, that is $f(n)<f(n-1)$ for every $n>1$. Hence $f$ is strictly decreasing, and by induction $f(n)<f(m)$ whenever $m<n$; in particular $f$ is injective.

Define $h:\ZZ_{-}\to B$ by $h(-n)=f(n)$. If $-n<-m$ then $n>m$, so $h(-n)=f(n)<f(m)=h(-m)$: the map $h$ is an order-preserving injection, and its image $C=h(\ZZ_{-})$ is a subset of $B$, hence of $A$, having the same order type as $\ZZ_{-}$.

*If $A$ contains a subset $C$ of the same order type as $\ZZ_{-}$.* Then $C\ne\varnothing$, and $C$ has no smallest element: an order isomorphism $C\to\ZZ_{-}$ would carry a smallest element of $C$ to a smallest element of $\ZZ_{-}$, which does not exist. So $A$ has a nonempty subset with no smallest element and is not well ordered.

(b) Let $A$ be simply ordered and suppose that every countable subset of $A$ is well ordered. Let $B\subset A$ be nonempty. If $B$ were not well ordered, part (a) would give a subset $C\subset B$ of the same order type as $\ZZ_{-}$. Then $C\subset A$ and $C$ is countable, being in bijection with the countable set $\ZZ_{-}$, so by hypothesis $C$ is well ordered; but $C$ has the order type of $\ZZ_{-}$, which is not well ordered, and this is impossible. Hence every nonempty subset $B$ of $A$ has a smallest element, that is, $A$ is well ordered.
:::
