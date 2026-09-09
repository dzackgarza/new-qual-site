---
schema: qual/card@1
id: P-G2RYI
kind: problem
title: Weierstrass theorem on locally uniform limits of holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
  - Holomorphic Functions
  - Morera
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
Let $\Omega \subseteq \mathbb{C}$ be an open domain, and let $\{f_n\}$ be a sequence of holomorphic functions on $\Omega$ that converges uniformly to a function $f$ on every compact subset $K \subset \Omega$.
Prove that:
(1) The limit function $f$ is holomorphic on $\Omega$.
(2) The sequence of derivatives $\{f_n'\}$ converges uniformly to $f'$ on every compact subset $K \subset \Omega$ (Weierstrass Convergence Theorem).
:::

::: solution
<1>1. The limit $f$ is holomorphic. Fix a closed triangle $T\subset\Omega$. Since $T$ is compact, $f_n\to f$ uniformly on $T$, and therefore $f$ is continuous there. Moreover,
\[
\int_{\partial T}f(z)\,dz
=\lim_{n\to\infty}\int_{\partial T}f_n(z)\,dz
=0,
\]
because every $f_n$ is holomorphic on a neighborhood of $T$. Since this holds for every such triangle, Morera's theorem gives that $f$ is holomorphic on $\Omega$.

<1>2. Let $K\subset\Omega$ be compact. Choose $r>0$ such that the closed $r$-neighborhood
\[
K_r=\{z:\operatorname{dist}(z,K)\le r\}
\]
is contained in $\Omega$. Then $K_r$ is compact.

<1>3. For every $z\in K$, Cauchy's derivative formula on $|\zeta-z|=r$ gives
\[
f_n'(z)-f'(z)
=\frac1{2\pi i}\int_{|\zeta-z|=r}
\frac{f_n(\zeta)-f(\zeta)}{(\zeta-z)^2}\,d\zeta.
\]
Hence
\[
|f_n'(z)-f'(z)|
\le\frac1r\sup_{\zeta\in K_r}|f_n(\zeta)-f(\zeta)|.
\]
Taking the supremum over $z\in K$ yields
\[
\sup_K|f_n'-f'|
\le\frac1r\sup_{K_r}|f_n-f|\longrightarrow0.
\]
Thus $f_n'\to f'$ uniformly on every compact subset of $\Omega$.
:::
