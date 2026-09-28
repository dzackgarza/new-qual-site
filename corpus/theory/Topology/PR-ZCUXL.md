---
schema: qual/card@1
id: PR-ZCUXL
kind: proposition
title: Continuous images of compact, connected and separable spaces
slogan: 'Continuous images preserve compactness, connectedness, and separability.'
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Compactness
  - Connectedness
  - Density
relations: []
review: draft
---

::: {.proposition}
Let $f\colon X\to Y$ be continuous.

- If $X$ is compact, then $f(X)$ is compact [@Mun00].

- If $X$ is connected, then $f(X)$ is connected [@Mun00].

- If $D\subseteq X$ is dense, then $f(D)$ is dense in $f(X)$ with the subspace topology; in particular, if $X$ is separable, then so is $f(X)$, and if $f$ is surjective, then $f(D)$ is dense in $Y$.
:::

::: {.remark}
A continuous map need not be [[D-CTGON|open or closed]]: the constant map $\RR\to\RR$, $x\mapsto 0$, sends the open set $\RR$ to $\ts{0}$, which is not open, and $x\mapsto e^x$ sends the closed set $\RR$ to $(0,\infty)$, which is not closed in $\RR$.
:::
