---
schema: qual/card@1
id: P-CAF09C
kind: problem
title: "Evaluation of the infinite product prod(1 - 1/n^2) in two different ways"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Evaluate $\prod_{n=2}^{\infty}\left(1 - \frac{1}{n^2}\right)$ in two different ways.
:::

::: solution
First telescope directly:
\[
1-\frac1{n^2}=\frac{(n-1)(n+1)}{n^2}
=\frac{n-1}{n}\frac{n+1}{n}.
\]
Hence
\[
\prod_{n=2}^N\left(1-\frac1{n^2}\right)
=\left(\prod_{n=2}^N\frac{n-1}{n}\right)
 \left(\prod_{n=2}^N\frac{n+1}{n}\right)
=\frac1N\cdot\frac{N+1}{2}
=\frac{N+1}{2N},
\]
so the infinite product equals $1/2$.

For a second method, use Euler's product
\[
\frac{\sin\pi z}{\pi z}
=\prod_{n=1}^\infty\left(1-\frac{z^2}{n^2}\right).
\]
Remove the $n=1$ factor and let $z\to1$:
\[
\prod_{n=2}^\infty\left(1-\frac1{n^2}\right)
=\lim_{z\to1}
\frac{\sin\pi z}{\pi z(1-z^2)}.
\]
Since $\sin\pi z\sim-\pi(z-1)$ and
$1-z^2\sim-2(z-1)$, the limit is
\[
\boxed{\frac12}.
\]
:::
