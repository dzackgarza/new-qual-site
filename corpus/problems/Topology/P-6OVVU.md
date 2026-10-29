---
schema: qual/card@1
id: P-6OVVU
kind: problem
title: $\RR^3\setminus S^1$ is homotopy equivalent to $S^2\vee S^1$
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
  note: "The problem block held a numbered solution sketch citing Hatcher, Example 1.23 (deformation retract R^3 minus S^1 onto a sphere together with a diameter through the circle, then slide the diameter's endpoints together) instead of a question. The statement now asks for the homotopy type; the sketch is a remark."
---

::: {.problem}
Let $S^1\subset\RR^3$ be the unit circle in the $xy$-plane. Show that $\RR^3\setminus S^1$ is homotopy equivalent to $S^2\vee S^1$.
:::

::: {.solution}

Write $C=S^1\subset\RR^3$ and choose a closed tubular neighborhood $N\cong S^1\times D^2$ of $C$; one exists because the normal bundle of $C$ in $\RR^3$ is trivial.

::: pf

::: {.pf-step #s2}

$\RR^3\setminus C$ deformation retracts onto $\RR^3\setminus\operatorname{int}N$.

::: pf-proof

Inside each normal disk of $N$, radially push every noncentral point away from the core circle to the boundary $S^1\times S^1$, while fixing the exterior of $N$. This gives a strong deformation retraction.

:::

:::

::: {.pf-step #s3}

$\RR^3\setminus\operatorname{int}N\cong V\setminus\{\infty\}$, where $V$ is a solid torus and $\infty$ lies in its interior.

::: pf-proof

In the one-point compactification $S^3=\RR^3\cup\{\infty\}$, the complement $V$ of the interior of a tubular neighborhood of the unknot $C$ is a solid torus, and $\infty$ lies in its interior.

:::

:::

::: {.pf-step #s4}

A solid torus with one interior point removed is homotopy equivalent to $S^1\vee S^2$.

::: pf-proof

It deformation retracts onto the solid torus minus a small open ball around the removed point. That space deformation retracts onto the union of the core circle, the boundary sphere of the ball, and an arc joining them, and collapsing the contractible arc is a homotopy equivalence onto $S^1\vee S^2$.

:::

:::

::: pf-step

$\boxed{\RR^3\setminus S^1\simeq S^1\vee S^2}$.

::: pf-proof

Combine steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

:::

:::

::: {.remark}
A direct picture: $\RR^3\setminus S^1$ deformation retracts onto a sphere enclosing the circle together with the diameter of that sphere that passes through the disk bounded by the circle. Points outside the sphere move to it, and points inside move away from the circle toward the diameter or the sphere. Sliding one endpoint of the diameter along the sphere to the other gives $S^2\vee S^1$.
:::
