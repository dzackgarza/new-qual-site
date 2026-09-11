---
schema: qual/card@1
id: E-SS3.EX-12
kind: problem
title: "The partial fractions identity for csc-squared"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
12. Suppose u is not an integer.
    Prove that

$$
\sum_ {n = - \infty} ^ {\infty} \frac {1}{(u + n) ^ {2}} = \frac {\pi^ {2}}{(\sin \pi u) ^ {2}}
$$

by integrating

$$
f (z) = \frac {\pi \cot \pi z}{(u + z) ^ {2}}
$$

over the circle $| z | = R _ { N } = N + 1 / 2$ (N integral, $N \geq | u | )$ , adding the residues of f inside the circle, and letting N tend to infinity.

Note.
Two other derivations of this identity, using Fourier series, were given in Book I.
:::

::: solution
Let
\[
f(z)=\frac{\pi\cot(\pi z)}{(u+z)^2},\qquad u\notin\mathbb Z,
\]
and let $C_N$ be $|z|=R_N=N+\tfrac12$, with $N\ge |u|$.

At each integer $n$ with $|n|\le N$, $\pi\cot(\pi z)$ has residue $1$, so
\[
\operatorname{Res}_{z=n}f(z)=\frac1{(u+n)^2}.
\]
At $z=-u$ there is a double pole. If $g(z)=\pi\cot(\pi z)$, then
\[
\operatorname{Res}_{z=-u}\frac{g(z)}{(z+u)^2}=g'(-u)
=-\pi^2\csc^2(\pi u).
\]
Therefore the residue theorem gives
\[
\int_{C_N}f(z)\,dz
=2\pi i\left(
\sum_{n=-N}^N\frac1{(u+n)^2}
-\frac{\pi^2}{\sin^2(\pi u)}
\right).
\tag{1}
\]

It remains to show the contour integral tends to $0$. On the circles $|z|=N+\tfrac12$, the distance to every integer is bounded below by a positive absolute constant in the horizontal direction, and the standard formula
\[
\cot(x+iy)=\frac{\sin 2x-i\sinh 2y}{\cosh 2y-\cos 2x}
\]
shows $|\cot(\pi z)|$ is uniformly bounded on all these circles. Also $|z+u|\ge R_N-|u|$. Hence
\[
\left|\int_{C_N}f(z)\,dz\right|
\le 2\pi R_N\,\frac{C}{(R_N-|u|)^2}\longrightarrow0.
\]
Letting $N\to\infty$ in (1) yields
\[
\sum_{n=-\infty}^{\infty}\frac1{(u+n)^2}
=\frac{\pi^2}{\sin^2(\pi u)}.
\]
:::
