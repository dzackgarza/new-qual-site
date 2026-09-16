---
schema: qual/card@1
id: P-CASP19G
kind: problem
title: "Poisson integral converges to the boundary value at points of continuity"
classification:
  areas:
  - complex-analysis
  topics:
  - Poisson Kernel
  - Harmonic Functions
  - Boundary Values
relations: []
review: draft
---

::: {.problem}
Let $f$ be a bounded, piecewise continuous function on $\partial \mathbb{D}$, and consider the harmonic function
$$
u(z) = \frac{1}{2\pi} \int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it}) \, dt, \quad z = re^{i\theta},
$$
where $P_r(t) := \operatorname{Re} \frac{1 + re^{it}}{1 - re^{it}}$ is the Poisson kernel in $\mathbb{D}$.
Assume that $f$ is continuous at $a = e^{i\theta_0}$, and show that $\lim_{z \to a} u(z) = f(a)$.
:::

::: {.solution}
Write the Poisson integral as $u$ (the statement denotes it by $\nu$ in the
display). Since
\[
\frac1{2\pi}\int_{-\pi}^{\pi}P_r(t)\,dt=1,
\]
we have
\[
u(re^{i\theta})-f(a)
=\frac1{2\pi}\int_{-\pi}^{\pi}
P_r(\theta-t)\bigl(f(e^{it})-f(a)\bigr)\,dt.
\]

Let $\varepsilon>0$. By continuity at $a=e^{i\theta_0}$, choose
$\delta>0$ so that
\[
|f(e^{it})-f(a)|<\varepsilon
\]
whenever $|t-\theta_0|<2\delta$. If $z=re^{i\theta}$ is sufficiently close
to $a$, then $|\theta-\theta_0|<\delta$. Split the integral into
$|t-\theta_0|<2\delta$ and its complement. The first part has absolute value
at most $\varepsilon$.

On the complement, $|\theta-t|\ge\delta$, and the Poisson kernel tends to
$0$ uniformly there as $r\to1^-$. Since $f$ is bounded, the complementary
integral therefore tends to $0$. Hence
\[
\limsup_{z\to a}|u(z)-f(a)|\le\varepsilon.
\]
As $\varepsilon$ is arbitrary,
\[
\boxed{\lim_{z\to a}u(z)=f(a)}.
\]
:::
