---
schema: qual/card@1
id: E-HAT-3.B-5
kind: problem
title: "Slant products"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.B, Exercise 5; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both definitions and the four invariance checks: for the homology product a cocycle kills
    the $\partial e^j$ summand and a boundary in the first variable gives a boundary; for the
    cohomology product a cycle in the second variable makes the cochain a cocycle, a cocycle
    $\varphi$ and a singular boundary give a coboundary through the swap sign $(-1)^{n-j+1}$, and
    $\varphi=\delta\theta$ gives a coboundary.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Rendering repair only, with the mathematics rechecked: five occurrences of $\varphi$ and one of
    $\varphi=\delta\theta$ were written with a doubled backslash, which renders as a literal
    "\\varphi" and which the schema check does not catch; they are now single. The argument itself
    is unchanged and checked against the two printed formulas of p.280 — for the first product the
    slant product of a boundary is φ(e^j) times the boundary of e^i, so it is a chain map, and the
    four invariance checks run through the swap sign (-1)^{n-j+1}.
---

::: {.problem}
Show that slant products

$$H_n(X \times Y; R) \times H^j(Y; R) \to H_{n-j}(X; R), \quad (e^i \times e^j, \varphi) \mapsto \varphi(e^j) e^i$$

$$H^n(X \times Y; R) \times H_j(Y; R) \to H^{n-j}(X; R), \quad (\varphi, e^j) \mapsto (e^i \mapsto \varphi(e^i \times e^j))$$

can be defined via the indicated cellular formulas.
[These "products" are in some ways more like division than multiplication, and this is reflected in the common notation $a/b$ for them, or $a \backslash b$ when the order of the factors is reversed. The first of the two slant products is related to cap product in the same way that the cohomology cross product is related to cup product.]
:::

::: {.solution}

::: pf

::: pf-step

First slant product: define $H_n(X \times Y) \times H^j(Y) \to H_{n-j}(X)$ on cellular chains by $(e^i \times e^j, \varphi) \mapsto \varphi(e^j) e^i$, where $e^i$ is an $i$-cell of $X$ and $e^j$ a $j$-cell of $Y$.

::: pf-proof

definition on the cellular level.

:::

:::

::: {.pf-step #s2}

This is well-defined on homology.

::: pf-proof

::: {.pf-step #s2-1}

The formula is bilinear and compatible with the boundary maps.

::: pf-proof

$\partial(e^i \times e^j) = \partial e^i \times e^j + (-1)^i e^i \times \partial e^j$, and applying the slant product (with $\varphi$ a cocycle, so $\varphi(\partial e^j) = 0$) gives $\varphi(e^j)\partial e^i$, which is the boundary of $\varphi(e^j) e^i$; hence the slant product is a chain map.

:::

:::

::: pf-step

Hence it induces a well-defined map on homology.

::: pf-proof

Step [](#s2-1){.pf-ref}.

:::

:::

:::

:::

::: pf-step

Second slant product: define $H^n(X \times Y) \times H_j(Y) \to H^{n-j}(X)$ by $(\varphi, e^j) \mapsto (e^i \mapsto \varphi(e^i \times e^j))$.

::: pf-proof

definition on the cellular level.

:::

:::

::: {.pf-step #s4}

This is well-defined on cohomology.

::: pf-proof

::: {.pf-step #s4-1}

The formula is bilinear and compatible with the coboundary maps.

::: pf-proof

Extend the displayed formula linearly to a cellular cycle $d$ in $Y$. If $\varphi$ is a cocycle, then the resulting cochain $c\mapsto\varphi(c\times d)$ is a cocycle: the product boundary formula and $\partial d=0$ give $\varphi(\partial c\times d)=\varphi(\partial(c\times d))=0$.

:::

:::

::: pf-step

Hence it induces a well-defined map on cohomology.

::: pf-proof

Step [](#s4-1){.pf-ref}.

:::

:::

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

The formulas also respect changes of representatives. For the first product, if $\varphi=\delta\psi$ and $z$ is a cellular cycle of total degree $n$, the product boundary formula gives $z/\varphi=(-1)^{n-j+1}\partial(z/\psi)$, so its homology class is zero. If $z=\partial w$ and $\varphi$ is a cocycle, then $z/\varphi=\partial(w/\varphi)$. For the second product, if $d=\partial e$ and $\varphi$ is a cocycle, then for a cell $c$ of degree $n-j$,
$$
\varphi(c\times\partial e)=(-1)^{n-j+1}\varphi(\partial c\times e),
$$
so $\varphi/d$ is a coboundary. If $\varphi=\delta\theta$ and $d$ is a cycle, then $\varphi/d=\delta(\theta/d)$. Thus both formulas descend to the stated homology and cohomology products.

:::
