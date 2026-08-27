---
schema: qual/card@1
id: P-JJHVX
kind: problem
title: Once complex differentiable implies holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
- Show that if $f$ is once complex differentiable at each point of $\Omega$, then $f$ is holomorphic.
:::

::: {.solution}
**Goal:** Show that if $f$ is once complex-differentiable at each point of a domain $\Omega$, then $f$ is holomorphic (i.e. analytic) on $\Omega$.

<1>1. $f$ is continuous on $\Omega$.
Proof: Differentiability at each point implies continuity at each point.

<1>2. (Goursat) $\int_T f = 0$ for every closed triangle $T$ contained (with interior) in $\Omega$.
<2>1. Assume, toward a contradiction, that $\abs{\int_T f} = M > 0$ for some triangle $T$.
Proof: Otherwise done.
<2>2. Subdivide $T$ into four congruent subtriangles $T_1, \ldots, T_4$; then $\abs{\int_{T_j} f} \geq M/4$ for some $j$.
Proof: The sum of the four integrals equals $\int_T f$ (interior edges cancel), so by the triangle inequality at least one has modulus $\geq M/4$.
<2>3. Iterating, get a nested sequence of triangles $T_n$ with $\abs{\int_{T_n} f} \geq M/4^n$ and diameters $\to 0$.
Proof: Repeat <2>2 indefinitely; the diameters shrink by a factor $1/2$ each step.
<2>4. The nested triangles have a common point $z_0 \in T$ (indeed $z_0 \in \Omega$). Proof: Nested compact sets with diameters tending to $0$ intersect in a single point.
<2>5. Write $f(z) = f(z_0) + f'(z_0)(z - z_0) + (z - z_0)\varepsilon(z)$ with $\varepsilon(z) \to 0$ as $z \to z_0$.
Proof: This is the definition of differentiability at $z_0$.
<2>6. $\int_{T_n} \qty[f(z_0) + f'(z_0)(z - z_0)]\, dz = 0$.
Proof: The constant $f(z_0)$ and the linear function $f'(z_0)(z - z_0)$ have primitives (e.g. $f'(z_0)(z - z_0)^2/2$), and $\int_{T_n} dz = \int_{T_n} z\, dz = 0$ for a closed contour.
<2>7. $\abs{\int_{T_n} f} = \abs{\int_{T_n} (z - z_0)\varepsilon(z)\, dz} \leq \sup_{z \in T_n} \abs{\varepsilon(z)} \cdot \operatorname{diam}(T_n) \cdot \operatorname{perim}(T_n)$.
Proof: Standard estimate: modulus of a line integral is bounded by the maximum of the integrand times the length of the contour.
<2>8. Contradiction.
Proof: $\operatorname{diam}(T_n) = 2^{-n} d$ and $\operatorname{perim}(T_n) = 2^{-n} p$ with $d, p$ fixed, so the bound in <2>7 is $\sup\abs\varepsilon \cdot dp/4^n$; but $\sup_{z \in T_n}\abs{\varepsilon(z)} \to 0$ (<2>5), so $\abs{\int_{T_n} f} < M/4^n$ for large $n$, contradicting <2>3.

<1>3. By Morera's theorem, $f$ is holomorphic.
Proof: Morera: if $f$ is continuous on $\Omega$ (<1>1) and $\int_T f = 0$ for every triangle $T \subset \Omega$ (<1>2), then $f$ is holomorphic.

<1>4. Q.E.D. Proof: <1>3 is the claim.
:::
