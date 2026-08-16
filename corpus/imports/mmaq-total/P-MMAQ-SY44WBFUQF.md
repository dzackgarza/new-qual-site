---
schema: qual/card@1
id: P-MMAQ-SY44WBFUQF
kind: problem
title: Let $(f_n)$ be a sequence of holomorphic functions in a domain $D$.
classification:
  areas:
  - complex-analysis
  topics:
  - convergence
relations: []
review: draft
---

::: problem
Let $(f_n)$ be a sequence of holomorphic functions in a domain $D$.
Suppose that $f_n \to f$ uniformly on each compact subset of $D$.
Show that

-   $f$ is holomorphic on $D$.

-   $f_n' \to f'$ uniformly on each compact subset of $D$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $(f_n)$ be a sequence of holomorphic functions on a domain $D \subset \mathbb{C}$ such that $f_n \to f$ uniformly on compact subsets of $D$ (locally uniformly). Prove that:
1. $f$ is holomorphic on $D$ (Weierstrass's Theorem on uniform convergence).
2. $f_n' \to f'$ uniformly on compact subsets of $D$.

---

### Part 1: $f$ is Holomorphic on $D$ (via Morera's Theorem)

<1>1. **$f$ is continuous on $D$.**
  <2>1. Each $f_n$ is holomorphic on $D$, hence continuous.
    *Proof:* Complex differentiability implies continuity.
  <2>2. For any point $z_0 \in D$, there exists a closed disk $\overline{D}(z_0, r) \subset D$, which is compact.
    *Proof:* $D$ is open.
  <2>3. By hypothesis, $f_n \to f$ uniformly on $\overline{D}(z_0, r)$.
    *Proof:* Uniform convergence on compact subsets.
  <2>4. The uniform limit of continuous functions is continuous, so $f$ is continuous on $\overline{D}(z_0, r)$, and hence continuous at $z_0$.
    *Proof:* Standard real/complex analysis theorem on uniform convergence preserving continuity.
  <2>5. Since $z_0 \in D$ was arbitrary, $f$ is continuous on all of $D$.
    *Proof:* Local continuity implies global continuity.
  <2>6. Q.E.D.

<1>2. **$\oint_{\partial T} f(z) \, dz = 0$ for every closed triangle $T \subset D$.**
  <2>1. Let $T \subset D$ be any closed triangle with boundary $\partial T$.
    *Proof:* Setting test contour for Morera's Theorem.
  <2>2. $T$ is a compact subset of $D$, so $f_n \to f$ uniformly on $\partial T \subset T$.
    *Proof:* Triangles are compact, and boundary is a closed subset of $T$.
  <2>3. Since each $f_n$ is holomorphic in the simply connected domain containing $T$, Cauchy's Theorem (Goursat's Lemma) implies $\oint_{\partial T} f_n(z) \, dz = 0$ for all $n$.
    *Proof:* Cauchy-Goursat theorem on triangles.
  <2>4. Uniform convergence justifies taking the limit inside the integral:
  $$\oint_{\partial T} f(z) \, dz = \oint_{\partial T} \lim_{n \to \infty} f_n(z) \, dz = \lim_{n \to \infty} \oint_{\partial T} f_n(z) \, dz = \lim_{n \to \infty} 0 = 0.$$
    *Proof:* $\left| \oint_{\partial T} (f_n - f) \, dz \right| \leq \sup_{z \in \partial T} |f_n(z) - f(z)| \cdot \text{length}(\partial T) \to 0$.
  <2>5. Q.E.D.

<1>3. **By Morera's Theorem, $f$ is holomorphic on $D$.**
  <2>1. $f$ is continuous on $D$ and $\oint_{\partial T} f(z) \, dz = 0$ for every triangle $T \subset D$.
    *Proof:* Established in <1>1 and <1>2.
  <2>2. By Morera's Theorem, $f$ is holomorphic on $D$.
    *Proof:* Morera's Theorem characterization of holomorphicity.
  <2>3. Q.E.D.

---

### Part 2: $f_n' \to f'$ Uniformly on Compact Subsets

<1>4. **Integral formula for derivatives on compact sets.**
  <2>1. Let $K \subset D$ be any compact subset.
    *Proof:* Arbitrary compact set.
  <2>2. Since $K$ is compact and $D^c = \mathbb{C} \setminus D$ is closed and disjoint from $K$, the distance $d \coloneqq \text{dist}(K, \partial D) > 0$.
    *Proof:* Distance between disjoint compact and closed sets in metric spaces is strictly positive.
  <2>3. Choose $r = d/2 > 0$. The enlarged set $K_r \coloneqq \{w \in \mathbb{C} : \text{dist}(w, K) \leq r\}$ is a compact subset of $D$.
    *Proof:* $K_r$ is closed, bounded, and contained in $D$ since $r < d$.
  <2>4. For every $z \in K$, the circle $C(z, r) = \{w : |w - z| = r\}$ is contained in $K_r \subset D$.
    *Proof:* Every point on $C(z, r)$ has distance $r$ from $z \in K$.
  <2>5. By Cauchy's Integral Formula for derivatives, for any $z \in K$:
  $$f_n'(z) - f'(z) = \frac{1}{2\pi i} \oint_{|w-z|=r} \frac{f_n(w) - f(w)}{(w - z)^2} \, dw.$$
    *Proof:* Linearity of Cauchy's derivative formula.
  <2>6. Q.E.D.

<1>5. **Bound $|f_n'(z) - f'(z)|$ uniformly over $z \in K$.**
  <2>1. For $w \in C(z, r)$, $|w - z| = r$, so $|(w - z)^2| = r^2$.
    *Proof:* Definition of circle.
  <2>2. Let $\varepsilon_n \coloneqq \sup_{w \in K_r} |f_n(w) - f(w)|$. By uniform convergence on the compact set $K_r$, $\lim_{n \to \infty} \varepsilon_n = 0$.
    *Proof:* Hypothesis of local uniform convergence applied to $K_r$.
  <2>3. Apply the $ML$-inequality to the Cauchy integral from <1>4.<2>5:
  $$|f_n'(z) - f'(z)| \leq \frac{1}{2\pi} \cdot \frac{\varepsilon_n}{r^2} \cdot (2\pi r) = \frac{\varepsilon_n}{r}.$$
    *Proof:* $ML$-inequality with $M = \varepsilon_n/r^2$ and $L = 2\pi r$.
  <2>4. Taking the supremum over all $z \in K$:
  $$\sup_{z \in K} |f_n'(z) - f'(z)| \leq \frac{\varepsilon_n}{r}.$$
    *Proof:* The upper bound $\varepsilon_n/r$ is independent of $z \in K$.
  <2>5. Since $\lim_{n \to \infty} \frac{\varepsilon_n}{r} = \frac{0}{r} = 0$, $f_n' \to f'$ uniformly on $K$.
    *Proof:* Squeeze theorem.
  <2>6. Q.E.D.
:::
