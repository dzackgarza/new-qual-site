---
schema: qual/card@1
id: P-TOPF02H
kind: problem
title: 'Fundamental group of the complement of a knot in $S^4$ via transversality'
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
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The six steps that asserted their claim with no proof body now carry one each: the Whitney
    approximation of the loop, the passage from trivial $\pi_1(S^4)$ to a smooth disc filling
    it, the relative Thom transversality theorem, the codimension count $2-(4-1)=-1$, the
    emptiness of a submanifold of negative dimension, and the conclusion that $G$ is a
    null-homotopy inside the complement. No claim is changed and the closing QED step stands.
    Cited by number only: the Whitney approximation theorem, the Thom transversality theorem in
    its relative form, and the codimension formula for the preimage of a submanifold under a
    transverse map.
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

::: pf-proof
$K$ is a compact embedded submanifold of $S^4$, hence closed, so $S^4\setminus K$ is an open subset of a smooth manifold and in particular a manifold itself. A continuous map from the compact manifold $S^1$ into a manifold is homotopic to a smooth one by the Whitney approximation theorem, and the homotopy can be taken relative to a closed set on which the map is already smooth — here the basepoint, if one wants the basepoint fixed. The homotopy stays in the target, which is $S^4\setminus K$.
:::

:::

::: pf-step
Since $S^4$ is simply connected ($\pi_1(S^4) = 0$), there exists a continuous null-homotopy of $\widetilde{\gamma}$ in $S^4$, which can be smoothed relative to the boundary to yield a smooth map $F: D^2 \to S^4$ with $F\restrict_{\partial D^2} = \widetilde{\gamma}$.

::: pf-proof
A null-homotopy of the loop $\widetilde\gamma$ is a continuous map $H:D^2\to S^4$ whose restriction to $\partial D^2=S^1$ is $\widetilde\gamma$, and one exists exactly because $\widetilde\gamma$ represents the identity of $\pi_1(S^4)$, which is trivial. Since $S^1$ is a closed submanifold of $D^2$ and $\widetilde\gamma$ is smooth there, the Whitney approximation theorem relative to the boundary homotopes $H$, fixing $\partial D^2$, to a smooth map $F$ with the same boundary values.
:::

:::

:::

:::

::: pf-step
Application of the Transversality Theorem:

::: pf-proof

::: pf-step
By the Thom Transversality Theorem (relative to $\partial D^2$), since $F(\partial D^2) = \widetilde{\gamma}(S^1) \subset S^4 \setminus K$, $F$ is homotopic relative to $\partial D^2$ to a smooth map $G: D^2 \to S^4$ that is transverse to the smoothly embedded 1-manifold $K \subset S^4$:
$$
G \pitchfork K.
$$

::: pf-proof
The Thom transversality theorem, in the relative form for a closed subset of the domain, says that a smooth map $F:D^2\to S^4$ may be homotoped, relative to $\partial D^2$, to a map transverse to the closed submanifold $K$; the hypothesis needed is that $F$ be smooth, which step 1.2 gives, and that $\partial D^2$ be a closed subset on which the homotopy is fixed. Since $F(\partial D^2)=\widetilde\gamma(S^1)$ misses $K$, fixing the boundary costs nothing: the resulting $G$ still satisfies $G\restrict_{\partial D^2}=\widetilde\gamma$ and is transverse to $K$.
:::
:::

::: pf-step
For a transverse map $G: D^2 \to S^4$ to the submanifold $K \subset S^4$, the dimension of the intersection preimage $G^{-1}(K) \subset D^2$ is:
$$
\dim\left(G^{-1}(K)\right) = \dim(D^2) + \dim(K) - \dim(S^4) = 2 + 1 - 4 = -1.
$$

::: pf-proof
For a map $G$ transverse to a submanifold $K$ of the target, the preimage $G^{-1}(K)$ is a submanifold of the domain of codimension equal to the codimension of $K$ in the target, that is $\dim G^{-1}(K)=\dim D^2-(\dim S^4-\dim K)$, which is the displayed formula. Here the codimension of $K$ is $4-1=3$, so the preimage is a submanifold of dimension $2-3=-1$.
:::
:::

::: pf-step
A submanifold of negative dimension is empty, so $G^{-1}(K) = \emptyset$.
Thus the image $G(D^2)$ is completely disjoint from $K$:
$$
G(D^2) \subseteq S^4 \setminus K.
$$

::: pf-proof
A manifold of dimension $n$ has a chart at each of its points onto an open subset of $\RR^n$, and $\RR^n$ is empty when $n<0$; so a submanifold of dimension $-1$ has no points. Hence $G^{-1}(K)=\varnothing$, which says exactly that no point of $D^2$ is carried into $K$, that is $G(D^2)\cap K=\varnothing$.
:::

:::

:::

:::

::: pf-step
Null-homotopy in the complement:

::: pf-proof

::: pf-step
The map $G: D^2 \to S^4 \setminus K$ satisfies $G\restrict_{\partial D^2} = \widetilde{\gamma}$, providing an explicit null-homotopy of $\widetilde{\gamma}$ inside $S^4 \setminus K$.
Thus every loop in $S^4 \setminus K$ is null-homotopic.

::: pf-proof
By step 2.3 the map $G$ takes all of $D^2$ into $S^4\setminus K$, and by step 2.1 it agrees with $\widetilde\gamma$ on $\partial D^2$; a map $D^2\to S^4\setminus K$ with boundary $\widetilde\gamma$ is exactly a null-homotopy of $\widetilde\gamma$ inside the complement. Since $\widetilde\gamma$ is homotopic to $\gamma$ in $S^4\setminus K$ by step 1.1, the loop $\gamma$ is null-homotopic there too. The loop $\gamma$ based at $x_0$ was arbitrary, so every element of $\pi_1(S^4\setminus K,x_0)$ is trivial.
:::

:::

:::

:::

::: pf-qed
Conclusion:
$\pi_1(S^4 \setminus K) \cong \{0\}$ (the trivial group).
:::

:::

:::
