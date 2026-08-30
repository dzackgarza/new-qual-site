---
schema: qual/card@1
id: P-HCAX2
kind: problem
title: Picard's theorem from the modular invariant
classification:
  areas:
  - complex-analysis
  topics:
  - Picard
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Prove Picard's theorem using the fact that the modular invariant $j$ uniformizes the hyperbolic triangle of type $(2,3,\infty)$ by the upper half-plane.
:::

::: {.solution}
<1>1. The modular invariant $j : \mathbb{H} \to \mathbb{C}$ is a surjective holomorphic map that is invariant under $\operatorname{PSL}_2(\mathbb{Z})$, and it uniformizes the hyperbolic triangle of type $(2,3,\infty)$: it is a covering map onto $\mathbb{C} \setminus \{0, 1\}$ (with ramification of order $2$ over $1$, order $3$ over $0$, and a cusp at $\infty$). Proof: the given fact about $j$.

<1>2. Let $f : \mathbb{C} \to \mathbb{C} \setminus \{0, 1\}$ be an entire function omitting $0$ and $1$.
Proof: suppose $f$ omits two values (normalize them to $0$ and $1$).

<1>3. Since $\mathbb{C}$ is simply connected and $j$ is a covering map onto $\mathbb{C} \setminus \{0,1\}$ (away from the ramification points), $f$ lifts to a holomorphic map $\tilde f : \mathbb{C} \to \mathbb{H}$ with $j \circ \tilde f = f$.
Proof: the lifting criterion (a map from a simply connected space lifts through a covering map).

<1>4. Compose $\tilde f$ with the Cayley transform $\mathbb{H} \to \mathbb{D}$ to get a bounded entire function $g : \mathbb{C} \to \mathbb{D}$.
Proof: the upper half-plane is conformally equivalent to the unit disk.

<1>5. By Liouville's theorem, $g$ is constant.
Proof: a bounded entire function is constant.

<1>6. Hence $f$ is constant.
Proof: <1>3–<1>5 (if $g$ is constant then $\tilde f$ is constant, so $f = j \circ \tilde f$ is constant).

<1>7. Therefore any entire function omitting two values is constant — Picard's (little) theorem.
Proof: <1>2 and <1>6.

<1>8. Q.E.D. Proof: <1>7.
:::
