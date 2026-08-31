---
schema: qual/card@1
id: E-SS8.EX-8
kind: exercise
title: "Harmonic function on the first quadrant with piecewise constant boundary values"
classification:
  areas:
  - complex-analysis
  topics: ['Conformal Mappings', 'Riemann Mapping Theorem', 'Automorphisms']
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
8. Find a harmonic function $u$ in the open first quadrant that extends continuously up to the boundary except at the points 0 and 1, and that takes on the following boundary values: $u(x, y) = 1$ on the half-lines $\{y = 0, x > 1\}$ and $\{x = 0, y > 0\}$, and $u(x, y) = 0$ on the segment $\{0 < x < 1, y = 0\}$.

[Hint: Find conformal maps $F_1, F_2, \ldots, F_5$ indicated in Figure 11. Note that $\frac{1}{\pi}\arg(z)$ is harmonic on the upper half-plane, equals 0 on the positive real axis, and 1 on the negative real axis.]
:::

::: solution
**Goal:** Construct a harmonic function $u(x, y)$ on the first quadrant $Q = \{z \in \mathbb{C} : \Re z > 0, \Im z > 0\}$ with the specified boundary values.

<1>1. Conformal mapping of the quadrant to the upper half-plane:
    *Proof:*
    <2>1. Let $Q = \{z \in \mathbb{C} : \Re z > 0, \Im z > 0\}$. Every $z \in Q$ has polar representation $z = r e^{i\theta}$ with $r > 0$ and $\theta \in (0, \pi/2)$.
    <2>2. Define $F(z) = z^2$. For $z \in Q$, $F(z) = r^2 e^{i 2\theta}$ with $2\theta \in (0, \pi)$, so $F$ maps $Q$ biholomorphically onto the upper half-plane $\mathbb{H} = \{w \in \mathbb{C} : \Im w > 0\}$.
    <2>3. The boundary components of $Q$ map under $z \mapsto z^2$ as follows:
        - The positive imaginary axis $\{x = 0, y > 0\}$ maps to the negative real axis $(-\infty, 0)$ via $(iy)^2 = -y^2 < 0$.
        - The segment $\{0 < x < 1, y = 0\}$ maps to the segment $(0, 1)$ on the real axis via $x^2 \in (0, 1)$.
        - The ray $\{x > 1, y = 0\}$ maps to the ray $(1, \infty)$ on the real axis via $x^2 \in (1, \infty)$.

<1>2. Construction of the harmonic profile on the upper half-plane $\mathbb{H}$:
    *Proof:*
    <2>1. For $w \in \mathbb{H}$, let $\arg(w) = \operatorname{Im}(\log w) \in (0, \pi)$ and $\arg(w - 1) = \operatorname{Im}(\log(w - 1)) \in (0, \pi)$, where $\log$ denotes the principal branch of logarithm holomorphic on $\mathbb{C} \setminus (-\infty, 0]$.
    <2>2. Both $\arg(w)$ and $\arg(w - 1)$ are real parts of holomorphic functions (namely $\operatorname{Re}(-i \log w)$), so they are harmonic on $\mathbb{H}$.
    <2>3. Define $v: \mathbb{H} \to \mathbb{R}$ by
    $$v(w) = 1 - \frac{1}{\pi}\Big(\arg(w - 1) - \arg(w)\Big).$$
    As a linear combination of harmonic functions, $v$ is harmonic on $\mathbb{H}$.
    <2>4. Boundary limits of $v(u + iv)$ as $v \to 0^+$:
        - For $u > 1$: $u > 0$ and $u - 1 > 0$, so $\arg(w) \to 0$ and $\arg(w - 1) \to 0$. Thus $\lim_{v \to 0^+} v(u + iv) = 1 - \frac{1}{\pi}(0 - 0) = 1$.
        - For $0 < u < 1$: $u > 0$ and $u - 1 < 0$, so $\arg(w) \to 0$ and $\arg(w - 1) \to \pi$. Thus $\lim_{v \to 0^+} v(u + iv) = 1 - \frac{1}{\pi}(\pi - 0) = 0$.
        - For $u < 0$: $u < 0$ and $u - 1 < 0$, so $\arg(w) \to \pi$ and $\arg(w - 1) \to \pi$. Thus $\lim_{v \to 0^+} v(u + iv) = 1 - \frac{1}{\pi}(\pi - \pi) = 1$.

<1>3. Pullback to the quadrant $Q$:
    *Proof:*
    <2>1. Define $u: Q \to \mathbb{R}$ by $u(z) = v(F(z)) = v(z^2)$.
    <2>2. Since $F(z) = z^2$ is holomorphic on $Q$ and $v$ is harmonic on $\mathbb{H}$, the composition $u = v \circ F$ is harmonic on $Q$.
    <2>3. By the boundary correspondence established in <1>1 and the boundary values of $v$ from <1>2:
        - For $z = x \in (1, \infty)$, $z^2 = x^2 \in (1, \infty)$, so $u(x, 0) = 1$.
        - For $z = x \in (0, 1)$, $z^2 = x^2 \in (0, 1)$, so $u(x, 0) = 0$.
        - For $z = iy$ with $y > 0$, $z^2 = -y^2 \in (-\infty, 0)$, so $u(0, y) = 1$.

<1>4. Conclusion:
    *Proof:*
    The function
    $$u(z) = 1 - \frac{1}{\pi}\Big(\arg(z^2 - 1) - \arg(z^2)\Big)$$
    is harmonic in the first quadrant $Q$, extends continuously to $\partial Q \setminus \{0, 1\}$, and takes the required boundary values $1, 0, 1$.
:::
