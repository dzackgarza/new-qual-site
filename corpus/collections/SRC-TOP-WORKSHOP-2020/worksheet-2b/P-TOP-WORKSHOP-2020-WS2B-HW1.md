---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2B-HW1
kind: problem
title: Retractions and deformation retractions of intervals and the circle
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
<1>1. (a) $[0,1]$ deformation retracts onto $\{0\}$, so it also retracts onto $\{0\}$.
::: {.proof}
$H(x, t) = (1-t)x$ is continuous with $H(x, 0) = x$, $H(x, 1) = 0$, and $H(0, t) = 0$ for all $t$; its end map $r(x) = 0$ is a retraction.
:::

<1>2. (b) $[0,1]$ admits no retraction onto $\{0,1\}$, hence no deformation retraction.
::: {.proof}
A retraction $r\colon [0,1] \to \{0,1\}$ would be a continuous surjection from a connected space onto a disconnected space, contradicting that continuous images of connected spaces are connected. The end map of a deformation retraction is a retraction.
:::

<1>3. (c) $S^1$ retracts onto $\{y\}$ but does not deformation retract onto it.
::: {.proof}
The constant map $r(x) = y$ is continuous and fixes $y$, so it is a retraction. A deformation retraction onto $\{y\}$ would make the inclusion $\{y\} \hookrightarrow S^1$ a homotopy equivalence, but $\pi_1(S^1) \cong \ZZ$ while $\pi_1(\{y\}) = 0$.
:::
:::
