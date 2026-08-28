---
schema: qual/card@1
id: P-CAF13D
kind: problem
title: "Conformal map from the upper half-plane onto the punctured unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Find a holomorphic function that maps the upper half-plane $\mathbb{C}_+$ onto the punctured unit disk $\mathbb{D} \setminus \{0\}$.
:::

::: {.solution}
**Goal.** Find a holomorphic map from the upper half-plane $\CC_+$ onto the punctured unit disk $\DD \sm \theset{0}$.

<1>1. The exponential maps a horizontal strip onto the punctured disk.
<2>1. $z \mapsto e^{iz}$ maps the strip $\theset{z : 0 < \Im z < \infty}$ onto $\DD \sm \theset{0}$.
Proof: for $z = x + iy$ with $y > 0$, $e^{iz} = e^{-y} e^{ix}$ has modulus $e^{-y} \in (0, 1)$ and arbitrary argument, so the image is $\theset{w : 0 < \abs w < 1} = \DD \sm \theset{0}$.
<2>2. The map is holomorphic and surjective onto $\DD \sm \theset{0}$.
Proof: $e^{iz}$ is entire; by <1>2.1 its restriction to the upper half-plane has image exactly the punctured disk.

<1>3. Q.E.D.
Proof: $f(z) = e^{iz}$ is the required map.
:::
