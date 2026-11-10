---
schema: qual/card@1
id: E-MUN-3-12
kind: problem
title: Three order types on $\ZZ_+\times\ZZ_+$
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 12, printed p. 29: the three
    order relations (dictionary; x_0 - y_0 with y breaking ties; x_0 + y_0 with y
    breaking ties) on Z_+ x Z_+, asking which elements have immediate predecessors,
    whether there is a smallest element, and that the three order types differ. The
    stored statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.12,
    printed pp. 31-35 (tmp/sources/munkres-solutions-whitman.pdf). All three answers and
    all three order-type separations are his, including his Lemma 3.12.1 (an
    order-isomorphism preserves having a smallest element) and the counting of elements
    without an immediate predecessor that separates (i) from (iii).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked the "no immediate predecessor" cases of (ii) against the printed order: for
    (x,y) with x = 1 or y = 1 and (x_0,y_0) < (x,y), the card shows x_0 - y_0 < x - y
    (the alternative forces x_0 < 1 in the case x = 1 and y_0 < 1 in the case y = 1),
    which is what makes (x_0+1, y_0+1) lie strictly in between.
---

::: {.exercise}

Let $\ZZ_+$ denote the set of positive integers. Consider the following order relations on $\ZZ_+ \times \ZZ_+$:

(i) The dictionary order.

(ii) $(x_0, y_0) < (x_1, y_1)$ if either $x_0 - y_0 < x_1 - y_1$, or $x_0 - y_0 = x_1 - y_1$ and $y_0 < y_1$.

(iii) $(x_0, y_0) < (x_1, y_1)$ if either $x_0 + y_0 < x_1 + y_1$, or $x_0 + y_0 = x_1 + y_1$ and $y_0 < y_1$.

In these order relations, which elements have immediate predecessors? Does the set have a smallest element? Show that all three order types are different.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.12, printed pp. 31--35** (`tmp/sources/munkres-solutions-whitman.pdf`); the three answers, the case analyses and the separation of the order types are his. Throughout, an element has no immediate predecessor exactly when each element below it has something strictly between.

| order | immediate predecessor | smallest element |
| --- | --- | --- |
| (i) | every $(x,y)$ with $y>1$, namely $(x,y-1)$; none with $y=1$ | $(1,1)$ |
| (ii) | every $(x,y)$ with $x>1$ and $y>1$, namely $(x-1,y-1)$; none with $x=1$ or $y=1$ | none |
| (iii) | every $(x,y)\ne(1,1)$; none other | $(1,1)$ |

*Order (i).* Here $(x_0,y_0)<(x_1,y_1)$ means $x_0<x_1$, or $x_0=x_1$ and $y_0<y_1$. $(1,1)$ is smallest: for any $(x,y)$, either $x>1$ and $(1,1)<(x,y)$, or $x=1$ and then $y\ge1$ with $(1,1)<(1,y)$ when $y>1$. If $y_1>1$, then $(x_1,y_1-1)<(x_1,y_1)$; if $(x_2,y_2)$ lay strictly between, then $x_2=x_1$ (as $x_1<x_2$ would give $(x_1,y_1)<(x_2,y_2)$) and $y_1-1<y_2<y_1$, impossible in $\ZZ_+$. If $y_1=1$ and $(x_0,y_0)<(x_1,1)$, then $x_0<x_1$ (since $y_0<1$ is impossible), and $(x_0,y_0+1)$ satisfies $(x_0,y_0)<(x_0,y_0+1)<(x_1,1)$; so nothing has $(x_1,1)$ as immediate successor.

*Order (ii).* For any $(x,y)$, the point $(x,y+1)$ has $x-(y+1)<x-y$, so it is smaller: there is no smallest element. If $x_1>1$ and $y_1>1$ then $(x_1-1,y_1-1)$ has the same value of $x-y$ and a smaller second coordinate, so it is smaller; a point strictly between would have to share the value $x_1-y_1$ (otherwise $(x_1,y_1)$ would be below it) and then $y_1-1<y_2<y_1$, impossible. If $x_1=1$ or $y_1=1$ and $(x_0,y_0)<(x_1,y_1)$, then $x_0-y_0<x_1-y_1$: the other alternative would give $y_0<y_1=1$, or with $x_1=1$ would give $x_0=(x_0-y_0)+y_0<(1-y_1)+y_1=1$. Hence $(x_0+1,y_0+1)$ has the same value of $x-y$ as $(x_0,y_0)$ and a larger second coordinate, so $(x_0,y_0)<(x_0+1,y_0+1)$, while $x_0-y_0<x_1-y_1$ gives $(x_0+1,y_0+1)<(x_1,y_1)$; so $(x_0,y_0)$ is never the immediate predecessor.

*Order (iii).* For $(x,y)\ne(1,1)$, either $x>1$, and then $2\le 1+y<x+y$ gives $(1,1)<(x,y)$, or $y>1$ and $2\le x+1<x+y$; so $(1,1)$ is smallest and has no predecessor. If $y_1=1$, then $x_1>1$ and $(1,x_1-1)$ has sum $x_1<x_1+y_1$, so it is smaller; a point $(x_2,y_2)$ strictly between would satisfy $x_2+y_2<x_1+1$ (the alternative needs $y_2<y_1=1$) and $x_1=1+(x_1-1)\le x_2+y_2$, a contradiction. If $y_1>1$, then $(x_1+1,y_1-1)$ has sum $x_1+y_1$ and second coordinate $y_1-1<y_1$, so it is smaller; a point strictly between would satisfy $x_1+y_1\le x_2+y_2\le x_1+y_1$, hence equality of sums, and then $y_1-1<y_2<y_1$, impossible.

*The order types are different.* An order isomorphism carries elements without an immediate predecessor to elements without one, since having an immediate predecessor is the emptiness of an open interval, and it carries a smallest element to a smallest element. Orders (i) and (iii) have a smallest element and (ii) does not, so (ii) differs from both. Between (i) and (iii): in (i) the elements without an immediate predecessor are those with $y=1$, infinitely many, while in (iii) there is exactly one, the smallest element; a bijection preserving order would put these two sets in bijective correspondence, which is impossible.
:::
