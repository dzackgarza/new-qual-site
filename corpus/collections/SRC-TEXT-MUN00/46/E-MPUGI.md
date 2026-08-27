---
schema: qual/card@1
id: E-MPUGI
kind: exercise
title: Products with a locally compact Hausdorff factor preserve quotient maps
subtitle: Munkres §46.9
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
---

::: {.exercise}

Here is an application of Theorem 46.11 to quotient maps.
(Compare [[E-S57IX]].)

Theorem.
If $p: A \to B$ is a quotient map and $X$ is locally compact Hausdorff, then $i_X \times p: X \times A \to X \times B$ is a quotient map.

(a) Let $Y$ be the quotient space induced by $i_X \times p$; let $q: X \times A \to Y$ be the quotient map.
Show there is a bijective continuous map $f: Y \to X \times B$ such that $f \circ q = i_X \times p$.

(b) Let $g = f^{-1}$.
Let $G: B \to \mathcal{C}(X, Y)$ and $Q: A \to \mathcal{C}(X, Y)$ be the maps induced by $g$ and $q$, respectively.
Show that $Q = G \circ p$.

(c) Show that $Q$ is continuous; conclude that $G$ is continuous, so that $g$ is continuous.
:::
