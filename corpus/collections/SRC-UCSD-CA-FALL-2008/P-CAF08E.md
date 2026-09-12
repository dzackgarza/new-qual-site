---
schema: qual/card@1
id: P-CAF08E
kind: problem
title: "Periodic entire function with subexponential growth must vanish"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Suppose that $f(z)$ is an entire function satisfying $f(z) = f(z + 1)$ for all $z$.
If there exists a real number $c$, with $c \neq 2\pi k$, $k \in \mathbb{Z}$, such that $|f(z)| \leq e^{c\,\operatorname{Im} z}$ for all $z \in \mathbb{C}$, prove that $f \equiv 0$.

Hint: Prove it first for the case $G = B(0; 1)$.
:::

::: solution
Because $f$ is $1$-periodic, it descends through the exponential map
\[
w=e^{2\pi i z}
\]
to a holomorphic function $F$ on $\mathbb C^*$, defined by
\[
F(e^{2\pi i z})=f(z).
\]
Write its Laurent expansion
\[
F(w)=\sum_{n\in\mathbb Z}a_n w^n.
\]
Then
\[
f(z)=\sum_{n\in\mathbb Z}a_n e^{2\pi i n z}.
\]

Let $z=x+iy$. The growth hypothesis gives
\[
|f(x+iy)|\le e^{cy}.
\]
For every integer $n$, Fourier inversion on one period gives
\[
a_n e^{-2\pi n y}
=\int_0^1 f(x+iy)e^{-2\pi i n x}\,dx,
\]
so
\[
|a_n|\le e^{(c+2\pi n)y}
\qquad (y\in\mathbb R).
\]
If $c+2\pi n>0$, let $y\to-\infty$; if $c+2\pi n<0$, let
$y\to+\infty$. In either case $a_n=0$. Therefore a coefficient can be nonzero
only when
\[
c+2\pi n=0.
\]
Equivalently, $c=-2\pi n=2\pi k$ for some $k\in\mathbb Z$. The hypothesis
excludes this possibility, so every Laurent coefficient vanishes and
$f\equiv0$.
:::
