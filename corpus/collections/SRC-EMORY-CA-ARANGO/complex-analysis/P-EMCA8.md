---
schema: qual/card@1
id: P-EMCA8
kind: problem
title: "Uniform convergence of holomorphic functions preserves holomorphicity"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $(f_n)$ be a sequence of holomorphic functions in a domain $D$.
Suppose that $f_n \to f$ uniformly on each compact subset of $D$.
Show that

(a) $f$ is holomorphic on $D$.

(b) $f_n' \to f'$ uniformly on each compact subset of $D$.
:::

::: solution
Fix a closed triangle $T\subset D$. Since $f_n\to f$ uniformly on the compact
set $\partial T$,
\[
\int_{\partial T}f(z)\,dz
=\lim_{n\to\infty}\int_{\partial T}f_n(z)\,dz=0.
\]
The locally uniform limit $f$ is continuous, so Morera's theorem implies that
$f$ is holomorphic on $D$.

Now let $K\subset D$ be compact. Choose $r>0$ so that the closed
$r$-neighborhood
\[
K_r=\{z\in D:\operatorname{dist}(z,K)\le r\}
\]
is compact and contained in $D$. For every $z\in K$, Cauchy's formula for the
derivative on the circle $|\zeta-z|=r$ gives
\[
f_n'(z)-f'(z)
=\frac{1}{2\pi i}\int_{|\zeta-z|=r}
\frac{f_n(\zeta)-f(\zeta)}{(\zeta-z)^2}\,d\zeta.
\]
Hence
\[
|f_n'(z)-f'(z)|
\le \frac1r\sup_{\zeta\in K_r}|f_n(\zeta)-f(\zeta)|.
\]
The right-hand side tends to $0$ independently of $z\in K$. Therefore
$f_n'\to f'$ uniformly on $K$. Since $K$ was arbitrary, the convergence is
uniform on every compact subset of $D$.
:::
