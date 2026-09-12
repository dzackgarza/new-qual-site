---
schema: qual/card@1
id: P-HCAX26
kind: problem
title: Define the Riemann zeta function
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
---

::: problem
Define the Riemann zeta function, including its analytic continuation.
:::

::: solution
For $\operatorname{Re}s>1$, the Riemann zeta function is defined by the absolutely convergent Dirichlet series
\[
\zeta(s)=\sum_{n=1}^{\infty}\frac1{n^s}.
\]
In this half-plane it also has the Euler product
\[
\zeta(s)=\prod_p\frac1{1-p^{-s}}.
\]

The function has a unique meromorphic continuation to all of $\mathbb C$. This continuation is holomorphic on
\[
\mathbb C\setminus\{1\}
\]
and has a simple pole at $s=1$ with residue $1$.

One standard continuation starts from the Mellin-transform identity, valid for $\operatorname{Re}s>1$,
\[
\Gamma(s)\zeta(s)
=\int_0^\infty \frac{t^{s-1}}{e^t-1}\,dt.
\]
Near $t=0$ one has
\[
\frac1{e^t-1}=\frac1t-\frac12+\frac{t}{12}-\cdots.
\]
Split the integral at $1$ and subtract finitely many terms of this expansion on $(0,1)$. The subtracted terms integrate explicitly to rational functions of $s$, while the remainder converges on a larger left half-plane. Repeating this procedure extends $\Gamma(s)\zeta(s)$ meromorphically across the plane, and division by $\Gamma(s)$ gives the meromorphic continuation of $\zeta$.

Equivalently, the completed zeta function
\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac s2\right)\zeta(s)
\]
extends to an entire function and satisfies
\[
\xi(s)=\xi(1-s).
\]
These properties determine the usual analytic continuation of the original Dirichlet series.
:::
