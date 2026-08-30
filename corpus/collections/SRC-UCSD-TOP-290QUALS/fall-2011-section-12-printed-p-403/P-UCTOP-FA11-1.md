---
schema: qual/card@1
id: P-UCTOP-FA11-1
kind: problem
title: Non-antipodal maps to S^2 are homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Let $f, g : X \to S^2$ be continuous maps such that for all $x$ in $X$, $f(x)$ is not antipodal to $g(x)$.
Show that $f$ is homotopic to $g$.

::: {.solution}
<1>1. For each $x \in X$, $f(x)$ and $g(x)$ are not antipodal, so the segment from $f(x)$ to $g(x)$ does not pass through the origin.
Proof: hypothesis (antipodal points are $p$ and $-p$, and the segment between them passes through $0$).

<1>2. Define $H : X \times [0,1] \to S^2$ by
$$H(x, t) = \frac{(1 - t) f(x) + t g(x)}{\|(1 - t) f(x) + t g(x)\|}.$$
Proof: the straight-line homotopy, normalized to lie on $S^2$.

<1>3. The denominator is never zero: if $(1-t)f(x) + t g(x) = 0$, then $f(x)$ and $g(x)$ would be antipodal (for $0 < t < 1$), contradicting <1>1.
Proof: <1>1.

<1>4. Hence $H$ is well-defined and continuous.
Proof: <1>2 and <1>3.

<1>5. $H(x, 0) = f(x)$ and $H(x, 1) = g(x)$.
Proof: <1>2.

<1>6. Hence $f \simeq g$.
Proof: <1>4 and <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
