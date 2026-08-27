---
schema: qual/card@1
id: PR-FL6T7
kind: proposition
title: Half-plane to Disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

:::{.proposition}
\[
F: \HH^\circ &\mapstofrom \DD^\circ \\
\ts{z\st \Im(z) > 0 } &\mapstofrom \ts{w\st \abs{w} < 1 } \\
z &\mapsto {i-z \over i+z} \\
i \qty{1-w \over 1+w} &\mapsfrom w
.\]

**Boundary behavior:**

- This maps $\RR\to \bd \DD$, where $F(\infty) = -1$, and as $x\in \RR$ ranges from $-\infty\to\infty$, $F(x)$ travels from $z=-1$ counter-clockwise through $S^1$ (starting at $z=-1$ and moving through the lower half first).

![](../../assets/figures/2021-07-29_19-02-54.png)

So this extends to a map $\HH\to \DD$.

> Mnemonic: every $z\in \HH$ is closer to $i$ than $-i$.

:::
