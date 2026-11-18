---
schema: qual/card@1
id: E-DPKX4
kind: problem
title: Associativity of finite products
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Homeomorphisms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §19 Exercise 4, printed p. 118, with Theorem 19.1
    for finite products and Lemma 16.1; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 19.4, printed p. 191.
    The regrouping map and both continuity arguments are his: it is a bijection carrying
    products of subsets to products of subsets, the preimage of a basis element contains a
    basis element, and the image of a basis element is a basis element.
    (tmp/sources/munkres-solutions-whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the pairing map, its inverse, the image of a
    product, and both continuity directions through basis elements of the two products,
    against Munkres §19 Exercise 4, printed p. 114, where the box and product topologies
    coincide on a finite index set. Whitman, Exercise 19.4, printed p. 191. The printed
    statement needed no repair.
---

::: {.exercise}

Show that $(X_1 \times \cdots \times X_{n-1}) \times X_n$ is homeomorphic with $X_1 \times \cdots \times X_n$.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.4, printed p. 191** (`tmp/sources/munkres-solutions-whitman.pdf`); the map and the two continuity arguments are his. Since the index set $\{1,\dots,n\}$ is finite, the box and product topologies on these finite products coincide, and the box description is used throughout.

::: pf

::: {.pf-step #bijection}
The map
$$
f:X_{1}\times\cdots\times X_{n}\to(X_{1}\times\cdots\times X_{n-1})\times X_{n},\qquad
f(x_{1},\dots,x_{n})=\big((x_{1},\dots,x_{n-1}),x_{n}\big)
$$
is a bijection.

::: pf-proof
The map $g\big((x_{1},\dots,x_{n-1}),x_{n}\big)=(x_{1},\dots,x_{n})$ is defined on all of the target and satisfies $g\circ f=\id$ and $f\circ g=\id$, by the two displayed formulas; hence $f$ is bijective with inverse $g$.
:::

:::

::: {.pf-step #images}
For subsets $A_{k}\subset X_{k}$ one has $f(A_{1}\times\cdots\times A_{n})=(A_{1}\times\cdots\times A_{n-1})\times A_{n}$.

::: pf-proof
Both sides consist of the pairs $\big((a_{1},\dots,a_{n-1}),a_{n}\big)$ with $a_{k}\in A_{k}$ for each $k$: the left-hand side by the formula for $f$, the right-hand side by the definition of the product set.
:::

:::

::: {.pf-step #f-continuous}
$f$ is continuous.

::: pf-proof
Let $C=V'\times V_{n}$ be a basis element of $(X_{1}\times\cdots\times X_{n-1})\times X_{n}$, with $V'$ open in $X_{1}\times\cdots\times X_{n-1}$ and $V_{n}$ open in $X_{n}$, and let $x=(x_{1},\dots,x_{n})\in f^{-1}(C)$. Then $(x_{1},\dots,x_{n-1})\in V'$, so there is a basis element $V_{1}\times\cdots\times V_{n-1}$ of $X_{1}\times\cdots\times X_{n-1}$ with $(x_{1},\dots,x_{n-1})\in V_{1}\times\cdots\times V_{n-1}\subset V'$. Then $B=V_{1}\times\cdots\times V_{n}$ is a basis element of $X_{1}\times\cdots\times X_{n}$ containing $x$, and $B\subset f^{-1}(C)$: for $y\in B$ one has $(y_{1},\dots,y_{n-1})\in V'$ and $y_{n}\in V_{n}$, so $f(y)\in V'\times V_{n}=C$. Hence every point of $f^{-1}(C)$ has a basis element around it inside $f^{-1}(C)$, so $f^{-1}(C)$ is open, and $f$ is continuous (Theorem 18.1).
:::

:::

::: {.pf-step #inverse-continuous}
$f^{-1}$ is continuous.

::: pf-proof
Let $B=U_{1}\times\cdots\times U_{n}$ be a basis element of $X_{1}\times\cdots\times X_{n}$, with each $U_{k}$ open in $X_{k}$. Then
$$
(f^{-1})^{-1}(B)=f(B)=(U_{1}\times\cdots\times U_{n-1})\times U_{n}
$$
by step [](#images){.pf-ref}. The set $U_{1}\times\cdots\times U_{n-1}$ is open in $X_{1}\times\cdots\times X_{n-1}$ and $U_{n}$ is open in $X_{n}$, so the right-hand side is a basis element of $(X_{1}\times\cdots\times X_{n-1})\times X_{n}$, hence open. So the preimage under $f^{-1}$ of every basis element is open, and $f^{-1}$ is continuous.
:::

:::

::: {.pf-step}
$f$ is a homeomorphism.

::: pf-proof
A homeomorphism is a continuous bijection with continuous inverse. Steps [](#bijection){.pf-ref}, [](#f-continuous){.pf-ref} and [](#inverse-continuous){.pf-ref} provide exactly this.
:::

:::

:::
:::
