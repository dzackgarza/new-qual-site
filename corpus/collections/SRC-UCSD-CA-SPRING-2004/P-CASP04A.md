---
schema: qual/card@1
id: P-CASP04A
kind: problem
title: "True or False: Möbius transformations, Cauchy sequences, contour integrals, limits of functions missing values, and lacunary series"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For each of the following, determine if the statement is true or false.

(a) There is a Möbius (linear fractional) transformation sending the triangle with vertices at $\{0, i, 1\}$ to that with vertices at $\{0, i, 2\}$.

(b) Let $(X, d)$ be a metric space.
If a Cauchy sequence $\{x_n\}_{n=1}^{\infty}$ in $X$ has a convergent subsequence, then $\{x_n\}_{n=1}^{\infty}$ is convergent.

(c) Let $\gamma_+(t) = e^{i\pi t}$ and $\gamma_-(t) = e^{-i\pi t}$, for $t \in [0, 1]$.
Then $\int_{\gamma_+} \frac{2}{(2z-1)^2}\,dz = \int_{\gamma_-} \frac{2}{(2z-1)^2}\,dz$.

(d) Let $f_n \in \mathcal{O}(G)$ be a sequence such that $f_n(G) \subset \mathbb{D} \setminus \{0\}$ for $n = 1, 2, \ldots$, and assume that $f_n \to f$ in $\mathcal{O}(G)$.
Then either $f$ is constant or $f(G) \subset \mathbb{D} \setminus \{0\}$.

(e) There is a sequence of complex numbers $\{a_n\}_{n=0}^{\infty}$ and strictly increasing sequence of integers $\{p_n\}_{n=0}^{\infty}$ with $p_n \geq n$ such that the radius of convergence of $\sum_{n=0}^{\infty} a_n z^n$ is one but that of $\sum_{n=0}^{\infty} a_n z^{p_n}$ is less than one.
:::

::: {.solution}
(a) **False.** Möbius transformations are conformal and hence preserve the
angles of a polygonal boundary. The triangle with vertices $0,i,1$ has angle
multiset $\{\pi/2,\pi/4,\pi/4\}$, whereas the triangle with vertices
$0,i,2$ is not isosceles and has a different angle multiset. Thus no Möbius
map can carry one triangle onto the other.

(b) **True.** Let $x_{n_j}\to x$. Given $\varepsilon>0$, choose $N$ so that
$d(x_m,x_n)<\varepsilon/2$ for $m,n\ge N$, and choose $j$ with
$n_j\ge N$ and $d(x_{n_j},x)<\varepsilon/2$. Then for every $n\ge N$,
\[
d(x_n,x)\le d(x_n,x_{n_j})+d(x_{n_j},x)<\varepsilon.
\]

(c) **True.** The integrand has the primitive
\[
-\frac1{2z-1},
\]
on $\mathbb C\setminus\{1/2\}$. Both curves run from $1$ to $-1$ and avoid
$1/2$, so the two integrals are equal.

(d) **True.** By Hurwitz's theorem, a locally uniform limit of zero-free
holomorphic functions is either identically zero or zero-free. If $f$ is not
constant, it is zero-free; moreover $|f|\le1$, and the maximum principle
excludes an interior value of modulus $1$. Hence
$f(G)\subset\mathbb D\setminus\{0\}$.

(e) **False.** By Cauchy--Hadamard,
\[
1=\limsup_{n\to\infty}|a_n|^{1/n}.
\]
For the lacunary series, the relevant limsup is
$\limsup |a_n|^{1/p_n}$. Since $p_n\ge n$, values with $|a_n|\ge1$ can only
decrease after taking the $p_n$th root, while values with $|a_n|<1$ remain
below $1$. Thus
\[
\limsup |a_n|^{1/p_n}\le1,
\]
so its radius of convergence is at least $1$, never less than $1$.
:::
