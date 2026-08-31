---
schema: qual/card@1
id: P-OSZPJ
kind: problem
title: Cell structure and homology of the torus $S^1\times S^1$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Describe a cell complex structure on the torus $T = S^1 \times S^1$ and use this to compute the homology groups of $T$.

> To justify your answer you will need to consider the attaching maps in detail.
:::

::: {.solution}
<1>1. Give $T = S^1 \times S^1$ a cell structure with one $0$-cell $e^0$, two $1$-cells $a, b$, and one $2$-cell $e^2$.
::: {.proof}
the standard CW structure on the torus, obtained from the square $[0,1]^2$ by identifying opposite edges.
:::

<1>2. The $1$-skeleton is $S^1 \vee S^1$, and the $2$-cell is attached by the map $aba^{-1}b^{-1}$.
::: {.proof}
the boundary of the square is traversed as $a$ then $b$ then $a$ reversed then $b$ reversed, giving the attaching word $aba^{-1}b^{-1}$.
:::

<1>3. The cellular chain complex is
$$0 \to \ZZ \xrightarrow{d_2} \ZZ^2 \xrightarrow{d_1} \ZZ \to 0.$$
::: {.proof}
one cell in each of dimensions $0, 2$ and two cells in dimension $1$.
:::

<1>4. $d_1 = 0$.
::: {.proof}
the boundary of each $1$-cell is $e^0 - e^0 = 0$ (both endpoints are the single $0$-cell).
:::

<1>5. $d_2 = 0$.
::: {.proof}
the attaching map $aba^{-1}b^{-1}$ has each generator appearing once positively and once negatively, so the boundary of $e^2$ is $a + b - a - b = 0$.
:::

<1>6. Hence $H_0(T) = \ZZ$, $H_1(T) = \ZZ^2$, $H_2(T) = \ZZ$, and $H_n(T) = 0$ for $n \ge 3$.
::: {.proof}
<1>3–<1>5, computing homology of the chain complex with all differentials zero.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
