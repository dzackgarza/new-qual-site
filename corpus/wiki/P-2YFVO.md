---
schema: qual/card@1
id: P-2YFVO
kind: problem
title: "Show that if $f, g$ are continuous and compactly supported, then\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - uniform-continuity
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
- Show that if $f, g$ are continuous and compactly supported, then so is $f\ast g$.

- Show that if $f\in L^1$ and $g$ is bounded, then  $f\ast g$ is bounded and uniformly continuous.

- If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

- Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

  - $f, g\in L^1$ are both bounded.

  - $f, g\in L^1$ with just $g$ bounded.

  - $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

  - $f\in L^1$ and $g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)

- Show that if $f\in L^1$ and $g'$ exists with $\dd{g}{x_i}$ all bounded, then $$\dd{}{x_i}(f\ast g) = f \ast \dd{g}{x_i}$$
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. If $f, g$ are continuous and compactly supported, then so is $f \ast g$.
<2>1. $f \ast g$ is continuous: $|f\ast g(x + h) - f\ast g(x)| \le \|g\|_1 \sup_z|f(z + h) - f(z)| \to 0$.
Proof: $f$ is uniformly continuous (continuous with compact support); triangle inequality on the defining integral.
<2>2. $f \ast g$ is compactly supported: $\supp(f\ast g) \subseteq \overline{\supp f + \supp g}$, compact.
Proof: if $x \notin \overline{\supp f + \supp g}$, then $f(x - y) = 0$ for all $y \in \supp g$; and $\supp f + \supp g$ is compact (continuous image of $\supp f \times \supp g$).

<1>2. If $f \in L^1$ and $g$ is bounded, then $f \ast g$ is bounded and uniformly continuous.
<2>1. $|f \ast g(x)| \le \|g\|_\infty\|f\|_1$ for all $x$.
Proof: $|f\ast g(x)| \le \int |f(x-y)||g(y)|\,dy \le \|g\|_\infty\|f\|_1$.
<2>2. $|f \ast g(x + h) - f \ast g(x)| \le \|g\|_\infty\int|f(u + h) - f(u)|\,du \to 0$ as $h \to 0$, uniformly in $x$.
Proof: substitute $u = x - y$; the integral is $\|\tau_h f - f\|_1 \to 0$ (strong continuity of translation in $L^1$).

<1>3. If $f, g$ are compactly supported, then $f \ast g$ is compactly supported — yes.
Proof: <1>2 of <1>1 applies without any continuity hypothesis: $\supp(f\ast g) \subseteq \overline{\supp f + \supp g}$, compact.

<1>4. Vanishing at infinity under each of the four assumptions.
<2>1. $f, g \in L^1$ both bounded: $|f\ast g(x)| \le \|g\|_\infty\int_{|x-y| \ge |x|/2}|f| + \|f\|_\infty\int_{|y| > |x|/2}|g| \to 0$.
Proof: split the defining integral at $|y| = |x|/2$; both $L^1$ tails tend to $0$.
<2>2. $f, g \in L^1$ with only $g$ bounded: approximate $f$ by bounded truncations $f_M = f\chi_{|f|\le M}$; $\|(f - f_M)\ast g\|_\infty \le \|f - f_M\|_1\|g\|_\infty \to 0$, and $f_M \ast g$ vanishes at infinity by <2>1. Proof: $\eps/2 + \eps/2$ with $M$ large then $|x|$ large.
<2>3. $f, g$ smooth and compactly supported: $f \ast g$ is smooth and compactly supported (by <1>1), hence vanishes at infinity.
Proof: smoothness by differentiation under the integral; compact support by <1>1. <2>4. $f \in L^1$, $g$ smooth and compactly supported: $f \ast g$ is smooth and vanishes at infinity.
Proof: smoothness by differentiation under the integral ($D^\alpha g$ bounded).
For vanishing: let $R$ bound $|y|$ on $\supp g$; for $|x| \ge 2R$ the integration range $\{y : |x - y| \le R\}$ satisfies $|y| \ge |x| - R \ge |x|/2$, so $|f\ast g(x)| \le \|g\|_\infty\int_{|x-y| \le R}|f(x-y)|\,dy = \|g\|_\infty\int_{|u| \ge |x|/2}|f(u)|\,du \to 0$ as $|x| \to \infty$ (the $L^1$ tail of $f$).

<1>5. If $f \in L^1$ and $g$ is differentiable with bounded partial derivatives $\dd{g}{x_i}$, then $\dd{}{x_i}(f \ast g) = f \ast \dd{g}{x_i}$.
Proof: difference quotient under the integral; the quotient of $g$ is bounded by $\sup|\dd{g}{\cdot_i}|$ (mean value theorem) and converges pointwise, so dominated convergence applies with $|f| \in L^1$.
:::
