---
schema: qual/card@1
id: E-HAT-1.2-10
kind: problem
title: Loop nullhomotopic in $D^2 \times I$ but not in complement of two arcs
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: The old solution used an unstated relator r and an unchecked map to S_3; rewritten to show the complement group is free on the two meridians and gamma is their commutator.
---

::: {.problem}
Consider two arcs $\alpha$ and $\beta$ embedded in $D^2 \times I$ as shown in the figure.
The loop $\gamma$ is nullhomotopic in $D^2 \times I$ (since $D^2 \times I$ is contractible), but show that there is no nullhomotopy of $\gamma$ in the complement of $\alpha \cup \beta$.
:::

::: {.solution}
Let $X=(D^2\times I)\setminus(\alpha\cup\beta)$, and let $x,y\in\pi_1(X)$ be meridian loops of $\alpha$ and $\beta$, joined to a basepoint near $\gamma$.

::: pf

::: {.pf-step #s1}

$\pi_1(X)$ is free on $x$ and $y$.

::: pf-proof

The two arcs in the figure form a single clasp, and their endpoints lie on the boundary of the ball $D^2\times I$.
Dragging the endpoints of $\beta$ along the boundary sphere around the endpoint of $\alpha$ undoes the clasp; this is an isotopy of the ball, so it is a homeomorphism of $X$ onto the complement of two unknotted, unlinked arcs.
That complement deformation retracts onto a disk with two holes, whose fundamental group is free on the two boundary loops of the holes, which are meridians of the two arcs.

:::

:::

::: {.pf-step #s2}

$[\gamma]=xyx^{-1}y^{-1}$ in $\pi_1(X)$, up to conjugation and inversion.

::: pf-proof

In the figure, $\gamma$ passes once through the clasp: it runs around $\alpha$, around $\beta$, back around $\alpha$ in the opposite direction, and back around $\beta$ in the opposite direction.
Each passage around an arc contributes the corresponding meridian or its inverse.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $[\gamma]$ is conjugate to $(xyx^{-1}y^{-1})^{\pm1}$, a nonempty reduced word in the free group $F(x,y)$, so $[\gamma]\ne1$ and $\gamma$ has no nullhomotopy in $X$.

:::

:::

:::
