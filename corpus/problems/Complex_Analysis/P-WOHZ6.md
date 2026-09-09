---
schema: qual/card@1
id: P-WOHZ6
kind: problem
title: Uniform convergence of $\sum\sin(nz)/2^n$ on $\{\Im z<\ln 2\}$ and on $|z|\le
  r$
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Convergence Tests
  - Series of Functions
  - Trigonometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Consider the series of complex functions:
$$
\sum_{n=1}^\infty \frac{\sin(nz)}{2^n}.
$$
(a) Determine whether the series converges uniformly on the half-plane $\{ z \in \mathbb{C} \mid \operatorname{Im}(z) < \ln 2 \}$, or clarify the correct domain of uniform convergence (such as $\{ \operatorname{Im}(z) \ge -c \}$ or compact subsets $\{ |\operatorname{Im}(z)| \le Y \}$ / disks $\{ |z| \le r \}$).
(b) Prove that for every $r$ with $0<r<\ln 2$, the series converges **uniformly on the closed disk** $\{ z \in \mathbb{C} \mid |z| \le r \}$.
:::

::: solution
Write $z=x+iy$. Since
\[
\sin(nz)=\frac{e^{inz}-e^{-inz}}{2i},
\]
we have
\[
|\sin(nz)|\le \frac{e^{-ny}+e^{ny}}2\le e^{n|y|}.
\]
Hence
\[
\left|\frac{\sin(nz)}{2^n}\right|
\le \left(\frac{e^{|\Im z|}}2\right)^n.
\]

Therefore, on every closed substrip
\[
|\Im z|\le Y<\log2,
\]
the series converges uniformly by the Weierstrass $M$-test, with majorant $(e^Y/2)^n$.

Conversely, if $|\Im z|>\log2$, then one of the two exponentials in $\sin(nz)$ dominates and
\[
\frac{|\sin(nz)|}{2^n}\not\longrightarrow0.
\]
For example, at $z=-iy$ with $y>\log2$,
\[
\frac{|\sin(nz)|}{2^n}=rac{\sinh(ny)}{2^n}\sim\frac12\left(\frac{e^y}{2}\right)^n.
\]
Thus the pointwise convergence region is exactly
\[
|\Im z|<\log2.
\]
In particular, the series is not uniformly convergent on the half-plane $\Im z<\log2$, since that half-plane contains points with imaginary part below $-\log2$ where the series diverges.

Finally, if $0<r<\log2$ and $|z|\le r$, then $|\Im z|\le r$, so
\[
\left|\frac{\sin(nz)}{2^n}\right|
\le\left(\frac{e^r}{2}\right)^n,
\]
and the $M$-test gives uniform convergence on the closed disk $|z|\le r$.
:::
