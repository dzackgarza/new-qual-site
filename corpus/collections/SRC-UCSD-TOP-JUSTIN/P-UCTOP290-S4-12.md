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
---

::: {.problem}
Let $F_2=\pi_1(S^1\vee S^1)=\langle a,b\rangle$, and let
$\phi:F_2\to\ZZ/3$ send $a$ to $1$ and $b$ to $2$.
Construct the covering space corresponding to $\ker\phi$.
:::

::: {.solution}

Take three vertices labeled $0,1,2$ modulo $3$.
For each $i$, draw the $a$-edge
$$
i\xrightarrow{a}i+1
$$
and the $b$-edge
$$
i\xrightarrow{b}i+2.
$$
Map every vertex to the wedge point, and map each labeled edge
homeomorphically onto its corresponding circle. Every vertex has
exactly one incoming and one outgoing edge of each label, so this
graph is a cover. It is connected because the $a$-edges form a
three-cycle.

A lifted word starting at $0$ ends at vertex $\phi(w)$.
Consequently the based loops in this graph read exactly
$\ker\phi$, as required. The cover is regular, with deck group
$\ZZ/3$ acting by translation on the vertex labels.

:::
