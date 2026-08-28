---
schema: qual/card@1
id: E-2Z1TM
kind: exercise
title: Lifting paths in the polar covering of the punctured plane
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the covering map $p: \mathbb{R} \times \mathbb{R}_+ \to \mathbb{R}^2 - 0$ of Example 6 of §53. Find liftings of the paths

$$
f(t) = (2 - t, 0),
$$

$$
g(t) = ((1 + t) \cos 2\pi t, (1 + t) \sin 2\pi t),
$$

$$
h(t) = f * g.
$$

Sketch these paths and their liftings.
:::

::: solution
**Goal:** Compute explicit formulas for the unique liftings of paths $f, g, h$ in $\mathbb{R}^2 \setminus \{0\}$ under the polar covering map $p: \mathbb{R} \times \mathbb{R}_+ \to \mathbb{R}^2 \setminus \{0\}$ given by $p(\theta, r) = (r \cos 2\pi \theta, r \sin 2\pi \theta)$.

<1>1. Lifting of $f(t) = (2 - t, 0)$ for $t \in [0, 1]$:
    *Proof:*
    <2>1. For all $t \in [0, 1]$, $2 - t > 0$, so $f(t)$ lies on the positive $x$-axis at radius $r(t) = 2 - t$ and angle $2\pi \theta(t) = 0 \pmod{2\pi}$.
    <2>2. Choosing an initial lift point in $p^{-1}(f(0)) = p^{-1}(2, 0) = \{(n, 2) : n \in \mathbb{Z}\}$, the continuous lift starting at $(n, 2)$ is:
        $$\tilde{f}_n(t) = (n, 2 - t) \quad \text{for } t \in [0, 1].$$
    <2>3. For $n = 0$, $\tilde{f}_0(t) = (0, 2 - t)$, which is a straight vertical segment in $\mathbb{R} \times \mathbb{R}_+$ running from $(0, 2)$ down to $(0, 1)$.

<1>2. Lifting of $g(t) = ((1 + t) \cos 2\pi t, (1 + t) \sin 2\pi t)$ for $t \in [0, 1]$:
    *Proof:*
    <2>1. The path $g(t)$ is an expanding spiral in $\mathbb{R}^2 \setminus \{0\}$ starting at $(1, 0)$ and ending at $(2, 0)$ after winding once counterclockwise around the origin.
    <2>2. The radius is $r(t) = 1 + t$ and the normalized angle is $\theta(t) = t$.
    <2>3. For an initial lift point $(m, 1) \in p^{-1}(g(0))$, the continuous lift is:
        $$\tilde{g}_m(t) = (m + t, 1 + t) \quad \text{for } t \in [0, 1].$$
    <2>4. For $m = 0$, $\tilde{g}_0(t) = (t, 1 + t)$, which is a straight diagonal line segment in the $\theta r$-plane from $(0, 1)$ to $(1, 2)$.

<1>3. Lifting of the concatenation $h(t) = (f * g)(t)$:
    *Proof:*
    <2>1. The concatenated path $h: [0, 1] \to \mathbb{R}^2 \setminus \{0\}$ is given by:
        $$h(t) = \begin{cases} f(2t) = (2 - 2t, 0) & \text{for } 0 \le t \le 1/2, \\ g(2t - 1) = (2t \cos 2\pi(2t-1), 2t \sin 2\pi(2t-1)) & \text{for } 1/2 \le t \le 1. \end{cases}$$
    <2>2. By the path-lifting property for concatenations, $\tilde{h} = \tilde{f} * \tilde{g}$.
    <2>3. Starting at $(n, 2)$, the unique lift is:
        $$\tilde{h}_n(t) = \begin{cases} (n, 2 - 2t) & \text{for } 0 \le t \le 1/2, \\ (n + 2t - 1, 2t) & \text{for } 1/2 \le t \le 1. \end{cases}$$
    <2>4. For $n = 0$, the lift $\tilde{h}_0$ starts at $(0, 2)$, moves vertically down to $(0, 1)$ at $t = 1/2$, and then moves along the diagonal segment to $(1, 2)$ at $t = 1$.

<1>4. Geometric description / sketches:
    - **In $\mathbb{R}^2 \setminus \{0\}$:** $f$ is a segment on the positive $x$-axis from $(2, 0)$ to $(1, 0)$; $g$ is a counterclockwise spiral from $(1, 0)$ to $(2, 0)$; $h$ traces the inward radial segment and then the outward spiral.
    - **In the covering space $\mathbb{R} \times \mathbb{R}_+$:** $\tilde{f}_0$ is the vertical line segment from $(0, 2)$ to $(0, 1)$; $\tilde{g}_0$ is the straight line segment from $(0, 1)$ to $(1, 2)$; $\tilde{h}_0$ is the polygonal path connecting $(0, 2) \to (0, 1) \to (1, 2)$. Q.E.D.
:::
