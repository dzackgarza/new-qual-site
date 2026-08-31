---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F08-17
kind: problem
title: The surface with polygonal symbol $xy^{-1}x^{-1}zwz^{-1}\nu yw^{-1}\nu^{-1}$, and
  classification of closed surfaces by even-sided polygons
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Classification
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
(i) The polygonal symbol of a certain surface without boundary is $xy^{-1}x^{-1}zwz^{-1}\nu yw^{-1}\nu^{-1}$.
Identify the surface.
What is its Euler characteristic?

(ii) Explain how polygons with an even number of sides may be used to classify surfaces without boundary.
You do not need to give detailed proofs.
:::

::: {.solution}
**Part (i).**

<1>1. The symbol has $10$ sides, and each of the five letters $x, y, z, w, \nu$ appears once with a positive and once with a negative exponent.
::: {.proof}
read off the symbol.
:::

<1>2. Hence the surface is orientable.
::: {.proof}
a surface is orientable iff each edge appears once with each orientation.
:::

<1>3. The number of edges after identification is $E = 5$ and the number of faces is $F = 1$.
::: {.proof}
five pairs of identified edges, one polygon.
:::

<1>4. The number of vertices after identification is $V = 2$.
<2>1. Label the vertices $v_0, \ldots, v_9$ in order around the polygon.
::: {.proof}
setup.
:::
<2>2. The edge identifications give $v_0 \sim v_3 \sim v_6$ and $v_1 \sim v_2 \sim v_4 \sim v_5 \sim v_7 \sim v_8 \sim v_9$.
::: {.proof}
tracing the identifications: $x$ gives $v_0 \sim v_3$ and $v_1 \sim v_2$; $y$ gives $v_7 \sim v_2$ and $v_8 \sim v_1$; $z$ gives $v_3 \sim v_6$ and $v_4 \sim v_5$; $w$ gives $v_4 \sim v_9$ and $v_5 \sim v_8$; $\nu$ gives $v_6 \sim v_0$ and $v_7 \sim v_9$. Chaining these yields exactly two equivalence classes.
:::
<2>3. Hence $V = 2$.
::: {.proof}
<2>2.
:::

<1>5. The Euler characteristic is $\chi = V - E + F = 2 - 5 + 1 = -2$.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. For an orientable surface of genus $g$, $\chi = 2 - 2g$, so $-2 = 2 - 2g$ gives $g = 2$.
::: {.proof}
solve for $g$.
:::

<1>7. Hence the surface is the orientable surface of genus $2$ (the connected sum of two tori), with Euler characteristic $-2$.
::: {.proof}
<1>5 and <1>6.
:::

**Part (ii).**

<1>1. Every closed (boundaryless) surface can be represented by a polygon with an even number of sides, whose sides are identified in pairs.
::: {.proof}
a surface is obtained from a $2n$-gon by identifying its $2n$ sides in $n$ pairs.
:::

<1>2. The classification is obtained by reducing the polygonal symbol to a normal form using elementary operations (cutting and pasting).
::: {.proof}
the standard operations (cutting along a diagonal and regluing) transform any symbol into a canonical form.
:::

<1>3. The normal forms are:
- orientable: $a_1 b_1 a_1^{-1} b_1^{-1} \cdots a_g b_g a_g^{-1} b_g^{-1}$ (genus $g$);
- nonorientable: $a_1 a_1 a_2 a_2 \cdots a_g a_g$ (genus $g$).
::: {.proof}
the classification theorem for surfaces.
:::

<1>4. The genus (and orientability) is read off from the normal form, and the Euler characteristic is $\chi = 2 - 2g$ (orientable) or $\chi = 2 - g$ (nonorientable).
::: {.proof}
standard formulas.
:::

<1>5. Q.E.D.
::: {.proof}
<1>7 (i) and <1>3–<1>4 (ii).
:::
:::
