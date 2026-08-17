---
schema: qual/card@1
id: P-6BKXI
kind: problem
title: Convolution with an approximate identity converges in $L^1$, almost everywhere, and uniformly
classification:
  areas:
  - real-analysis
  topics:
  - approximations-to-the-identity
  - convolution
  - l1
relations: []
review: draft
solved: true
---

::: problem
- Show that if $\phi$ is an approximate identity, then $$\norm{f\ast \phi_t - f}_1 \converges{t\to 0}\to 0.$$

  - Show that if additionally $\abs{\phi(x)} \leq c(1 + \abs{x})^{-n-\eps}$ for some $c,\eps>0$, then this converges is almost everywhere.

- Show that is $f$ is bounded and uniformly continuous and $\phi_t$ is an approximation to the identity, then $f\ast \phi_t$ uniformly converges to $f$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $\|f \ast \phi_t - f\|_1 \to 0$ as $t \to 0$ for $f \in L^1$ and $\phi$ an approximate identity.
Proof: standard — rewrite $f\ast\phi_t(x) - f(x) = \int\phi(y)(f(x - ty) - f(x))\,dy$ using $\int\phi = 1$; then $\|f\ast\phi_t - f\|_1 \le \int|\phi(y)|\|\tau_{-ty}f - f\|_1\,dy \to 0$ by strong continuity of translation in $L^1$ (split into $|y| \le M$ and the $L^1$ tail of $\phi$).

<1>2. If additionally $|\phi(x)| \le c(1 + |x|)^{-n-\eps}$ for some $c, \eps > 0$, then $f \ast \phi_t \to f$ a.e. as $t \to 0$.
<2>1. The decay condition gives a maximal-function bound: $|f \ast \phi_t(x)| \le C (Mf)(x)$ for all $t > 0$, where $Mf$ is the Hardy–Littlewood maximal function.
Proof: $|\phi(y)| \le c(1+|y|)^{-n-\eps} \le c(1+|y|)^{-n}$ and $c(1+|y|)^{-n}$ is a radial decreasing integrable majorant of $|\phi|$; the standard maximal theorem says convolution with such a majorant is controlled by $CMf$ (a simple layer-cake / dyadic-annulus argument).
<2>2. $Mf$ is finite a.e. for $f \in L^1$, and the maximal inequality $\mu\{Mf > \lambda\} \le \frac{C}{\lambda}\|f\|_1$ holds.
Proof: Hardy–Littlewood maximal theorem.
<2>3. A.e. convergence: it is enough to show $\limsup_{t\to 0}|f\ast\phi_t(x) - f(x)| = 0$ a.e.; by the density argument it suffices to prove convergence on the dense class $C_c$, where it holds everywhere (by <1>3-type uniform convergence and the maximal bound to control the error).
Proof: standard argument: for $\delta > 0$ choose $g \in C_c$ with $\|f - g\|_1 < \delta$; then $\limsup_t|f\ast\phi_t - f| \le \limsup_t|(f-g)\ast\phi_t| + |f - g| \le C(M(f-g) + |f - g|)$ (using <2>1), and $\mu\{C(M(f-g) + |f-g|) > \eps\}$ is $O(\|f - g\|_1/\eps)$ by <2>2; letting $\delta \to 0$ over a countable sequence gives a.e. convergence.
<2>4. Q.E.D. Proof: <2>1–<2>3.

<1>3. If $f$ is bounded and uniformly continuous and $\phi_t$ is an approximation to the identity, then $f \ast \phi_t \to f$ uniformly.
<2>1. $|f \ast \phi_t(x) - f(x)| \le \int |\phi(y)|\,|f(x - ty) - f(x)|\,dy$.
Proof: same rewriting as <1>1, using $\int\phi = 1$.
<2>2. Given $\eps > 0$: split the integral at $|y| \le M$ and $|y| > M$; the tail contributes $\le 2\|f\|_\infty\int_{|y|>M}|\phi| < \eps/2$ for $M$ large, and the main part $\le \|\phi\|_1 \sup_{|u| \le tM}|f(x - u) - f(x)| < \eps/2$ for $t$ small by uniform continuity.
Proof: $\phi \in L^1$ (tail); $f$ uniformly continuous (main part).
<2>3. Q.E.D. Proof: <2>2 shows $\sup_x|f\ast\phi_t(x) - f(x)| < \eps$ for all small $t$.
:::
