---
schema: qual/card@1
id: P-TOPF02H
kind: problem
title: "Fundamental group of the complement of a knot in S^4 via transversality"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Transversality
  - Knot Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Suppose $K$ is a knot (a smoothly embedded image of the circle $S^1$) in $S^4$.
Use transversality to compute the fundamental group of the complement $S^4 \setminus K$.
:::

::: {.solution}

::: pf

::: pf-step
Smooth approximation of loops and discs:

::: pf-proof

::: pf-step
Let $x_0 \in S^4 \setminus K$ be a basepoint, and let $\gamma: S^1 \to S^4 \setminus K$ be a continuous loop based at $x_0$.
By the Whitney Approximation Theorem, $\gamma$ is homotopic in $S^4 \setminus K$ to a smooth loop $\widetilde{\gamma}: S^1 \to S^4 \setminus K$.
:::

::: pf-step
Since $S^4$ is simply connected ($\pi_1(S^4) = 0$), there exists a continuous null-homotopy of $\widetilde{\gamma}$ in $S^4$, which can be smoothed relative to the boundary to yield a smooth map $F: D^2 \to S^4$ with $F|_{\partial D^2} = \widetilde{\gamma}$.
:::

:::

:::

::: pf-step
Application of the Transversality Theorem:

::: pf-proof

::: pf-step
By the Thom Transversality Theorem (relative to $\partial D^2$), since $F(\partial D^2) = \widetilde{\gamma}(S^1) \subset S^4 \setminus K$, $F$ is homotopic relative to $\partial D^2$ to a smooth map $G: D^2 \to S^4$ that is transverse to the smoothly embedded 1-manifold $K \subset S^4$:
\[
G \pitchfork K.
\]
:::

::: pf-step
For a transverse map $G: D^2 \to S^4$ to the submanifold $K \subset S^4$, the dimension of the intersection preimage $G^{-1}(K) \subset D^2$ is:
\[
\dim\left(G^{-1}(K)\right) = \dim(D^2) + \dim(K) - \dim(S^4) = 2 + 1 - 4 = -1.
\]
:::

::: pf-step
A submanifold of negative dimension is empty, so $G^{-1}(K) = \emptyset$.
Thus the image $G(D^2)$ is completely disjoint from $K$:
\[
G(D^2) \subseteq S^4 \setminus K.
\]
:::

:::

:::

::: pf-step
Null-homotopy in the complement:

::: pf-proof

::: pf-step
The map $G: D^2 \to S^4 \setminus K$ satisfies $G|_{\partial D^2} = \widetilde{\gamma}$, providing an explicit null-homotopy of $\widetilde{\gamma}$ inside $S^4 \setminus K$.
Thus every loop in $S^4 \setminus K$ is null-homotopic.
:::

:::

:::

::: pf-qed
Conclusion:
$\pi_1(S^4 \setminus K) \cong \{0\}$ (the trivial group).
:::

:::

:::
