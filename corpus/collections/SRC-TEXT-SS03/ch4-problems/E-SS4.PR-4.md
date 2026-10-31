---
schema: qual/card@1
id: E-SS4.PR-4
kind: problem
title: Borel representation of entire functions of exponential type
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Fourier Transform
relations: []
review: draft
---

::: {.exercise}
There is a relation between the Paley–Wiener theorem and an earlier representation due to E. Borel.

(a) A function $f$, holomorphic on $\CC$, satisfies $\abs{f(z)}\leq A_\varepsilon e^{2\pi(M+\varepsilon)\abs{z}}$ for all $\varepsilon>0$ if and only if it has a representation
$$
f(z)=\int_C e^{2\pi izw}g(w)\,dw,
$$
where $g$ is holomorphic outside the circle of radius $M$ centered at the origin and vanishes at infinity. Here $C$ is any circle centered at the origin with radius larger than $M$. In fact, if $f(z)=\sum_{n=0}^{\infty}a_nz^n$, then $g(w)=\sum_{n=0}^{\infty}A_nw^{-n-1}$, with $a_n=A_n(2\pi i)^{n+1}/n!$.

(b) The connection with Theorem 3.3 is as follows. For these functions $f$, if in addition $f$ and $\hat f$ are of moderate decrease on the real axis, show that $g$ is holomorphic on the slit plane $\CC\setminus[-M,M]$ and
$$
g(z)=\frac{1}{2\pi i}\int_{-M}^{M}\frac{\hat f(\xi)}{\xi-z}\,d\xi.
$$
Thus $\hat f$ represents the jump of $g$ across $[-M,M]$:
$$
\hat f(x)=\lim_{\varepsilon\to0,\,\varepsilon>0}\bigl(g(x+i\varepsilon)-g(x-i\varepsilon)\bigr).
$$
See Problem 5 in Chapter 3.
:::
