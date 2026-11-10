---
schema: qual/card@1
id: E-MUN-10-3
kind: problem
title: Order types of $\{1,2\} \times \ZZ_+$ and $\ZZ_+ \times \{1,2\}$
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
    Read against Munkres, Topology (2000), §10 Exercise 3, printed p. 67; the stored
    statement is the printed question, and both ordered sets are as printed (dictionary
    order).
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 10.3, printed p. 109.
    The answer (they do not have the same order type) and the proof are his: (2,1) has no
    immediate predecessor in {1,2}xZ_+, while every element of Z_+x{1,2} other than the
    least has an immediate predecessor, and an order isomorphism would have to carry one to
    the other. His closing ordinal-number remark is kept as a remark.
---

::: {.exercise}

Both $\{1,2\} \times \ZZ_{+}$ and $\ZZ_{+} \times \{1,2\}$ are well-ordered in the dictionary order.
Do they have the same order type?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.3, printed p. 109** (`tmp/sources/munkres-solutions-whitman.pdf`); the proof and the closing remark are his.

They do **not** have the same order type. Write $A=\{1,2\}\times\ZZ_{+}$ and $B=\ZZ_{+}\times\{1,2\}$, both in the dictionary order, and suppose there is an order-preserving bijection $f:A\to B$ (an order isomorphism onto $B$).

The element $(1,1)$ is the smallest element of both $A$ and $B$. Hence $(2,1)\in A$ is not the smallest element of $A$, so $f(2,1)=(n,b)$ with $(n,b)\ne(1,1)$. We exhibit the immediate predecessor of $(n,b)$ in $B$:

- if $b=1$, then $n>1$, and $y=(n-1,2)$;
- if $b=2$, then $y=(n,1)$.

In the first case $(n-1,2)<(n,1)$ because $n-1<n$, and nothing lies strictly between: an element $(m,c)$ with $(n-1,2)<(m,c)<(n,1)$ has $n-1\le m\le n$; for $m=n-1$ the inequality $(n-1,2)<(n-1,c)$ forces $c>2$, impossible, and for $m=n$ the inequality $(m,c)<(n,1)$ forces $c<1$, impossible. In the second case $(n,1)<(n,2)$ and an element between them has $m=n$, forcing $1<c<2$, or $m\ne n$, which puts it outside the interval. So in both cases $y$ is the immediate predecessor of $(n,b)$ in $B$.

Now let $x=f^{-1}(y)$. An order-preserving bijection has an order-preserving inverse, so $y<f(2,1)$ gives $x<(2,1)$, and therefore $x=(1,a)$ for some $a\in\ZZ_{+}$: the first coordinate of $x$ cannot be $2$, since $(2,a')\ge(2,1)$ for every $a'\in\ZZ_{+}$. But then
$$
x=(1,a)<(1,a+1)<(2,1),
$$
and applying the order-preserving $f$,
$$
y=f(1,a)<f(1,a+1)<f(2,1)=(n,b),
$$
which contradicts $y$ being an immediate predecessor of $f(2,1)$ in $B$. So no order-preserving bijection $A\to B$ exists, and the two ordered sets have different order types.

As Whitman notes, in the theory of ordinal numbers $A$ has order type $\omega+\omega=\omega\cdot 2$ while $B$ has order type $\omega$; distinct ordinals are never of the same order type, which is a second way to see the answer.
:::
