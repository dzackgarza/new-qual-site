---
schema: qual/card@1
id: E-HAT-3.B-5
kind: exercise
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
---

Show that slant products

$$H_n(X \times Y; R) \times H^j(Y; R) \to H_{n-j}(X; R), \quad (e^i \times e^j, \varphi) \mapsto \varphi(e^j) e^i$$

$$H^n(X \times Y; R) \times H_j(Y; R) \to H^{n-j}(X; R), \quad (\varphi, e^j) \mapsto (e^i \mapsto \varphi(e^i \times e^j))$$

can be defined via the indicated cellular formulas.
[These "products" are in some ways more like division than multiplication, and this is reflected in the common notation $a/b$ for them, or $a \backslash b$ when the order of the factors is reversed. The first of the two slant products is related to cap product in the same way that the cohomology cross product is related to cup product.]

::: {.solution}
<1>1. First slant product: define $H_n(X \times Y) \times H^j(Y) \to H_{n-j}(X)$ on cellular chains by $(e^i \times e^j, \varphi) \mapsto \varphi(e^j) e^i$, where $e^i$ is an $i$-cell of $X$ and $e^j$ a $j$-cell of $Y$.
::: {.proof}
definition on the cellular level.
:::

<1>2. This is well-defined on homology.
<2>1. The formula is bilinear and compatible with the boundary maps.
::: {.proof}
$\partial(e^i \times e^j) = \partial e^i \times e^j + (-1)^i e^i \times \partial e^j$, and applying the slant product (with $\varphi$ a cocycle, so $\varphi(\partial e^j) = 0$) gives $\varphi(e^j)\partial e^i$, which is the boundary of $\varphi(e^j) e^i$; hence the slant product is a chain map.
:::
<2>2. Hence it induces a well-defined map on homology.
::: {.proof}
<2>1.
:::

<1>3. Second slant product: define $H^n(X \times Y) \times H_j(Y) \to H^{n-j}(X)$ by $(\varphi, e^j) \mapsto (e^i \mapsto \varphi(e^i \times e^j))$.
::: {.proof}
definition on the cellular level.
:::

<1>4. This is well-defined on cohomology.
<2>1. The formula is bilinear and compatible with the coboundary maps.
::: {.proof}
if $\varphi$ is a cocycle, then the resulting cochain $e^i \mapsto \varphi(e^i \times e^j)$ is a cocycle (its coboundary vanishes since $\delta\varphi = 0$ and $\partial e^j = 0$ for a cycle $e^j$).
:::
<2>2. Hence it induces a well-defined map on cohomology.
::: {.proof}
<2>1.
:::

<1>5. Q.E.D.
::: {.proof}
<1>2 and <1>4.
:::
:::
