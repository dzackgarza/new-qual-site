---
schema: qual/card@1
id: P-FVQWC
kind: problem
title: The surface with polygonal symbol $xyzxy^{-1}z^{-1}$
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Classification
  - Quotient Spaces
relations: []
review: draft
---

::: {.problem}
What surface is represented by the $6\dash$gon with edges identified according to the symbol $xyzx\inverseof{y} \inverseof{z}$ ?
:::

::: {.solution}

::: pf

::: pf-step

Label the six polygon vertices cyclically $v_0,\dots,v_5$.
The edge pairings identify all six vertices.

::: pf-proof

The two $x$-edges have the same orientation, giving $v_0\sim v_3$ and $v_1\sim v_4$.
The $y,y^{-1}$ pairing gives $v_1\sim v_5$ and $v_2\sim v_4$.
The $z,z^{-1}$ pairing gives $v_2\sim v_0$ and $v_3\sim v_5$.
These relations put every vertex in one equivalence class.

:::

:::

::: pf-step

The quotient therefore has one vertex, three edges, and one $2$-cell, so
$$\chi=1-3+1=-1.$$

::: pf-proof

There is one quotient edge for each of the labels $x,y,z$.

:::

:::

::: pf-step

The quotient surface is nonorientable.

::: pf-proof

The label $x$ occurs twice with the same boundary orientation. In an orientable polygon presentation, each edge label must occur once in each orientation; a same-direction pairing produces a crosscap.

:::

:::

::: pf-step

A closed connected nonorientable surface $N_h=\#^h\mathbb{RP}^2$ has Euler characteristic $2-h$. Hence $2-h=-1$, so $h=3$.

::: pf-proof

Apply the classification theorem for closed connected surfaces.

:::

:::

::: pf-step

Thus the polygon represents
$$\boxed{\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2.}$$

::: pf-proof

This is the unique closed connected nonorientable surface of Euler characteristic $-1$.

:::

:::

:::

:::
