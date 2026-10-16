---
schema: qual/card@1
id: P-K2AR1
kind: problem
title: $\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k$ when $zf(z)\to k$ in a sector
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Let $f$ be continuous on
\[
D=\{z:|z|>R,\ 0\le\arg z\le\theta\},\qquad 0\le\theta\le2\pi,
\]
and suppose $zf(z)\to k$ as $z\to\infty$ in $D$. If $L_{R'}$ is the
part of $|z|=R'$ lying in $D$, show that
\[
\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k.
\]
:::

::: {.solution}
Parametrize the arc by $z=R'e^{it}$, $0\le t\le\theta$. Then
\[
\int_{L_{R'}}f(z)\,dz
=i\int_0^\theta R'e^{it}f(R'e^{it})\,dt.
\]
The hypothesis $zf(z)\to k$ as $z\to\infty$ in the region means that the
integrand converges uniformly in $t\in[0,\theta]$ to $k$. Therefore
\[
\lim_{R'\to\infty}\int_{L_{R'}}f(z)\,dz=i\theta k.
\]
:::