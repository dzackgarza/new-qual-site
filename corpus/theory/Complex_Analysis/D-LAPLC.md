---
schema: qual/card@1
id: D-LAPLC
kind: definition
title: Laplace transform
classification:
  areas:
  - complex-analysis
  topics:
  - Transforms
  - Special Functions
relations: []
review: draft
---

::: {.definition}
For a function $f\colon[0,\infty)\to\CC$ and $p\in\CC$, the \dfn{Laplace transform} of $f$ is
$$
\mcl(f)(p)\coloneqq\int_0^\infty e^{-pt}f(t)\dt,
$$
whenever the integral converges absolutely; it then converges, and defines a holomorphic function of $p$, on a half-plane $\Re p>\sigma$.

For $\Re p$ large enough, the entries for $1$, $t^n$, $e^{\lambda t}$, $t^ne^{\lambda t}$, $\sin\omega t$, $\cos\omega t$, $\sinh\lambda t$, $\cosh\lambda t$, $e^{\lambda t}\sin\omega t$ and $e^{\lambda t}\cos\omega t$ are:
$$
\begin{array}{c|c}
f(t) & \mcl(f)(p)\\\hline
1 & \dfrac1p\\
t^n & \dfrac{n!}{p^{n+1}}\\
e^{\lambda t} & \dfrac1{p-\lambda}\\
t^ne^{\lambda t} & \dfrac{n!}{(p-\lambda)^{n+1}}\\
\sin\omega t & \dfrac{\omega}{p^2+\omega^2}\\
\cos\omega t & \dfrac{p}{p^2+\omega^2}\\
\sinh\lambda t & \dfrac{\lambda}{p^2-\lambda^2}\\
\cosh\lambda t & \dfrac{p}{p^2-\lambda^2}\\
e^{\lambda t}\sin\omega t & \dfrac{\omega}{(p-\lambda)^2+\omega^2}\\
e^{\lambda t}\cos\omega t & \dfrac{p-\lambda}{(p-\lambda)^2+\omega^2}
\end{array}
$$
Each entry is computed from the definition by integrating $e^{-(p-\lambda)t}$ times a power or a pair of exponentials.
:::
