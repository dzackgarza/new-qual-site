---
schema: qual/card@1
id: P-5MZYU
kind: problem
title: Images of the unit circle under linear transformations of $\mathbb{R}^2$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What are the possible images of the unit circle under a linear transformation of $\mathbb{R}^2$?
:::

::: solution
**Goal:** Classify all possible images $T(S^1)$ of the unit circle $S^1 = \{x \in \mathbb{R}^2 \mid \|x\| = 1\}$ under a linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$.

<1>1. Singular Value Decomposition (SVD):
    *Proof:*
    <2>1. Represent $T$ by a $2 \times 2$ real matrix $A$.
    <2>2. By the Singular Value Decomposition, there exist orthogonal matrices $U, V \in O(2)$ and a diagonal matrix $\Sigma = \begin{pmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{pmatrix}$ with $\sigma_1 \ge \sigma_2 \ge 0$ such that:
        $$A = U \Sigma V^T.$$

<1>2. Action on the unit circle:
    *Proof:*
    <2>1. Since $V \in O(2)$ is orthogonal (an isometry), $V^T(S^1) = S^1$.
    <2>2. The diagonal matrix $\Sigma$ maps the unit circle $\{(\cos\theta, \sin\theta) \mid \theta \in [0, 2\pi)\}$ to the set:
        $$\Sigma(S^1) = \{(\sigma_1 \cos\theta, \sigma_2 \sin\theta) \mid \theta \in [0, 2\pi)\}.$$
    <2>3. The orthogonal matrix $U \in O(2)$ rotates and/or reflects this set, preserving all geometric properties (lengths of semi-axes, center at the origin).

<1>3. Case analysis on the rank of $A$:
    *Proof:*
    <2>1. **Rank 2 ($\sigma_1 \ge \sigma_2 > 0$):**
        - If $\sigma_1 = \sigma_2 > 0$, the image is a circle of radius $\sigma_1$ centered at the origin.
        - If $\sigma_1 > \sigma_2 > 0$, the image $\Sigma(S^1)$ satisfies $(u/\sigma_1)^2 + (v/\sigma_2)^2 = 1$, which is an ellipse centered at the origin with semi-major axis $\sigma_1$ and semi-minor axis $\sigma_2$. Applying $U$ rotates the axes, giving a general ellipse centered at the origin.
    <2>2. **Rank 1 ($\sigma_1 > 0, \sigma_2 = 0$):**
        - The image $\Sigma(S^1)$ is $\{(\sigma_1 \cos\theta, 0) \mid \theta \in [0, 2\pi)\} = [-\sigma_1, \sigma_1] \times \{0\}$.
        - Applying $U$, the image is a closed line segment centered at the origin of length $2\sigma_1$.
    <2>3. **Rank 0 ($\sigma_1 = \sigma_2 = 0$):**
        - $T = 0$, so the image is the single point $\{(0, 0)\}$.

<1>4. Conclusion:
    The possible images of $S^1$ under a linear map of $\mathbb{R}^2$ are:
    1. An ellipse centered at the origin (including a circle as a special case when singular values are equal).
    2. A closed line segment centered at the origin.
    3. The single point $\{0\}$.
    Q.E.D.
:::
