---
schema: qual/card@1
id: P-AW6IK
kind: problem
title: A function holomorphic on $0<|z|<1$ with $\int_{|z|=r}f=0$ for all $r<1$, but
  not holomorphic at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Singularities
  - Counterexamples
  - Residues
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show by example that there exists a function $f(z)$ that is holomorphic on the punctured disk $D^*(0, 1) = \{z \in \mathbb{C} \mid 0 < |z| < 1\}$ such that for all $0 < r < 1$:
$$\oint_{|z| = r} f(z) \, dz = 0,$$
but $f$ is not holomorphic at $z = 0$.
:::

::: solution
**Goal:** Exhibit an explicit function $f(z)$ holomorphic on the punctured disk with $\operatorname{Res}(f, 0) = 0$ (hence $\oint_{|z|=r} f(z) \, dz = 0$ for all $r$) having a non-removable singularity at $z = 0$.

<1>1. Candidate Function: $f(z) = \frac{1}{z^2}$:
    *Proof:*
    <2>1. Define $f(z) = \frac{1}{z^2}$ for $z \in \mathbb{C} \setminus \{0\}$.
    <2>2. **$f$ is holomorphic on $0 < |z| < 1$:** As a rational function with pole only at $z = 0$, $f$ is analytic and holomorphic on the punctured unit disk $\{0 < |z| < 1\}$.
    <2>3. **$f$ is not holomorphic at $z = 0$:** The limit $\lim_{z \to 0} |f(z)| = \lim_{z \to 0} \frac{1}{|z|^2} = \infty$. Thus $z = 0$ is a pole of order 2, which is an isolated non-removable singularity; in particular, $f$ cannot be extended holomorphically to $z = 0$.

<1>2. Verification of the Integral Condition for all $0 < r < 1$:
    *Proof:*
    <2>1. Parameterize the circle $\gamma_r(t) = r e^{it}$ for $t \in [0, 2\pi]$ (so $dz = i r e^{it} dt$).
    <2>2. **Direct computation:**
        $$\oint_{|z|=r} f(z) \, dz = \int_0^{2\pi} \frac{1}{(r e^{it})^2} (i r e^{it}) \, dt = \frac{i}{r} \int_0^{2\pi} e^{-it} \, dt = \frac{i}{r} \left[ \frac{e^{-it}}{-i} \right]_0^{2\pi} = -\frac{1}{r}(1 - 1) = 0.$$
    <2>3. **Via the Residue Theorem:**
        - By the Cauchy Residue Theorem:
            $$\oint_{|z|=r} f(z) \, dz = 2\pi i \operatorname{Res}(f, 0).$$
        - The Laurent series of $f(z) = \frac{1}{z^2}$ around $z = 0$ is simply $z^{-2}$.
        - The coefficient of $z^{-1}$ is $c_{-1} = 0$.
        - Thus $\operatorname{Res}(f, 0) = 0$, which implies $\oint_{|z|=r} f(z) \, dz = 2\pi i (0) = 0$ for every $0 < r < 1$.
    <2>4. **Via Antiderivatives:** On the punctured plane $\mathbb{C} \setminus \{0\}$, $f(z) = \frac{1}{z^2}$ has a single-valued holomorphic primitive $F(z) = -\frac{1}{z}$. By the Fundamental Theorem of Calculus for contour integrals, the integral along any closed loop $\gamma$ is $F(\gamma(b)) - F(\gamma(a)) = 0$.

<1>3. Other Examples (Higher order poles and essential singularities):
    *Proof:*
    <2>1. Any function $f(z) = \frac{1}{z^k}$ for integer $k \ge 2$ satisfies $\oint_{|z|=r} \frac{1}{z^k} \, dz = 0$ and has a pole of order $k$ at $0$.
    <2>2. $f(z) = \cos(1/z) = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} z^{-2n} = 1 - \frac{1}{2z^2} + \frac{1}{24z^4} - \cdots$ has an essential singularity at $z = 0$, but all odd negative powers vanish, so $\operatorname{Res}(f, 0) = 0$ and $\oint_{|z|=r} \cos(1/z) \, dz = 0$.

<1>4. Conclusion:
    $f(z) = \frac{1}{z^2}$ is holomorphic on $0 < |z| < 1$, satisfies $\oint_{|z|=r} f(z) \, dz = 0$ for all $r \in (0, 1)$, and has a pole of order 2 at $0$. Q.E.D.
:::
