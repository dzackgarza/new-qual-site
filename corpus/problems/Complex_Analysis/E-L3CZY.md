---
schema: qual/card@1
id: E-L3CZY
kind: problem
title: Compactly convergent series of holomorphic functions are holomorphic
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
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

::: {.exercise}
Show that if each $f_n$ is holomorphic on an open set $\Omega \subseteq \mathbb{C}$ and $F \coloneqq \sum_{n=1}^\infty f_n$ converges uniformly on every compact subset of $\Omega$, then $F$ is holomorphic on $\Omega$.
:::

::: solution
Let
\[
S_N=\sum_{n=1}^N f_n.
\]
Each $S_N$ is holomorphic on $\Omega$.

<1>1. The limit $F$ is continuous. For every $z_0\in\Omega$, choose $r>0$ with
\[
\overline{D_r(z_0)}\subset\Omega.
\]
The convergence $S_N\to F$ is uniform on this compact disk, so $F$ is a uniform limit of continuous functions there and is therefore continuous near $z_0$.

<1>2. Let $T$ be any closed triangle contained in $\Omega$. Since each $S_N$ is holomorphic on a neighborhood of $T$, Cauchy's theorem gives
\[
\int_{\partial T}S_N(z)\,dz=0.
\]
The boundary $\partial T$ is compact, so $S_N\to F$ uniformly on $\partial T$. Hence
\[
\int_{\partial T}F(z)\,dz
=\lim_{N\to\infty}\int_{\partial T}S_N(z)\,dz
=0.
\]

<1>3. Morera's theorem now implies that $F$ is holomorphic on $\Omega$.

<1>4. Moreover, once holomorphy is known, Cauchy's integral formula on nested compact disks shows that for every $k\ge1$,
\[
F^{(k)}=\sum_{n=1}^\infty f_n^{(k)}
\]
with locally uniform convergence of the derivative series.
:::
