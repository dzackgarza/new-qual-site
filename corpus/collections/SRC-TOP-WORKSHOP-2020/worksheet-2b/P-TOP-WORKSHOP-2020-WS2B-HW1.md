---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-HW1
kind: problem
title: Determine retractions and deformation retractions in basic spaces (warm-up)
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Determine whether the following spaces $X$ admit a retraction and/or a deformation retraction onto the designated subspace $Y$:

(a) $X=[0,1]$, $Y=\{0\}$.

(b) $X=[0,1]$, $Y=\{0,1\}$.

(c) $X=S^1$, $Y=\{y\}$, any singleton.
:::

::: {.solution}
**Goal.** Determine retractions and deformation retractions for the three pairs.

<1>1. (a) $X = [0,1]$, $Y = \theset{0}$.
<2>1. There is a retraction $r: [0,1] \to \theset{0}$, namely $r(x) = 0$.
::: {.proof}
$r$ is continuous and $r(0) = 0$.
:::
<2>2. There is a deformation retraction: $H(x, t) = (1-t)x$.
::: {.proof}
$H(x, 0) = x$, $H(x, 1) = 0$, and $H(0, t) = 0$ for all $t$ (fixes $Y$ throughout).
:::

<1>2. (b) $X = [0,1]$, $Y = \theset{0, 1}$.
<2>1. There is no retraction $[0,1] \to \theset{0,1}$.
::: {.proof}
$[0,1]$ is connected and $\theset{0,1}$ is disconnected; a retraction would be a continuous surjection onto a disconnected space, contradicting that the continuous image of a connected space is connected.
:::
<2>2. Hence there is no deformation retraction either.
::: {.proof}
a deformation retraction is in particular a retraction.
:::

<1>3. (c) $X = S^1$, $Y = \theset{y}$.
<2>1. There is a retraction $S^1 \to \theset{y}$, namely the constant map $r(x) = y$.
::: {.proof}
the constant map is continuous and fixes $y$.
:::
<2>2. There is no deformation retraction of $S^1$ onto a point.
::: {.proof}
a deformation retraction of $S^1$ onto a point would be a homotopy equivalence $S^1 \simeq \ast$, but $\pi_1(S^1) = \ZZ \neq 0 = \pi_1(\ast)$, contradiction.
:::

<1>4. Q.E.D.
::: {.proof}
(a) retraction and deformation retraction; (b) neither; (c) retraction but no deformation retraction.
:::
:::
