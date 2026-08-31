---
schema: qual/card@1
id: E-BV7DD
kind: problem
title: Polynomials cannot uniformly approximate $z^{-m}$ on an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Polynomials
  - Uniform Convergence
  - Laurent Series
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: problem
(1) Let $p(z)$ be a polynomial, $R>0$ any positive number, and $m \geq 1$ an integer.
Let $M_R = \sup \{ |z^{m} p(z) - 1|: |z| = R  \}$.
Show that $M_R>1$.

(2) Let $m \geq 1$ be an integer and $K = \{z \in {\mathbb C}: r \leq |z| \leq R \}$ where $r<R$.
Show (i) using (1) as well as, (ii) without using (1) that there exists a positive number $\varepsilon_0>0$ such that for each polynomial $p(z)$, $$\sup \{|p(z) - z^{-m}|: z \in K  \} \geq \varepsilon_0 \, .$$
:::

::: {.solution}
**Goal:**
1. For any polynomial $p(z)$, $R > 0$, and integer $m \geq 1$, prove that $M_R = \sup_{|z|=R} |z^m p(z) - 1| > 1$.
2. For $K = \{z \in \mathbb{C} : r \leq |z| \leq R\}$ with $0 < r < R$, prove the existence of $\varepsilon_0 > 0$ such that $\sup_{z \in K} |p(z) - z^{-m}| \geq \varepsilon_0$ for all polynomials $p$:
   - (i) using (1);
   - (ii) without using (1) (via contour integration / residue / Laurent coefficient).

---

### Part (1): Proof that $M_R > 1$

<1>1. **Define $f(z) = z^m p(z) - 1$.**
  <2>1. $f(z)$ is a polynomial, hence entire.
::: {.proof}
$z^m p(z)$ is the product of two polynomials, and subtracting the constant $1$ gives a polynomial, which is entire.
:::
  <2>2. $f(0) = 0^m p(0) - 1 = -1$ since $m \geq 1$.
::: {.proof}
Since $m \ge 1$, we have $0^m = 0$, so $f(0) = 0 \cdot p(0) - 1 = -1$.
:::
  <2>3. Thus $|f(0)| = |-1| = 1$.
::: {.proof}
The absolute value of $-1$ is $1$.
:::
  <2>4. Q.E.D.

<1>2. **Apply the Maximum Modulus Principle to $f(z)$ on the disk $\overline{D}(0, R)$.**
  <2>1. If $p(z) \equiv 0$, then $f(z) \equiv -1$, which is constant, so $M_R = |-1| = 1$ would hold. However, if $p(z) \equiv 0$, then on $|z|=R$, $|z^m(0) - 1| = 1$. But for any polynomial $p(z) \not\equiv 0$, $f(z)$ is non-constant. (If $p \equiv 0$, then $z^m p(z) - 1 \equiv -1$. Note: the problem formulation assumes $p$ is a non-trivial polynomial or that $M_R \geq 1$ with strict inequality $M_R > 1$ for non-constant $f$; if $p(z) \neq 0$, $f$ has degree $\geq m \geq 1$, so $f$ is non-constant).
::: {.proof}
For any polynomial $p \not\equiv 0$, the term $z^m p(z)$ has degree $m + \deg(p) \ge m \ge 1$, so $f(z) = z^m p(z) - 1$ is non-constant.
:::
  <2>2. By the Maximum Modulus Principle, a non-constant holomorphic function on a bounded domain cannot attain its maximum in the interior.
::: {.proof}
The Maximum Modulus Principle states that a non-constant holomorphic function on a connected bounded domain has no interior maximum of its modulus.
:::
  <2>3. Since $0 \in D(0, R)$ is an interior point, $M_R = \sup_{|z|=R} |f(z)| > |f(0)| = 1$.
::: {.proof}
If $f$ is non-constant, its modulus on the boundary circle $|z| = R$ must exceed its value $|f(0)| = 1$ at the interior point $0$; hence $M_R > 1$.
:::
  <2>4. (For $p \equiv 0$, $|p(z) - z^{-m}| = |z|^{-m}$, whose supremum on $K$ is $r^{-m} > 0$).
::: {.proof}
When $p \equiv 0$, the function $z^m p(z) - 1 \equiv -1$ is constant, so the strict inequality $M_R > 1$ fails; this degenerate case is handled separately in Part (2).
:::
  <2>5. Q.E.D.

---

### Part (2)(i): Proof using Part (1)

<1>3. **Establish the uniform lower bound using Part (1).**
  <2>1. For any polynomial $p(z)$ and $z \in K$, on the outer boundary $|z| = R$:
  $$|p(z) - z^{-m}| = \frac{|z^m p(z) - 1|}{|z|^m} = \frac{|z^m p(z) - 1|}{R^m}.$$
