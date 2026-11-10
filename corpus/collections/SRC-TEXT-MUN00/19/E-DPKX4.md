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
---

::: {.exercise}

Show that $(X_1 \times \cdots \times X_{n-1}) \times X_n$ is homeomorphic with $X_1 \times \cdots \times X_n$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 19.4, printed p. 191** (`tmp/sources/munkres-solutions-whitman.pdf`); the map and the two continuity arguments are his.

Since the index set $\{1,\dots,n\}$ is finite, the box and product topologies on these finite products coincide, and we use the box description. Define
$$
f:X_{1}\times\cdots\times X_{n}\longrightarrow (X_{1}\times\cdots\times X_{n-1})\times X_{n},\qquad
f(x_{1},\dots,x_{n})=\big((x_{1},\dots,x_{n-1}),x_{n}\big).
$$
It is a bijection, with inverse $\big((x_{1},\dots,x_{n-1}),x_{n}\big)\mapsto(x_{1},\dots,x_{n})$, and for subsets $A_{k}\subset X_{k}$ one has $f(A_{1}\times\cdots\times A_{n})=(A_{1}\times\cdots\times A_{n-1})\times A_{n}$.

*$f$ is continuous.* Let $C=V'\times V_{n}$ be a basis element of $(X_{1}\times\cdots\times X_{n-1})\times X_{n}$, with $V'$ open in $X_{1}\times\cdots\times X_{n-1}$ and $V_{n}$ open in $X_{n}$, and let $x\in f^{-1}(C)$. Then $(x_{1},\dots,x_{n-1})\in V'$, so there is a basis element $V_{1}\times\cdots\times V_{n-1}\subset V'$ of $X_{1}\times\cdots\times X_{n-1}$ containing $(x_{1},\dots,x_{n-1})$. Then $B=V_{1}\times\cdots\times V_{n}$ is a basis element of $X_{1}\times\cdots\times X_{n}$ containing $x$, and $B\subset f^{-1}(C)$: for $y\in B$ one has $(y_{1},\dots,y_{n-1})\in V'$ and $y_{n}\in V_{n}$, so $f(y)\in C$. Hence $f^{-1}(C)$ is open.

*$f^{-1}$ is continuous.* Let $B=U_{1}\times\cdots\times U_{n}$ be a basis element of $X_{1}\times\cdots\times X_{n}$. Then
$$
(f^{-1})^{-1}(B)=f(B)=(U_{1}\times\cdots\times U_{n-1})\times U_{n},
$$
a basis element of $(X_{1}\times\cdots\times X_{n-1})\times X_{n}$, because $U_{1}\times\cdots\times U_{n-1}$ is open there and $U_{n}$ is open in $X_{n}$.

So $f$ is a continuous bijection with continuous inverse: a homeomorphism.
:::
