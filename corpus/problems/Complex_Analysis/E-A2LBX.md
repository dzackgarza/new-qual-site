---
schema: qual/card@1
id: E-A2LBX
kind: problem
title: '$f: D\rightarrow {\mathbb C}$ be a continuous function, where'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
a. $f: D\rightarrow {\mathbb C}$ be a continuous function, where $D\subset {\mathbb C}$ is a domain.Let $\alpha:[a,b]\rightarrow D$ be a smooth curve.
Give a precise definition of the *complex line integral* $$\int_{\alpha} f.$$

b. Assume that there exists a constant $M$ such that $|f(\tau)|\leq M$ for all $\tau\in \mbox{\textrm Image}(\alpha$). Prove that $$\big | \int_{\alpha} f \big |\leq M \times \mbox{\textrm length}(\alpha).$$

c. Let $C_R$ be the circle $|z|=R$, described in the counterclockwise direction, where $R>1$.
Using the parametrization $z=Re^{it}$ for $0\le t\le2\pi$ and the pathwise determination $\log(Re^{it})=\log R+it$, provide an upper bound for $\big | \int_{C_R} \dfrac{\log{(z)} }{z^2} \big |$ depending only on $R$ and universal constants.
:::

::: solution
<1>1. If $\alpha:[a,b]\to D$ is piecewise $C^1$, define
\[
\int_\alpha f(z)\,dz
:=\int_a^b f(\alpha(t))\alpha'(t)\,dt,
\]
where the right-hand side is the usual integral of a complex-valued function of a real variable.

<1>2. If $|f(\alpha(t))|\le M$ for all $t$, then
\[
\left|\int_\alpha f(z)\,dz\right|
\le\int_a^b|f(\alpha(t))|\,|\alpha'(t)|\,dt
\le M\int_a^b|\alpha'(t)|\,dt.
\]
Thus
\[
\left|\int_\alpha f(z)\,dz\right|
\le M\,\operatorname{length}(\alpha).
\]

<1>3. For part (c), a global continuous branch of $\log z$ does not exist on the circle $C_R$ because it winds once around $0$. Interpret the integral along the standard parametrization
\[
\alpha(t)=Re^{it},\qquad0\le t\le2\pi,
\]
using the pathwise determination
\[
\log(\alpha(t))=\log R+it.
\]
Then
\[
|\log(\alpha(t))|
\le\log R+2\pi
\]
and
\[
\left|\frac{\log(\alpha(t))}{\alpha(t)^2}\right|
\le\frac{\log R+2\pi}{R^2}.
\]
Since $\operatorname{length}(C_R)=2\pi R$, the estimate from <1>2 gives
\[
\left|\int_{C_R}\frac{\log z}{z^2}\,dz\right|
\le\frac{2\pi(\log R+2\pi)}{R}
\]
for this specified determination of the logarithm along the path.
:::
