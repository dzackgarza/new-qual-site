---
schema: qual/card@1
id: P-IZZ3T
kind: problem
title: Riemann integrability under $|g(x)-g(y)|\le|f(x)-f(y)|$
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
---

::: problem
Suppose $f, g: [0, 1] \to \RR$ where $f$ is Riemann integrable and for $x, y\in [0, 1]$,
\[
\abs{g(x) - g(y)} \leq \abs{f(x) - f(y)}
.\]

Prove that $g$ is Riemann integrable.
:::

::: solution
Because $f$ is Riemann integrable on $[0,1]$, it is bounded. Fix $x_0\in[0,1]$.
Then
\[
|g(x)|\le |g(x_0)|+|g(x)-g(x_0)|
\le |g(x_0)|+|f(x)-f(x_0)|,
\]
so $g$ is also bounded.

For an interval $I\subset[0,1]$, let
\[
\omega_f(I)=\sup_{x,y\in I}|f(x)-f(y)|,
\qquad
\omega_g(I)=\sup_{x,y\in I}|g(x)-g(y)|.
\]
The hypothesis gives
\[
\omega_g(I)\le \omega_f(I)
\]
for every $I$.

Since $f$ is Riemann integrable, for every $\varepsilon>0$ there is a partition
$P$ of $[0,1]$ such that
\[
U(f,P)-L(f,P)
=\sum_{I\in P}\omega_f(I)|I|<\varepsilon.
\]
For the same partition,
\[
U(g,P)-L(g,P)
=\sum_{I\in P}\omega_g(I)|I|
\le\sum_{I\in P}\omega_f(I)|I|
<\varepsilon.
\]
Hence the Darboux criterion shows that $g$ is Riemann integrable.
:::
