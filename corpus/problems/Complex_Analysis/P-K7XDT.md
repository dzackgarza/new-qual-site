---
schema: qual/card@1
id: P-K7XDT
kind: problem
title: A conformal map from $\{\Re z>0,\ |z-i|>1\}$ onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Find a conformal map from $\Omega = \{z\in \mathbb{C} \mid |z-i| > 1,\, \operatorname{Re}(z) > 0\}$ to $\mathbb{H} = \{w \in \mathbb{C} \mid \operatorname{Im}(w) > 0\}$.
:::

::: solution
**Goal:** Construct a conformal equivalence $f: \Omega \to \mathbb{H}$ where $\Omega = \{z \in \mathbb{C} \mid |z-i| > 1, \, \operatorname{Re}(z) > 0\}$.

<1>1. Analysis of the domain boundary:
    *Proof:*
    <2>1. The domain $\Omega$ is bounded by the imaginary axis $\{it \mid t \in \mathbb{R}\}$ and the right semi-circle of $\partial D(i, 1)$, meeting at $z = 0$ and $z = 2i$.
    <2>2. The angle at each vertex ($z = 0$ and $z = 2i$) is $\pi/2$.

<1>2. Step 1: Mobius transformation sending the vertices $0$ and $2i$ to $0$ and $\infty$:
    *Proof:*
    <2>1. Define $T_1(z) = \frac{z}{z - 2i}$.
    <2>2. $T_1(0) = 0$, $T_1(2i) = \infty$, $T_1(i) = \frac{i}{-i} = -1$, and $T_1(1+i) = \frac{1+i}{1-i} = i$.
    <2>3. The circle $|z-i| = 1$ passes through $0, 2i, 1+i$, so its image under $T_1$ is a line through $0, \infty, i$, which is the imaginary axis $i\mathbb{R}$.
    <2>4. The imaginary axis $i\mathbb{R}$ passes through $0, 2i, i$, so its image under $T_1$ is a line through $0, \infty, -1$, which is the real axis $\mathbb{R}$.
    <2>5. Since $T_1(1+i) = i$ and $1+i \in \Omega$ with $\operatorname{Re}(1+i) > 0$ and $|1+i-i| = 1$ (on the boundary), points in $\Omega$ with $\operatorname{Re}(z) > 0$ and $|z-i| > 1$ map to the second quadrant $Q_2 = \{w \in \mathbb{C} \mid \operatorname{Re}(w) < 0, \, \operatorname{Im}(w) > 0\}$.
    <2>6. Verification: test $z = 2+i \in \Omega$:
        $$T_1(2+i) = \frac{2+i}{2-i} = \frac{(2+i)^2}{5} = \frac{3+4i}{5} \notin Q_2.$$
        Wait: the angle between the circle and imaginary axis at $0$ is $\pi/2$. The circle goes into the right half-plane.
        At $z=0$, the tangent to the circle points into the right half-plane (direction $+1$), and the imaginary axis points upward (direction $+i$).
        $T_1'(0) = \frac{-2i}{(-2i)^2} = \frac{1}{2i} = -\frac{i}{2}$.
        The tangent $+1$ maps to $-i/2$ (negative imaginary axis).
        The tangent $+i$ maps to $(-i/2)(i) = 1/2$ (positive real axis).
        The region between them maps to the fourth quadrant $Q_4 = \{w \mid \operatorname{Re}(w) > 0, \, \operatorname{Im}(w) < 0\}$.
    <2>7. Indeed, for $z = 2+i$: $|z-i| = 2 > 1$ and $\operatorname{Re}(z) = 2 > 0$, so $z \in \Omega$.
        $T_1(2+i) = \frac{3+4i}{5}$ has positive real and imaginary parts (first quadrant).
        Since $T_1$ maps the two boundary curves to the positive real axis and negative imaginary axis, $\Omega$ maps conformally to the fourth quadrant $Q_4 = \{w \mid \operatorname{Arg}(w) \in (-\pi/2, 0)\}$.

<1>3. Step 2: Rotation to the upper half-plane:
    *Proof:*
    <2>1. To send the wedge $(-\pi/2, 0)$ to the first quadrant $(0, \pi/2)$, multiply by $i = e^{i\pi/2}$:
        $$T_2(w) = iw \quad \text{maps } Q_4 \text{ to } Q_1 = \{u \in \mathbb{C} \mid \operatorname{Re}(u) > 0, \, \operatorname{Im}(u) > 0\}.$$
    <2>2. Composing: $T_2(T_1(z)) = i \frac{z}{z - 2i} = \frac{iz}{z - 2i}$.

<1>4. Step 3: Squaring to open the first quadrant to the upper half-plane:
    *Proof:*
    <2>1. The map $T_3(\zeta) = \zeta^2$ maps the first quadrant $Q_1 = \{\zeta \in \mathbb{C} \mid \operatorname{Arg}(\zeta) \in (0, \pi/2)\}$ conformally onto the upper half-plane $\mathbb{H} = \{W \in \mathbb{C} \mid \operatorname{Im}(W) > 0\}$.
    <2>2. Combining all three steps:
        $$f(z) = T_3(T_2(T_1(z))) = \left(\frac{iz}{z - 2i}\right)^2 = -\frac{z^2}{(z - 2i)^2} = \left(\frac{z}{2i - z}\right)^2.$$

<1>5. Verification:
    *Proof:*
    <2>1. For $z = 1 \in \Omega$ ($|1-i| = \sqrt{2} > 1$, $\operatorname{Re}(1) = 1 > 0$):
        $$\frac{i(1)}{1-2i} = \frac{i(1+2i)}{5} = \frac{-2+i}{5} \in Q_2.$$
        Wait, earlier $T_2(T_1(1)) = i \cdot \frac{1}{1-2i} = \frac{-2+i}{5} \in Q_2$, which has argument in $(\pi/2, \pi)$.
        Squaring gives argument in $(\pi, 2\pi) \implies \operatorname{Im} < 0$.
        Let's adjust the rotation: $T_1(1) = \frac{1}{1-2i} = \frac{1+2i}{5} \in Q_1$.
        Let's check $T_1(\Omega)$: $z=1$ gives $T_1(1) \in Q_1$. $z=2$ gives $T_1(2) = \frac{2}{2-2i} = \frac{1}{1-i} = \frac{1+i}{2} \in Q_1$.
        So $T_1(\Omega)$ is actually the first quadrant $Q_1 = \{w \mid \operatorname{Re}(w) > 0, \operatorname{Im}(w) > 0\}$.
    <2>2. Since $T_1(\Omega) = Q_1$, we simply need $f(z) = (T_1(z))^2 = \left(\frac{z}{z-2i}\right)^2$.
    <2>3. Check for $z = 2$: $T_1(2) = \frac{1+i}{2}$, which has argument $\pi/4$.
        Then $(T_1(2))^2 = \left(\frac{1+i}{2}\right)^2 = \frac{2i}{4} = \frac{i}{2} \in \mathbb{H}$.
    <2>4. The squaring map $w \mapsto w^2$ maps the first quadrant $Q_1$ biholomorphically onto the upper half-plane $\mathbb{H}$.

<1>6. Conclusion:
    The map $f(z) = \left(\frac{z}{z - 2i}\right)^2$ is a conformal map from $\Omega$ onto $\mathbb{H}$. Q.E.D.
:::
