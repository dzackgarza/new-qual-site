---
schema: qual/card@1
id: P-IJQ5Z
kind: problem
title: A conformal map from $\CC\setminus(-\infty,0]$ onto $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Construct an explicit **conformal map** (biholomorphic equivalence) from the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$ onto the open unit disk $\mathbb{D} = \{w \in \mathbb{C} \mid |w| < 1\}$.
:::

::: solution
**Goal:** Construct a biholomorphic isomorphism $F: \mathbb{C} \setminus (-\infty, 0] \xrightarrow{\sim} \mathbb{D}$ as a composition of standard elementary conformal transformations.

<1>1. Step 1: Conformal Map to the Right Half-Plane via Principal Square Root:
    *Proof:*
    <2>1. On the slit plane $\Omega = \mathbb{C} \setminus (-\infty, 0]$, every point $z$ has a unique polar representation:
        $$z = r e^{i\theta} \quad \text{with } r > 0 \text{ and } \theta \in (-\pi, \pi).$$
    <2>2. Define the **principal branch of the square root**:
        $$f_1(z) = \sqrt{z} = \sqrt{r} e^{i\theta/2}.$$
    <2>3. Since $\theta \in (-\pi, \pi)$, the argument $\theta/2 \in (-\pi/2, \pi/2)$.
    <2>4. Thus $\operatorname{Re}(f_1(z)) = \sqrt{r} \cos(\theta/2) > 0$.
    <2>5. The map $f_1: \Omega \to \mathbb{H}_R = \{u \in \mathbb{C} \mid \operatorname{Re}(u) > 0\}$ is a **biholomorphic conformal isomorphism** from the slit plane $\Omega$ onto the open **right half-plane** $\mathbb{H}_R$.

<1>2. Step 2: Conformal Map from the Right Half-Plane to the Unit Disk via Cayley Transform:
    *Proof:*
    <2>1. The standard Möbius (Cayley) transformation mapping the right half-plane $\mathbb{H}_R$ to the open unit disk $\mathbb{D}$ is:
        $$f_2(u) = \frac{u - 1}{u + 1}.$$
    <2>2. We verify that $f_2(\mathbb{H}_R) = \mathbb{D}$:
        - For any $u = x + i y$ with $x > 0$:
          $$|f_2(u)|^2 = \frac{|(x - 1) + i y|^2}{|(x + 1) + i y|^2} = \frac{(x - 1)^2 + y^2}{(x + 1)^2 + y^2} = \frac{x^2 - 2x + 1 + y^2}{x^2 + 2x + 1 + y^2}.$$
        - Since $x > 0$, $-2x < 2x$, so the numerator is strictly smaller than the denominator:
          $$|f_2(u)| < 1 \implies f_2(u) \in \mathbb{D}.$$
        - On the imaginary axis $x = 0$, $|f_2(i y)| = \frac{|-1 + i y|}{|1 + i y|} = 1$, mapping the boundary line to the boundary circle $\partial\mathbb{D}$.
        - $f_2(1) = \frac{1 - 1}{1 + 1} = 0 \in \mathbb{D}$.
    <2>3. Thus $f_2: \mathbb{H}_R \to \mathbb{D}$ is a biholomorphic isomorphism.

<1>3. Composition to form the Full Conformal Map:
    *Proof:*
    <2>1. Composing $f_2 \circ f_1$:
        $$F(z) = f_2(f_1(z)) = \frac{\sqrt{z} - 1}{\sqrt{z} + 1}$$
        where $\sqrt{z}$ denotes the principal branch of the square root on $\mathbb{C} \setminus (-\infty, 0]$.
    <2>2. Being the composition of two biholomorphic maps:
        $$\Omega = \mathbb{C} \setminus (-\infty, 0] \xrightarrow{\quad \sqrt{z} \quad} \mathbb{H}_R \xrightarrow{\quad \frac{u-1}{u+1} \quad} \mathbb{D}$$
        $F: \Omega \to \mathbb{D}$ is an explicit conformal map onto $\mathbb{D}$.

<1>4. Inverse Map:
    *Proof:*
    <2>1. Solving $w = \frac{\sqrt{z} - 1}{\sqrt{z} + 1}$ for $z$:
        $$w(\sqrt{z} + 1) = \sqrt{z} - 1 \implies \sqrt{z}(1 - w) = 1 + w \implies \sqrt{z} = \frac{1 + w}{1 - w}.$$
    <2>2. Squaring gives:
        $$F^{-1}(w) = \left( \frac{1 + w}{1 - w} \right)^2 \quad \text{for } w \in \mathbb{D}.$$

<1>5. Conclusion:
    The map $F(z) = \frac{\sqrt{z} - 1}{\sqrt{z} + 1}$ is a conformal isomorphism from $\mathbb{C} \setminus (-\infty, 0]$ onto $\mathbb{D}$. Q.E.D.
:::
