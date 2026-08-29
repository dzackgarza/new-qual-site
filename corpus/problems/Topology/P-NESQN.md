---
schema: qual/card@1
id: P-NESQN
kind: problem
title: $\pi_1(S^n)$ by van Kampen on the complements of the north and south poles
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
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Compute the fundamental group $\pi_1(S^n, x_0)$ for $n \ge 2$ using the **Seifert–van Kampen Theorem** by decomposing the $n$-sphere $S^n$ into the complements of the north and south poles.
:::

::: solution
**Goal:** Prove that $\pi_1(S^n) = 0$ for all $n \ge 2$ using the Seifert–van Kampen Theorem.

<1>1. Open Cover of $S^n$:
    *Proof:*
    <2>1. Let $n \ge 2$, and let $N = (0, \dots, 0, 1)$ and $S = (0, \dots, 0, -1)$ denote the north and south poles of the $n$-sphere $S^n \subset \mathbb{R}^{n+1}$.
    <2>2. Define the two open sets:
        $$U = S^n \setminus \{S\}, \qquad V = S^n \setminus \{N\}.$$
    <2>3. Then $U \cup V = S^n$.
    <2>4. Via stereographic projection from the south pole, $U \cong \mathbb{R}^n$, which is contractible ($U \simeq \{*\}$).
    <2>5. Via stereographic projection from the north pole, $V \cong \mathbb{R}^n$, which is contractible ($V \simeq \{*\}$).
    <2>6. Thus both $U$ and $V$ are open, path-connected subsets with trivial fundamental groups:
        $$\pi_1(U, x_0) = 0, \qquad \pi_1(V, x_0) = 0.$$

<1>2. Path-Connectedness of the Intersection $U \cap V$:
    *Proof:*
    <2>1. The intersection is $U \cap V = S^n \setminus \{N, S\}$.
    <2>2. Stereographic projection from the north pole maps $U \cap V$ homeomorphically to $\mathbb{R}^n \setminus \{0\}$.
    <2>3. The punctured Euclidean space $\mathbb{R}^n \setminus \{0\}$ deformation retracts radially onto the equatorial sphere $S^{n-1}$.
    <2>4. Since $n \ge 2$, the dimension of the equatorial sphere is $n - 1 \ge 1$.
    <2>5. The sphere $S^{n-1}$ is **path-connected** for all $n - 1 \ge 1$ (i.e. $n \ge 2$).
    <2>6. Therefore, $U \cap V$ is a non-empty, **path-connected** open subset of $S^n$.

<1>3. Application of the Seifert–van Kampen Theorem:
    *Proof:*
    <2>1. Choose a basepoint $x_0 \in U \cap V$ (e.g. an equatorial point $(1, 0, \dots, 0)$).
    <2>2. Since $U, V$, and $U \cap V$ are all open and path-connected with $U \cup V = S^n$, the hypotheses of the **Seifert–van Kampen Theorem** are satisfied.
    <2>3. The fundamental group of the union is the amalgamated free product:
        $$\pi_1(S^n, x_0) \cong \pi_1(U, x_0) *_{\pi_1(U \cap V, x_0)} \pi_1(V, x_0).$$
    <2>4. Since $\pi_1(U, x_0) = \{e\}$ and $\pi_1(V, x_0) = \{e\}$:
        $$\pi_1(S^n, x_0) \cong \{e\} *_{\pi_1(U \cap V, x_0)} \{e\} = \{e\} = 0.$$

<1>4. Conclusion:
    The fundamental group $\pi_1(S^n) = 0$ is trivial (simply connected) for all $n \ge 2$. Q.E.D.
:::
