---
schema: qual/card@1
id: P-JOGPB
kind: problem
title: $\lim_{r\to 0}\int_{\gamma_r}f=iA\beta_0$ when $(z-a)f(z)\to A$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Laurent Series
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.problem}
Assume $f$ is continuous in the region:
\[
0 < \abs{z-a} \leq R,\quad 0 \leq \Arg(z-a) \leq \beta_0 \qquad \beta_0\in (0, 2\pi]
.\]

and the following limit exists:
\[
\lim_{z\to a}(z-a)f(z) = A
.\]
Show that
$$\lim_{r \rightarrow 0} \int_{\gamma_r} f(z) dz  = i A \beta_0 \; , \; \;$$
where
\[
\gamma_r : = \{ z \; | \; z = a + r e^{it}, \; 0 \leq  t \leq \beta_0 \}.
.\]
:::

::: {.solution}
**Goal:** Let $S = \{z \in \mathbb{C} : 0 < |z-a| \leq R, 0 \leq \arg(z-a) \leq \beta_0\}$ with $0 < \beta_0 \leq 2\pi$.
Let $f: S \to \mathbb{C}$ be continuous with $\lim_{z \to a, z \in S} (z-a) f(z) = A \in \mathbb{C}$.
Prove that along the circular arcs $\gamma_r(t) = a + r e^{it}$ ($t \in [0, \beta_0]$), $$\lim_{r \to 0^+} \int_{\gamma_r} f(z) \, dz = i A \beta_0.$$

* * *

### Step 1: Parametrize the Integral and Isolate the Main Term

::: pf

::: pf-step
**Parametrize $\int_{\gamma_r} \frac{A}{z-a}\,dz$.**

::: pf-proof

::: pf-step
With $\gamma_r(t) = a + r e^{it}$ for $t \in [0, \beta_0]$, $dz = i r e^{it} dt$.

::: pf-proof
Differentiating the parametrization $\gamma_r(t) = a + r e^{it}$ with respect to $t$ gives $\gamma_r'(t) = i r e^{it}$, so $dz = i r e^{it}\,dt$.
:::

:::

