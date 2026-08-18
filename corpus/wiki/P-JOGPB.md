---
schema: qual/card@1
id: P-JOGPB
kind: problem
title: $\lim_{r\to 0}\int_{\gamma_r}f=iA\beta_0$ when $(z-a)f(z)\to A$
classification:
  areas:
  - complex-analysis
  topics:
  - residues
  - contour-integration
  - laurent-series
  - poles
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
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
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $S = \{z \in \mathbb{C} : 0 < |z-a| \leq R, 0 \leq \arg(z-a) \leq \beta_0\}$ with $0 < \beta_0 \leq 2\pi$.
Let $f: S \to \mathbb{C}$ be continuous with $\lim_{z \to a, z \in S} (z-a) f(z) = A \in \mathbb{C}$.
Prove that along the circular arcs $\gamma_r(t) = a + r e^{it}$ ($t \in [0, \beta_0]$), $$\lim_{r \to 0^+} \int_{\gamma_r} f(z) \, dz = i A \beta_0.$$

* * *

### Step 1: Parametrize the Integral and Isolate the Main Term

<1>1. **Parametrize $\int_{\gamma_r} \frac{A}{z-a}\,dz$.** <2>1. With $\gamma_r(t) = a + r e^{it}$ for $t \in [0, \beta_0]$, $dz = i r e^{it} dt$.
*Proof:* Derivative of parametrization.
<2>2. The integral of the simple pole term is: $$\int_{\gamma_r} \frac{A}{z-a} \, dz = \int_0^{\beta_0} \frac{A}{r e^{it}} \cdot i r e^{it} \, dt = i A \int_0^{\beta_0} dt = i A \beta_0.$$ *Proof:* Direct cancellation of $r e^{it}$ and integration of constant $1$.
<2>3. Q.E.D.

<1>2. **Express $f(z)$ as $\frac{A}{z-a} + \frac{g(z)}{z-a}$ where $g(z) = (z-a)f(z) - A$.** <2>1. Define $g(z) = (z-a)f(z) - A$ for $z \in S$.
*Proof:* Algebraic definition.
<2>2. By the hypothesis $\lim_{z \to a, z \in S} (z-a)f(z) = A$, we have $\lim_{z \to a, z \in S} g(z) = 0$.
*Proof:* Definition of limit.
<2>3. For any $z \in S$, $f(z) = \frac{A + g(z)}{z-a} = \frac{A}{z-a} + \frac{g(z)}{z-a}$.
*Proof:* Dividing $g(z) + A = (z-a)f(z)$ by $z-a \neq 0$.
<2>4. Q.E.D.

* * *

### Step 2: Bound the Error Term

<1>3. **Show that $\lim_{r \to 0^+} \int_{\gamma_r} \frac{g(z)}{z-a}\,dz = 0$.** <2>1. Let $\varepsilon > 0$ be given.
*Proof:* Standard epsilon-delta argument.
<2>2. Since $\lim_{z \to a, z \in S} g(z) = 0$, there exists $\delta > 0$ (with $\delta \leq R$) such that for all $z \in S$ with $0 < |z-a| < \delta$, $|g(z)| < \frac{\varepsilon}{\beta_0}$.
*Proof:* Definition of limit of a function.
<2>3. For any $r \in (0, \delta)$, the entire arc $\gamma_r$ is contained in $\{z \in S : 0 < |z-a| = r < \delta\}$.
*Proof:* Modulus of $z - a = r e^{it}$ is $r < \delta$.
<2>4. On $\gamma_r$, $\left| \frac{g(z)}{z-a} \right| = \frac{|g(z)|}{r} < \frac{\varepsilon}{\beta_0 r}$.
*Proof:* Division by $|z-a| = r$.
<2>5. The length of the arc $\gamma_r$ is $L(\gamma_r) = r \beta_0$.
*Proof:* Arc length of circular sector of angle $\beta_0$ and radius $r$.
<2>6. By the $ML$-inequality: $$\left| \int_{\gamma_r} \frac{g(z)}{z-a} \, dz \right| \leq \left( \sup_{z \in \gamma_r} \left| \frac{g(z)}{z-a} \right| \right) \cdot L(\gamma_r) \leq \frac{\varepsilon}{\beta_0 r} \cdot (r \beta_0) = \varepsilon.$$ *Proof:* $ML$-inequality for contour integrals.
<2>7. Since $\varepsilon > 0$ was arbitrary, $\lim_{r \to 0^+} \int_{\gamma_r} \frac{g(z)}{z-a} \, dz = 0$.
*Proof:* Squeeze theorem / epsilon-delta definition of limit.
<2>8. Q.E.D.

* * *

### Step 3: Conclusion

<1>4. **$\lim_{r \to 0^+} \int_{\gamma_r} f(z)\,dz = i A \beta_0$.** <2>1. By linearity of the line integral: $$\int_{\gamma_r} f(z) \, dz = \int_{\gamma_r} \frac{A}{z-a} \, dz + \int_{\gamma_r} \frac{g(z)}{z-a} \, dz = i A \beta_0 + \int_{\gamma_r} \frac{g(z)}{z-a} \, dz.$$ *Proof:* Follows from <1>1.<2>2 and <1>2.<2>3. <2>2. Taking the limit as $r \to 0^+$ on both sides: $$\lim_{r \to 0^+} \int_{\gamma_r} f(z) \, dz = i A \beta_0 + \lim_{r \to 0^+} \int_{\gamma_r} \frac{g(z)}{z-a} \, dz = i A \beta_0 + 0 = i A \beta_0.$$ *Proof:* Follows from <1>3.<2>7. <2>3. Q.E.D.
:::
