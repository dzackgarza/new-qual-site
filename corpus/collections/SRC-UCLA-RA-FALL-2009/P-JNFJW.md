---
schema: qual/card@1
id: P-JNFJW
kind: problem
title: Injectivity of holomorphic functions with $\operatorname{Re}(f')>0$, and the
  need for convexity
classification:
  areas:
  - real-analysis
  topics:
  - Holomorphic Functions
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\Omega$ be an open convex region in the complex plane.
Assume $f$ is a holomorphic function on $\Omega$ and the $\text{Re}(f'(z))>0$ for all $z\in\Omega$.

a. Prove that $f$ is one-to-one.

b. Show by example that the word "convex" cannot be replaced by "connected and simply connected".
:::

::: {.solution}
<1>1. Part (a): $f$ is one-to-one on convex $\Omega$:
<2>1. Let $z_1, z_2 \in \Omega$ with $z_1 \neq z_2$.
Since $\Omega$ is convex, the straight line segment $\gamma(t) = (1-t)z_1 + t z_2$ for $t \in [0, 1]$ lies entirely in $\Omega$.
Proof: definition of convexity.
<2>2. By the Fundamental Theorem of Calculus along the segment $\gamma$:
\[
f(z_2) - f(z_1) = \int_0^1 \frac{d}{dt} f(\gamma(t)) \, dt = (z_2 - z_1) \int_0^1 f'\big((1-t)z_1 + t z_2\big) \, dt.
\]
Proof: chain rule and path integration of holomorphic functions.
<2>3. Dividing by $z_2 - z_1 \neq 0$ and taking the real part:
\[
\operatorname{Re}\left(\frac{f(z_2) - f(z_1)}{z_2 - z_1}\right) = \int_0^1 \operatorname{Re}\Big(f'\big((1-t)z_1 + t z_2\big)\Big) \, dt.
\]
Proof: real part commutes with integration over real intervals.
<2>4. The integrand $t \mapsto \operatorname{Re}(f'(\gamma(t)))$ is continuous and strictly positive on $[0, 1]$ since $\operatorname{Re}(f'(z)) > 0$ for all $z \in \Omega$.
Thus:
\[
\int_0^1 \operatorname{Re}\Big(f'(\gamma(t))\Big) \, dt > 0.
\]
Proof: integral of a strictly positive continuous function is strictly positive.
<2>5. Therefore $\operatorname{Re}\left(\frac{f(z_2) - f(z_1)}{z_2 - z_1}\right) \neq 0$, which implies $f(z_2) - f(z_1) \neq 0$, so $f(z_1) \neq f(z_2)$.
Thus $f$ is one-to-one.
Proof: non-zero real part implies non-zero complex number.

<1>2. Part (b): Counterexample for simply connected non-convex domains:
<2>1. Consider the function $f(z) = z + \frac{1}{z}$, with derivative $f'(z) = 1 - \frac{1}{z^2}$.
Proof: definition of $f$.
<2>2. On the unit circle $z = e^{i\theta}$, the derivative is:
\[
f'(e^{i\theta}) = 1 - e^{-2i\theta} = (1 - \cos 2\theta) + i \sin 2\theta = 2\sin^2\theta + i \sin 2\theta.
\]
Thus $\operatorname{Re}(f'(e^{i\theta})) = 2\sin^2\theta > 0$ for all $\theta \in (0, \pi) \cup (-\pi, 0)$.
Proof: trigonometric double angle identity.
<2>3. For $r = 1 + \varepsilon$ with $\varepsilon > 0$, $\operatorname{Re}(f'(r e^{i\theta})) = 1 - \frac{\cos 2\theta}{r^2} \ge 1 - \frac{1}{(1+\varepsilon)^2} > 0$ for all $\theta$.
Proof: $r > 1 \implies 1/r^2 < 1$.
<2>4. Let $\Omega$ be a simply connected, C-shaped tube containing the arc of the unit circle between $\theta = -\pi/3$ and $\theta = \pi/3$, bulging outward to $r > 1$ near $\theta = 0$.
On this domain, $\operatorname{Re}(f'(z)) > 0$ everywhere.
Proof: <2>2 and <2>3.
<2>5. Evaluate $f$ at the two endpoints $z_1 = e^{i\pi/3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$ and $z_2 = e^{-i\pi/3} = \frac{1}{2} - i\frac{\sqrt{3}}{2}$:
\[
f(z_1) = e^{i\pi/3} + e^{-i\pi/3} = 2\cos\left(\frac{\pi}{3}\right) = 1,
\]
and
\[
f(z_2) = e^{-i\pi/3} + e^{i\pi/3} = 2\cos\left(-\frac{\pi}{3}\right) = 1.
\]
Thus $f(z_1) = f(z_2) = 1$ even though $z_1 \neq z_2$, so $f$ is not one-to-one.
Proof: $e^{i\theta} + e^{-i\theta} = 2\cos\theta$.

<1>3. Conclusion:
$f$ is injective on convex domains, but convexity cannot be relaxed to simply connected domains. Q.E.D.
Proof: <1>1 and <1>2.
:::
