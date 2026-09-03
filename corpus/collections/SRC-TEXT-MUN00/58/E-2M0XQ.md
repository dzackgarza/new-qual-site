---
schema: qual/card@1
id: E-2M0XQ
kind: problem
title: Fundamental groups of twelve standard spaces
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

For each of the following spaces, the fundamental group is either trivial, infinite cyclic, or isomorphic to the fundamental group of the figure eight.
Determine for each space which of the three alternatives holds.

(a) The "solid torus," $B^2 \times S^1$.

(b) The torus $T$ with a point removed.

(c) The cylinder $S^1 \times I$.

(d) The infinite cylinder $S^1 \times \mathbb{R}$.

(e) $\mathbb{R}^3$ with the nonnegative $x$, $y$, and $z$ axes deleted.

The following subsets of $\mathbb{R}^2$:

(f) $\ts{x \mid \norm{x} > 1}$

(g) $\ts{x \mid \norm{x} \geq 1}$

(h) $\ts{x \mid \norm{x} < 1}$

(i) $S^1 \cup (\mathbb{R}_+ \times 0)$

(j) $S^1 \cup (\mathbb{R}_+ \times \mathbb{R})$

(k) $S^1 \cup (\mathbb{R} \times 0)$

(l) $\mathbb{R}^2 - (\mathbb{R}_+ \times 0)$
:::

::: solution
**Goal:** Determine the fundamental group of each of the twelve spaces, classifying each as trivial ($\{1\}$), infinite cyclic ($\mathbb{Z}$), or figure-eight ($\mathbb{Z} * \mathbb{Z}$).

<1>1. Spaces with fundamental group $\pi_1 \cong \mathbb{Z}$ (infinite cyclic):
    *Proof:*
    <2>1. **(a) Solid torus $B^2 \times S^1$:** $B^2$ is contractible to $\{0\}$, so $B^2 \times S^1$ deformation retracts onto $\{0\} \times S^1 \cong S^1$. Hence $\pi_1(B^2 \times S^1) \cong \pi_1(S^1) \cong \mathbb{Z}$.
    <2>2. **(c) Cylinder $S^1 \times I$:** The interval $I = [0, 1]$ is contractible, so $S^1 \times I$ deformation retracts onto $S^1 \times \{0\} \cong S^1$, giving $\pi_1(S^1 \times I) \cong \mathbb{Z}$.
    <2>3. **(d) Infinite cylinder $S^1 \times \mathbb{R}$:** Deformation retracts onto $S^1 \times \{0\} \cong S^1$, giving $\pi_1(S^1 \times \mathbb{R}) \cong \mathbb{Z}$.
    <2>4. **(f) $\{x \in \mathbb{R}^2 : \|x\| > 1\}$:** Deformation retracts radially onto the circle of radius 2 (or any circle of radius $r > 1$), so $\pi_1 \cong \mathbb{Z}$.
    <2>5. **(g) $\{x \in \mathbb{R}^2 : \|x\| \ge 1\}$:** Deformation retracts radially onto the unit circle $S^1$, so $\pi_1 \cong \mathbb{Z}$.
    <2>6. **(i) $S^1 \cup (\mathbb{R}_+ \times \{0\})$:** The attached half-line $[1, \infty) \times \{0\}$ deformation retracts linearly into $(1, 0) \in S^1$, so the entire space deformation retracts onto $S^1$, giving $\pi_1 \cong \mathbb{Z}$.
    <2>7. **(j) $S^1 \cup (\mathbb{R}_+ \times \mathbb{R})$:** The open right half-plane $\mathbb{R}_+ \times \mathbb{R}$ is convex (contractible) and contains the right half of $S^1$. The space deformation retracts onto the circle formed by the left half of $S^1$ and the segment $[0, 1] \times \{0\}$, giving $\pi_1 \cong \mathbb{Z}$.

<1>2. Spaces with fundamental group $\pi_1 \cong \mathbb{Z} * \mathbb{Z}$ (figure eight):
    *Proof:*
    <2>1. **(b) Punctured torus $T^2 \setminus \{p\}$:** Representing $T^2$ as a square with identified edges $aba^{-1}b^{-1}$, removing the center point allows the open punctured 2-cell to deformation retract onto the boundary 1-skeleton $S^1 \vee S^1$. Hence $\pi_1(T^2 \setminus \{p\}) \cong \pi_1(S^1 \vee S^1) \cong \mathbb{Z} * \mathbb{Z}$.
    <2>2. **(e) $\mathbb{R}^3 \setminus (\text{nonnegative axes})$:** Radially deformation retracts onto $S^2$ minus three points $(1,0,0), (0,1,0), (0,0,1)$. By stereographic projection from one puncture, $S^2$ minus 3 points is homeomorphic to the twice-punctured plane $\mathbb{R}^2 \setminus \{p, q\}$, which deformation retracts onto $S^1 \vee S^1$. Hence $\pi_1 \cong \mathbb{Z} * \mathbb{Z}$.
    <2>3. **(k) $S^1 \cup (\mathbb{R} \times \{0\})$:** The external rays $(-\infty, -1] \times \{0\}$ and $[1, \infty) \times \{0\}$ deformation retract onto $(-1, 0)$ and $(1, 0)$. The remaining space $S^1 \cup ([-1, 1] \times \{0\})$ is the theta space $\theta$, which deformation retracts onto $S^1 \vee S^1$. Hence $\pi_1 \cong \mathbb{Z} * \mathbb{Z}$.

<1>3. Spaces with fundamental group $\pi_1 \cong \{1\}$ (trivial):
    *Proof:*
    <2>1. **(h) $\{x \in \mathbb{R}^2 : \|x\| < 1\}$:** The open unit disk is convex, hence contractible to the origin $\{0\}$, so $\pi_1 \cong \{1\}$.
    <2>2. **(l) $\mathbb{R}^2 \setminus (\mathbb{R}_+ \times \{0\})$:** The slit plane is contractible via vertical deformation retraction onto the negative $x$-axis $(-\infty, 0] \times \{0\}$, which is itself contractible. Hence $\pi_1 \cong \{1\}$.

<1>4. Summary Table:
    - **Trivial ($\{1\}$):** (h), (l).
    - **Infinite cyclic ($\mathbb{Z}$):** (a), (c), (d), (f), (g), (i), (j).
    - **Figure eight ($\mathbb{Z} * \mathbb{Z}$):** (b), (e), (k).
    Q.E.D.
:::
