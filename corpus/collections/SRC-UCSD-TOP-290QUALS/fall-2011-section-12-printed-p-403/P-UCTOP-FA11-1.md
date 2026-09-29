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

::: {.problem}
Let $f, g : X \to S^2$ be continuous maps such that for all $x$ in $X$, $f(x)$ is not antipodal to $g(x)$.
Show that $f$ is homotopic to $g$.
:::

::: {.solution}

::: pf

::: {.pf-step #segment-avoids-origin}
For each $x \in X$, $f(x)$ and $g(x)$ are not antipodal, so the segment from $f(x)$ to $g(x)$ does not pass through the origin.

::: pf-proof
hypothesis (antipodal points are $p$ and $-p$, and the segment between them passes through $0$).
:::

:::

::: {.pf-step #define-h}
Define $H : X \times [0,1] \to S^2$ by $$H(x, t) = \frac{(1 - t) f(x) + t g(x)}{\|(1 - t) f(x) + t g(x)\|}.$$

::: pf-proof
the straight-line homotopy, normalized to lie on $S^2$.
:::

:::

::: {.pf-step #denominator-nonzero}
The denominator is never zero: if $(1-t)f(x) + t g(x) = 0$, then $f(x)$ and $g(x)$ would be antipodal (for $0 < t < 1$), contradicting step [](#segment-avoids-origin){.pf-ref}.

::: pf-proof
Step [](#segment-avoids-origin){.pf-ref}.
:::

:::

::: {.pf-step #h-well-defined-continuous}
Hence $H$ is well-defined and continuous.

::: pf-proof
Steps [](#define-h){.pf-ref} and [](#denominator-nonzero){.pf-ref}.
:::

:::

::: {.pf-step #h-endpoint-values}
$H(x, 0) = f(x)$ and $H(x, 1) = g(x)$.

::: pf-proof
Step [](#define-h){.pf-ref}.
:::

:::

::: {.pf-step #f-homotopic-g}
Hence $f \simeq g$.

::: pf-proof
Steps [](#h-well-defined-continuous){.pf-ref} and [](#h-endpoint-values){.pf-ref}.
:::

:::

::: pf-qed
Step [](#f-homotopic-g){.pf-ref}.
:::

:::

:::
