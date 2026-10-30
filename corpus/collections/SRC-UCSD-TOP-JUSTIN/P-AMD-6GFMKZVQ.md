---
schema: qual/card@1
id: P-AMD-6GFMKZVQ
kind: problem
title: Fundamental group of the torus from the hexagon model
classification:
  areas:
    - topology
  topics:
    - Fundamental Group
    - Surfaces
relations: []
review: draft
audit:
  - event: solution-written
    by: gemini-3.7-flash
    date: 2026-08-25
---

::: {.problem}
Recall from Sheet 2 that the torus $T$ can be made from a solid hexagon with sides glued in pairs according to the labelled arrows.
Use van Kampen's theorem to compute a presentation of the fundamental group, and show that it is isomorphic to $\ZZ^2$.
:::

::: {.solution}

::: pf

::: {.pf-step #cw}

The hexagon model gives $T$ a CW structure with two $0$-cells $u,w$, three $1$-cells $a,b,c$, each joining $u$ to $w$, and one $2$-cell attached along the word
$$abca^{-1}b^{-1}c^{-1}.$$

::: pf-proof

Number the sides $1,\dots,6$ counterclockwise. Side $i+3$ is the translate of side $i$, and the counterclockwise boundary runs along side $i+3$ against the translated direction of side $i$; this gives the word. The translations identify alternate corners of the hexagon, so the six corners fall into two classes $u,w$ of three, and each side joins a corner of one class to a corner of the other.

:::

:::

::: {.pf-step #vk}

$\pi_1(T)\cong\langle a,b,c\mid c,\ abca^{-1}b^{-1}c^{-1}\rangle$.

::: pf-proof

The $1$-skeleton is a graph with two vertices and three edges. The edge $c$ is a maximal tree, so the $1$-skeleton has free fundamental group on $a,b,c$ with $c=1$. By van Kampen's theorem, attaching the $2$-cell adds its boundary word as a relator (Hatcher, Proposition 1.26).

:::

:::

::: pf-qed

Eliminating $c$ with the relator $c$ gives
$$\boxed{\pi_1(T)\cong\langle a,b\mid aba^{-1}b^{-1}\rangle\cong\ZZ^2.}$$
The isomorphism sends $a\mapsto(1,0)$ and $b\mapsto(0,1)$. It is well defined because $\ZZ^2$ is abelian, and its inverse $(m,n)\mapsto a^mb^n$ is a homomorphism because $a$ and $b$ commute in the presented group; the two composites fix the generators.

:::

:::

:::
