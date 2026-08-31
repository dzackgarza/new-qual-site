---
schema: qual/card@1
id: P-AMD-7IWMHJHE
kind: problem
title: Hexagon with identifications $a+b+c-a-b-c$
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
A hexagon with the identifications $a+b+c-a-b-c$
:::

::: {.solution}
**Goal:** Identify the closed 2-dimensional surface $X$ represented by a regular hexagon whose perimeter edges are identified according to the boundary word $w = a b c a^{-1} b^{-1} c^{-1}$, compute its Euler characteristic $\chi(X)$, classify the surface, and determine its fundamental group $\pi_1(X)$.

<1>1. Cellular structure of the polygonal quotient $X$.
  <2>1. 2-cells: There is 1 two-cell $e^2$ (the hexagon interior).
  <2>2. 1-cells: There are 3 one-cells, corresponding to the edge labels $a, b, c$.
  <2>3. 0-cells: Determine the vertex identification classes from the boundary word $a b c a^{-1} b^{-1} c^{-1}$.
  - Label the 6 vertices of the hexagon sequentially around the perimeter as $v_0, v_1, v_2, v_3, v_4, v_5$ so that the directed edges are:
    - Edge 1 ($a$): $v_0 \to v_1$,
    - Edge 2 ($b$): $v_1 \to v_2$,
    - Edge 3 ($c$): $v_2 \to v_3$,
    - Edge 4 ($a^{-1}$): $v_3 \to v_4$ (so the second $a$-edge is directed $v_4 \to v_3$),
    - Edge 5 ($b^{-1}$): $v_4 \to v_5$ (so the second $b$-edge is directed $v_5 \to v_4$),
    - Edge 6 ($c^{-1}$): $v_5 \to v_0$ (so the second $c$-edge is directed $v_0 \to v_5$).
  - Vertex identifications:
    - The two $a$-edges are $v_0 \to v_1$ and $v_4 \to v_3$, so $v_0 \sim v_4$ and $v_1 \sim v_3$.
    - The two $b$-edges are $v_1 \to v_2$ and $v_5 \to v_4$, so $v_1 \sim v_5$ and $v_2 \sim v_4$.
    - The two $c$-edges are $v_2 \to v_3$ and $v_0 \to v_5$, so $v_2 \sim v_0$ and $v_3 \sim v_5$.
  - Chaining these identifications gives two equivalence classes:
    - Vertex Class 1: $\{v_0, v_2, v_4\}$ (since $v_0 \sim v_4$, $v_4 \sim v_2$, $v_2 \sim v_0$),
    - Vertex Class 2: $\{v_1, v_3, v_5\}$ (since $v_1 \sim v_3$, $v_3 \sim v_5$, $v_5 \sim v_1$).
::: {.proof}
  <2>4. Each edge label appears twice, once in each orientation, so the start and end vertices of the two copies of each edge are identified pairwise; tracing these identifications gives the two classes $\{v_0, v_2, v_4\}$ and $\{v_1, v_3, v_5\}$.
:::

<1>2. Compute the Euler characteristic $\chi(X)$ and classify the surface.
  <2>1. Let $V = 2$ (number of 0-cells), $E = 3$ (number of 1-cells $a, b, c$), and $F = 1$ (the single 2-cell).
  <2>2. The Euler characteristic is:
  $$\chi(X) = V - E + F = 2 - 3 + 1 = 0.$$
  <2>3. Orientability: in the boundary word $w = a b c a^{-1} b^{-1} c^{-1}$, each letter $a, b, c$ appears twice with opposite exponents ($+1$ and $-1$), so the surface is orientable.
  <2>4. A closed connected orientable surface of genus $g$ has $\chi = 2 - 2g$; solving $2 - 2g = 0$ gives $g = 1$.
::: {.proof}
  <2>5. The Euler–Poincaré formula gives $\chi = V - E + F = 0$, and the classification of closed orientable surfaces identifies the unique such surface as the torus $T^2$.
:::

<1>3. Fundamental group $\pi_1(X)$.
  <2>1. The 1-skeleton has $V = 2$ vertices and $E = 3$ edges, so a maximal tree $T$ has $V - 1 = 1$ edge; take $T$ to be the edge $a$.
  <2>2. Collapsing $T$ leaves $E - (V - 1) = 3 - 1 = 2$ generators, namely $b$ and $c$, in the quotient 1-skeleton $X^1 / T \cong S^1 \vee S^1$.
  <2>3. Setting $a = 1$ in the boundary word reduces it to $b c b^{-1} c^{-1}$, so the relation from the 2-cell is $b c b^{-1} c^{-1} = 1$, i.e. $bc = cb$.
  <2>4. Thus $\pi_1(X) \cong \langle b, c \mid b c b^{-1} c^{-1} = 1 \rangle \cong \mathbb{Z}^2$.
::: {.proof}
  <2>5. The cellular Seifert–van Kampen theorem gives $\pi_1(X) \cong \pi_1(X^1)/\langle\langle [\phi] \rangle\rangle$; collapsing the maximal tree $T$ identifies $\pi_1(X^1)$ with the free group on $b, c$, and the attaching word $b c b^{-1} c^{-1}$ imposes the single relation $bc = cb$, yielding $\mathbb{Z}^2$.
:::

<1>4. Q.E.D.
::: {.proof}
  <2>1. Steps <1>1–<1>3 show that $X$ is the torus: $\chi(X) = 0$ and $\pi_1(X) \cong \mathbb{Z}^2$.
:::
:::

