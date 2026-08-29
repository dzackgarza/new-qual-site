---
schema: qual/card@1
id: E-GQEMZ
kind: exercise
title: $\partial_i(f\ast g)=f\ast\partial_i g$ for $f\in L^1$
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- $f\in L^1$ and $g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

- Show that if $f\in L^1$ and $g'$ exists with $\dd{g}{x_i}$ all bounded, then $$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$$
:::

::: {.solution}
**Goal:** If $f \in L^1(\RR^n)$ and $g$ is differentiable with bounded partial derivatives $\dd{g}{x_i}$, show $\dd{}{x_i}(f \ast g) = f \ast \dd{g}{x_i}$; in particular $f \ast g$ is smooth when $g$ is smooth and compactly supported.

<1>1. $f \ast g$ is differentiable in $x_i$, with $\dd{}{x_i}(f\ast g)(x) = (f \ast \dd{g}{x_i})(x)$.
<2>1. Write the difference quotient: $\frac{(f\ast g)(x + h e_i) - (f\ast g)(x)}{h} = \int f(x-y)\, \frac{g(y + h e_i) - g(y)}{h}\,dy$.
Proof: change variables $y \mapsto y + h e_i$ in the first term, then rearrange.
<2>2. The integrands converge pointwise to $f(x-y)\,\dd{g}{y_i}(y)$ and are dominated by $|f(x-y)| \sup_z |\dd{g}{z_i}(z)|$, which is integrable in $y$.
Proof: $g$ is differentiable with bounded partial derivative, so $\frac{g(y+he_i) - g(y)}{h} \to \dd{g}{y_i}(y)$ (a.e. — indeed everywhere, by differentiability) and $|\frac{g(y+he_i)-g(y)}{h}| \leq \sup |\dd{g}{\cdot_i}|$ by the mean value theorem; $f \in L^1$ gives integrability.
<2>3. Q.E.D. Proof: dominated convergence in <2>2 lets the limit $h \to 0$ pass under the integral in <2>1, giving the claimed identity.
<1>2. If $g$ is smooth and compactly supported, then $f \ast g$ is smooth.
Proof: every partial derivative $D^\alpha g$ of a smooth compactly supported $g$ is bounded, so <1>1 applies iteratively: $D^\alpha(f\ast g) = f \ast D^\alpha g$ for every multi-index $\alpha$, and the right side is defined (an $L^1$ function convolved with a bounded measurable function).
Hence all derivatives of all orders exist.
<1>3. Q.E.D. Proof: <1>1 proves the differentiation formula; <1>2 proves smoothness of $f\ast g$ under the smooth-compactly-supported hypothesis.
:::
