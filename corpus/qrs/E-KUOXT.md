---
schema: qual/card@1
id: E-KUOXT
kind: exercise
title: Almost everywhere and uniform convergence of approximations to the identity
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - Uniform Convergence
relations: []
review: draft
---

::: exercise
- Show that if additionally $\abs{\phi(x)} \leq c(1 + \abs{x})^{-n-\eps}$ for some $c,\eps>0$, then this converges is almost everywhere.

- Show that is $f$ is bounded and uniformly continuous and $\phi_t$ is an approximation to the identity, then $f\ast \phi_t$ uniformly converges to $f$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) If $\phi$ decays like $|\phi(x)| \leq c(1+|x|)^{-n-\eps}$ with $c, \eps > 0$, then $f \ast \phi_t \to f$ almost everywhere as $t \to 0$ for $f \in L^1$; (2) if $f$ is bounded and uniformly continuous and $\phi_t$ is an approximation to the identity, then $f \ast \phi_t \to f$ uniformly.

<1>1. Setup: $\phi_t(x) := t^{-n} \phi(x/t)$, $\int \phi = 1$; $\phi$ satisfies the pointwise decay bound $|\phi(x)| \leq c(1+|x|)^{-n-\eps}$.
Proof: this is the standing hypothesis; the decay bound makes $\phi \in L^1$ and gives a majorant $\Psi(x) := c(1+|x|)^{-n-\eps}$ that is radially decreasing and integrable.
<1>2. Almost everywhere convergence: for $f \in L^1$, $f \ast \phi_t(x) \to f(x)$ for a.e. $x$.
<2>1. It suffices to show $\sup_{t>0} |f \ast \phi_t(x)| \leq C \, Mf(x)$ for a.e. $x$, where $Mf$ is the Hardy–Littlewood maximal function.
Proof: the maximal function is finite a.e. for $f \in L^1$ (weak-type $(1,1)$ estimate).
Once the sup bound holds, split $f\ast\phi_t(x) - f(x) = \int \phi_t(y)\big(f(x-y) - f(x)\big)\,dy$ and argue as follows: for any $\eta > 0$ choose continuous compactly supported $g$ with $\|f - g\|_1 < \eta$; then $|f\ast\phi_t - f| \leq |(f-g)\ast\phi_t| + |g\ast\phi_t - g| + |g - f|$; the middle term tends to $0$ uniformly in $x$ (uniform continuity of $g$, standard mollifier argument) and the two outer terms are each bounded by $C\, M(f-g)(x) + |f-g|(x)$-type quantities that are small in $L^1$, so a.e. convergence follows from the a.e. finiteness of the maximal function applied to $f-g$ and the Borel–Cantelli/diagonal argument.
<2>2. The maximal bound: $|f \ast \phi_t(x)| \leq C \, Mf(x)$.
Proof: the decay bound gives $|\phi(y)| \leq \Psi(|y|)$ with $\Psi$ radially decreasing and integrable; the standard computation (layer-cake / dyadic annuli) shows $\sup_t |f\ast\phi_t(x)| \leq \|\Psi\|_1^{-1}\! \int_0^\infty \Psi(s) \frac{1}{m(B_s)}\int_{B_s} |f(x-y)|\,dy\,ds' \leq C Mf(x)$; that is, the convolution against a radially decreasing integrable kernel is controlled by the maximal function.
<1>3. Uniform convergence when $f$ is bounded and uniformly continuous.
<2>1. Split: $f\ast\phi_t(x) - f(x) = \int \phi_t(y)\big(f(x-y) - f(x)\big)\,dy$, using $\int \phi_t = 1$.
Proof: $\int \phi_t = \int \phi = 1$.
<2>2. Given $\eps > 0$, pick $\delta > 0$ with $|f(x-y) - f(x)| < \eps/2$ whenever $|y| < \delta$ (uniform continuity), and split the integral at $|y| = \delta$.
Proof: uniform continuity of $f$ is the hypothesis.
<2>3. The inner part satisfies $|\int_{|y|<\delta} \phi_t(y)(f(x-y)-f(x))\,dy| \leq \eps/2$.
Proof: bound the integrand by $(\eps/2)|\phi_t(y)|$ and use $\int_{|y|<\delta} |\phi_t| \leq \int |\phi_t| = \|\phi\|_1$; more precisely $\leq \eps/2 \cdot \int |\phi_t| = \eps/2 \cdot \|\phi\|_1$, so normalize $\|\phi\|_1$ into the constant.
<2>4. The outer part satisfies $\int_{|y|\geq\delta} |\phi_t(y)|\,|f(x-y) - f(x)|\,dy \leq 2\|f\|_\infty \int_{|y| \geq \delta} |\phi_t(y)|\,dy \to 0$ as $t \to 0$, uniformly in $x$.
Proof: $\int_{|y| \geq \delta} |\phi_t(y)|\,dy = \int_{|z| \geq \delta/t} |\phi(z)|\,dz \to 0$ since $\phi \in L^1$ (or $\phi$ has compact support for a standard approximation to the identity).
<2>5. Q.E.D. Proof: <2>3 and <2>4 show $|f\ast\phi_t(x) - f(x)| < \eps$ for all $x$ once $t$ is small, i.e. uniform convergence.
<1>4. Q.E.D. Proof: <1>2 gives a.e. convergence under the decay hypothesis; <1>3 gives uniform convergence for bounded uniformly continuous $f$.
:::
