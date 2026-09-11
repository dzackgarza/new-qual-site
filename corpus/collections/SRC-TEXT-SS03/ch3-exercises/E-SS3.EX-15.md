---
schema: qual/card@1
id: E-SS3.EX-15
kind: problem
title: "Applications of the Cauchy inequalities and the maximum modulus principle"
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
15. Use the Cauchy inequalities or the maximum modulus principle to solve the following problems:

(a) Prove that if f is an entire function that satisfies

$$
\sup _ {| z | = R} | f (z) | \leq A R ^ {k} + B
$$

for all $R > 0$ , and for some integer $k \geq 0$ and some constants $A , B > 0$ , then f is a polynomial of degree $\leq k$

(b) Show that if f is holomorphic in the unit disc, is bounded, and converges uniformly to zero in the sector $\theta < \arg z < \varphi { \mathrm { ~ a s ~ } } | z | \to 1$ , then $f = 0$

(c) Let $w _ { 1 } , \ldots , w _ { n }$ be points on the unit circle in the complex plane.
Prove that there exists a point z on the unit circle such that the product of the distances from z to the points w<sub>j</sub>, $1 \leq j \leq n _ { \mathrm { : } }$ , is at least 1. Conclude that there exists a point w on the unit circle such that the product of the distances from w to the points w<sub>j</sub> , $1 \leq j \leq n$ , is exactly equal to 1.

(d) Show that if the real part of an entire function f is bounded, then f is constant.
:::

::: solution
(a) Write $f(z)=\sum_{n\ge0}a_nz^n$. Cauchy's estimate on $|z|=R$ gives
\[
|a_n|\le \frac{AR^k+B}{R^n}.
\]
For $n>k$, letting $R\to\infty$ yields $a_n=0$. Hence $f$ is a polynomial of degree at most $k$.

(b) By hypothesis there is an open boundary arc
\[
I=\{e^{it}:\theta<t<\varphi\}
\]
on which $f(z)\to0$ uniformly as $|z|\to1$ inside the sector. Thus defining $f=0$ on $I$ gives a continuous extension to that arc. Fix a smaller open subarc $I'\Subset I$. After rotating coordinates, a neighborhood of each point of $I'$ is conformally equivalent to a half-disc whose diameter lies on the real axis, and the boundary values of $f$ there are identically $0$, hence real. By the Schwarz reflection principle, $f$ extends holomorphically across $I'$, with the extension vanishing on $I'$. The identity theorem then forces the extension, and hence $f$ on $\mathbb D$, to vanish identically.

(c) Let
\[
P(z)=\prod_{j=1}^n(z-w_j).
\]
Since $P$ is monic, $P(0)=(-1)^n\prod_jw_j$, so $|P(0)|=1$. By the maximum modulus principle applied on the closed unit disc,
\[
1=|P(0)|\le \max_{|z|=1}|P(z)|.
\]
Hence some $z$ on the unit circle satisfies
\[
\prod_{j=1}^n|z-w_j|=|P(z)|\ge1.
\]
On the other hand, $P(w_1)=0$. The continuous function $|P|$ on the connected unit circle therefore takes every value between $0$ and its maximum, in particular the value $1$. Thus there is $w$ on the unit circle with
\[
\prod_{j=1}^n|w-w_j|=1.
\]

(d) Suppose $|\Re f|\le M$. Then
\[
g(z)=e^{f(z)}
\]
is entire and satisfies $|g(z)|=e^{\Re f(z)}\le e^M$. By Liouville, $g$ is constant. Differentiating gives
\[
0=g'(z)=f'(z)e^{f(z)},
\]
so $f'\equiv0$ and $f$ is constant.
:::