::: {.proof}
Multiplying $p(z) - z^{-m}$ by $z^m$ gives $z^m p(z) - 1$, so $|p(z) - z^{-m}| = \frac{|z^m p(z) - 1|}{|z|^m}$; on $|z| = R$ this denominator is $R^m$.
:::
  <2>2. Taking the supremum over the sub-circle $|z| = R \subset K$:
  $$\sup_{z \in K} |p(z) - z^{-m}| \geq \sup_{|z|=R} |p(z) - z^{-m}| = \frac{1}{R^m} \sup_{|z|=R} |z^m p(z) - 1| = \frac{M_R}{R^m}.$$
::: {.proof}
The supremum over the larger set $K$ is at least the supremum over the subset $|z| = R$; by <2>1 the latter equals $\frac{1}{R^m} M_R$.
:::
  <2>3. By Part (1), for non-zero polynomials $M_R > 1 \geq 1$, and for $p \equiv 0$, $\sup_{z \in K} |0 - z^{-m}| = r^{-m} > R^{-m}$. Thus for all polynomials $p$, $M_R \geq 1$.
::: {.proof}
For $p \not\equiv 0$, Part (1) gives $M_R > 1$; for $p \equiv 0$, the supremum of $|z^{-m}|$ on $K$ is $r^{-m}$, which exceeds $R^{-m}$ since $r < R$.
:::
  <2>4. Therefore, setting $\varepsilon_0 = \frac{1}{R^m} > 0$, we have $\sup_{z \in K} |p(z) - z^{-m}| \geq \varepsilon_0$ for all polynomials $p(z)$.
::: {.proof}
By <2>2> and <2>3>, $\sup_{z \in K} |p(z) - z^{-m}| \ge \frac{M_R}{R^m} \ge \frac{1}{R^m} = \varepsilon_0 > 0$.
:::
  <2>5. Q.E.D.

---

### Part (2)(ii): Proof without using Part (1) (Contour Integration)

<1>4. **Integrate along the concentric circle $\gamma_\rho: z = \rho e^{i\theta}$ for $r < \rho < R$.**
  <2>1. Choose $\rho = \frac{r+R}{2}$, so the circle $\gamma_\rho$ lies entirely in the interior of the annulus $K$.
    *Proof:* $r < \rho < R$.
  <2>2. For any polynomial $p(z) = \sum_{k=0}^N a_k z^k$, consider the integral:
  $$\oint_{\gamma_\rho} \big( p(z) - z^{-m} \big) z^{m-1} \, dz = \oint_{\gamma_\rho} p(z) z^{m-1} \, dz - \oint_{\gamma_\rho} \frac{dz}{z}.$$
    *Proof:* Linearity of the contour integral and $(z^{-m}) z^{m-1} = z^{-1}$.
  <2>3. Since $p(z) z^{m-1}$ is a polynomial (entire), by Cauchy's Theorem $\oint_{\gamma_\rho} p(z) z^{m-1} \, dz = 0$.
    *Proof:* Cauchy's theorem for holomorphic functions on simply connected domains.
  <2>4. By the standard circle integral, $\oint_{\gamma_\rho} \frac{dz}{z} = 2\pi i$.
    *Proof:* Direct evaluation via parametrization.
  <2>5. Thus, for any polynomial $p(z)$:
  $$\oint_{\gamma_\rho} \big( p(z) - z^{-m} \big) z^{m-1} \, dz = 0 - 2\pi i = -2\pi i.$$
    *Proof:* Subtraction of the two integral values.
  <2>6. Q.E.D.

<1>5. **Apply the $ML$-inequality to deduce the lower bound $\varepsilon_0$.**
  <2>1. Let $S = \sup_{z \in K} |p(z) - z^{-m}|$.
    *Proof:* Definition of the supremum.
  <2>2. On $\gamma_\rho$, $|z| = \rho$, so $|z^{m-1}| = \rho^{m-1}$, and the length of $\gamma_\rho$ is $2\pi \rho$.
    *Proof:* Circle radius and circumference.
  <2>3. By the $ML$-inequality:
  $$2\pi = |-2\pi i| = \left| \oint_{\gamma_\rho} \big( p(z) - z^{-m} \big) z^{m-1} \, dz \right| \leq S \cdot \rho^{m-1} \cdot (2\pi \rho) = 2\pi \rho^m S.$$
    *Proof:* Modulus of integral is bounded by maximum of integrand times curve length.
  <2>4. Dividing both sides by $2\pi \rho^m$:
  $$S \geq \frac{1}{\rho^m}.$$
    *Proof:* Division by $2\pi \rho^m > 0$.
  <2>5. Setting $\varepsilon_0 = \frac{1}{\rho^m} = \left(\frac{2}{r+R}\right)^m > 0$, which is independent of the polynomial $p(z)$, we conclude $\sup_{z \in K} |p(z) - z^{-m}| \geq \varepsilon_0$.
    *Proof:* $\varepsilon_0 > 0$ depends only on $r, R, m$.
  <2>6. Q.E.D.
:::
