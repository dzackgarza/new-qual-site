---
schema: qual/card@1
id: P-Y3MQA
kind: problem
title: "This problem is about the integral $I = \\int_0^\\infty \\frac{\\cos u\\, du}{u^4+1}$"
classification:
  areas:
  - real-analysis
  topics:
  - contour-integration
  - integrals
  - riemann-integrability
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
This problem is about the integral $$I = \int_0^\infty \frac{\cos u\, du}{u^4+1}.$$

a. Show directly that $I$ is a convergent improper Riemann integral.
b. Is $$\int_{[0,\infty)} \frac{\cos u}{u^4+1}d\mu(u)$$ a well-defined Lebesgue integral, where $\mu$ denotes the Lebesgue measure on $\mathbb{R}$?
c. (main part) Evaluate the integral in (a).
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $I = \int_0^\infty \frac{\cos u}{u^4 + 1}\, du$.
(a) Show $I$ converges as an improper Riemann integral.
(b) Is $\int_{[0,\infty)} \frac{\cos u}{u^4+1}\, d\mu(u)$ a well-defined Lebesgue integral?
(c) Evaluate $I$.

<1>1. (a) $\int_0^\infty \frac{du}{u^4 + 1} < \infty$.
Proof: near $0$ the integrand is bounded; near $\infty$, $\frac{1}{u^4+1} \le \frac{2}{u^4}$ for $u \ge 1$ and $\int_1^\infty u^{-4}\, du = \tfrac13 < \infty$.

<1>2. (a) $I$ converges absolutely as an improper Riemann integral.
Proof: $\qty|\frac{\cos u}{u^4+1}| \le \frac{1}{u^4+1}$, so <1>1 gives absolute convergence.

<1>3. (b) Yes: the Lebesgue integral is well defined and equals $I$.
Proof: $\int_{[0,\infty)}\frac{|\cos u|}{u^4+1}\, d\mu \le \int_{[0,\infty)}\frac{du}{u^4+1} < \infty$ by <1>1, so the integrand is in $L^1(\mu)$; for absolutely convergent integrals the Lebesgue and improper Riemann integrals agree.

<1>4. (c) Setup: $I = \tfrac12\Re\int_{-\infty}^{\infty}\frac{e^{iu}}{u^4 + 1}\, du$.
Proof: $\cos u = \Re e^{iu}$ and the integrand is even, so $\int_0^\infty \cos u/(u^4+1)\, du = \tfrac12 \int_{-\infty}^\infty \cos u/(u^4+1)\, du$.

<1>5. The poles of $e^{iz}/(z^4 + 1)$ in the upper half-plane are $z_0 = e^{i\pi/4}$ and $z_1 = e^{3i\pi/4}$, with $\Res_{z_k} = \frac{e^{iz_k}}{4z_k^3}$.
Proof: $z^4 = -1 = e^{i\pi}$ has roots $e^{i(\pi + 2\pi k)/4}$, $k = 0, 1, 2, 3$; the two with positive imaginary part are $z_0, z_1$; each pole is simple, so the residue of $e^{iz}/(z^4+1)$ at $z_k$ is $e^{iz_k}/(4z_k^3)$.

<1>6. The arc contribution vanishes: $\int_{-\infty}^{\infty}\frac{e^{iu}}{u^4+1}\, du = 2\pi i (\Res_{z_0} + \Res_{z_1})$.
Proof: residue theorem on the upper semicircle $|z| = R$, $\Im z > 0$; on the arc, $|e^{iz}| = e^{-\Im z} \le 1$ and $|z^4 + 1| \ge R^4 - 1$, so the arc integral is $O(\pi R/(R^4 - 1)) \to 0$.

<1>7. Compute the residue sum: $\Res_{z_0} + \Res_{z_1} = \frac{e^{-1/\sqrt2}}{4}\qty{e^{i/\sqrt2}e^{-3i\pi/4} + e^{-i/\sqrt2}e^{-i\pi/4}}$.
Proof: $z_0^3 = e^{3i\pi/4}$, $z_1^3 = e^{i\pi/4}$, so $1/z_0^3 = e^{-3i\pi/4}$, $1/z_1^3 = e^{-i\pi/4}$; and $e^{iz_0} = e^{-1/\sqrt2}e^{i/\sqrt2}$, $e^{iz_1} = e^{-1/\sqrt2}e^{-i/\sqrt2}$.

<1>8. Simplify: $\Res_{z_0} + \Res_{z_1} = -\frac{i}{2\sqrt2}e^{-1/\sqrt2}\qty{\cos\tfrac{1}{\sqrt2} + \sin\tfrac{1}{\sqrt2}}$.
Proof: let $c = \cos\tfrac{1}{\sqrt2}$, $s = \sin\tfrac{1}{\sqrt2}$; from <1>7, $e^{i/\sqrt2}e^{-3i\pi/4} = (c + is)\frac{-1-i}{\sqrt2}$ and $e^{-i/\sqrt2}e^{-i\pi/4} = (c - is)\frac{1-i}{\sqrt2}$; summing gives $\frac{1}{\sqrt2}\qty{(c+is)(-1-i) + (c-is)(1-i)} = \frac{-2i(c+s)}{\sqrt2}$, and multiplying by $e^{-1/\sqrt2}/4$ yields the claim.

<1>9. $I = \frac{\pi}{2\sqrt2}e^{-1/\sqrt2}\qty{\cos\tfrac{1}{\sqrt2} + \sin\tfrac{1}{\sqrt2}}$.
Proof: <1>6 and <1>8 give $\int_{-\infty}^\infty \frac{e^{iu}}{u^4+1}\,du = 2\pi i\cdot\qty{-\frac{i}{2\sqrt2}e^{-1/\sqrt2}(c+s)} = \frac{\pi}{\sqrt2}e^{-1/\sqrt2}(c+s)$, which is real; <1>4 halves it.

<1>10. Q.E.D. Proof: <1>2 answers (a); <1>3 answers (b); <1>4–<1>9 evaluate (c).
:::
