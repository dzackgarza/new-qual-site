---
schema: qual/card@1
id: P-LJTUV
kind: problem
title: $\pi_i(T^n)=0$ for $i\geq 2$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Covering Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the higher homotopy groups $\pi_i(T^n)$ of the $n$-torus $T^n = (S^1)^n$ for all $i \ge 2$.
:::

::: solution
**Goal:** Prove that $\pi_i(T^n) = 0$ for all $i \ge 2$ and all $n \ge 1$.

<1>1. Universal covering space of the $n$-torus:
    *Proof:*
    <2>1. The standard exponential map $p: \mathbb{R} \to S^1$ given by $p(t) = e^{2\pi i t}$ is the universal covering space of the circle $S^1$.
    <2>2. Taking the product of $n$ copies gives a covering map:
        $$p^{\times n}: \mathbb{R}^n \to (S^1)^n = T^n, \qquad (t_1, \dots, t_n) \mapsto (e^{2\pi i t_1}, \dots, e^{2\pi i t_n}).$$
    <2>3. Because $\mathbb{R}^n$ is path-connected and simply connected ($\pi_1(\mathbb{R}^n) = 0$), $\mathbb{R}^n$ is the universal covering space of $T^n$.

<1>2. Isomorphism on higher homotopy groups for covering spaces:
    *Proof:*
    <2>1. For any covering space $p: \widetilde{X} \to X$ with $\widetilde{X}$ path-connected, the induced homomorphism on homotopy groups:
        $$p_*: \pi_i(\widetilde{X}, \tilde{x}_0) \to \pi_i(X, x_0)$$
        is an isomorphism for all $i \ge 2$.
    <2>2. *Proof of isomorphism:* In the long exact sequence of homotopy groups for the fibration $\mathbb{Z}^n \hookrightarrow \widetilde{X} \to X$:
        $$\cdots \to \pi_i(F) \to \pi_i(\widetilde{X}) \to \pi_i(X) \to \pi_{i-1}(F) \to \cdots$$
        the fiber $F = p^{-1}(x_0) \cong \mathbb{Z}^n$ is a discrete space.
    <2>3. For any discrete space $F$, $\pi_i(F) = 0$ for all $i \ge 1$.
    <2>4. Thus the boundary and entry homomorphisms vanish, yielding exact sequences $0 \to \pi_i(\widetilde{X}) \xrightarrow{p_*} \pi_i(X) \to 0$ for all $i \ge 2$.
    <2>5. Hence $p_*: \pi_i(\widetilde{X}) \xrightarrow{\cong} \pi_i(X)$ for all $i \ge 2$.

<1>3. Homotopy groups of Euclidean space $\mathbb{R}^n$:
    *Proof:*
    <2>1. The Euclidean space $\mathbb{R}^n$ is contractible (it deformation retracts to the origin via $H(x, t) = (1-t)x$).
    <2>2. Therefore, $\pi_i(\mathbb{R}^n) = 0$ for all $i \ge 1$.

<1>4. Computation of $\pi_i(T^n)$:
    *Proof:*
    <2>1. By the covering space isomorphism:
        $$\pi_i(T^n) \cong \pi_i(\mathbb{R}^n) = 0 \quad \text{for all } i \ge 2.$$
    <2>2. (Note: for $i = 1$, $\pi_1(T^n) \cong \pi_1(S^1)^n \cong \mathbb{Z}^n$, so $T^n$ is an Eilenberg–MacLane space $K(\mathbb{Z}^n, 1)$).

<1>5. Conclusion:
    $\pi_i(T^n) = 0$ for all $i \ge 2$. Q.E.D.
:::
