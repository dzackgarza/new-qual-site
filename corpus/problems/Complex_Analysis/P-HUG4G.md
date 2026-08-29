---
schema: qual/card@1
id: P-HUG4G
kind: problem
title: Cauchy's theorem via Green's theorem, and Goursat's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Cauchy Integral Theorem
  - Contour Integration
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $\Omega \subseteq \mathbb{C}$ be an open domain, and let $T \subset \Omega$ be a closed triangle whose interior $T^\circ \subset \Omega$.
1. Assuming $f \in C^1(\Omega)$ (meaning $f(z) = u(x, y) + i v(x, y)$ has continuous real partial derivatives), apply **Green's Theorem** and the Cauchy-Riemann equations to prove Cauchy's Theorem on triangles:
$$\oint_{\partial T} f(z) \, dz = 0.$$

2. State **Goursat's Theorem** (which removes the assumption that $f'$ is continuous) and outline Goursat's proof via triangular subdivision.
:::

::: solution
**Goal:** Prove $\oint_{\partial T} f(z) \, dz = 0$ via Green's Theorem assuming $C^1$, and outline Goursat's classical subdivision proof requiring only complex differentiability.

<1>1. Part 1: Cauchy's Theorem via Green's Theorem:
    *Proof:*
    <2>1. Let $f(z) = u(x, y) + i v(x, y)$ with $z = x + i y$ and $dz = dx + i dy$.
    <2>2. The complex contour integral over the boundary $\partial T$ (oriented counterclockwise) expands into real line integrals:
        $$\oint_{\partial T} f(z) \, dz = \oint_{\partial T} (u + i v)(dx + i dy) = \oint_{\partial T} (u \, dx - v \, dy) + i \oint_{\partial T} (v \, dx + u \, dy).$$
    <2>3. Apply **Green's Theorem** to each real line integral:
        - For the real part: $F_1 = u, G_1 = -v$:
          $$\oint_{\partial T} (u \, dx - v \, dy) = \iint_{T^\circ} \left( \frac{\partial (-v)}{\partial x} - \frac{\partial u}{\partial y} \right) dx dy = -\iint_{T^\circ} \left( \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y} \right) dx dy.$$
        - For the imaginary part: $F_2 = v, G_2 = u$:
          $$\oint_{\partial T} (v \, dx + u \, dy) = \iint_{T^\circ} \left( \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} \right) dx dy.$$
    <2>4. Since $f$ is holomorphic on $\Omega$, the **Cauchy-Riemann equations** hold throughout $T^\circ$:
        $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \implies \frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} = 0,$$
        $$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \implies \frac{\partial v}{\partial x} + \frac{\partial u}{\partial y} = 0.$$
    <2>5. Substituting these into the double integrals:
        $$\oint_{\partial T} f(z) \, dz = -\iint_{T^\circ} 0 \, dx dy + i \iint_{T^\circ} 0 \, dx dy = 0.$$

<1>2. Part 2: Goursat's Theorem (subdivision without assuming $C^1$):
    *Proof:*
    <2>1. **Theorem (Goursat):** If $f: \Omega \to \mathbb{C}$ is complex differentiable at every point in $\Omega$ (no continuity of $f'$ is assumed), then $\oint_{\partial T} f(z) \, dz = 0$ for every closed triangle $T \subset \Omega$.
    <2>2. **Subdivision Construction:**
        - Subdivide $T = T^{(0)}$ into 4 congruent sub-triangles $T_1, T_2, T_3, T_4$ by connecting the midpoints of the edges.
        - The integral over $\partial T$ equals the sum of integrals over the sub-triangles (interior edges cancel):
          $$\oint_{\partial T} f(z) \, dz = \sum_{j=1}^4 \oint_{\partial T_j} f(z) \, dz.$$
        - By the triangle inequality, at least one sub-triangle, say $T^{(1)}$, satisfies:
          $$\left| \oint_{\partial T^{(1)}} f(z) \, dz \right| \ge \frac{1}{4} \left| \oint_{\partial T} f(z) \, dz \right|.$$
        - The perimeter satisfies $\operatorname{diam}(T^{(1)}) = \frac{1}{2} \operatorname{diam}(T)$ and $\operatorname{length}(\partial T^{(1)}) = \frac{1}{2} L$, where $L = \operatorname{length}(\partial T)$.
    <2>3. Repeating this recursively generates a nested sequence of closed triangles:
        $$T = T^{(0)} \supset T^{(1)} \supset T^{(2)} \supset \cdots \supset T^{(n)} \supset \cdots$$
        such that $\operatorname{diam}(T^{(n)}) = 2^{-n} \operatorname{diam}(T)$, $\operatorname{length}(\partial T^{(n)}) = 2^{-n} L$, and:
        $$\left| \oint_{\partial T} f(z) \, dz \right| \le 4^n \left| \oint_{\partial T^{(n)}} f(z) \, dz \right|.$$
    <2>4. By Cantor's Intersection Theorem on compact sets, the intersection $\bigcap_{n=0}^\infty T^{(n)} = \{z_0\}$ contains a unique point $z_0 \in T$.
    <2>5. Since $f$ is complex differentiable at $z_0$:
        $$f(z) = f(z_0) + f'(z_0)(z - z_0) + \eta(z)(z - z_0),$$
        where $\lim_{z \to z_0} \eta(z) = 0$.
    <2>6. Constant and linear terms have exact primitives ($F(z) = f(z_0) z + \frac{1}{2} f'(z_0)(z - z_0)^2$), so their integrals over any closed loop vanish:
        $$\oint_{\partial T^{(n)}} (f(z_0) + f'(z_0)(z - z_0)) \, dz = 0.$$
    <2>7. Thus:
        $$\left| \oint_{\partial T^{(n)}} f(z) \, dz \right| = \left| \oint_{\partial T^{(n)}} \eta(z)(z - z_0) \, dz \right| \le \max_{z \in T^{(n)}} |\eta(z)| \cdot \operatorname{diam}(T^{(n)}) \cdot \operatorname{length}(\partial T^{(n)}) = \varepsilon_n \cdot 2^{-n} \operatorname{diam}(T) \cdot 2^{-n} L,$$
        where $\varepsilon_n = \max_{z \in T^{(n)}} |\eta(z)| \to 0$ as $n \to \infty$.
    <2>8. Multiplying by $4^n$:
        $$\left| \oint_{\partial T} f(z) \, dz \right| \le 4^n \cdot \varepsilon_n \cdot 4^{-n} \operatorname{diam}(T) L = \varepsilon_n \cdot \operatorname{diam}(T) L \xrightarrow{n \to \infty} 0.$$
    <2>9. Therefore, $\oint_{\partial T} f(z) \, dz = 0$.

<1>3. Conclusion:
    Green's theorem yields Cauchy's theorem for $C^1$ functions; Goursat's nested triangle construction proves it for all holomorphic functions. Q.E.D.
:::
