---
schema: qual/card@1
id: E-IPIKC
kind: problem
title: Entire functions with $|f(z)/z^{n}|$ bounded at infinity are polynomials of
  degree at most $n$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Cauchy Estimates
  - Polynomials
  - Liouville's Theorem
relations: []
review: draft
---

::: {.exercise}
Show that if $\abs{f(z)/z^n}$ is bounded for $\abs{z}\geq R$, then $f$ is a polynomial of degree at most $n$.
What happens if this bound holds on all of $\CC$?

:::

::: {.solution}
Let $f$ be entire with $\abs{f(z)}\le M\abs z^n$ for $\abs z\ge R$.
Taylor expand at $z=0$ to get $f(z) = \sum_{j\geq 0}c_j z^j$ everywhere.
Claim: $c_{n+k} = 0$ for all $k\geq 1$.
By the formula for Taylor coefficients, it suffices to show $f^{(n+k)}(0) = 0$ for all $k\geq 1$.
Apply the Cauchy estimate on the circle of radius $\rho\geq R$:
\[
\abs{ f^{(n+k)} (0)} 
&\leq {(n+k)! \over 2\pi} \int_{\abs{\xi} = \rho} \abs{f(\xi) \over \xi^{n+k+1}}\abs{\dxi}\\
&\leq {(n+k)! \over 2\pi} \int_{\abs{\xi} = \rho} {M\abs{\xi}^n \over \abs{\xi}^{n+k+1}}\abs{\dxi}\\
&= {(n+k)! \over 2\pi} {M\over \rho^{k+1}} \cdot 2\pi \rho \\
&= (n+k)!\,M\rho^{-k} \convergesto{\rho\to\infty} 0
.\]
So $f$ is a polynomial of degree at most $n$.

If the bound holds on all of $\CC\setminus\theset0$, then $h(z) \da f(z)/z^n$ is bounded near $0$, so its singularity at $0$ is removable, and $h$ is a bounded entire function. By Liouville $h$ is constant, and $f(z) = cz^n$.
:::

