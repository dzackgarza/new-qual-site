---
schema: qual/card@1
id: P-MMAQ-S7C4CCIUTP
kind: problem
title: Cauchy's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Theorem
  - Green's Theorem
relations: []
review: draft
---

::: problem
Use Green theorem or otherwise to prove the Cauchy theorem.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** State and prove Cauchy's Theorem (under the classical assumption that $f'$ is continuous) using Green's Theorem.

* * *

### Statement of Cauchy's Theorem

**Theorem:** Let $\Omega \subset \mathbb{C}$ be a simply connected domain.
Let $f: \Omega \to \mathbb{C}$ be a holomorphic function whose derivative $f'$ is continuous ($f \in C^1(\Omega)$). Let $\gamma$ be a piecewise smooth, positively oriented simple closed curve whose interior $\text{Int}(\gamma)$ is contained in $\Omega$.
Then: $$\oint_\gamma f(z) \, dz = 0.$$

* * *

### Proof via Green's Theorem

<1>1. **Decompose the complex contour integral into real line integrals.** <2>1. Write $f(z) = u(x, y) + i v(x, y)$ where $z = x + iy$, and $dz = dx + i dy$.
*Proof:* Decomposition of complex functions and differentials into real and imaginary parts.
<2>2. The product $f(z) \, dz$ expands as: $$f(z) \, dz = (u + iv)(dx + i dy) = (u \, dx - v \, dy) + i (v \, dx + u \, dy).$$ *Proof:* Algebraic expansion of complex multiplication ($i^2 = -1$). <2>3. Integrating along $\gamma$: $$\oint_\gamma f(z) \, dz = \oint_\gamma (u \, dx - v \, dy) + i \oint_\gamma (v \, dx + u \, dy).$$ *Proof:* Linearity of integration.
<2>4. Q.E.D.

<1>2. **Recall Green's Theorem on the bounded region $D = \text{Int}(\gamma)$.** <2>1. Let $D \subset \mathbb{R}^2$ be the bounded region enclosed by $\gamma = \partial D$.
If $P, Q: \overline{D} \to \mathbb{R}$ are $C^1$, then: $$\oint_\gamma (P \, dx + Q \, dy) = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA.$$ *Proof:* Statement of Green's Theorem for planar regions.
<2>2. Since $f'$ is continuous, the partial derivatives $u_x, u_y, v_x, v_y$ exist and are continuous on $\overline{D}$, so Green's Theorem is applicable.
*Proof:* Continuity of $f'$ implies $u, v \in C^1(\overline{D})$.
<2>3. Q.E.D.

<1>3. **Evaluate the real part $\oint_\gamma (u \, dx - v \, dy)$.** <2>1. Set $P = u$ and $Q = -v$.
*Proof:* Identification of components.
<2>2. By Green's Theorem: $$\oint_\gamma (u \, dx - v \, dy) = \iint_D \left( \frac{\partial(-v)}{\partial x} - \frac{\partial u}{\partial y} \right) dA = -\iint_D \left( \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y} \right) dA.$$ *Proof:* Applying Green's Theorem to $P = u, Q = -v$.
<2>3. By the Cauchy-Riemann equations for the holomorphic function $f$, $u_y = -v_x \iff v_x + u_y = 0$.
*Proof:* Cauchy-Riemann equations hold everywhere in $\Omega \supset \overline{D}$.
<2>4. Therefore: $$\oint_\gamma (u \, dx - v \, dy) = -\iint_D 0 \, dA = 0.$$ *Proof:* Substitution of <2>3 into <2>2. <2>5. Q.E.D.

<1>4. **Evaluate the imaginary part $\oint_\gamma (v \, dx + u \, dy)$.** <2>1. Set $P = v$ and $Q = u$.
*Proof:* Identification of components.
<2>2. By Green's Theorem: $$\oint_\gamma (v \, dx + u \, dy) = \iint_D \left( \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \right) dA.$$ *Proof:* Applying Green's Theorem to $P = v, Q = u$.
<2>3. By the Cauchy-Riemann equations for $f$, $u_x = v_y \iff u_x - v_y = 0$.
*Proof:* Cauchy-Riemann equations.
<2>4. Therefore: $$\oint_\gamma (v \, dx + u \, dy) = \iint_D 0 \, dA = 0.$$ *Proof:* Substitution of <2>3 into <2>2. <2>5. Q.E.D.

<1>5. **Conclusion: $\oint_\gamma f(z) \, dz = 0$.** <2>1. Combining the real and imaginary parts from <1>3 and <1>4: $$\oint_\gamma f(z) \, dz = 0 + i(0) = 0.$$ *Proof:* Follows from <1>1.<2>3. <2>2. Q.E.D.
:::
