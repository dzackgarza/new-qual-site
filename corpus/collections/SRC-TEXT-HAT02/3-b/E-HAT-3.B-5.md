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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Issue #170's continuation, outside the sections already closed. Read against Hatcher, Exercise 5
    of §3.B, printed p. 280 — the §3.B exercises 1--5 are on that page, checked at PDF page 289 of
    the held book — with its two displayed formulas and its bracketed remark. Checked: the
    chain-level formula and the computation
    $\partial(e^i\times e^j)=\partial e^i\times e^j+(-1)^ie^i\times\partial e^j$ giving
    $\varphi(e^j)\partial e^i$ for a cocycle $\varphi$; the cohomological formula and the cocycle
    condition $\varphi(\partial c\times d)=\varphi(\partial(c\times d))=0$ for a cycle $d$; and the
    closing paragraph on changes of representatives, including the sign $(-1)^{n-j+1}$ displayed in
    it. One structural repair: two steps whose entire proof was a reference to another step, and a
    `pf-qed` whose entire argument was "Steps s2 and s4", are removed and their content folded into
    the steps that carry it — the chain-map computation into the well-definedness step, the cocycle
    condition into the cohomological one. The mathematics is unchanged.
---

::: {.problem}
Show that slant products

$$H_n(X \times Y; R) \times H^j(Y; R) \to H_{n-j}(X; R), \quad (e^i \times e^j, \varphi) \mapsto \varphi(e^j) e^i$$

$$H^n(X \times Y; R) \times H_j(Y; R) \to H^{n-j}(X; R), \quad (\varphi, e^j) \mapsto (e^i \mapsto \varphi(e^i \times e^j))$$

can be defined via the indicated cellular formulas.
[These "products" are in some ways more like division than multiplication, and this is reflected in the common notation $a/b$ for them, or $a \backslash b$ when the order of the factors is reversed. The first of the two slant products is related to cap product in the same way that the cohomology cross product is related to cup product.]
:::

::: {.solution}
The exercise is §3.B Exercise 5, printed p. 280.

::: pf

::: {.pf-step #s1}
The first slant product is defined on cellular chains by
$$H_n(X\times Y)\times H^j(Y)\to H_{n-j}(X),\qquad (e^i\times e^j,\ \varphi)\mapsto \varphi(e^j)\,e^i .$$

::: pf-proof
This is the definition on cellular chains, extended bilinearly; $e^i$ is an $i$-cell of $X$ and $e^j$ a $j$-cell of $Y$.
:::

:::

::: {.pf-step #s2}
For a cocycle $\varphi$ the formula is a chain map, so it is well defined on homology.

::: pf-proof
The boundary of a product cell is $\partial(e^i\times e^j)=\partial e^i\times e^j+(-1)^i e^i\times\partial e^j$, and applying the slant product gives $\varphi(e^j)\,\partial e^i$ because $\varphi(\partial e^j)=0$; that is the boundary of $\varphi(e^j)e^i$. Hence the slant product of a cycle is a cycle and the slant product of a boundary is a boundary, which is exactly the assertion.
:::

:::

::: {.pf-step #s3}
The second slant product is defined on cellular chains by
$$H^n(X\times Y)\times H_j(Y)\to H^{n-j}(X),\qquad (\varphi,\ e^j)\mapsto\bigl(e^i\mapsto \varphi(e^i\times e^j)\bigr).$$

::: pf-proof
This is the definition on cellular chains, extended bilinearly.
:::

:::

::: {.pf-step #s4}
For a cocycle $\varphi$ and a cycle $d$ the cochain $c\mapsto\varphi(c\times d)$ is a cocycle, so the formula is well defined on cohomology.

::: pf-proof
The product boundary formula and $\partial d=0$ give $\varphi(\partial c\times d)=\varphi(\partial(c\times d))=0$, which says that the cochain is a cocycle.
:::

:::

:::

The formulas also respect changes of representatives. For the first product, if $\varphi=\delta\psi$ and $z$ is a cellular cycle of total degree $n$, the product boundary formula gives $z/\varphi=(-1)^{n-j+1}\partial(z/\psi)$, so its homology class is zero. If $z=\partial w$ and $\varphi$ is a cocycle, then $z/\varphi=\partial(w/\varphi)$. For the second product, if $d=\partial e$ and $\varphi$ is a cocycle, then for a cell $c$ of degree $n-j$,
$$
\varphi(c\times\partial e)=(-1)^{n-j+1}\varphi(\partial c\times e),
$$
so $\varphi/d$ is a coboundary. If $\varphi=\delta\theta$ and $d$ is a cycle, then $\varphi/d=\delta(\theta/d)$. Thus both formulas descend to the stated homology and cohomology products.

:::
