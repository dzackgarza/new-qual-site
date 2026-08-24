---
schema: qual/card@1
id: P-4BJMK
kind: problem
title: Evaluate $\int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Contour Integration
  - Integrals
  - Riemann Integrability
relations: []
review: draft
---

::: {.problem title="?"}
This problem is about the integral $$I = \int_{-\infty}^{\infty} \frac{\sin x}{x}dx.$$

- Show directly that $I$ is a convergent improper Riemann integral.

- Use a contour integral to evaluate $I$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (Part 1) The integral is a convergent improper Riemann integral.
Proof: the integrand extends continuously to $x=0$ ($\sin x/x \to 1$), so only the tail matters.
For the tail, integrate by parts: for $A < B$, \[ \int_A^B \frac{\sin x}{x}\,dx = \Big[\frac{-\cos x}{x}\Big]_A^B - \int_A^B \frac{\cos x}{x^2}\,dx, \] and as $A,B\to\infty$ the boundary terms tend to $0$ while $\int_1^\infty |\cos x|/x^2\,dx < \infty$; hence $\int_1^\infty \sin x/x\,dx$ converges (equivalently, Dirichlet's test: $\sin x$ has bounded partial integrals and $1/x \downarrow 0$). So $I$ is a convergent improper Riemann integral.
<1>2. (Part 2, setup) Integrate $e^{iz}/z$ over a semicircular contour.
Proof: let $R > 1 > \rho > 0$ and integrate $f(z) = e^{iz}/z$ over the boundary of the region $\{\rho \le |z| \le R,\ \Im z \ge 0\}$: the segment $[-R,-\rho]\cup[\rho,R]$ on the real axis, the large semicircle $C_R$ (counterclockwise), and the small semicircle $C_\rho$ (clockwise).
Since $f$ is holomorphic on and inside the region (no pole: the origin is outside), the total integral is $0$.
<1>3. The large semicircle contributes $0$ in the limit.
Proof: on $C_R$, $z = Re^{i\theta}$, $0\le\theta\le\pi$: $|e^{iz}| = e^{-\Im z} \le 1$ and $|dz| = R\,d\theta$, so $|\int_{C_R}e^{iz}/z\,dz| \le \int_0^\pi e^{-R\sin\theta}d\theta \to 0$ (Jordan's lemma / dominated convergence: $e^{-R\sin\theta} \to 0$ except at $\theta=0,\pi$). <1>4. The small semicircle contributes $-\pi i$.
Proof: on $C_\rho$, $z = \rho e^{i\theta}$ traversed clockwise: $e^{iz} = 1 + O(\rho)$, so \[ \int_{C_\rho}\frac{e^{iz}}{z}\,dz = \int_{\pi}^{0}\frac{1+O(\rho)}{\rho e^{i\theta}}\,\rho i e^{i\theta}\,d\theta \to -i\pi . \] (Equivalently, the residue of $e^{iz}/z$ at $0$ is $1$, and the clockwise small semicircle gives $-\pi i$ times the residue.)
<1>5. Conclusion.
Proof: by <1>2--<1>4, $\int_{[-R,-\rho]\cup[\rho,R]}\frac{e^{ix}}{x}\,dx \to \pi i$.
Taking imaginary parts, \[ 2\int_{\rho}^{R}\frac{\sin x}{x}\,dx \to \pi, \] so $I = \int_{-\infty}^{\infty}\frac{\sin x}{x}\,dx = \pi$.
<1>6. Q.E.D.
:::
