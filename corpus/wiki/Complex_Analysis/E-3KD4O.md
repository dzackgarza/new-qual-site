---
schema: qual/card@1
id: E-3KD4O
kind: exercise
title: Once complex-differentiable functions are holomorphic
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
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $f$ is once complex differentiable at each point of $\Omega$, then $f$ is holomorphic.
:::

::: solution
**Goal:** Prove the Goursat Theorem: a function $f: \Omega \to \mathbb{C}$ that is complex differentiable at every point of an open set $\Omega \subseteq \mathbb{C}$ (without assuming continuity of $f'$) is analytic ($C^\infty$) on $\Omega$.

<1>1. Goursat's Lemma for triangles:
    For any closed solid triangle $T \subset \Omega$, the contour integral vanishes:
    $$\oint_{\partial T} f(z) \, dz = 0.$$
    *Proof:*
    <2>1. Subdivide $T = T_0$ into 4 congruent sub-triangles $T^{(1)}, \dots, T^{(4)}$ by joining the edge midpoints.
    <2>2. The contour integral satisfies $\oint_{\partial T} f(z) \, dz = \sum_{j=1}^4 \oint_{\partial T^{(j)}} f(z) \, dz$.
    <2>3. By the triangle inequality, at least one sub-triangle $T_1 \in \{T^{(1)}, \dots, T^{(4)}\}$ satisfies:
        $$\left|\oint_{\partial T_1} f(z) \, dz\right| \ge \frac{1}{4} \left|\oint_{\partial T} f(z) \, dz\right|.$$
    <2>4. Inductively repeat this subdivision to construct a nested sequence of closed triangles $T = T_0 \supset T_1 \supset T_2 \supset \dots$ such that:
        $$\left|\oint_{\partial T_n} f(z) \, dz\right| \ge 4^{-n} \left|\oint_{\partial T} f(z) \, dz\right|, \quad \operatorname{diam}(T_n) = 2^{-n} \operatorname{diam}(T), \quad \operatorname{Length}(\partial T_n) = 2^{-n} L.$$
    <2>5. By Cantor's Intersection Theorem, $\bigcap_{n=0}^\infty T_n = \{z_0\}$ for a unique point $z_0 \in T \subset \Omega$.
    <2>6. Since $f$ is complex differentiable at $z_0$, for any $z \in \Omega$:
        $$f(z) = f(z_0) + f'(z_0)(z - z_0) + \eta(z)(z - z_0), \quad \text{where } \lim_{z \to z_0} \eta(z) = 0.$$
    <2>7. Polynomials have global primitives, so $\oint_{\partial T_n} 1 \, dz = 0$ and $\oint_{\partial T_n} (z - z_0) \, dz = 0$.
    <2>8. Thus $\oint_{\partial T_n} f(z) \, dz = \oint_{\partial T_n} \eta(z)(z - z_0) \, dz$.
    <2>9. For any $\varepsilon > 0$, choose $N$ such that $|\eta(z)| < \varepsilon$ for all $z \in T_N$. For all $n \ge N$:
        $$\left|\oint_{\partial T_n} f(z) \, dz\right| \le \varepsilon \cdot \operatorname{diam}(T_n) \cdot \operatorname{Length}(\partial T_n) = \varepsilon \cdot 2^{-n} \operatorname{diam}(T) \cdot 2^{-n} L = \varepsilon 4^{-n} \operatorname{diam}(T) L.$$
    <2>10. Multiplying by $4^n$ gives $\left|\oint_{\partial T} f(z) \, dz\right| \le \varepsilon \operatorname{diam}(T) L$. Since $\varepsilon > 0$ is arbitrary, $\oint_{\partial T} f(z) \, dz = 0$.

<1>2. Existence of a local holomorphic primitive:
    On any open convex disk $D \subseteq \Omega$, $f$ has a holomorphic primitive $F: D \to \mathbb{C}$ with $F'(z) = f(z)$.
    *Proof:*
    <2>1. Fix $z_0 \in D$ and define $F(z) = \int_{[z_0, z]} f(w) \, dw$.
    <2>2. For any $z \in D$ and small $h \in \mathbb{C}$, applying Goursat's Lemma on the triangle with vertices $z_0, z, z+h$ yields:
        $$F(z+h) - F(z) = \int_{[z, z+h]} f(w) \, dw.$$
    <2>3. Since $f$ is continuous at $z$, $\frac{F(z+h) - F(z)}{h} = \frac{1}{h} \int_0^1 f(z + th) h \, dt = \int_0^1 f(z + th) \, dt \xrightarrow{h \to 0} f(z)$.
    <2>4. Thus $F'(z) = f(z)$ on $D$.

<1>3. Smoothness and analyticity:
    *Proof:*
    <2>1. By the Cauchy Integral Formula applied to the primitive $F$, $F$ is analytic and infinitely differentiable on $D$.
    <2>2. Therefore $f = F'$ is analytic ($C^\infty$) on $D$ and represented by a locally convergent power series.
    <2>3. Since every point of $\Omega$ has a disk neighborhood $D \subseteq \Omega$, $f$ is holomorphic on all of $\Omega$. Q.E.D.
:::
