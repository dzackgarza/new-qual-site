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

::: problem
What surface is represented by the $6\dash$gon with edges identified according to the symbol $xyzxy\inv z\inv$ ?
:::

::: {.solution}
<1>1. Label the six polygon vertices cyclically $v_0,\dots,v_5$. The edge pairings identify all six vertices.
::: {.proof}
The two $x$-edges have the same orientation, giving $v_0\sim v_3$ and $v_1\sim v_4$. The $y,y^{-1}$ pairing gives $v_1\sim v_5$ and $v_2\sim v_4$. The $z,z^{-1}$ pairing gives $v_2\sim v_0$ and $v_3\sim v_5$. These relations put every vertex in one equivalence class.
:::

<1>2. The quotient therefore has one vertex, three edges, and one $2$-cell, so
$$\chi=1-3+1=-1.$$
::: {.proof}
There is one quotient edge for each of the labels $x,y,z$.
:::

<1>3. The quotient surface is nonorientable.
::: {.proof}
The label $x$ occurs twice with the same boundary orientation. In an orientable polygon presentation, each edge label must occur once in each orientation; a same-direction pairing produces a crosscap.
:::

<1>4. A closed connected nonorientable surface $N_h=\#^h\mathbb{RP}^2$ has Euler characteristic $2-h$. Hence $2-h=-1$, so $h=3$.
::: {.proof}
Apply the classification theorem for closed connected surfaces.
:::

<1>5. Thus the polygon represents
$$\boxed{\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2.}$$
::: {.proof}
This is the unique closed connected nonorientable surface of Euler characteristic $-1$.
:::
:::
