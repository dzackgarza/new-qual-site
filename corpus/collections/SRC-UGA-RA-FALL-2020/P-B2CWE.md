---
schema: qual/card@1
id: P-B2CWE
kind: problem
title: Convolution against dilates of an $L^1$ kernel is bounded on $L^1$ and converges
  to $\alpha f$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
---

::: problem
Suppose $\varphi \in L^1(\mathbb{R})$ with
$$
\int_{\mathbb{R}} \varphi(x) \, dx = \alpha.
$$
For each $\delta > 0$ and $f \in L^1(\mathbb{R})$, define
$$
A_\delta f(x) = \int_{\mathbb{R}} f(x-y) \delta^{-1} \varphi(\delta^{-1} y) \, dy.
$$

(a) Prove that for all $\delta > 0$,
$$
\|A_\delta f\|_{L^1} \le \|\varphi\|_{L^1} \|f\|_{L^1}.
$$

(b) Prove that
$$
A_\delta f \to \alpha f \quad \text{in } L^1(\mathbb{R}) \text{ as } \delta \to 0^+.
$$

*(You may use without proof the fact that for all $f \in L^1(\mathbb{R})$, $\lim_{y \to 0} \int_{\mathbb{R}} |f(x-y) - f(x)| \, dx = 0$.)*
:::

::: solution
**Goal:** Prove the boundedness of the family of convolution operators $A_\delta$ on $L^1(\mathbb{R})$ via Tonelli's Theorem in (a), and prove $L^1$ convergence to $\alpha f$ via the Dominated Convergence Theorem on translations in (b).

<1>1. Part (a): Boundedness of $A_\delta f$ in $L^1(\mathbb{R})$.
    *Proof:*
    <2>1. Define $\varphi_\delta(y) = \delta^{-1} \varphi(\delta^{-1} y)$.
    <2>2. By the change of variables $u = \delta^{-1} y$ ($du = \delta^{-1} dy$):
    $$\|\varphi_\delta\|_{L^1} = \int_{\mathbb{R}} \delta^{-1} |\varphi(\delta^{-1} y)| \, dy = \int_{\mathbb{R}} |\varphi(u)| \, du = \|\varphi\|_{L^1}.$$
    <2>3. Apply the integral Minkowski inequality (or Tonelli's Theorem to the non-negative product):
    $$\|A_\delta f\|_{L^1} = \int_{\mathbb{R}} \left| \int_{\mathbb{R}} f(x-y) \varphi_\delta(y) \, dy \right| dx \le \int_{\mathbb{R}} \int_{\mathbb{R}} |f(x-y)| |\varphi_\delta(y)| \, dy \, dx.$$
    <2>4. By Tonelli's Theorem, interchange the order of integration:
    $$\int_{\mathbb{R}} \int_{\mathbb{R}} |f(x-y)| |\varphi_\delta(y)| \, dy \, dx = \int_{\mathbb{R}} |\varphi_\delta(y)| \left( \int_{\mathbb{R}} |f(x-y)| \, dx \right) dy.$$
    <2>5. By translation invariance of Lebesgue measure, $\int_{\mathbb{R}} |f(x-y)| \, dx = \|f\|_{L^1}$ for every $y \in \mathbb{R}$.
    <2>6. Thus:
    $$\|A_\delta f\|_{L^1} \le \|f\|_{L^1} \int_{\mathbb{R}} |\varphi_\delta(y)| \, dy = \|f\|_{L^1} \|\varphi_\delta\|_{L^1} = \|\varphi\|_{L^1} \|f\|_{L^1}.$$

<1>2. Part (b): Representation of the error $A_\delta f(x) - \alpha f(x)$.
    *Proof:*
    <2>1. By change of variables, $\int_{\mathbb{R}} \varphi_\delta(y) \, dy = \int_{\mathbb{R}} \delta^{-1} \varphi(\delta^{-1} y) \, dy = \int_{\mathbb{R}} \varphi(u) \, du = \alpha$.
    <2>2. Multiply this identity by $f(x)$:
    $$\alpha f(x) = \int_{\mathbb{R}} f(x) \varphi_\delta(y) \, dy.$$
    <2>3. Subtract this from $A_\delta f(x)$:
    $$A_\delta f(x) - \alpha f(x) = \int_{\mathbb{R}} (f(x-y) - f(x)) \delta^{-1} \varphi(\delta^{-1} y) \, dy.$$
    <2>4. Substitute $y = \delta z$ ($dy = \delta dz$):
    $$A_\delta f(x) - \alpha f(x) = \int_{\mathbb{R}} (f(x - \delta z) - f(x)) \varphi(z) \, dz.$$

<1>3. Part (b): $L^1$ norm estimate and Dominated Convergence Theorem.
    *Proof:*
    <2>1. Take the $L^1$ norm:
    $$\|A_\delta f - \alpha f\|_{L^1} = \int_{\mathbb{R}} \left| \int_{\mathbb{R}} (f(x - \delta z) - f(x)) \varphi(z) \, dz \right| dx \le \int_{\mathbb{R}} \int_{\mathbb{R}} |f(x - \delta z) - f(x)| |\varphi(z)| \, dz \, dx.$$
    <2>2. By Tonelli's Theorem, interchange the order of integration:
    $$\|A_\delta f - \alpha f\|_{L^1} \le \int_{\mathbb{R}} |\varphi(z)| \left( \int_{\mathbb{R}} |f(x - \delta z) - f(x)| \, dx \right) dz = \int_{\mathbb{R}} |\varphi(z)| \|\tau_{\delta z} f - f\|_{L^1} \, dz,$$
    where $\tau_h f(x) = f(x - h)$.
    <2>3. Pointwise convergence:
        - For each fixed $z \in \mathbb{R}$, as $\delta \to 0^+$, the shift $h = \delta z \to 0$.
        - By $L^1$-continuity of translations:
        $$\lim_{\delta \to 0^+} \|\tau_{\delta z} f - f\|_{L^1} = 0 \implies \lim_{\delta \to 0^+} |\varphi(z)| \|\tau_{\delta z} f - f\|_{L^1} = 0.$$
    <2>4. Domination:
        - By the triangle inequality, $\|\tau_{\delta z} f - f\|_{L^1} \le \|\tau_{\delta z} f\|_{L^1} + \|f\|_{L^1} = 2 \|f\|_{L^1}$.
        - Thus for all $\delta > 0$ and all $z \in \mathbb{R}$:
        $$|\varphi(z)| \|\tau_{\delta z} f - f\|_{L^1} \le 2 \|f\|_{L^1} |\varphi(z)| =: g(z).$$
        - Since $\varphi \in L^1(\mathbb{R})$, $g \in L^1(\mathbb{R})$.
    <2>5. By the Dominated Convergence Theorem:
    $$\lim_{\delta \to 0^+} \|A_\delta f - \alpha f\|_{L^1} \le \int_{\mathbb{R}} \lim_{\delta \to 0^+} \left( |\varphi(z)| \|\tau_{\delta z} f - f\|_{L^1} \right) dz = \int_{\mathbb{R}} 0 \, dz = 0.$$

<1>4. Conclusion:
    *Proof:*
    $\|A_\delta f\|_{L^1} \le \|\varphi\|_{L^1} \|f\|_{L^1}$ and $\lim_{\delta \to 0^+} \|A_\delta f - \alpha f\|_{L^1} = 0$.
:::

