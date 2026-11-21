---
schema: qual/card@1
id: E-MD9QR
kind: problem
title: The ordered square is locally connected but not locally path connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §25 Exercise 3, printed p. 162, with Example 1
    and Example 6 of §24 and Theorem 24.1; the two questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 25.3, PDF pp. 8-9. Basis intervals of the ordered
    square are connected, so it is locally connected; no neighbourhood of p x 1 is path
    connected, since a path leaving it would inject an uncountable interval into the
    rationals; the path components are the vertical fibres. The presentation of the last
    paragraph is repaired. (tmp/sources/munkres-solutions-positron-ch3.pdf).
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the three parts into numbered steps and corrected two phrases of the transcription
    while doing so. The claim that a path from p x 1 to q x 0 "contains every point between them" is
    replaced by what the intermediate value theorem gives and what the argument needs: the path
    meets every fibre {s} x [0,1] with s between the two first coordinates. And the last paragraph,
    which said the earlier argument applies "with p = x'", now states the general counting lemma once
    and applies it in both places. Also supplied: that the fibres are open, respectively closed, in
    the order topology, which is what makes the preimages open subsets of [0,1], and that a fibre is
    homeomorphic to [0,1]. Not re-read this session: the positron0802 pages, PDF pp. 8-9, and
    Munkres printed p. 162.
---

::: {.exercise}

Show that the ordered square is locally connected but not locally path connected.
What are the path components of this space?
:::

::: {.solution}

The argument is that of **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 25.3, PDF pp. 8--9** (`tmp/sources/munkres-solutions-positron-ch3.pdf`), with its last paragraph rewritten as the general counting lemma below. The statement was checked against Munkres, *Topology* (2000), §25 Exercise 3, printed p. 162.

Let $I_{o}^{2}=[0,1]\times[0,1]$ carry the dictionary order, and for $x\in[0,1]$ let $F_{x}=\{x\}\times[0,1]$ be the fibre over $x$.

::: pf

::: {.pf-step #interval}
Every basis interval of $I_{o}^{2}$ is connected.

::: pf-proof
$I_{o}^{2}$ is a linear continuum (Example 1 of §24): the dictionary order on $[0,1]\times[0,1]$ is dense, since between $x\times y$ and $x\times y'$ with $y<y'$ lies $x\times\tfrac{y+y'}{2}$ and between $x\times y$ and $x'\times y'$ with $x<x'$ lies $x\times\tfrac{y+1}{2}$, and it has the least upper bound property. Theorem 24.1 states that intervals and rays of a linear continuum are connected.
:::

:::

::: {.pf-step #locally-connected}
$I_{o}^{2}$ is locally connected.

::: pf-proof
Given a point and a neighbourhood $U$ of it, $U$ contains a basis element about the point, and that basis element is connected by step [](#interval){.pf-ref}. So every neighbourhood of every point contains a connected neighbourhood of that point.
:::

:::

::: {.pf-step #fibres}
For $x\in[0,1]$ the set $\{x\}\times(0,1)$ is open and $F_{x}$ is closed in $I_{o}^{2}$, and $F_{x}$ is homeomorphic to $[0,1]$.

::: pf-proof
$\{x\}\times(0,1)=(x\times0,\,x\times1)$ is an open interval. Its complement is the union of the two rays $\{p\mid p<x\times0\}$ and $\{p\mid p>x\times1\}$, both open, so $F_{x}$ is closed. The map $y\mapsto x\times y$ is an order isomorphism onto $F_{x}$ with its order topology, hence a homeomorphism.
:::

:::

::: {.pf-step #counting}
If $x<x'$ and a path $f\colon[0,1]\to I_{o}^{2}$ meets both $F_{x}$ and $F_{x'}$, then $(x,x')$ injects into $\QQ$, which is impossible.

::: pf-proof
The first-coordinate map $\pi\colon I_{o}^{2}\to[0,1]$ is continuous, $\pi^{-1}(a,b)$ being the open set of points whose first coordinate lies in $(a,b)$; so $\pi f$ is continuous and takes the values $x$ and $x'$ at the two points where $f$ meets $F_{x}$ and $F_{x'}$. For every $s$ between those values the intermediate value theorem gives $t$ with $\pi f(t)=s$, so $f^{-1}\bigl(\{s\}\times(0,1)\bigr)$ is nonempty; it is open, being the preimage of an open set under the continuous $f$. These open subsets of $[0,1]$ are pairwise disjoint, since a point of $I_{o}^{2}$ has one first coordinate, so picking a rational in each gives an injection of the uncountable interval into $\QQ$.
:::

:::

::: {.pf-step #not-locally-path}
$I_{o}^{2}$ is not locally path connected at $p\times1$ for $0<p<1$, nor at $q\times0$ for $0<q<1$.

::: pf-proof
Let $V$ be a neighbourhood of $p\times1$ with $0<p<1$; it contains a basis interval $(L,U)$ with $L<p\times1<U$. The first coordinate of $U$ must exceed $p$ (the alternative, first coordinate $p$ and second coordinate greater than $1$, is impossible), say it is $c>p$; then the points $s\times0$ with $p<s<c$ lie in $(L,U)\subset V$. Choose such an $s$: if $V$ were path connected there would be a path in $V$ from $p\times1$ to $s\times0$, meeting $F_{p}$ and $F_{s}$, which step [](#counting){.pf-ref} forbids. The argument at $q\times0$ with $0<q<1$ is the same with the roles of the first coordinates reversed: every neighbourhood of $q\times0$ contains points with first coordinate below $q$.
:::

:::

::: {.pf-step #components}
The path components of $I_{o}^{2}$ are the fibres $F_{x}$.

::: pf-proof
$F_{x}$ is homeomorphic to $[0,1]$ by step [](#fibres){.pf-ref}, hence path connected, so all its points lie in one path component. If $u\in F_{x}$ and $v\in F_{x'}$ with $x<x'$ were in one path component, a path joining them would meet $F_{x}$ and $F_{x'}$, contradicting step [](#counting){.pf-ref}. So distinct fibres lie in distinct path components.
:::

:::

::: {.pf-step}
The ordered square is locally connected but not locally path connected, and its path components are the vertical fibres.

::: pf-proof
Steps [](#locally-connected){.pf-ref}, [](#not-locally-path){.pf-ref} and [](#components){.pf-ref} are the three assertions.
:::

:::

:::

:::
