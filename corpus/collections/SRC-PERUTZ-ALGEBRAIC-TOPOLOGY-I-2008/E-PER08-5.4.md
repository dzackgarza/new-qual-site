---
schema: qual/card@1
id: E-PER08-5.4
kind: problem
title: Perutz Algebraic Topology I Exercise 5.4
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
---

::: {.problem}
Write out the missing details.
:::

::: {.solution}
We supply the omitted details in Lemma 5.7.

<1>1. Paths and homotopies lift uniquely once an initial lift is fixed.
::: {.proof}
Cover the compact interval $I$ by finitely many subintervals on each of which the given path lies in an evenly covered open set.
Starting from the prescribed lift, lift successively by the inverse of the appropriate sheet homeomorphism.
On overlaps uniqueness follows because two lifts agreeing at one point must remain in the same sheet.
This proves path lifting and uniqueness.

For a homotopy $H:I^2\to X$, compactness of $I^2$ and a Lebesgue-number subdivision reduce the square to finitely many small rectangles mapped into evenly covered sets.
Lift rectangle by rectangle, starting from the specified value at $(0,0)$.
Agreement on common edges follows from uniqueness of path lifts.
:::

<1>2. $p_*:\pi_1(\widetilde X,\widetilde x)\to\pi_1(X,x)$ is injective.
::: {.proof}
If $p\circ\alpha$ is null-homotopic rel endpoints, lift a null-homotopy starting with $\alpha$.
Its opposite edge is a lift of the constant path beginning at $\widetilde x$, hence is constant.
The lifted homotopy therefore contracts $\alpha$ rel endpoints.
:::

<1>3. The subgroups obtained from different points of the fibre are conjugate, and every conjugate occurs.
::: {.proof}
If $\widetilde x'$ lies over $x$ and $\eta$ is a path from $\widetilde x'$ to $\widetilde x$, change of basepoint gives
\[
p_*\pi_1(\widetilde X,\widetilde x')=[p\eta]\,p_*\pi_1(\widetilde X,\widetilde x)\,[p\eta]^{-1}.
\]
Conversely, for any loop $\gamma$ at $x$, lift $\gamma$ from $\widetilde x$ and let $\widetilde x'$ be its endpoint.
Applying the preceding formula to the lifted path produces the conjugate by $[\gamma]$.
Hence all conjugates arise.
:::
:::
