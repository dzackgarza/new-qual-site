---
schema: qual/card@1
id: E-YMM6X
kind: problem
title: Weierstrass's theorem on locally uniform limits of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: {.exercise}
Show that if $\theset{f_n}$ is a sequence of holomorphic functions converging uniformly to a function $f$ on every compact subset of $\Omega$, then $f$ is holomorphic on $\Omega$ and $\theset{f_n'}$ converges uniformly to $f'$ on every such compact subset.
:::

::: {.solution}
**Goal:** Let $(f_n)$ be a sequence of holomorphic functions on a domain $D \subset \mathbb{C}$ such that $f_n \to f$ uniformly on compact subsets of $D$ (locally uniformly).
Prove that:

1. $f$ is holomorphic on $D$ (Weierstrass's Theorem on uniform convergence).

2. $f_n' \to f'$ uniformly on compact subsets of $D$.

* * *

### Part 1: $f$ is Holomorphic on $D$ (via Morera's Theorem)

<1>1. **$f$ is continuous on $D$.** <2>1. Each $f_n$ is holomorphic on $D$, hence continuous.
::: {.proof}
Complex differentiability at a point implies continuity at that point, so every holomorphic function is continuous.
:::
<2>2. For any point $z_0 \in D$, there exists a closed disk $\overline{D}(z_0, r) \subset D$, which is compact.
::: {.proof}
Since $D$ is open, some open disk $D(z_0, r)$ lies in $D$, and its closure $\overline{D}(z_0, r)$ is a compact subset of $D$.
:::
<2>3. By hypothesis, $f_n \to f$ uniformly on $\overline{D}(z_0, r)$.
::: {.proof}
The closed disk is compact, and the hypothesis gives uniform convergence on every compact subset of $D$.
:::
<2>4. The uniform limit of continuous functions is continuous, so $f$ is continuous on $\overline{D}(z_0, r)$, and hence continuous at $z_0$.
::: {.proof}
A uniform limit of continuous functions is continuous; since each $f_n$ is continuous and $f_n \to f$ uniformly on $\overline{D}(z_0, r)$, $f$ is continuous there, in particular at $z_0$.
:::
<2>5. Since $z_0 \in D$ was arbitrary, $f$ is continuous on all of $D$.
::: {.proof}
Continuity at every point of $D$ is exactly continuity on $D$.
:::
<2>6. Q.E.D.

<1>2. **$\oint_{\partial T} f(z) \, dz = 0$ for every closed triangle $T \subset D$.** <2>1. Let $T \subset D$ be any closed triangle with boundary $\partial T$.
::: {.proof}
We fix an arbitrary closed triangle $T$ contained in $D$ to verify the hypothesis of Morera's theorem.
:::
<2>2. $T$ is a compact subset of $D$, so $f_n \to f$ uniformly on $\partial T \subset T$.
::: {.proof}
A closed triangle is compact, and its boundary is a closed (hence compact) subset of $T$, so uniform convergence on $T$ implies uniform convergence on $\partial T$.
:::
<2>3. Since each $f_n$ is holomorphic in the simply connected domain containing $T$, Cauchy's Theorem (Goursat's Lemma) implies $\oint_{\partial T} f_n(z) \, dz = 0$ for all $n$.
::: {.proof}
Goursat's lemma states that a function holomorphic on a domain has vanishing integral over the boundary of any triangle contained in that domain.
:::
<2>4. Uniform convergence justifies taking the limit inside the integral: $$\oint_{\partial T} f(z) \, dz = \oint_{\partial T} \lim_{n \to \infty} f_n(z) \, dz = \lim_{n \to \infty} \oint_{\partial T} f_n(z) \, dz = \lim_{n \to \infty} 0 = 0.$$
::: {.proof}
The $ML$-inequality gives $\left| \oint_{\partial T} (f_n - f) \, dz \right| \leq \sup_{z \in \partial T} |f_n(z) - f(z)| \cdot \text{length}(\partial T)$, and this tends to $0$ by uniform convergence, so the limit and the integral commute.
:::
<2>5. Q.E.D.

<1>3. **By Morera's Theorem, $f$ is holomorphic on $D$.** <2>1. $f$ is continuous on $D$ and $\oint_{\partial T} f(z) \, dz = 0$ for every triangle $T \subset D$.
::: {.proof}
These are exactly the conclusions of <1>1 and <1>2.
:::
<2>2. By Morera's Theorem, $f$ is holomorphic on $D$.
::: {.proof}
Morera's theorem states that a continuous function whose integral over every triangle vanishes is holomorphic.
:::
<2>3. Q.E.D.

* * *

### Part 2: $f_n' \to f'$ Uniformly on Compact Subsets

<1>4. **Integral formula for derivatives on compact sets.** <2>1. Let $K \subset D$ be any compact subset.
::: {.proof}
We fix an arbitrary compact subset $K$ of $D$ on which to prove uniform convergence of the derivatives.
:::
<2>2. Since $K$ is compact and $D^c = \mathbb{C} \setminus D$ is closed and disjoint from $K$, the distance $d \coloneqq \text{dist}(K, \partial D) > 0$.
::: {.proof}
The distance between a compact set and a disjoint closed set in a metric space is strictly positive; here $K$ is compact and $\partial D$ is closed with $K \cap \partial D = \varnothing$.
:::
<2>3. Choose $r = d/2 > 0$.
The enlarged set $K_r \coloneqq \{w \in \mathbb{C} : \text{dist}(w, K) \leq r\}$ is a compact subset of $D$.
::: {.proof}
$K_r$ is closed and bounded, hence compact; since $r < d$, every point of $K_r$ is at distance at most $r < d$ from $K$, so it stays inside $D$.
:::
<2>4. For every $z \in K$, the circle $C(z, r) = \{w : |w - z| = r\}$ is contained in $K_r \subset D$.
::: {.proof}
Every point $w$ on $C(z, r)$ has distance $r$ from $z \in K$, so $\text{dist}(w, K) \le r$, meaning $w \in K_r$.
:::
<2>5. By Cauchy's Integral Formula for derivatives, for any $z \in K$: $$f_n'(z) - f'(z) = \frac{1}{2\pi i} \oint_{|w-z|=r} \frac{f_n(w) - f(w)}{(w - z)^2} \, dw.$$
::: {.proof}
Cauchy's derivative formula gives $f_n'(z) = \frac{1}{2\pi i}\oint \frac{f_n(w)}{(w-z)^2}\,dw$ and $f'(z) = \frac{1}{2\pi i}\oint \frac{f(w)}{(w-z)^2}\,dw$; subtracting and using linearity of the integral gives the stated formula.
:::
<2>6. Q.E.D.

<1>5. **Bound $|f_n'(z) - f'(z)|$ uniformly over $z \in K$.** <2>1. For $w \in C(z, r)$, $|w - z| = r$, so $|(w - z)^2| = r^2$.
::: {.proof}
The circle $C(z, r)$ consists of points at distance exactly $r$ from $z$, so $|w - z| = r$ and $|(w-z)^2| = r^2$.
:::
<2>2. Let $\varepsilon_n \coloneqq \sup_{w \in K_r} |f_n(w) - f(w)|$.
By uniform convergence on the compact set $K_r$, $\lim_{n \to \infty} \varepsilon_n = 0$.
::: {.proof}
The hypothesis of local uniform convergence applied to the compact set $K_r$ gives $\sup_{w \in K_r} |f_n(w) - f(w)| \to 0$.
:::
<2>3. Apply the $ML$-inequality to the Cauchy integral from <1>4.<2>5: $$|f_n'(z) - f'(z)| \leq \frac{1}{2\pi} \cdot \frac{\varepsilon_n}{r^2} \cdot (2\pi r) = \frac{\varepsilon_n}{r}.$$
::: {.proof}
The integrand is bounded by $M = \varepsilon_n / r^2$ and the contour has length $L = 2\pi r$, so the $ML$-inequality gives $\frac{1}{2\pi} \cdot \frac{\varepsilon_n}{r^2} \cdot 2\pi r = \frac{\varepsilon_n}{r}$.
:::
<2>4. Taking the supremum over all $z \in K$: $$\sup_{z \in K} |f_n'(z) - f'(z)| \leq \frac{\varepsilon_n}{r}.$$
::: {.proof}
The upper bound $\varepsilon_n / r$ does not depend on $z$, so it bounds the supremum over $z \in K$.
:::
<2>5. Since $\lim_{n \to \infty} \frac{\varepsilon_n}{r} = \frac{0}{r} = 0$, $f_n' \to f'$ uniformly on $K$.
::: {.proof}
As $n \to \infty$, $\varepsilon_n \to 0$, so $\varepsilon_n / r \to 0$; the bound in <2>4 then forces $\sup_{z \in K} |f_n'(z) - f'(z)| \to 0$, which is uniform convergence on $K$.
:::
<2>6. Q.E.D.
:::
