---
schema: qual/card@1
id: P-MMAQ-EKX7KY2GUH
kind: problem
title: Divergence theorem on a rectangle in $\RR^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
State and prove the divergence theorem on any rectangle in $\mathbb{R}^2$.
:::

::: {.solution}
### Statement of the divergence theorem on a rectangle

Let $R = [a, b] \times [c, d] \subset \mathbb{R}^2$ be a closed rectangle, and let $\partial R$ denote its boundary oriented counterclockwise.
Let $\mathbf{F} = (P, Q): U \to \mathbb{R}^2$ be a $C^1$ vector field defined on an open neighborhood $U \supset R$.
Then: $$\iint_R \text{div}(\mathbf{F}) \, dA = \oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds,$$ where $\text{div}(\mathbf{F}) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y}$, $\mathbf{n}$ is the outward-pointing unit normal vector along $\partial R$, and $ds$ is the arc length element.
In coordinates, $\oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds = \oint_{\partial R} (P \, dy - Q \, dx)$.

* * *

### Proof

::: pf

::: pf-step
**Decompose the theorem into separate claims for $P$ and $Q$.**

::: pf-proof

::: pf-step
Linearity of the integral gives: $$\iint_R \text{div}(\mathbf{F}) \, dA = \iint_R \frac{\partial P}{\partial x} \, dA + \iint_R \frac{\partial Q}{\partial y} \, dA.$$

::: pf-proof
*Proof:* Additivity of the double integral.
:::

:::

::: pf-step
The boundary flux splits into: $$\oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds = \oint_{\partial R} P \, dy - \oint_{\partial R} Q \, dx.$$

::: pf-proof
*Proof:* Standard identification of $\mathbf{n}\,ds = (dy, -dx)$ for counterclockwise boundary orientation.
:::

:::

