---
schema: qual/card@1
id: E-ZY1RB
kind: problem
title: Connected ordered sets are linear continua
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 4, printed p. 158, with the
    definition of linear continuum and the order topology of §14; the stored statement is
    the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.4, PDF p. 4. A nonempty bounded set without a
    least upper bound gives a separation of X into the union of the open rays below its
    members and the union of the open rays above its upper bounds, and a gap between two
    points gives a separation into two open rays. (tmp/sources/munkres-solutions-positron-
    ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the same argument, with two repairs from
    reading it against the book. The source says the left-hand piece of its separation is
    nonempty "since A does not have a supremum", which does not follow from that alone: the
    card now argues that some element of A is not the least element of X, since otherwise A
    is that one element and the set of upper bounds has a least element. And the definition
    on printed p. 153 requires a linear continuum to have more than one element, a clause
    the printed exercise omits; the one-point ordered set is connected and is not a linear
    continuum, so the solution now names the hypothesis it uses and records that exception.
    The statement is unchanged, and the two separations are still the source's.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Review repair: the exercise is printed on p. 158, not p. 157, and the solution's citation is
    corrected. Checked against the PDF, where the page numbered 158 carries the exercise and page 157
    does not. Nothing else on the card changed.
---

::: {.exercise}

Let $X$ be an ordered set in the order topology.
Show that if $X$ is connected, then $X$ is a linear continuum.

:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.4, PDF p. 4** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both separations below are that solution's, and the argument for the nonemptiness of its first piece is supplied here, the source asserting it from the absence of a supremum, which does not give it. The statement was checked against Munkres, *Topology* (2000), §24 Exercise 4, printed p. 158, with the definition of a linear continuum printed on p. 153: a simply ordered set *having more than one element* with the least upper bound property and, for all $x<y$, an element strictly between them. The printed exercise omits the clause on the number of elements, and that clause cannot be dropped, since a one-point ordered set is connected and is not a linear continuum. The claim is therefore proved for an ordered set of more than one element, the only case in which the book's term applies.

Throughout, $X$ is a simply ordered set with more than one element carrying the order topology, and $X$ is assumed connected. For $x\in X$ the sets $(-\infty,x)=\theset{y\in X\mid y<x}$ and $(x,+\infty)=\theset{y\in X\mid x<y}$ are the open rays, which are open in the order topology (§14, printed p. 86). An upper bound of a subset $A\subset X$ is an element $b$ with $a\leq b$ for every $a\in A$, and $X$ has the least upper bound property when every nonempty such $A$ that has an upper bound has a least one.

::: pf

::: {.pf-step #lub}

$X$ has the least upper bound property.

:::: pf-proof

Let $A\subset X$ be nonempty and bounded above, let $B$ be the set of its upper bounds, and suppose that $A$ has no least upper bound, that is, that $B$ has no least element. Put
$$
C\coloneqq\bigcup_{a\in A}(-\infty,a),\qquad D\coloneqq\bigcup_{b\in B}(b,+\infty);
$$
the aim is to show that these two sets separate $X$.

::: {.pf-step #open}

$C$ and $D$ are open in $X$.

::: pf-proof

Each is a union of open rays, and the open rays are open in the order topology (§14, printed p. 86), so each is a union of open sets.

:::

:::

::: {.pf-step #disjoint}

$C\cap D=\varnothing$.

::: pf-proof

If $x\in C\cap D$ there are $a\in A$ and $b\in B$ with $x<a$ and $b<x$. Then $b<x<a$ with $a\in A$, so $b$ is not an upper bound of $A$, contradicting $b\in B$.

:::

:::

::: {.pf-step #cover}

$C\cup D=X$.

::: pf-proof

Let $x\in X$. If $x\in B$, then, $B$ having no least element, there is $b\in B$ with $b<x$, so $x\in(b,+\infty)\subset D$. If $x\notin B$, then $x$ is not an upper bound of $A$, so $x<a$ for some $a\in A$, and $x\in(-\infty,a)\subset C$.

:::

:::

::: {.pf-step #nonempty}

$C\neq\varnothing$ and $D\neq\varnothing$.

::: pf-proof

$D\neq\varnothing$: $A$ is bounded above, so $B\neq\varnothing$, and if $b\in B$ then, $B$ having no least element, some $b^{\prime}\in B$ satisfies $b^{\prime}<b$, whence $b\in(b^{\prime},+\infty)\subset D$. For $C$, not every element of $A$ can be the least element of $X$: if they all were, $A$ would be the singleton of the least element $a_{0}$ of $X$, which is an upper bound of $A$, and then $B=\theset{b\in X\mid a_{0}\leq b}$ would have the least element $a_{0}$, contrary to the hypothesis. So some $a\in A$ is not the least element of $X$, there is $y\in X$ with $y<a$, and $y\in(-\infty,a)\subset C$.

:::

:::

::: pf-step

$C$ and $D$ separate $X$, which is impossible; hence $B$ has a least element, and $A$ has a least upper bound.

::: pf-proof

By steps [](#open){.pf-ref}, [](#disjoint){.pf-ref}, [](#cover){.pf-ref} and [](#nonempty){.pf-ref} the pair $\theset{C,D}$ is a separation of $X$, which the hypothesis forbids. So the supposition fails, $B$ has a least element, and that element is by definition the least upper bound of $A$.

:::

:::

::::

:::

::: {.pf-step #dense}

For all $x<y$ in $X$ there is $z\in X$ with $x<z<y$.

::: pf-proof

Suppose $x<y$ and that no $z$ satisfies $x<z<y$. Then $(-\infty,y)$ and $(x,+\infty)$ are open rays, hence open; they are nonempty, containing $x$ and $y$ respectively; they are disjoint, since a common point $u$ would satisfy $x<u<y$; and their union is $X$, since $u<y$ or $u\geq y>x$ for every $u\in X$. So they separate $X$, contrary to the hypothesis, and an element strictly between $x$ and $y$ exists.

:::

:::

::: pf-step

Therefore $X$ is a linear continuum.

::: pf-proof

$X$ has the least upper bound property by step [](#lub){.pf-ref} and satisfies the density condition by step [](#dense){.pf-ref}, and it has more than one element by hypothesis. Those are the two clauses of the definition on printed p. 153, so $X$ is a linear continuum.

:::

:::

:::

:::
