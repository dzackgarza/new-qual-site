---
schema: qual/card@1
id: E-SS3.EX-14
kind: problem
title: "SS 3.14: Injective entire functions are affine"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
14. Prove that all entire functions that are also injective take the form $f ( z ) = a z + b$ with $a , b \in \mathbb { C }$ , and $a \neq 0$

[Hint: Apply the Casorati-Weierstrass theorem to $f ( 1 / z ) . ]$
:::

::: solution
Let $f$ be entire and injective, and define $g(z)=f(1/z)$ on a punctured neighborhood of $0$.

The singularity of $g$ at $0$ cannot be removable: otherwise $f(z)$ would have a finite limit as $z\to\infty$, hence would be bounded outside a large disc and therefore bounded on all of $\mathbb C$; Liouville would make $f$ constant, contradicting injectivity.

It also cannot be essential. By Casorati-Weierstrass, if $0$ were an essential singularity of $g$, then for any $w\in\mathbb C$ and every punctured neighborhood of $0$, the values of $g$ would come arbitrarily close to $w$. Choose $z_0\ne0$ and set $w=f(z_0)$. Then there exists a sequence $\zeta_n\to0$, with $\zeta_n\ne 1/z_0$, such that
\[
f(1/\zeta_n)=g(\zeta_n)\to f(z_0).
\]
Because $f$ is injective and entire, the inverse function theorem applies at $z_0$ once we note $f'(z_0)\ne0$ (otherwise the local power-series expansion would have multiplicity at least $2$, contradicting local injectivity). Hence $f$ is locally one-to-one with a continuous local inverse near $f(z_0)$, forcing $1/\zeta_n\to z_0$, impossible since $|1/\zeta_n|\to\infty$.

Therefore $g$ has a pole at $0$. Equivalently, $f$ has a pole at infinity, so $f$ is a polynomial. An injective polynomial must have degree $1$: if $\deg f=d\ge2$, then $f'$ has degree $d-1$ and hence has a zero, contradicting injectivity as above. Thus
\[
f(z)=az+b,
\qquad a\ne0.
\]
:::
