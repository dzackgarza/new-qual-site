---
schema: qual/card@1
id: E-SS5.EX-4
kind: problem
title: "SS 5.4: Growth and zeros of a product with geometrically spaced zeros"
classification:
  areas:
  - complex-analysis
  topics: ['Entire Functions', 'Hadamard Factorization', "Jensen's Formula"]
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

::: exercise
Let $t > 0$ be given and fixed, and define $F(z)$ by
$$
F(z) = \prod_{n=1}^{\infty} (1 - e^{-2\pi n t} e^{2\pi i z}).
$$
Note that the product defines an entire function of $z$.

(a) Show that $|F(z)| \le A e^{a |z|^2}$, hence $F$ is of order 2.

(b) Show that $F$ vanishes exactly when $z = -i n t + m$ for $n \ge 1$ and $m \in \mathbb{Z}$ (integers).
Deduce that if $\{z_k\}$ is an enumeration of these zeros, we have
$$
\sum_k \frac{1}{|z_k|^2} = \infty \quad \text{but} \quad \sum_k \frac{1}{|z_k|^{2+\varepsilon}} < \infty \quad \text{for any } \varepsilon > 0.
$$
:::

::: solution
Write $q=e^{-2\pi t}\in(0,1)$. On every compact subset of $\mathbb C$, the series $\sum_{n\ge1}|q^n e^{2\pi iz}|$ converges uniformly, so
\[
F(z)=\prod_{n\ge1}(1-q^n e^{2\pi iz})
\]
defines an entire function.

Let $N=\lfloor |z|/t\rfloor+1$. For $n>N$,
\[
q^n|e^{2\pi iz}|\le e^{-2\pi nt+2\pi|z|}\le e^{-2\pi t(n-N)},
\]
so the tail product is bounded uniformly in $z$. For $1\le n\le N$,
\[
|1-q^ne^{2\pi iz}|\le1+e^{2\pi|z|}\le2e^{2\pi|z|}.
\]
Hence, for suitable $A,a>0$ depending only on $t$,
\[
|F(z)|\le A e^{a|z|^2}.
\]
Thus the order is at most $2$.

A factor vanishes exactly when
\[
q^n e^{2\pi iz}=1,
\]
i.e. exactly at
\[
z=m-int,\qquad m\in\mathbb Z,\ n\ge1.
\]
There are no other zeros because the locally uniformly convergent product is nonzero wherever no factor vanishes.

For these zeros,
\[
|m-int|^2=m^2+n^2t^2.
\]
For each $n$, at least $c_t n$ integers satisfy $|m|\le nt$, and for those terms $m^2+n^2t^2\le2n^2t^2$. Consequently
\[
\sum_{n\ge1}\sum_{m\in\mathbb Z}\frac1{m^2+n^2t^2}
\ge c\sum_{n\ge1}\frac1n=\infty.
\]
For $p=1+\varepsilon/2>1$, comparison with the corresponding integral over unit rectangles gives
\[
\sum_{n\ge1}\sum_{m\in\mathbb Z}(m^2+n^2t^2)^{-p}<\infty,
\]
since in polar coordinates the tail is bounded by a constant multiple of
\[
\int_1^\infty r^{1-2p}\,dr
=
\int_1^\infty r^{-1-\varepsilon}\,dr<\infty.
\]
Thus the exponent of convergence of the zero set is exactly $2$.

It remains to rule out order $<2$. If the order were $\rho<2$, choose $\rho<\sigma<2$. Then for large $r$, $\log M(r)=O(r^\sigma)$. Jensen's formula implies that the number $N(r)$ of zeros in $|z|\le r$ satisfies
\[
N(r/2)\log2\le \log M(r)-\log|F(0)|=O(r^\sigma).
\]
But the lattice above contains at least $c r^2$ points in $|z|\le r$ for all large $r$, a contradiction. Hence the order is exactly $2$.
:::
