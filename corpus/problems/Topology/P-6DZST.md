---
schema: qual/card@1
id: P-6DZST
kind: problem
title: $S^2$ minus two points deformation retracts onto $S^1$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The problem block held a numbered solution sketch (flow along great circles through the poles to the equator; alternatively S^2 minus a point is R^2 and R^2 minus a point is S^1 x R) instead of a question. The statement now asks for the deformation retraction; the great-circle flow is a remark."
---

::: {.problem}
Let $p_0\neq p_1$ be points of $S^2$ and $X=S^2\setminus\theset{p_0,p_1}$. Show that $X$ deformation retracts onto a subspace homeomorphic to $S^1$.
:::

::: {.solution}

::: pf

::: {.pf-step #stereographic}

There is a homeomorphism $\sigma:X\to\RR^2\setminus\{0\}$.

::: pf-proof

Stereographic projection from $p_0$ is a homeomorphism $S^2\setminus\{p_0\}\to\RR^2$; compose it with the translation taking the image of $p_1$ to $0$.

:::

:::

::: {.pf-step #punctured-plane}

$\RR^2\setminus\{0\}$ strongly deformation retracts onto the unit circle $S^1$ by $H(x,t)=\bigl((1-t)+t/\norm{x}\bigr)x$.

::: pf-proof

For $x\ne0$ the scalar is positive, so the homotopy stays in the punctured plane; at $t=1$ it is radial projection, and it fixes the unit circle.

:::

:::

::: pf-step

$X$ strongly deformation retracts onto $\sigma^{-1}(S^1)\cong S^1$.

::: pf-proof

Conjugate the homotopy of step [](#punctured-plane){.pf-ref} by the homeomorphism of step [](#stereographic){.pf-ref}: $(x,t)\mapsto\sigma^{-1}H(\sigma(x),t)$.

:::

:::

:::

:::

::: {.remark}
When $p_0,p_1$ are antipodal, say the north and south poles, a direct deformation retraction onto the equator moves each point of $X$ along its meridian at linear speed in latitude to the equator. It is defined everywhere except at the poles, which are not in $X$, and it fixes the equator.
:::
