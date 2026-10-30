---
schema: qual/card@1
id: P-CASP09H
kind: problem
title: 'Entire functions with $\abs{f(x+iy)}\leq e^{\abs{xy}}$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Find all entire functions $f(z)$ with the property that for all $z$, $\abs{f(z)} \leq e^{\abs{xy}}$, where $x$ and $y$ are the real and imaginary parts of $z$.
:::

::: {.solution}

::: pf

::: pf-step

Boundary behavior on the coordinate axes:

::: pf-proof

::: pf-step

On the real axis ($y = 0$), $z = x \in \RR$:
$$
\abs{f(x)} \le e^{\abs{x \cdot 0}} = e^0 = 1 \quad \text{for all } x \in \RR.
$$

:::

::: pf-step

On the imaginary axis ($x = 0$), $z = iy$ with $y \in \RR$:
$$
\abs{f(iy)} \le e^{\abs{0 \cdot y}} = e^0 = 1 \quad \text{for all } y \in \RR.
$$

:::

::: pf-step

Thus $\abs{f(z)} \le 1$ on the entire real and imaginary axes, which form the boundaries of the four open quadrants.

:::

:::

:::

::: pf-step

Application of the Phragmén–Lindelöf Principle:

::: pf-proof

::: pf-step

In each quadrant $Q_k$ (where the opening angle is $\pi/2$), $f$ is holomorphic.
The growth of $f$ satisfies $\abs{f(z)} \le e^{\abs{xy}} \le e^{\abs{z}^2 / 2}$ for all $z \in \CC$.

:::

::: pf-step

Consider the first quadrant $Q_1 = \{ z = r e^{i\theta} \mid 0 < \theta < \pi/2 \}$.
For $\alpha \in (0, 2)$, say $\alpha = 3/2$, and any $\varepsilon > 0$, define the auxiliary function:
$$
g_\varepsilon(z) = f(z) e^{-\varepsilon z^{7/4} e^{-i 7\pi / 16}} \quad \text{or} \quad F(z) = f(z) e^{\frac{i}{2} z^2}.
$$
For $F(z) = f(z) e^{\frac{i}{2} z^2}$, compute the modulus in $Q_1$:
$$
\abs{F(z)} = \abs{f(z)} \abs{ e^{\frac{i}{2}(x^2 - y^2 + 2ixy)} } = \abs{f(z)} e^{-xy} \le e^{xy} e^{-xy} = 1.
$$
Thus $F$ is bounded by $1$ on all of $\overline{Q_1}$, which implies $\abs{f(z)} \le e^{xy}$ with $\abs{f(z)} \le 1$ on $\partial Q_1$.

:::

::: pf-step

Applying the Phragmén–Lindelöf Theorem to the sector of opening angle $\pi/2$, since $\abs{f} \le 1$ on $\partial Q_1$ and $f$ has order of growth $\le 2$, we obtain:
$$
\abs{f(z)} \le 1 \quad \text{for all } z \in Q_1.
$$

:::

::: pf-step

Applying the identical argument to the remaining quadrants $Q_2, Q_3, Q_4$ yields $\abs{f(z)} \le 1$ on all of $\CC$.

:::

:::

:::

::: pf-step

Application of Liouville’s Theorem:

::: pf-proof

::: pf-step

$f$ is an entire function satisfying $\abs{f(z)} \le 1$ for all $z \in \CC$.
By Liouville’s Theorem, $f$ must be a constant function:
$$
f(z) = c \quad \text{for some constant } c \in \CC \text{ with } \abs{c} \le 1.
$$

:::

::: pf-step

Conversely, for any constant $c \in \CC$ with $\abs{c} \le 1$, $\abs{c} \le 1 \le e^{\abs{xy}}$ holds for all $x, y \in \RR$.

:::

:::

:::

::: pf-step

Conclusion:

:::

:::

The entire functions satisfying the given condition are precisely the constant functions $f(z) = c$ with $\abs{c} \le 1$. Q.E.D.
:::
