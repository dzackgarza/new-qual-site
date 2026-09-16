---
schema: qual/card@1
id: P-CAF24F
kind: problem
title: 'Meromorphic function with poles in the disc and $|f-1|\le 1/|z|^2$ outside'
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be meromorphic in $\mathbb{C}$ with finitely many zeros and poles.
Write $\alpha_1,\ldots,\alpha_n$ for the zeros and poles of $f$, and let $m_1,\ldots,m_n$ be their orders.
Assume that

- the poles of $f$ are in the unit disc $\mathbb{D}$,

- $|f(z) - 1| \le \dfrac{1}{|z|^2}$ for all $|z| \ge 1$.

(i) Show that $f$ is a rational function.

(ii) Show that $\displaystyle\sum_{i=1}^{n} m_i \alpha_i = 0$.
:::

::: {.solution}
We use the standard signed order convention: $m_i>0$ at a zero and $m_i<0$
at a pole.

(i) The estimate
\[
|f(z)-1|\le |z|^{-2}
\]
for $|z|\ge1$ shows that $f$ is holomorphic near $\infty$ with
\[
f(\infty)=1.
\]
Since $f$ has only finitely many poles in $\mathbb C$, it is meromorphic on the
Riemann sphere. Every meromorphic function on the sphere is rational. Hence
$f$ is rational.

(ii) For a rational function, the logarithmic derivative records the signed
divisor:
\[
\frac{f'(z)}{f(z)}
=\sum_{i=1}^n\frac{m_i}{z-\alpha_i}.
\]
Expanding at infinity,
\[
\frac{f'(z)}{f(z)}
=\frac{\sum_i m_i}{z}
+\frac{\sum_i m_i\alpha_i}{z^2}
+O(z^{-3}).
\]
On the other hand, the hypothesis gives the Laurent expansion
\[
f(z)=1+O(z^{-2})
\]
at infinity. By Cauchy's estimates on large circles,
\[
f'(z)=O(z^{-3}),
\]
and hence
\[
\frac{f'(z)}{f(z)}=O(z^{-3}).
\]
The coefficients of both $z^{-1}$ and $z^{-2}$ in the preceding expansion
must therefore vanish. In particular,
\[
\boxed{\sum_{i=1}^n m_i\alpha_i=0.}
\]
:::
