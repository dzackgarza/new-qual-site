---
schema: qual/card@1
id: E-SS5.EX-5
kind: exercise
title: "SS 5.5: The Fourier transform of exp(-|t|^alpha) has order alpha/(alpha-1)"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: exercise
5. Show that if $\alpha > 1$ , then

$$
F _ {\alpha} (z) = \int_ {- \infty} ^ {\infty} e ^ {- | t | ^ {\alpha}} e ^ {2 \pi i z t} d t
$$

is an entire function of growth order $\alpha / ( \alpha - 1 )$

[Hint: Show that

$$
- \frac {| t | ^ {\alpha}}{2} + 2 \pi | z | | t | \leq c | z | ^ {\alpha / (\alpha - 1)}
$$

by considering the two cases $| t | ^ { \alpha - 1 } \leq A | z | { \mathrm { ~ a n d ~ } } | t | ^ { \alpha - 1 } \geq A | z | .$ , for an appropriate constant A.]
:::

::: {.solution}
<1>1. Holomorphicity of $F_\alpha(z)$:
<2>1. For any $z = x + iy \in \mathbb{C}$ and $t \in \mathbb{R}$:
\[
\left| e^{-|t|^\alpha} e^{2\pi i z t} \right| = e^{-|t|^\alpha} e^{-2\pi y t} \le e^{-|t|^\alpha + 2\pi |z| |t|}.
\]
::: {.proof}
$|e^{2\pi i (x+iy)t}| = e^{-2\pi y t} \le e^{2\pi |z| |t|}$.
:::
<2>2. Since $\alpha > 1$, as $|t| \to \infty$ the term $-|t|^\alpha$ dominates $2\pi |z| |t|$, ensuring that for any compact subset $K \subset \mathbb{C}$, the integrand and its $z$-derivative $2\pi i t e^{-|t|^\alpha} e^{2\pi i z t}$ are uniformly dominated by an $L^1(\mathbb{R})$ function.
By Morera’s Theorem and Fubini’s Theorem, $F_\alpha(z)$ is an entire function.
::: {.proof}
differentiation under the integral sign / Morera's Theorem.
:::

<1>2. Upper bound on the order of growth:
<2>1. Let $\beta = \frac{\alpha}{\alpha - 1}$, so that $\frac{1}{\alpha} + \frac{1}{\beta} = 1$ are conjugate exponents.
By Young’s inequality $ab \le \frac{a^\alpha}{\alpha} + \frac{b^\beta}{\beta}$ with $a = 2^{1/\alpha} |t|$ and $b = 2^{-1/\alpha} (2\pi |z|)$:
\[
2\pi |z| |t| = (2^{1/\alpha} |t|) (2^{-1/\alpha} 2\pi |z|) \le \frac{2 |t|^\alpha}{\alpha} + \frac{(2^{-1/\alpha} 2\pi |z|)^\beta}{\beta} \le \frac{|t|^\alpha}{2} + c |z|^\beta,
\]
where $c = \frac{(2\pi)^\beta}{\beta 2^{\beta/\alpha}} > 0$.
::: {.proof}
Young's inequality for conjugate exponents.
:::
<2>2. Rearranging gives $-|t|^\alpha + 2\pi |z| |t| \le -\frac{|t|^\alpha}{2} + c |z|^\beta$.
Integrating over $\mathbb{R}$:
\[
|F_\alpha(z)| \le \int_{-\infty}^\infty e^{-|t|^\alpha + 2\pi |z| |t|} \, dt \le e^{c |z|^\beta} \int_{-\infty}^\infty e^{-|t|^\alpha / 2} \, dt = C_0 e^{c |z|^\beta},
\]
where $C_0 = \int_{-\infty}^\infty e^{-|t|^\alpha / 2} \, dt < \infty$.
Thus the growth order $\rho(F_\alpha) \le \beta = \frac{\alpha}{\alpha - 1}$.
::: {.proof}
integral estimate.
:::

<1>3. Lower bound on the order of growth:
<2>1. Evaluate $F_\alpha$ on the negative imaginary axis $z = -i y$ for $y > 0$:
\[
F_\alpha(-iy) = \int_{-\infty}^\infty e^{-|t|^\alpha + 2\pi y t} \, dt \ge \int_0^\infty e^{-t^\alpha + 2\pi y t} \, dt.
\]
::: {.proof}
restricting domain of integration to $[0, \infty)$.
:::
<2>2. The exponent $g(t) = -t^\alpha + 2\pi y t$ attains its maximum at $t_0 = \left(\frac{2\pi y}{\alpha}\right)^{1/(\alpha-1)}$, with maximum value:
\[
g(t_0) = -\left(\frac{2\pi y}{\alpha}\right)^{\frac{\alpha}{\alpha-1}} + 2\pi y \left(\frac{2\pi y}{\alpha}\right)^{\frac{1}{\alpha-1}} = \left(1 - \frac{1}{\alpha}\right) \left(\frac{2\pi}{\alpha}\right)^\beta y^\beta = c' y^\beta \quad (c' > 0).
\]
::: {.proof}
calculus optimization of $g(t)$.
:::
<2>3. Integrating over the interval $[t_0, t_0 + 1]$ gives $F_\alpha(-iy) \ge C_1 e^{c' y^\beta}$ for large $y > 0$.
Thus the order of growth satisfies:
\[
\rho(F_\alpha) = \limsup_{r \to \infty} \frac{\log \log M(r)}{\log r} \ge \beta = \frac{\alpha}{\alpha - 1}.
\]
::: {.proof}
maximum modulus along a ray.
:::

<1>4. Conclusion:
$F_\alpha$ is an entire function of exact growth order $\rho = \frac{\alpha}{\alpha - 1}$. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
