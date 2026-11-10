---
schema: qual/card@1
id: E-MUN-4-4
kind: problem
title: Largest element of finite subsets of $\{1, \ldots, n\}$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 4, printed p. 34; both parts are
    stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.4,
    printed p. 50 (tmp/sources/munkres-solutions-whitman.pdf). The induction is his: a
    nonempty subset of {1, ..., n+1} either contains n+1, which is then its largest
    element, or lies in {1, ..., n}. Part (b) is his remark that the induction is about
    one fixed initial segment and gives no bound for an arbitrary subset of Z_+, with
    Z_+ itself as the example of a subset with no largest element.
---

::: {.exercise}

(a) Prove by induction that given $n \in \ZZ_+$, every nonempty subset of $\{1, \ldots, n\}$ has a largest element.

(b) Explain why you cannot conclude from (a) that every nonempty subset of $\ZZ_{+}$ has a largest element.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.4, printed p. 50** (`tmp/sources/munkres-solutions-whitman.pdf`); the induction and the answer to (b) below are his.

(a) Let $P(n)$ be the assertion that every nonempty subset of $\{1,\dots,n\}$ has a largest element.

For $n=1$, the only nonempty subset is $\{1\}$, whose largest element is $1$.

Assume $P(n)$, and let $A\subset\{1,\dots,n+1\}$ be nonempty. If $n+1\in A$, then $n+1$ is the largest element of $A$. If $n+1\notin A$, then
$$
A\subset\{1,\dots,n\},
$$
so $A$ has a largest element by the inductive hypothesis. Thus $P(n+1)$ holds. By induction, $P(n)$ holds for every $n\in\ZZ_+$.

(b) Part (a) concerns subsets contained in one fixed finite initial segment $\{1,\dots,n\}$. A general nonempty subset of $\ZZ_+$ need not be bounded above and hence need not lie in any such segment. For example, $\ZZ_+$ itself has no largest element, since $m+1\in\ZZ_+$ and $m+1>m$ for every $m\in\ZZ_+$.
:::
