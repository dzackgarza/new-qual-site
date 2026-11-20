---
schema: qual/card@1
id: E-0B5CJ
kind: problem
title: Punctured products of connected spaces are connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 9, printed p. 152, with Theorem 23.3
    and Theorem 23.6; both sets and both properness hypotheses are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.9, PDF p. 2. Two families of T-shaped sets, one
    over the points of X - A and one over the points of Y - B, are connected and share a
    point, and their union is the complement of A x B; both inclusions are checked on the
    card. (tmp/sources/munkres-solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $A$ be a proper subset of $X$, and let $B$ be a proper subset of $Y$.
If $X$ and $Y$ are connected, show that

$$
(X \times Y) - (A \times B)
$$

is connected.
:::

::: {.solution}

The argument is the published solution of **positron0802**, *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.9 (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the T-shaped sets $U_{x}$ and $V_{y}$ and their union are that solution's, and every step below is checked against Munkres, *Topology* (2000), §23 Exercise 9, with Theorem 23.3 and Theorem 23.5 on printed p. 150. Throughout, $X$ and $Y$ are connected spaces, $A\subsetneq X$ and $B\subsetneq Y$, and $X-A$, $Y-B$ denote complements in $X$ and $Y$.

::: pf

::: {.pf-step #base-point}
$(X-A)\times(Y-B)\neq\emptyset$.

::: pf-proof
Since $A$ is a proper subset of $X$ there is a point of $X$ outside $A$, so $X-A\neq\emptyset$, and likewise $Y-B\neq\emptyset$. Choosing $c\in X-A$ and $d\in Y-B$ gives the point $(c,d)$ of the product.
:::

:::

::: {.pf-step #t-connected}
For every $x\in X-A$ the set $U_{x}\coloneqq(X\times\theset{d})\cup(\theset{x}\times Y)$ is connected and contains $(c,d)$.

:::: pf-proof

::: {.pf-step #slices}
$X\times\theset{d}$ and $\theset{x}\times Y$ are connected.

::: pf-proof
The maps $u\mapsto(u,d)$ and $v\mapsto(x,v)$ are homeomorphisms of $X$ and $Y$ onto those two slices. Both slices are therefore continuous images of connected spaces, hence connected by Theorem 23.5.
:::

:::

::: {.pf-step #meet}
$(x,d)\in(X\times\theset{d})\cap(\theset{x}\times Y)$.

::: pf-proof
The point $(x,d)$ has second coordinate $d$ and first coordinate $x$, so it belongs to each of the two slices.
:::

:::

::: {.pf-step #t-union}
$U_{x}$ is connected and $(c,d)\in U_{x}$.

::: pf-proof
$U_{x}$ is a union of connected subspaces of $X\times Y$ with the common point $(x,d)$ of step [](#meet){.pf-ref}, so it is connected by Theorem 23.3; this uses step [](#slices){.pf-ref}. Since $c\in X-A$ and $d\in Y-B$, the point $(c,d)$ satisfies $(c,d)\in X\times\theset{d}\subset U_{x}$.
:::

:::

::::

:::

::: {.pf-step #u-connected}
$U\coloneqq\bigcup_{x\in X-A}U_{x}$ is connected and contains $(c,d)$.

::: pf-proof
This is a union of connected subspaces of $X\times Y$ that share the point $(c,d)$ by step [](#t-connected){.pf-ref}, so Theorem 23.3 applies.
:::

:::

::: {.pf-step #v-connected}
$V\coloneqq\bigcup_{y\in Y-B}V_{y}$, where $V_{y}\coloneqq(X\times\theset{y})\cup(\theset{c}\times Y)$, is connected and contains $(c,d)$.

::: pf-proof
Repeat the argument of steps [](#t-connected){.pf-ref} and [](#u-connected){.pf-ref} with the two factors interchanged and $c,d$ interchanged: the slices $X\times\theset{y}$ and $\theset{c}\times Y$ are connected and meet in $(c,y)$, and every $V_{y}$ contains $(c,d)$, so Theorem 23.3 gives the connectedness of each $V_{y}$ and then of $V$.
:::

:::

::: {.pf-step #cover}
$U\cup V=(X\times Y)-(A\times B)$.

::: pf-proof
For the inclusion $\subset$: a point of $X\times\theset{d}$ has second coordinate outside $B$, and a point of $\theset{x}\times Y$ with $x\in X-A$ has first coordinate outside $A$, so neither lies in $A\times B$; every point of $U$, and symmetrically every point of $V$, has one of these two forms. For the inclusion $\supset$: if $(x,y)\notin A\times B$ then $x\notin A$ or $y\notin B$; in the first case $(x,y)\in\theset{x}\times Y\subset U_{x}\subset U$, and in the second $(x,y)\in X\times\theset{y}\subset V_{y}\subset V$.
:::

:::

::: pf-step
Therefore $(X\times Y)-(A\times B)$ is connected.

::: pf-proof
By step [](#cover){.pf-ref} the complement is $U\cup V$, a union of the connected sets of steps [](#u-connected){.pf-ref} and [](#v-connected){.pf-ref} sharing the point $(c,d)$; Theorem 23.3 makes it connected.
:::

:::

:::

:::
