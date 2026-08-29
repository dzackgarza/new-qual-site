---
schema: qual/card@1
id: P-CWXEW
kind: problem
title: "Conformal map from a slit lens to the upper half plane"
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
Find a bijective conformal map from $G$ to $\mathbb{H} = \{w \in \mathbb{C} \mid \operatorname{Im}(w) > 0\}$, where
$$G \coloneqq \{z \in \mathbb{C} \mid |z-1| < \sqrt{2}, \, |z+1| < \sqrt{2}\} \setminus [0, i).$$
:::

::: solution
**Goal:** Construct an explicit bijective conformal equivalence $f: G \to \mathbb{H}$ from the slit lens domain $G$ to the upper half plane $\mathbb{H}$.

<1>1. Geometry of the lens domain $L = \{|z-1| < \sqrt{2}\} \cap \{|z+1| < \sqrt{2}\}$:
    *Proof:*
    <2>1. The boundary circular arcs are $|z-1| = \sqrt{2}$ and $|z+1| = \sqrt{2}$.
    <2>2. Intersection points: $(x-1)^2 + y^2 = 2$ and $(x+1)^2 + y^2 = 2 \implies x = 0, y^2 = 1 \implies z = \pm i$.
    <2>3. The tangent vectors to the two circles at $z = -i$ and $z = i$ make an interior angle of $\pi/2$ (since the radii to $1$ and $-1$ from $i$ are orthogonal: vectors $(-1, 1)$ and $(1, 1)$ have dot product 0).
    <2>4. Thus $L$ is a symmetric circular lens with vertices at $\pm i$ and internal angle $\pi/2$.

<1>2. Step 1: Möbius transformation to an infinite wedge:
    *Proof:*
    <2>1. Send the vertices $i \mapsto 0$ and $-i \mapsto \infty$ via the Möbius transformation:
        $$T_1(z) = \frac{z - i}{z + i}.$$
    <2>2. Test boundary/interior points:
        - $z = 0 \in L \implies T_1(0) = \frac{-i}{i} = -1 = e^{i\pi}$.
        - $z = 1 \implies T_1(1) = \frac{1-i}{1+i} = -i = e^{i 3\pi/2}$.
        - $z = -1 \implies T_1(-1) = \frac{-1-i}{-1+i} = i = e^{i \pi/2}$.
    <2>3. Thus, $T_1$ maps the unslit lens $L$ conformally onto the wedge (sector):
        $$W = \left\{ w \in \mathbb{C} \;\middle|\; \frac{\pi}{2} < \arg(w) < \frac{3\pi}{2} \right\}.$$
    <2>4. The slit $[0, i)$ connects $0$ to $i$. Under $T_1$, as $t$ goes from $0$ to $1$ along $z = it$:
        $$T_1(it) = \frac{i(t-1)}{i(t+1)} = \frac{t-1}{t+1} \in (-1, 0].$$
    <2>5. Thus the slit $[0, i)$ is mapped to the line segment $(-1, 0]$ on the negative real axis (which bisects the wedge $W$).
    <2>6. Hence $T_1(G)$ is the wedge $W \setminus (-1, 0]$.

<1>3. Step 2: Rotate the wedge to the right half-plane:
    *Proof:*
    <2>1. Apply $T_2(w) = -w = e^{-i\pi} w$.
    <2>2. The wedge $W$ rotates to the right half-plane:
        $$\mathbb{H}_R = \left\{ \zeta \in \mathbb{C} \;\middle|\; -\frac{\pi}{2} < \arg(\zeta) < \frac{\pi}{2} \right\} = \{\operatorname{Re}(\zeta) > 0\}.$$
    <2>3. The slit $(-1, 0]$ becomes the slit $[0, 1)$ along the positive real axis.
    <2>4. So $T_2(T_1(G)) = \mathbb{H}_R \setminus [0, 1)$.

<1>4. Step 3: Square to open the right half-plane into the slit plane:
    *Proof:*
    <2>1. Apply $T_3(\zeta) = \zeta^2$.
    <2>2. $\mathbb{H}_R$ maps bijectively onto the cut complex plane $\mathbb{C} \setminus (-\infty, 0]$.
    <2>3. The slit $[0, 1)$ on the positive real axis maps to the slit $[0, 1)$ on the positive real axis.
    <2>4. Thus $T_3(T_2(T_1(G))) = \mathbb{C} \setminus ((-\infty, 0] \cup [0, 1)) = \mathbb{C} \setminus (-\infty, 1)$.

<1>5. Step 4: Shift and square root to the upper half plane:
    *Proof:*
    <2>1. Shift by $1$: $T_4(u) = u - 1$, mapping $\mathbb{C} \setminus (-\infty, 1)$ to $\mathbb{C} \setminus (-\infty, 0]$.
    <2>2. Principal square root: $T_5(v) = \sqrt{v}$, mapping $\mathbb{C} \setminus (-\infty, 0]$ conformally to the right half-plane $\mathbb{H}_R$.
    <2>3. Rotate by $i$: $T_6(s) = i s$, mapping $\mathbb{H}_R$ to the upper half plane $\mathbb{H}$.
    <2>4. Composing the transformations:
        $$f(z) = i \sqrt{ \left(-\frac{z-i}{z+i}\right)^2 - 1 } = i \sqrt{ \frac{(z-i)^2 - (z+i)^2}{(z+i)^2} } = i \sqrt{ \frac{-4iz}{(z+i)^2} } = \frac{i \sqrt{-4iz}}{z+i} = \frac{2 e^{i\pi/4} \sqrt{z}}{z+i}.$$

<1>6. Conclusion:
    The map $f(z) = \frac{2 e^{i\pi/4}\sqrt{z}}{z+i}$ (with appropriate branch) is a bijective conformal map from $G$ to $\mathbb{H}$. Q.E.D.
:::
