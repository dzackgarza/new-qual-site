---
schema: qual/card@1
id: P-HHPDB
kind: problem
title: Uniform convergence $f*\phi_t\to f$ as $t\to 0$ for bounded uniformly continuous $f$ when $\int\phi=1$
classification:
  areas:
  - real-analysis
  topics:
  - approximations-to-the-identity
  - convolution
  - uniform-convergence
relations: []
review: draft
solved: true
---

::: problem
Let $\phi\in L^1(\RR^n)$ such that $\int \phi = 1$ and define $\phi_t(x) = t^{-n}\phi(t\inv x)$.
Show that if $f$ is bounded and uniformly continuous then $f\ast \phi_t \converges{t\to 0}\to f$ uniformly.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Since $\int \phi = 1$ and $\phi_t(x) = t^{-n}\phi(x/t)$, we have $\int \phi_t = 1$ for all $t$.
Proof: substitute $y = x/t$: $\int t^{-n}\phi(x/t)\,dx = \int \phi(y)\,dy = 1$.

<1>2. Pointwise identity: $$(f \ast \phi_t)(x) - f(x) = \int \phi_t(y)\,(f(x-y) - f(x))\,dy = \int \phi(y)\,(f(x - ty) - f(x))\,dy.$$ Proof: $f \ast \phi_t = \int f(x-y)\phi_t(y)\,dy$; subtract $f(x)\int\phi_t = f(x)$ (by <1>1); the second equality is the change of variables $y \mapsto ty$.

<1>3. Given $\eps > 0$: <2>1. Choose $R$ with $\int_{|z| > R}|\phi(z)|\,dz < \dfrac{\eps}{4\|f\|_\infty}$ (possible since $\phi \in L^1$; take $\|f\|_\infty = 0$ as trivial).
Proof: dominated convergence / definition of the $L^1$ integral.
<2>2. By uniform continuity of $f$, choose $\eta > 0$ with $|u - v| < \eta \Rightarrow |f(u) - f(v)| < \dfrac{\eps}{2\|\phi\|_1}$.
Proof: hypothesis on $f$.

<1>4. For $t < \eta/R$ and every $x$: $|(f \ast \phi_t)(x) - f(x)| < \eps$.
<2>1. Split: $|(f\ast\phi_t)(x) - f(x)| \le \int_{|y| \le R/t}|\phi_t(y)|\,|f(x-y) - f(x)|\,dy + \int_{|y| > R/t}|\phi_t(y)|\,|f(x-y) - f(x)|\,dy$.
Proof: triangle inequality applied to <1>2. <2>2. First term: $\le \dfrac{\eps}{2\|\phi\|_1}\int_{|y| \le R/t}|\phi_t(y)|\,dy \le \dfrac{\eps}{2}$.
Proof: for $|y| \le R/t < \eta$ (since $t < \eta/R$), uniform continuity (<1>3<2>2) bounds $|f(x-y) - f(x)|$; and $\int |\phi_t| = \|\phi\|_1$.
<2>3. Second term: $\le 2\|f\|_\infty \int_{|y| > R/t}|\phi_t(y)|\,dy = 2\|f\|_\infty \int_{|z| > R}|\phi(z)|\,dz < \dfrac{\eps}{2}$.
Proof: $|f(x-y) - f(x)| \le 2\|f\|_\infty$; change variables $z = ty$; the bound is <1>3<2>1. <2>4. Q.E.D. Proof: <2>1, <2>2, <2>3 give $|(f\ast\phi_t)(x) - f(x)| < \eps$ for all $x$, i.e. $\|f\ast\phi_t - f\|_\infty < \eps$.

<1>5. Q.E.D. Proof: <1>4 shows $f \ast \phi_t \to f$ uniformly as $t \to 0$.
(Only boundedness and uniform continuity of $f$ are used.)
:::
