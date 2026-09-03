---
schema: qual/card@1
id: E-UGSM8
kind: problem
title: The general Ascoli theorem implies the classical version
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Show that the general version of Ascoli's theorem implies the classical version (Theorem 45.4) when $X$ is Hausdorff.
:::

::: {.solution}
<1>1. The classical Ascoli theorem (Theorem 45.4) states: a subset $\mathcal{F}$ of $C(X, \mathbb{R}^n)$ (for compact Hausdorff $X$) is compact iff it is closed, bounded, and equicontinuous.
::: {.proof}
statement of the classical version.
:::

<1>2. The general Ascoli theorem states: a subset $\mathcal{F}$ of $C(X, Y)$ (for $X$ compact Hausdorff, $Y$ metric) is compact iff it is closed, pointwise relatively compact, and equicontinuous.
::: {.proof}
statement of the general version.
:::

<1>3. For $Y = \mathbb{R}^n$, "pointwise relatively compact" is equivalent to "bounded" (a subset of $\mathbb{R}^n$ is relatively compact iff it is bounded).
::: {.proof}
Heine–Borel.
:::

<1>4. Hence the general version, specialized to $Y = \mathbb{R}^n$, gives exactly the classical version: $\mathcal{F}$ compact iff closed, bounded, and equicontinuous.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