::: {.pf-step #main-term-integral}
The integral of the simple pole term is: $$\int_{\gamma_r} \frac{A}{z-a} \, dz = \int_0^{\beta_0} \frac{A}{r e^{it}} \cdot i r e^{it} \, dt = i A \int_0^{\beta_0} dt = i A \beta_0.$$

::: pf-proof
Substituting $z - a = r e^{it}$ and $dz = i r e^{it}\,dt$, the factors $r e^{it}$ cancel, leaving the integral of the constant $iA$ over $[0, \beta_0]$, which is $iA\beta_0$.
:::

:::

:::

:::

::: pf-step
**Express $f(z)$ as $\frac{A}{z-a} + \frac{g(z)}{z-a}$ where $g(z) = (z-a)f(z) - A$.**

::: pf-proof

::: pf-step
Define $g(z) = (z-a)f(z) - A$ for $z \in S$.

::: pf-proof
This is the definition of $g$: the difference between $(z-a)f(z)$ and its limit $A$.
:::

:::

::: pf-step
By the hypothesis $\lim_{z \to a, z \in S} (z-a)f(z) = A$, we have $\lim_{z \to a, z \in S} g(z) = 0$.

::: pf-proof
Subtracting the constant $A$ from a function converging to $A$ gives a function converging to $0$.
:::

:::

::: {.pf-step #f-decomposition}
For any $z \in S$, $f(z) = \frac{A + g(z)}{z-a} = \frac{A}{z-a} + \frac{g(z)}{z-a}$.

::: pf-proof
Since $g(z) + A = (z-a)f(z)$, dividing both sides by $z - a \neq 0$ (valid because $z \in S$ has $|z-a| > 0$) gives the decomposition.
:::

:::

:::

:::

:::

* * *

### Step 2: Bound the Error Term

::: pf

::: pf-step
**Show that $\lim_{r \to 0^+} \int_{\gamma_r} \frac{g(z)}{z-a}\,dz = 0$.**

::: pf-proof

::: pf-step
Let $\varepsilon > 0$ be given.

::: pf-proof
We prove the limit by the epsilon–delta definition: for an arbitrary $\varepsilon > 0$ we exhibit a $\delta$ such that the integral is bounded by $\varepsilon$ whenever $r < \delta$.
:::

:::

::: {.pf-step #g-bound}
Since $\lim_{z \to a, z \in S} g(z) = 0$, there exists $\delta > 0$ (with $\delta \leq R$) such that for all $z \in S$ with $0 < |z-a| < \delta$, $|g(z)| < \frac{\varepsilon}{\beta_0}$.

::: pf-proof
This is the definition of the limit $\lim_{z \to a} g(z) = 0$ applied with the tolerance $\frac{\varepsilon}{\beta_0}$.
:::

:::

::: pf-step
For any $r \in (0, \delta)$, the entire arc $\gamma_r$ is contained in $\{z \in S : 0 < |z-a| = r < \delta\}$.

::: pf-proof
For $z = a + r e^{it}$ on $\gamma_r$, we have $|z - a| = |r e^{it}| = r < \delta$, and $0 \le t \le \beta_0$ keeps $z$ in $S$.
:::

:::

::: {.pf-step #integrand-bound}
On $\gamma_r$, $\left| \frac{g(z)}{z-a} \right| = \frac{|g(z)|}{r} < \frac{\varepsilon}{\beta_0 r}$.

::: pf-proof
Since $|z - a| = r$ on $\gamma_r$ and $|g(z)| < \frac{\varepsilon}{\beta_0}$ by step [](#g-bound){.pf-ref}, dividing gives the bound.
:::

:::

::: {.pf-step #arc-length}
The length of the arc $\gamma_r$ is $L(\gamma_r) = r \beta_0$.

::: pf-proof
The arc is a circular sector of radius $r$ subtending angle $\beta_0$, so its length is $r \beta_0$.
:::

:::

::: pf-step
By the $ML$-inequality: $$\left| \int_{\gamma_r} \frac{g(z)}{z-a} \, dz \right| \leq \left( \sup_{z \in \gamma_r} \left| \frac{g(z)}{z-a} \right| \right) \cdot L(\gamma_r) \leq \frac{\varepsilon}{\beta_0 r} \cdot (r \beta_0) = \varepsilon.$$

::: pf-proof
The $ML$-inequality bounds the modulus of a contour integral by the product of the maximum of the integrand and the length of the contour; substituting the bounds from step [](#integrand-bound){.pf-ref} and step [](#arc-length){.pf-ref} gives $\varepsilon$.
:::

:::

::: {.pf-step #error-term-vanishes}
Since $\varepsilon > 0$ was arbitrary, $\lim_{r \to 0^+} \int_{\gamma_r} \frac{g(z)}{z-a} \, dz = 0$.

::: pf-proof
For every $\varepsilon > 0$ we found $\delta$ such that $r < \delta$ forces the integral to be at most $\varepsilon$ in modulus, which is exactly the definition of the limit being $0$.
:::

:::

:::

:::

:::

* * *

### Step 3: Conclusion

::: pf

::: pf-step
**$\lim_{r \to 0^+} \int_{\gamma_r} f(z)\,dz = i A \beta_0$.**

::: pf-proof

::: pf-step
By linearity of the line integral: $$\int_{\gamma_r} f(z) \, dz = \int_{\gamma_r} \frac{A}{z-a} \, dz + \int_{\gamma_r} \frac{g(z)}{z-a} \, dz = i A \beta_0 + \int_{\gamma_r} \frac{g(z)}{z-a} \, dz.$$

::: pf-proof
By step [](#f-decomposition){.pf-ref}, $f(z) = \frac{A}{z-a} + \frac{g(z)}{z-a}$, so the integral splits by linearity; by step [](#main-term-integral){.pf-ref}, the first term equals $iA\beta_0$.
:::

:::

::: pf-step
Taking the limit as $r \to 0^+$ on both sides: $$\lim_{r \to 0^+} \int_{\gamma_r} f(z) \, dz = i A \beta_0 + \lim_{r \to 0^+} \int_{\gamma_r} \frac{g(z)}{z-a} \, dz = i A \beta_0 + 0 = i A \beta_0.$$

::: pf-proof
The first term $iA\beta_0$ is constant in $r$, and by step [](#error-term-vanishes){.pf-ref} the second term tends to $0$, so the limit is $iA\beta_0$.
:::

:::

:::

:::

:::

:::
