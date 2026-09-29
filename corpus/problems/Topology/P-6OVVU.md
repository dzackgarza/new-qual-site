---
schema: qual/card@1
id: P-6OVVU
kind: problem
title: Deformation retract of $\RR^3\setminus S^1$ onto $S^2\vee S^1$
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
relations: []
review: draft
---

::: {.problem}
6. **Main Idea**: Using a funky deformation retract.
   See Hatcher, PDF page 55, Example 1.23. Add picture!!

Deformation retract $\RR^3 - S^1$ onto $S^2 - U$, where $U$ is a diameter inside $S^2$ also passing through the middle of $S^1$ in the interior.
This can be done by moving points outside of $S^2$ towards the surface, and points inside $S^2$ just move away from the $S^1$ inside (either towards $U$ or towards the surface of $S^2$, so they don't hit $S^1$).

Then take a geodesic between the endpoints of the diameter on $S^2$, pick any point $p$ on the geodesic, and move both diameter points towards it.
This yields $S^2 \vee S^1$ at the point $p$.
:::

::: {.solution}

::: pf

::: pf-step

Let $C\subset\mathbb R^3$ be the standard unknotted circle and choose a closed tubular neighborhood $N\cong S^1\times D^2$ of $C$.

::: pf-proof

The normal bundle of the standard circle in $\mathbb R^3$ is trivial.

:::

:::

::: {.pf-step #s2}

The complement $\mathbb R^3\setminus C$ deformation retracts onto $\mathbb R^3\setminus\operatorname{int}N$.

::: pf-proof

Inside each normal disk of $N$, radially push every noncentral point away from the core circle to the boundary $S^1\times S^1$, while fixing the exterior of $N$. This gives a strong deformation retraction.

:::

:::

::: {.pf-step #s3}

After one-point compactifying $\mathbb R^3$ to $S^3$, the closure of $\mathbb R^3\setminus\operatorname{int}N$ is the complementary solid torus $V$ of the unknot; the point at infinity lies in the interior of $V$. Thus
$$\mathbb R^3\setminus\operatorname{int}N\cong V\setminus\{\infty\}.$$

::: pf-proof

The complement in $S^3$ of a tubular neighborhood of an unknot is again a solid torus.

:::

:::

::: {.pf-step #s4}

A solid torus with one interior point removed deformation retracts onto the wedge of its core circle with a small $2$-sphere surrounding the deleted point.

::: pf-proof

Remove a small open $3$-ball around the missing point. The resulting punctured solid torus has a handle decomposition with one $0$-handle, one $1$-handle, and the additional spherical boundary component. Collapse the $0$- and $1$-handle part to the core circle while retaining that boundary sphere, joining them by a single arc and then collapsing the arc to the wedge point.

:::

:::

::: pf-step

Consequently
$$\boxed{\mathbb R^3\setminus S^1\simeq S^1\vee S^2.}$$

::: pf-proof

Combine steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::