::: {.pf-step #suffices-to-prove-I-and-II}
It suffices to prove: $$\text{(I)} \quad \iint_R \frac{\partial P}{\partial x} \, dA = \oint_{\partial R} P \, dy, \qquad \text{and} \qquad \text{(II)} \quad \iint_R \frac{\partial Q}{\partial y} \, dA = -\oint_{\partial R} Q \, dx.$$

::: pf-proof
*Proof:* Adding (I) and (II) yields the full theorem.
:::

:::

:::

::: pf-qed
Step [](#suffices-to-prove-I-and-II){.pf-ref}.
:::

:::

::: {.pf-step #claim-I-proof}
**Proof of Claim (I): $\iint_R \frac{\partial P}{\partial x} \, dA = \oint_{\partial R} P \, dy$.**

::: pf-proof

::: {.pf-step #claim-I-ftc-identity}
By Fubini's Theorem and the Fundamental Theorem of Calculus: $$\iint_R \frac{\partial P}{\partial x} \, dA = \int_c^d \left( \int_a^b \frac{\partial P}{\partial x}(x, y) \, dx \right) dy = \int_c^d \big( P(b, y) - P(a, y) \big) \, dy.$$

::: pf-proof
*Proof:* FTC on the inner integral since $P$ is $C^1$.
:::

:::

::: pf-step
Parametrize the four sides of the boundary $\partial R = \gamma_1 + \gamma_2 + \gamma_3 + \gamma_4$:

- Bottom edge $\gamma_1$: $x \in [a, b], y = c \implies dy = 0$.

- Right edge $\gamma_2$: $x = b, y \in [c, d]$ (oriented upwards) $\implies dy = dy$.

- Top edge $\gamma_3$: $x \in [a, b], y = d \implies dy = 0$.

- Left edge $\gamma_4$: $x = a, y \in [c, d]$ (oriented downwards) $\implies dy = -dy$.

::: pf-proof
*Proof:* Counterclockwise orientation of the rectangle perimeter.
:::

:::

::: {.pf-step #claim-I-line-integral-computation}
Compute the line integral $\oint_{\partial R} P \, dy$: $$\oint_{\partial R} P \, dy = \int_{\gamma_1} P \, dy + \int_{\gamma_2} P \, dy + \int_{\gamma_3} P \, dy + \int_{\gamma_4} P \, dy = 0 + \int_c^d P(b, y) \, dy + 0 + \int_d^c P(a, y) \, dy = \int_c^d \big( P(b, y) - P(a, y) \big) \, dy.$$

::: pf-proof
*Proof:* Sum of line integrals along the four segments.
:::

:::

::: {.pf-step #claim-I-established}
Comparing step [](#claim-I-ftc-identity){.pf-ref} and step [](#claim-I-line-integral-computation){.pf-ref} establishes $\iint_R \frac{\partial P}{\partial x} \, dA = \oint_{\partial R} P \, dy$.

::: pf-proof
*Proof:* Both equal $\int_c^d (P(b,y) - P(a,y))\,dy$.
:::

:::

:::

::: pf-qed
Step [](#claim-I-established){.pf-ref}.
:::

:::

::: {.pf-step #claim-II-proof}
**Proof of Claim (II): $\iint_R \frac{\partial Q}{\partial y} \, dA = -\oint_{\partial R} Q \, dx$.**

::: pf-proof

::: {.pf-step #claim-II-ftc-identity}
By Fubini's Theorem and the Fundamental Theorem of Calculus: $$\iint_R \frac{\partial Q}{\partial y} \, dA = \int_a^b \left( \int_c^d \frac{\partial Q}{\partial y}(x, y) \, dy \right) dx = \int_a^b \big( Q(x, d) - Q(x, c) \big) \, dx.$$

::: pf-proof
*Proof:* FTC on the inner integral with respect to $y$.
:::

:::

::: pf-step
Compute the line integral $\oint_{\partial R} Q \, dx$ along the four sides:

- Bottom edge $\gamma_1$: $x \in [a, b]$ from left to right, $y = c \implies \int_{\gamma_1} Q \, dx = \int_a^b Q(x, c) \, dx$.

- Right edge $\gamma_2$: $x = b \implies dx = 0$.

- Top edge $\gamma_3$: $x$ from $b$ to $a$, $y = d \implies \int_{\gamma_3} Q \, dx = \int_b^a Q(x, d) \, dx = -\int_a^b Q(x, d) \, dx$.

- Left edge $\gamma_4$: $x = a \implies dx = 0$.

::: pf-proof
*Proof:* Parametrizations of the four edges.
:::

:::

::: {.pf-step #claim-II-line-integral-computation}
Summing these four contributions: $$\oint_{\partial R} Q \, dx = \int_a^b Q(x, c) \, dx - \int_a^b Q(x, d) \, dx = -\int_a^b \big( Q(x, d) - Q(x, c) \big) \, dx.$$

::: pf-proof
*Proof:* Adding line integrals along the boundary.
:::

:::

::: {.pf-step #claim-II-established}
Negating both sides yields $-\oint_{\partial R} Q \, dx = \int_a^b (Q(x, d) - Q(x, c)) \, dx = \iint_R \frac{\partial Q}{\partial y} \, dA$.

::: pf-proof
*Proof:* Compares step [](#claim-II-ftc-identity){.pf-ref} and step [](#claim-II-line-integral-computation){.pf-ref}.
:::

:::

:::

::: pf-qed
Step [](#claim-II-established){.pf-ref}.
:::

:::

::: pf-step
**Conclusion: $\iint_R \text{div}(\mathbf{F}) \, dA = \oint_{\partial R} \mathbf{F} \cdot \mathbf{n} \, ds$.**

::: pf-proof

::: {.pf-step #theorem-follows-from-claims}
Adding the equalities from step [](#claim-I-proof){.pf-ref} and step [](#claim-II-proof){.pf-ref} proves the theorem for any closed rectangle $R$.

::: pf-proof
*Proof:* Follows from step [](#suffices-to-prove-I-and-II){.pf-ref}.
:::

:::

:::

::: pf-qed
Step [](#theorem-follows-from-claims){.pf-ref}.
:::

:::

:::
