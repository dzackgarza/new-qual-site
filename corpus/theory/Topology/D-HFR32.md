---
schema: qual/card@1
id: D-HFR32
kind: definition
title: Homotopy equivalence
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
A continuous map $f\colon X\to Y$ is a \dfn{homotopy equivalence} if there is a continuous map $g\colon Y\to X$ with $f\circ g\simeq\id_Y$ and $g\circ f\simeq\id_X$, where $\simeq$ denotes [[D-Z7I7F|homotopy]].
Such a map $g$ is a \dfn{homotopy inverse} of $f$.
The spaces $X$ and $Y$ are \dfn{homotopy equivalent}, or have the same \dfn{homotopy type}, written $X\simeq Y$, if there is a homotopy equivalence $X\to Y$.
:::

::: {.example}
Every [[D-9KQZT|homeomorphism]] is a homotopy equivalence, and the converse fails: for $n\geq 1$ the inclusion $\ts{0}\hookrightarrow\RR^n$ is a homotopy equivalence, with homotopy inverse the constant map $\RR^n\to\ts{0}$ and homotopy $H(x, t) = tx$ from the constant map to $\id_{\RR^n}$, but $\ts{0}$ and $\RR^n$ are not homeomorphic.
:::
