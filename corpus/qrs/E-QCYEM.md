---
schema: qual/card@1
id: E-QCYEM
kind: exercise
title: $\|f\ast\phi_t-f\|_1\to 0$ as $t\to 0$ for an approximate identity $\phi$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
---

::: exercise
- Show that if $\phi$ is an approximate identity, then $$\norm{f\ast \phi_t - f}_1 \converges{t\to 0}\to 0.$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Rewrite the difference: $f \ast \phi_t(x) - f(x) = \int \phi(y)\big(f(x - ty) - f(x)\big)\,dy$.
Proof: substitute $u = ty$ in $f \ast \phi_t(x) = \int f(x - ty)\phi(y)\,dy$, and use $\int \phi = 1$ to write $f(x) = f(x)\int\phi(y)\,dy$.

<1>2. $\|f \ast \phi_t - f\|_1 \le \int |\phi(y)|\,\|\tau_{-ty}f - f\|_1\,dy$.
Proof: take $L^1$ norms in $x$ in <1>1 and use Minkowski's inequality for integrals: the $L^1$ norm of the integral is at most the integral of the $L^1$ norms.

<1>3. For each fixed $y$, $\|\tau_{-ty}f - f\|_1 \to 0$ as $t \to 0$.
Proof: strong continuity of translation in $L^1(\RR^n)$.

<1>4. Given $\eps > 0$, the integral in <1>2 is $< \eps$ for all sufficiently small $t$.
<2>1. Choose $M$ with $2\|f\|_1\int_{|y| > M}|\phi(y)|\,dy < \eps/2$.
Proof: $\phi \in L^1$, so the tail integral tends to $0$ as $M \to \infty$; also $\|\tau_{-ty}f - f\|_1 \le 2\|f\|_1$.
<2>2. $\sup_{|y| \le M}\|\tau_{-ty}f - f\|_1 \to 0$ as $t \to 0$.
Proof: the translates $\{-ty : |y| \le M\}$ lie in the ball of radius $tM$ about $0$, and $\|\tau_h f - f\|_1 \to 0$ as $h \to 0$ by <1>3. <2>3. For small $t$, $\int_{|y| \le M}|\phi(y)|\,\|\tau_{-ty}f - f\|_1\,dy \le \|\phi\|_1 \sup_{|y|\le M}\|\tau_{-ty}f - f\|_1 < \eps/2$.
Proof: <2>2 and $\phi \in L^1$.
<2>4. Q.E.D. Proof: <2>1 bounds the tail by $\eps/2$ and <2>3 bounds the main part by $\eps/2$, so the whole integral in <1>2 is $< \eps$.

<1>5. Q.E.D. Proof: <1>2 and <1>4 give $\|f \ast \phi_t - f\|_1 \to 0$ as $t \to 0$.
:::
