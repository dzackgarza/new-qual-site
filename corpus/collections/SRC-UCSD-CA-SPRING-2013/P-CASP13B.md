---
schema: qual/card@1
id: P-CASP13B
kind: problem
title: "True or False: harmonic critical points, Mittag-Leffler interpolation, harmonic limits, and polynomial approximation"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Determine if the following statements are True or False.

(a) Let $U \subseteq \mathbb{C}$ be an open set, and let $u: U \to \mathbb{R}$ be a non-constant harmonic function.
Set $Z = \{z \in U : u_x(z) = u_y(z) = 0\}$.
It is possible for $Z$ to have an accumulation point in $U$.

(b) There is a meromorphic function $f$ on $\mathbb{C} \setminus (2\mathbb{Z})^2$ such that, if $n, m \in 2\mathbb{Z}$ are even integers, then $f$ has a pole of order $n^2 + m^2$ at $(n, m)$, and if $(n, m) \in \mathbb{Z} \times \mathbb{Z}$ with at least one odd, then $f$ has a zero of order $n^2 + m^2$ at $(n, m)$.

(c) Let $\{u_n\}$ be a sequence of harmonic functions in $\mathbb{D}$.
If $u_n$ converges to $u$ uniformly on compact subsets, then $u$ is harmonic on $\mathbb{D}$.

(d) There is a sequence of holomorphic polynomials $p_n$ such that $$\lim_{n \to \infty} \sup_{2 \leq |z| \leq 3} \left|\frac{1}{z^2(z-5)^3} - p_n(z)\right| = 0.$$
:::

::: solution
**(a) True.** The hypothesis says only that $U$ is open, not connected. Take
\[
U=D(0,1)\cup D(3,1),
\]
and define $u=0$ on $D(0,1)$ and $u(z)=\operatorname{Re}z$ on $D(3,1)$.
Then $u$ is harmonic and nonconstant on $U$, while every point of $D(0,1)$
lies in
\[
Z=\{u_x=u_y=0\}.
\]
Thus $Z$ has accumulation points in $U$.

**(b) False.** Taking $n=m=0$, the statement requires a pole of order
\[
n^2+m^2=0
\]
at $(0,0)$. A pole has positive integer order, so a pole of order $0$ does
not exist. Hence the asserted meromorphic function cannot exist as stated.

**(c) True.** The mean-value property passes to locally uniform limits. If
$\overline{B(a,r)}\subset\mathbb D$, then
\[
u_n(a)=\frac1{2\pi}\int_0^{2\pi}u_n(a+re^{it})\,dt.
\]
Taking $n\to\infty$ uniformly on the circle gives the same identity for $u$.
Hence $u$ has the mean-value property and is harmonic.

**(d) False.** Let
\[
K=\{2\le |z|\le3\}.
\]
If polynomials $p_n$ converged uniformly on $K$ to
\[
h(z)=\frac1{z^2(z-5)^3},
\]
then for the circle $|z|=5/2$ we would have
\[
\int_{|z|=5/2}p_n(z)\,dz\to
\int_{|z|=5/2}h(z)\,dz.
\]
The left side is always $0$. But the right side is
$2\pi i\operatorname{Res}_{z=0}h$, and that residue is nonzero. Contradiction.
Thus such polynomial approximation is impossible.
:::
