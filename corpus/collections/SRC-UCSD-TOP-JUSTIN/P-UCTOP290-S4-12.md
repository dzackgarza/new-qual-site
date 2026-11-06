---
schema: qual/card@1
id: P-UCTOP290-S4-12
kind: problem
title: Three-sheeted cover with opposite loop shifts
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 4, Problem 12 against its extraction and PDF page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 4, problem 12
    (assets/attachments/UCSD_290_F14_sheet4.pdf, printed page 254), from the
    checked-in extraction and a 300 dpi render. The printed problem identifies
    pi_1(S^1 vee S^1) with <a,b> and asks for the cover corresponding to the
    kernel of F_2 -> Z_3 sending a to 1 and b to 2. The card states exactly this,
    so no repair was needed.
---

::: {.problem}
Let $F_2=\pi_1(S^1\vee S^1)=\langle a,b\rangle$, and let
$\phi:F_2\to\ZZ/3$ send $a$ to $1$ and $b$ to $2$.
Construct the covering space corresponding to $\ker\phi$.
:::

::: {.solution}

Let $F_2=\langle a,b\rangle=\pi_1(S^1\vee S^1)$ and let $\phi\colon
F_2\to\ZZ/3$ send $a\mapsto1$ and $b\mapsto2$.

::: pf

::: {.pf-step #cover}

The labelled graph with vertices $0,1,2\in\ZZ/3$, an $a$-edge $i\to i+1$ and a
$b$-edge $i\to i+2$ at every vertex, is a connected three-sheeted covering of
$S^1\vee S^1$.

::: pf-proof

For each label, $i\mapsto i+1$ and $i\mapsto i+2$ are bijections of $\ZZ/3$,
so every vertex has exactly one incoming and one outgoing edge of each label,
which is the covering condition; the $a$-edges form the cycle $0\to1\to2\to0$,
so the graph is connected; it has three vertices, one for each sheet. Mapping
every vertex to the wedge point and every labelled edge onto the circle of its
label gives the covering map.

:::

:::

::: {.pf-step #subgroup}

The subgroup of this cover at the vertex $0$ is exactly $\ker\phi$.

::: pf-proof

A word $w$ lifted from $0$ ends at the vertex
$1\cdot\abs{w}_a+2\cdot\abs{w}_b$ in $\ZZ/3$, where $\abs{w}_a$ and
$\abs{w}_b$ are the exponent sums in the two letters; reading the lifted loop
down in $S^1\vee S^1$ returns $w$, so the loops at $0$ are the words whose
total exponent sum is $\phi(w)=0$. The covering map injects on fundamental
groups, so the subgroup is precisely $\ker\phi$.

:::

:::

::: {.pf-step #deck}

The cover is regular with deck group $\ZZ/3$, acting by translation of the
vertex labels, and $\ker\phi$ has index $3$ and rank $4$.

::: pf-proof

$\ker\phi$ is a kernel, hence normal, and $F_2/\ker\phi\cong\ZZ/3$, so the
deck group is $\ZZ/3$ and acts by translation of the vertices $i\mapsto
i+\phi(h)$ for a deck transformation induced by $h$. The graph has three
vertices and six edges, so its fundamental group is free of rank $1-3+6=4$,
which is also $1+3(2-1)$ for a three-sheeted cover of a wedge of two circles.

:::

:::

:::


:::
