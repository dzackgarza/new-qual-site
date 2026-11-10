---
schema: qual/card@1
id: E-K8RRE
kind: problem
title: Closure of an interval in the order topology
classification:
  areas:
  - topology
  topics:
  - Closure
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 5, printed p. 100, with the
    definition of the order topology in §14 and Theorem 17.5 on printed p. 97; the stored
    statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 17.5, printed p. 161.
    The closed interval is closed because its complement is a union of open rays, and the
    criterion for equality - a has no immediate successor and b no immediate predecessor -
    is his, proved by the open ray below the immediate successor one way and by the absence
    of one the other. Two things are added: the case a = b, where the closure of the empty
    interval is empty and equality fails whatever the endpoints are like, and an explicit
    check that a basis element at a contains the points between a and its right end.
    (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Let $X$ be an ordered set in the order topology.
Show that $\overline{(a, b)} \subset [a, b]$.
Under what conditions does equality hold?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.5, printed p. 161** (`tmp/sources/munkres-solutions-whitman.pdf`); the inclusion, the criterion for equality in terms of immediate successor and predecessor, and the remark that the Hausdorff axiom does not suffice are his. The degenerate case $a=b$ is added: it is the one case his criterion does not cover.

*The inclusion.* The complement of the closed interval is a union of open rays,
$$
X-[a,b]=(-\infty,a)\cup(b,\infty),
$$
which is open in the order topology; so $[a,b]$ is closed. As $(a,b)\subset[a,b]$ and $\overline{(a,b)}$ is the smallest closed set containing $(a,b)$ (Theorem 17.5, printed p. 97), $\overline{(a,b)}\subset[a,b]$.

*When equality holds.* Suppose $a<b$, so that $[a,b]-(a,b)=\{a,b\}$. Then $\overline{(a,b)}=[a,b]$ exactly when $a$ and $b$ both lie in $\overline{(a,b)}$, that is, when each of them is a limit point of $(a,b)$. We show

*$a$ is a limit point of $(a,b)$ if and only if $a$ has no immediate successor in $X$.*

If $a$ has the immediate successor $c$, then $(-\infty,c)$ is an open set containing $a$ that meets $(a,b)$ in no point: such a point $x$ would satisfy $a<x<b$ and $x<c$, so $a<x<c$, contradicting the immediacy of $c$. Conversely, suppose $a$ has no immediate successor. Let $B$ be a basis element of the order topology containing $a$; it is an interval with $a$ in it, so in every case $B$ contains $\{x\in X\mid a<x<d\}$ for some $d>a$ (with $d$ the right end of the interval, or the largest element of $X$ if $B$ is of the form $[e,d]$ or of the form $[e,\rightarrow)$ with $e$ least; if $a$ is the least element of $X$ then $B$ contains $\{x\mid a<x<d\}$ as well). Since $a<b$, the element $\min(d,b)$ is greater than $a$, and since $a$ has no immediate successor there is $x$ with $a<x<\min(d,b)$; then $x\in B$ and $x\in(a,b)$. So every basis element at $a$, hence every neighbourhood of $a$, meets $(a,b)$.

The same argument with the order reversed shows that $b$ is a limit point of $(a,b)$ if and only if $b$ has no immediate predecessor in $X$. Hence for $a<b$,
$$
\overline{(a,b)}=[a,b]\iff a \text{ has no immediate successor and } b \text{ has no immediate predecessor}.
$$

If $a=b$ then $(a,b)=\varnothing$, so $\overline{(a,b)}=\varnothing\ne\{a\}=[a,b]$: equality fails even when $a$ has neither an immediate successor nor an immediate predecessor.

As Whitman observes, the Hausdorff axiom does not settle the question: $X=\ZZ$ with the order topology is discrete, hence Hausdorff, and every element has an immediate successor, so $\overline{(a,b)}\subsetneq[a,b]$ there.
:::
