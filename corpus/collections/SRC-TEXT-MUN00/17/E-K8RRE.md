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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as the inclusion, the two endpoint criteria, and the resulting criterion for equality; the degenerate case $a=b$ stays inside the last step, and Whitman's observation on the Hausdorff axiom moved to a remark block. The basis-element argument at $a$ was re-checked. No statement change.
---

::: {.exercise}

Let $X$ be an ordered set in the order topology.
Show that $\overline{(a, b)} \subset [a, b]$.
Under what conditions does equality hold?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 17.5, printed p. 161** (`tmp/sources/munkres-solutions-whitman.pdf`); the inclusion, the criterion for equality in terms of immediate successor and predecessor, and the remark that the Hausdorff axiom does not suffice are his. The degenerate case $a=b$ is added here: it is the one case his criterion does not cover.

Let $X$ be an ordered set in the order topology, and let $a\le b$ in $X$.

::: pf

::: {.pf-step #inclusion}

$\overline{(a,b)}\subset[a,b]$.

::: pf-proof

The complement of the closed interval is a union of open rays,
$$
X-[a,b]=(-\infty,a)\cup(b,\infty),
$$
which is open in the order topology; so $[a,b]$ is closed. As $(a,b)\subset[a,b]$ and $\overline{(a,b)}$ is the smallest closed set containing $(a,b)$ (Theorem 17.5), the inclusion follows.

:::

:::

::: {.pf-step #left-end}

For $a<b$, $a\in\overline{(a,b)}$ if and only if $a$ has no immediate successor in $X$.

::: pf-proof

If $a$ has the immediate successor $c$, then $(-\infty,c)$ is an open set containing $a$ that meets $(a,b)$ in no point: such a point would satisfy $a<x<b$ and $x<c$, hence $a<x<c$, contradicting the immediacy of $c$. Conversely, suppose $a$ has no immediate successor, and let $B$ be a basis element of the order topology containing $a$. Then $B$ is an interval containing $a$, so it contains $\{x\in X\mid a<x<d\}$ for some $d>a$: take $d$ to be the right endpoint of $B$, and if $B$ has no right endpoint take $d$ to be the largest element of $X$, which exists in that case. Since $a<b$, the element $\min(d,b)$ exceeds $a$, and since $a$ has no immediate successor there is $x$ with $a<x<\min(d,b)$; then $x\in B$ and $x\in(a,b)$. So every basis element at $a$, hence every neighbourhood of $a$, meets $(a,b)$.

:::

:::

::: {.pf-step #right-end}

For $a<b$, $b\in\overline{(a,b)}$ if and only if $b$ has no immediate predecessor in $X$.

::: pf-proof

The argument of step [](#left-end){.pf-ref} with the order reversed: an immediate predecessor $c$ of $b$ gives the open set $(c,+\infty)$ meeting $(a,b)$ in nothing, and if $b$ has none then every basis element at $b$ contains $\{x\mid e<x<b\}$ for some $e<b$, which meets $(a,b)$ because $a<b$.

:::

:::

::: pf-step

$\overline{(a,b)}=[a,b]$ if and only if $a<b$, $a$ has no immediate successor in $X$ and $b$ has no immediate predecessor in $X$.

::: pf-proof

By step [](#inclusion){.pf-ref}, $\overline{(a,b)}\subset[a,b]$. If $a<b$ then $[a,b]-(a,b)=\{a,b\}$, so the equality holds exactly when $a$ and $b$ both lie in $\overline{(a,b)}$, which steps [](#left-end){.pf-ref} and [](#right-end){.pf-ref} decide. If $a=b$ then $(a,b)=\varnothing$ and $\overline{(a,b)}=\varnothing\ne\{a\}=[a,b]$, so the equality fails even when $a$ has neither an immediate successor nor an immediate predecessor.

:::

:::

:::
:::

::: {.remark}
The Hausdorff axiom does not settle the question. $X=\ZZ$ with the order topology is discrete, hence Hausdorff, and every element has an immediate successor, so $\overline{(a,b)}\subsetneq[a,b]$ there.
:::
