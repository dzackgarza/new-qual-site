---
schema: qual/card@1
id: D-JOINX
kind: definition
title: Join of spaces
prompts:
- What is the join $X\ast Y$ of two spaces?
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces and $I=[0,1]$.
The \dfn{join} $X\ast Y$ is the quotient of $X\cross Y\cross I$ by the identifications $(x,y_1,0)\sim(x,y_2,0)$ for all $x\in X$ and $y_1,y_2\in Y$, and $(x_1,y,1)\sim(x_2,y,1)$ for all $x_1,x_2\in X$ and $y\in Y$ [@Hat02, Chapter 0].
:::

::: {.remark}
A point of $X\ast Y$ is a formal linear combination $t_1x+t_2y$ with $0\leq t_1,t_2\leq 1$ and $t_1+t_2=1$, subject to $0x+1y=y$ and $1x+0y=x$.
The join $X\ast S^0$ is the [[D-RZKQD|suspension]] $SX$, and the join of a point with $Y$ is the [[D-II4M4|cone]] $CY$.
:::
