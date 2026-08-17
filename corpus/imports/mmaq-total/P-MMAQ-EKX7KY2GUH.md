---
schema: qual/card@1
id: P-MMAQ-EKX7KY2GUH
kind: problem
title: Divergence theorem on a rectangle in $\RR^2$
classification:
  areas:
  - complex-analysis
  topics:
  - green-s-theorem
relations: []
review: draft
solved: true
---

::: problem
State and prove the divergence theorem on any rectangle in $\mathbb{R}^2$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** State and prove the 2D Divergence Theorem (Green's theorem in normal form) on any closed rectangle $R = [a, b] \times [c, d] \subset \mathbb{R}^2$.

* * *

### Statement of the Divergence Theorem on a Rectangle

**Theorem:** Let $R = [a, b] \times [c, d] \subset \mathbb{R}^2$ be a closed rectangle, and let $\partial R$ denote its boundary oriented counterclockwise.
Let $\mathbf{F} = (P, Q): U \to \mathbb{R}^2$ be a $C^1$ vector field defined on an open neighborhood $U \supset R$.
Then: $$\iint_R \text{div}(\mathbf{F}) \, dA = \oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds,$$ where $\text{div}(\mathbf{F}) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}$, $\mathbf{n}$ is the outward-pointing unit normal vector along $\partial R$, and $ds$ is the arc length element.
In coordinates, $\oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds = \oint_{\partial R} (P \, dy - Q \, dx)$.

* * *

### Proof

<1>1. **Decompose the theorem into separate claims for $P$ and $Q$.** <2>1. Linearity of the integral gives: $$\iint_R \text{div}(\mathbf{F}) \, dA = \iint_R \frac{\partial P}{\partial x} \, dA + \iint_R \frac{\partial Q}{\partial y} \, dA.$$ *Proof:* Additivity of the double integral.
<2>2. The boundary flux splits into: $$\oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds = \oint_{\partial R} P \, dy - \oint_{\partial R} Q \, dx.$$ *Proof:* Standard identification of $\mathbf{n}\,ds = (dy, -dx)$ for counterclockwise boundary orientation.
<2>3. It suffices to prove: $$\text{(I)} \quad \iint_R \frac{\partial P}{\partial x} \, dA = \oint_{\partial R} P \, dy, \qquad \text{and} \qquad \text{(II)} \quad \iint_R \frac{\partial Q}{\partial y} \, dA = -\oint_{\partial R} Q \, dx.$$ *Proof:* Adding (I) and (II) yields the full theorem.
<2>4. Q.E.D.

<1>2. **Proof of Claim (I): $\iint_R \frac{\partial P}{\partial x} \, dA = \oint_{\partial R} P \, dy$.** <2>1. By Fubini's Theorem and the Fundamental Theorem of Calculus: $$\iint_R \frac{\partial P}{\partial x} \, dA = \int_c^d \left( \int_a^b \frac{\partial P}{\partial x}(x, y) \, dx \right) dy = \int_c^d \big( P(b, y) - P(a, y) \big) \, dy.$$ *Proof:* FTC on the inner integral since $P$ is $C^1$.
<2>2. Parametrize the four sides of the boundary $\partial R = \gamma_1 + \gamma_2 + \gamma_3 + \gamma_4$:

- Bottom edge $\gamma_1$: $x \in [a, b], y = c \implies dy = 0$.

- Right edge $\gamma_2$: $x = b, y \in [c, d]$ (oriented upwards) $\implies dy = dy$.

- Top edge $\gamma_3$: $x \in [a, b], y = d \implies dy = 0$.

- Left edge $\gamma_4$: $x = a, y \in [c, d]$ (oriented downwards) $\implies dy = -dy$.
  *Proof:* Counterclockwise orientation of the rectangle perimeter.
  <2>3. Compute the line integral $\oint_{\partial R} P \, dy$: $$\oint_{\partial R} P \, dy = \int_{\gamma_1} P \, dy + \int_{\gamma_2} P \, dy + \int_{\gamma_3} P \, dy + \int_{\gamma_4} P \, dy = 0 + \int_c^d P(b, y) \, dy + 0 + \int_d^c P(a, y) \, dy = \int_c^d \big( P(b, y) - P(a, y) \big) \, dy.$$ *Proof:* Sum of line integrals along the four segments.
  <2>4. Comparing <2>1 and <2>3 establishes $\iint_R \frac{\partial P}{\partial x} \, dA = \oint_{\partial R} P \, dy$.
  *Proof:* Both equal $\int_c^d (P(b,y) - P(a,y))\,dy$.
  <2>5. Q.E.D.

<1>3. **Proof of Claim (II): $\iint_R \frac{\partial Q}{\partial y} \, dA = -\oint_{\partial R} Q \, dx$.** <2>1. By Fubini's Theorem and the Fundamental Theorem of Calculus: $$\iint_R \frac{\partial Q}{\partial y} \, dA = \int_a^b \left( \int_c^d \frac{\partial Q}{\partial y}(x, y) \, dy \right) dx = \int_a^b \big( Q(x, d) - Q(x, c) \big) \, dx.$$ *Proof:* FTC on the inner integral with respect to $y$.
<2>2. Compute the line integral $\oint_{\partial R} Q \, dx$ along the four sides:

- Bottom edge $\gamma_1$: $x \in [a, b]$ from left to right, $y = c \implies \int_{\gamma_1} Q \, dx = \int_a^b Q(x, c) \, dx$.

- Right edge $\gamma_2$: $x = b \implies dx = 0$.

- Top edge $\gamma_3$: $x$ from $b$ to $a$, $y = d \implies \int_{\gamma_3} Q \, dx = \int_b^a Q(x, d) \, dx = -\int_a^b Q(x, d) \, dx$.

- Left edge $\gamma_4$: $x = a \implies dx = 0$.
  *Proof:* Parametrizations of the four edges.
  <2>3. Summing these four contributions: $$\oint_{\partial R} Q \, dx = \int_a^b Q(x, c) \, dx - \int_a^b Q(x, d) \, dx = -\int_a^b \big( Q(x, d) - Q(x, c) \big) \, dx.$$ *Proof:* Adding line integrals along the boundary.
  <2>4. Negating both sides yields $-\oint_{\partial R} Q \, dx = \int_a^b (Q(x, d) - Q(x, c)) \, dx = \iint_R \frac{\partial Q}{\partial y} \, dA$.
  *Proof:* Compares <2>1 and <2>3. <2>5. Q.E.D.

<1>4. **Conclusion: $\iint_R \text{div}(\mathbf{F}) \, dA = \oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds$.** <2>1. Adding the equalities from <1>2 and <1>3 proves the theorem for any closed rectangle $R$.
*Proof:* Follows from <1>1.<2>3. <2>2. Q.E.D.
:::
