---
schema: qual/card@1
id: P-CASP09H
kind: problem
title: "Characterization of entire functions bounded by e^{xy}"
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

::: problem
Find all entire functions $f(z)$ with the property that for all $z$, $|f(z)| \leq e^{|xy|}$, where $x$ and $y$ are the real and imaginary parts of $z$.
:::

::: {.solution}
<1>1. Boundary behavior on the coordinate axes:
<2>1. On the real axis ($y = 0$), $z = x \in \mathbb{R}$:
\[
|f(x)| \le e^{|x \cdot 0|} = e^0 = 1 \quad \text{for all } x \in \mathbb{R}.
\]
Proof: hypothesis evaluated at $y = 0$.
<2>2. On the imaginary axis ($x = 0$), $z = iy$ with $y \in \mathbb{R}$:
\[
|f(iy)| \le e^{|0 \cdot y|} = e^0 = 1 \quad \text{for all } y \in \mathbb{R}.
\]
Proof: hypothesis evaluated at $x = 0$.
<2>3. Thus $|f(z)| \le 1$ on the entire real and imaginary axes, which form the boundaries of the four open quadrants.
Proof: combining real and imaginary axes.

<1>2. Application of the Phragmén–Lindelöf Principle:
<2>1. In each quadrant $Q_k$ (where the opening angle is $\pi/2$), $f$ is holomorphic.
The growth of $f$ satisfies $|f(z)| \le e^{|xy|} \le e^{|z|^2 / 2}$ for all $z \in \mathbb{C}$.
Proof: $|xy| \le \frac{x^2 + y^2}{2} = \frac{|z|^2}{2}$.
<2>2. Consider the first quadrant $Q_1 = \{ z = r e^{i\theta} \mid 0 < \theta < \pi/2 \}$.
For $\alpha \in (0, 2)$, say $\alpha = 3/2$, and any $\varepsilon > 0$, define the auxiliary function:
\[
g_\varepsilon(z) = f(z) e^{-\varepsilon z^{7/4} e^{-i 7\pi / 16}} \quad \text{or} \quad F(z) = f(z) e^{\frac{i}{2} z^2}.
\]
For $F(z) = f(z) e^{\frac{i}{2} z^2}$, compute the modulus in $Q_1$:
\[
|F(z)| = |f(z)| \left| e^{\frac{i}{2}(x^2 - y^2 + 2ixy)} \right| = |f(z)| e^{-xy} \le e^{xy} e^{-xy} = 1.
\]
Thus $F$ is bounded by $1$ on all of $\overline{Q_1}$, which implies $|f(z)| \le e^{xy}$ with $|f(z)| \le 1$ on $\partial Q_1$.
Proof: calculation of $|e^{\frac{i}{2} z^2}|$.
<2>3. Applying the Phragmén–Lindelöf Theorem to the sector of opening angle $\pi/2$, since $|f| \le 1$ on $\partial Q_1$ and $f$ has order of growth $\le 2$, we obtain:
\[
|f(z)| \le 1 \quad \text{for all } z \in Q_1.
\]
Proof: Phragmén–Lindelöf Theorem for sectors of angle $\pi/2$.
<2>4. Applying the identical argument to the remaining quadrants $Q_2, Q_3, Q_4$ yields $|f(z)| \le 1$ on all of $\mathbb{C}$.
Proof: symmetry across all four quadrants.

<1>3. Application of Liouville’s Theorem:
<2>1. $f$ is an entire function satisfying $|f(z)| \le 1$ for all $z \in \mathbb{C}$.
By Liouville’s Theorem, $f$ must be a constant function:
\[
f(z) = c \quad \text{for some constant } c \in \mathbb{C} \text{ with } |c| \le 1.
\]
Proof: Liouville’s Theorem.
<2>2. Conversely, for any constant $c \in \mathbb{C}$ with $|c| \le 1$, $|c| \le 1 \le e^{|xy|}$ holds for all $x, y \in \mathbb{R}$.
Proof: $e^{|xy|} \ge e^0 = 1 \ge |c|$.

<1>4. Conclusion:
The entire functions satisfying the given condition are precisely the constant functions $f(z) = c$ with $|c| \le 1$. Q.E.D.
Proof: <1>1 through <1>3.
:::
