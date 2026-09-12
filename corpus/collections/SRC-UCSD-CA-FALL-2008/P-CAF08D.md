---
schema: qual/card@1
id: P-CAF08D
kind: problem
title: "Analytic continuation and maximum principle for power series with nonnegative coefficients"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f(z) = \sum_{n=0}^{\infty} a_n z^n$, $a_n \geq 0$ for all $n$, where the series is absolutely convergent for $|z| < 1$.

(a) For any $r$, $0 \leq r < 1$, any $\theta \in \mathbb{R}$, and any nonnegative integer $k$, prove that $|f^{(k)}(re^{i\theta})| \leq |f^{(k)}(r)|$.

(b) If $f(z)$ extends analytically to $B(1 - \delta; 2\delta)$ for some $\delta$, $0 < \delta < 1$, prove that $f(z)$ extends analytically to $B((1-\delta)e^{i\theta}; 2\delta)$ for any $\theta \in \mathbb{R}$.

(c) Prove that if $f(z)$ extends analytically to an open neighborhood of $z = 1$, then the radius of convergence of the series $\sum_{n=0}^{\infty} a_n z^n$ is strictly greater than 1.
:::

::: solution
For every $k\ge0$ and $|z|<1$,
\[
f^{(k)}(z)=\sum_{n=k}^\infty \frac{n!}{(n-k)!}a_n z^{n-k}.
\]
Since all coefficients are nonnegative, for $0\le r<1$,
\[
|f^{(k)}(re^{i\theta})|
\le \sum_{n=k}^\infty \frac{n!}{(n-k)!}a_n r^{n-k}
=f^{(k)}(r).
\]
This proves (a).

For (b), fix $\theta$ and put
\[
z_\theta=(1-\delta)e^{i\theta}.
\]
The given continuation to $B(1-\delta,2\delta)$ implies that the Taylor series of
$f$ about $1-\delta$ has radius at least $2\delta$. Hence
\[
\limsup_{k\to\infty}
\left(\frac{|f^{(k)}(1-\delta)|}{k!}\right)^{1/k}
\le \frac1{2\delta}.
\]
By part (a),
\[
|f^{(k)}(z_\theta)|\le f^{(k)}(1-\delta),
\]
so the Taylor series of $f$ about $z_\theta$ also has radius at least
$2\delta$. It therefore gives an analytic continuation to
$B(z_\theta,2\delta)$.

For (c), choose $\delta>0$ so small that $f$ is analytic on
$B(1-\delta,2\delta)$. By (b), $f$ analytically continues to
\[
\bigcup_{\theta\in\mathbb R}
B((1-\delta)e^{i\theta},2\delta).
\]
Together with the original unit disk, this union contains the larger disk
$|z|<1+\delta$: indeed, if $1\le |z|<1+\delta$, choose
$\theta=\arg z$; then
\[
|z-(1-\delta)e^{i\theta}|=|z|-(1-\delta)<2\delta.
\]
Thus the germ at $0$ represented by the original power series extends
holomorphically to $|z|<1+\delta$. Consequently its radius of convergence is
at least $1+\delta>1$.
:::
