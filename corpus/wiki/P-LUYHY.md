---
schema: qual/card@1
id: P-LUYHY
kind: problem
title: Young's convolution inequality
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Suppose $1\leq p,q,r \leq \infty$ with
\[
{1\over p } + {1 \over q} = 1 + {1 \over r}
.\]

Prove that
\[
f \in L^p, g\in L^q \implies f \convolve g \in L^r \text{ and } \norm{f \convolve g}_r \leq \norm{f}_p \norm{g}_q
.\]
:::
::: {.solution}
<1>1. Setup: $1 \le p, q, r \le \infty$ with $\frac{1}{p} + \frac{1}{q} = 1 + \frac{1}{r}$; $f \in L^p$, $g \in L^q$ on $\RR^n$. Claim: $f \ast g \in L^r$ with $\|f \ast g\|_r \le \|f\|_p\|g\|_q$. This is Young's convolution inequality.
    Proof: standard theorem; we prove it via the two endpoint estimates and Riesz–Thorin interpolation.

<1>2. Endpoint 1: $q = 1$, $r = p$: $\|f \ast g\|_p \le \|f\|_p\|g\|_1$.
    Proof: Minkowski's inequality for integrals: $\|f\ast g\|_p = \left(\int\left|\int f(y)g(x-y)\,dy\right|^p dx\right)^{1/p} \le \int\left(\int|f(y)g(x-y)|^p\,dx\right)^{1/p}dy = \int |g(y)|\,dy\,\|f\|_p = \|g\|_1\|f\|_p$.

<1>3. Endpoint 2: $r = \infty$, $p, q$ conjugate ($1/p + 1/q = 1$): $\|f \ast g\|_\infty \le \|f\|_p\|g\|_q$.
    Proof: Hölder: $|(f\ast g)(x)| \le \int |f(y)||g(x-y)|\,dy \le \|f\|_p\left(\int|g(x-y)|^q dy\right)^{1/q} = \|f\|_p\|g\|_q$ (translation invariance of $\|\cdot\|_q$); taking the sup over $x$ gives the bound.

<1>4. General case by interpolation.
    <2>1. Fix $f \in L^p$. The map $T: g \mapsto f \ast g$ is bounded $L^1 \to L^p$ with norm $\le \|f\|_p$ (by <1>2) and $L^{p'} \to L^\infty$ with norm $\le \|f\|_p$ (by <1>3, where $p'$ is conjugate to $p$).
        Proof: <1>2 with $f$ fixed; <1>3 with $q = p'$.
    <2>2. The given exponents satisfy $\frac{1}{q} = \frac{1-\theta}{1} + \frac{\theta}{p'}$ and $\frac{1}{r} = \frac{1-\theta}{p} + \frac{\theta}{\infty}$ for $\theta = \frac{p(r-1)}{r}$... more precisely $\theta$ solving $\frac{1}{q} = 1 - \theta + \frac{\theta}{p'}$: then $\frac{1}{r} = \frac{1-\theta}{p}$.
        Proof: from $\frac{1}{p}+\frac{1}{q} = 1 + \frac{1}{r}$ and $\frac{1}{p'} = 1 - \frac{1}{p}$: $1 - \theta + \theta(1 - 1/p) = 1 - \theta/p = 1/q$, so $\theta = p(1 - 1/q) = p(\frac{1}{p} - \frac{1}{r}) = 1 - \frac{p}{r}$; then $\frac{1-\theta}{p} = \frac{p/r}{p} = \frac{1}{r}$. Consistent.
    <2>3. Riesz–Thorin: $T$ is bounded $L^q \to L^r$ with norm $\le \|f\|_p$.
        Proof: Riesz–Thorin interpolation between the two endpoint estimates (<2>1), using the exponents in <2>2.

<1>5. Q.E.D.
    Proof: <1>4<2>3 gives $\|f\ast g\|_r \le \|f\|_p\|g\|_q$ for all $f \in L^p, g \in L^q$. (Endpoint cases $p, q \in \{1, \infty\}$ or $r = \infty$ are covered directly by <1>2 and <1>3. An elementary proof without interpolation exists via the three-function Hölder inequality.)
:::
