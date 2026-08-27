---
schema: qual/card@1
id: P-2RS4X
kind: problem
title: The integral of $1/(1+x^4)$ over $\RR$ and the poles of $1/(1+z^4)$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Poles
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Evaluate the integral
\[
\int_\RR {dx \over 1 + x^4}
.\]

What are the poles of ${1\over 1 + z^4}$ ?
:::

::: {.solution}
**Goal:** Evaluate $\int_\RR \frac{dx}{1 + x^4}$ and identify the poles of $1/(1 + z^4)$.

<1>1. The poles of $1/(1 + z^4)$ are the simple poles $z_k = e^{i\pi(1 + 2k)/4}$, $k = 0, 1, 2, 3$.
    Proof: $1 + z^4 = 0$ iff $z^4 = -1 = e^{i\pi}$, so $z_k = e^{i(\pi + 2\pi k)/4}$ for $k = 0,1,2,3$: $z_0 = e^{i\pi/4}$, $z_1 = e^{3i\pi/4}$, $z_2 = e^{5i\pi/4}$, $z_3 = e^{7i\pi/4}$. Each is simple since $\dv{z}(1 + z^4) = 4z^3 \neq 0$ at each root.

<1>2. Two poles lie in the upper half-plane: $z_0 = e^{i\pi/4}$ and $z_1 = e^{3i\pi/4}$.
    Proof: <1>1: $z_0, z_1$ have positive imaginary parts; $z_2, z_3$ have negative imaginary parts.

<1>3. Integrate $f(z) = 1/(1 + z^4)$ over the semicircle $\Gamma_R$: the real segment $[-R, R]$ plus the arc $z = Re^{it}$, $t \in [0, \pi]$.
    Proof: Standard contour setup; by the residue theorem, $\int_{\Gamma_R} f = 2\pi i \qty(\Res_{z_0} f + \Res_{z_1} f)$ for $R > 1$.

<1>4. The arc contribution tends to $0$ as $R \to \infty$.
    Proof: On the arc, $\abs{1 + z^4} \ge \abs{z}^4 - 1 = R^4 - 1$, so $\abs{f(z)} \le 1/(R^4 - 1)$ and the arc integral is bounded by $\pi R /(R^4 - 1) \to 0$.

<1>5. Compute the residues.
    Proof: $\Res_{z_k} f = \lim_{z \to z_k} (z - z_k)/(1 + z^4) = 1/(4 z_k^3)$. With $z_k^4 = -1$, $1/z_k^3 = -z_k/1$? Compute directly: $z_0^3 = e^{3i\pi/4}$, so $\Res_{z_0} = \frac{1}{4e^{3i\pi/4}} = \frac14 e^{-3i\pi/4}$; $z_1^3 = e^{9i\pi/4} = e^{i\pi/4}$, so $\Res_{z_1} = \frac14 e^{-i\pi/4}$. Sum: $\frac14\qty(e^{-3i\pi/4} + e^{-i\pi/4}) = \frac14\qty(-\frac{\sqrt2}{2} - i\frac{\sqrt2}{2} + \frac{\sqrt2}{2} - i\frac{\sqrt2}{2}) = \frac14(-i\sqrt2) = -\frac{i\sqrt2}{4}$.

<1>6. Evaluate the integral.
    Proof: <1>3–<1>5: $\int_{\Gamma_R} f \to \int_\RR \frac{dx}{1+x^4}$ as $R \to \infty$ (arc vanishes by <1>4), and the residue sum is $2\pi i \cdot \qty(-\frac{i\sqrt2}{4}) = \frac{2\pi\sqrt2}{4} = \frac{\pi\sqrt2}{2}$.

<1>7. Q.E.D.
    Proof: $\int_\RR \frac{dx}{1+x^4} = \frac{\pi}{\sqrt2}$ by <1>6; the poles are the four simple roots of $1 + z^4$ from <1>1.

:::
