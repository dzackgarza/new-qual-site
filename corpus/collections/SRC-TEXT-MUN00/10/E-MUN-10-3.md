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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed proof into numbered steps and supplied the two principles it used
    silently: an order isomorphism carries the least element of one ordered set to the least
    element of the other, and its inverse is order-preserving, so strict inequalities are reflected
    as well as preserved. The two interval computations (nothing lies between (n-1,2) and (n,1),
    nothing between (n,1) and (n,2)) are kept, since the argument turns on them. The mathematics is
    the earlier reading's. Not re-read this session: the Whitman page, printed p. 109.
---

::: {.exercise}

Both $\{1,2\} \times \ZZ_{+}$ and $\ZZ_{+} \times \{1,2\}$ are well-ordered in the dictionary order.
Do they have the same order type?
:::

::: {.solution}

The proof and the closing remark are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 10.3, printed p. 109** (`tmp/sources/munkres-solutions-whitman.pdf`).

Write $A=\{1,2\}\times\ZZ_{+}$ and $B=\ZZ_{+}\times\{1,2\}$, each with the dictionary order: $(i,a)<(j,b)$ when $i<j$, or when $i=j$ and $a<b$.

::: pf

::: {.pf-step #wellordered}
$A$ and $B$ are well ordered.

::: pf-proof
For a nonempty subset of $A$, the set of first coordinates is a nonempty subset of $\{1,2\}$ with least element $i_{0}$; the second coordinates of elements with first coordinate $i_{0}$ form a nonempty subset of $\ZZ_{+}$ with least element $a_{0}$, and $(i_{0},a_{0})$ is the least element of the subset. The same argument with the coordinates interchanged handles $B$, whose first coordinate set $\ZZ_{+}$ and second coordinate set $\{1,2\}$ are both well ordered.
:::

:::

::: {.pf-step #least}
$(1,1)$ is the least element of $A$ and of $B$.

::: pf-proof
In $A$, $(1,1)\leq(1,a)\leq(2,a')$ for all $a,a'\in\ZZ_{+}$. In $B$, $(1,1)\leq(n,b)$ for all $n\geq1$, with equality only when $(n,b)=(1,1)$.
:::

:::

::: {.pf-step #no-pred}
$(2,1)$ has no immediate predecessor in $A$.

::: pf-proof
If $x<(2,1)$ then the first coordinate of $x$ is $1$, say $x=(1,a)$, and $(1,a)<(1,a+1)<(2,1)$ because $a<a+1$ and $1<2$. So no $x$ is an immediate predecessor.
:::

:::

::: {.pf-step #has-pred}
Every element of $B$ other than $(1,1)$ has an immediate predecessor in $B$.

::: pf-proof
Let $(n,b)\neq(1,1)$. If $b=2$, take $y=(n,1)$; then $y<(n,2)$, and an element $(m,c)$ with $(n,1)<(m,c)<(n,2)$ must have $m=n$, forcing $1<c<2$, which is impossible. If $b=1$, then $n>1$ and $y=(n-1,2)<(n,1)$; an element $(m,c)$ between them has $n-1\leq m\leq n$, and $m=n-1$ forces $c>2$ while $m=n$ forces $c<1$, both impossible. So in each case $y$ is the immediate predecessor.
:::

:::

::: {.pf-step #order-iso}
An order isomorphism preserves and reflects the order, carries the least element to the least element, and has an order-preserving inverse.

::: pf-proof
If $f$ is an order isomorphism then $x<y$ implies $f(x)<f(y)$; conversely $f(x)<f(y)$ implies $x<y$, since $x=y$ or $y<x$ would give $f(x)=f(y)$ or $f(y)<f(x)$. So $f^{-1}$ is order-preserving. If $m$ is least in the domain and $z<f(m)$, then $f^{-1}(z)<m$, impossible; so $f(m)$ is least in the codomain.
:::

:::

::: {.pf-step #contradiction}
No order isomorphism $f\colon A\to B$ exists.

::: pf-proof
Suppose $f$ is one. By steps [](#least){.pf-ref} and [](#order-iso){.pf-ref}, $f(1,1)=(1,1)$. The element $(2,1)$ is not least in $A$, so $f(2,1)=(n,b)\neq(1,1)$, and by step [](#has-pred){.pf-ref} it has an immediate predecessor $y$ in $B$. Put $x=f^{-1}(y)$; since $y<f(2,1)$ and $f^{-1}$ is order-preserving, $x<(2,1)$, so by step [](#no-pred){.pf-ref} $x=(1,a)$ with $(1,a)<(2,1)$, and then $(1,a)<(1,a+1)<(2,1)$. Applying $f$ gives $y=f(1,a)<f(1,a+1)<f(2,1)$, contradicting that $y$ is the immediate predecessor of $f(2,1)$.
:::

:::

::: {.pf-step}
$A$ and $B$ do not have the same order type.

::: pf-proof
Having the same order type means being related by an order isomorphism, which step [](#contradiction){.pf-ref} excludes. Equivalently, in ordinal arithmetic $A$ has type $\omega\cdot2$ and $B$ has type $\omega$, and distinct ordinals are never of the same order type.
:::

:::

:::

:::
