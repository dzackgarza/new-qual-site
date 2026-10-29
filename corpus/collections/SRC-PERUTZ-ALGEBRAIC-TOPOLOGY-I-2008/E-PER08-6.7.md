---
schema: qual/card@1
id: E-PER08-6.7
kind: problem
title: The doubled full rotation loop in $SO(3)$ is nullhomotopic
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retyped the mathematics against Exercise 6.7 of the Perutz 2008 notes.
---

::: {.problem}
Rotation about a fixed axis, by angles increasing from $0$ up to $2\pi$, determines a loop $\gamma$ in $SO(3)$.
Show that $\gamma*\gamma$ is nullhomotopic.
:::

::: {.solution}
Identify $SU(2)$ with the unit quaternions $S^3$.
A unit quaternion $q$ acts on the purely imaginary quaternions $\RR^3$ by $v \mapsto q v \bar q$, and this gives a covering homomorphism $p\colon S^3 \to SO(3)$ with kernel $\theset{\pm 1}$.
Let $u$ be a unit vector along the axis, so that $\gamma(t)$ is rotation by $t$ about $u$ for $t \in [0, 2\pi]$.

::: pf

::: {.pf-step #lift}
The path $\tilde\gamma(t) = \cos(t/2) + \sin(t/2)\, u$, $t \in [0, 4\pi]$, is a lift of $\gamma * \gamma$ to $S^3$, and it is a closed loop at $1$.

::: pf-proof
For $q = \cos(t/2) + \sin(t/2)\, u$, the map $v \mapsto q v \bar q$ fixes $u$ and rotates the plane orthogonal to $u$ by the angle $t$.
So $p(\tilde\gamma(t))$ is rotation by $t$ about $u$, and as $t$ runs over $[0, 4\pi]$ it traverses $\gamma$ twice, which is $\gamma * \gamma$ after reparametrization.
Also $\tilde\gamma(0) = 1 = \cos(2\pi) = \tilde\gamma(4\pi)$.
:::

:::

::: pf-step
$\gamma * \gamma$ is nullhomotopic.

::: pf-proof
$S^3$ is simply connected, so the loop $\tilde\gamma$ of step [](#lift){.pf-ref} is nullhomotopic rel endpoints.
Composing that nullhomotopy with $p$ gives a nullhomotopy of $p \circ \tilde\gamma$, which is a reparametrization of $\gamma * \gamma$.
:::

:::

:::
:::
