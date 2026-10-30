---
schema: qual/card@1
id: P-CAF07A
kind: problem
title: "True or False: subsequential convergence, contour integrals, entire functions omitting a disk, biholomorphisms, and harmonicity"
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Contour Integration
  - Entire Functions
  - Conformal Maps
  - Harmonic Functions
relations: []
review: draft
---

::: {.problem}
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample.

(a) Let $(X, d)$ be a metric space.
Let $\{x_n\}_{n=1}^{\infty}$ be a sequence and assume that every subsequence has a convergent subsequence.
Then $\{x_n\}_{n=1}^{\infty}$ is convergent.

(b) Let $\gamma_+(t) = e^{it}$, $t \in [0, \pi]$, and $\gamma_-(t) = e^{-it}$, $t \in [0, \pi]$.
Then $\int_{\gamma_+} e^{1/z^2}\,dz = \int_{\gamma_-} e^{1/z^2}\,dz$.

(c) If $f(z)$ is an entire function and there are $\alpha \in \CC$, $r > 0$, such that $f(\CC) \subset \CC \setminus \overline{B(\alpha, r)}$, then $f(z)$ is constant.

(d) There is an analytic bijection (biholomorphism) from $\DD \setminus \{0\}$ onto $\CC \setminus \{0\}$.

(e) The function $u(z) := \ln\abs{z^2 + 1}$ is harmonic in $\CC \setminus \{-i, i\}$.
:::

::: {.solution}
**(a) False.** In $\RR$, let
$$
x_n=\begin{cases}0,&n\text{ even},\\1,&n\text{ odd}.
\end{cases}
$$
Every subsequence contains an infinite constant subsequence, hence a convergent
subsequence, but $(x_n)$ itself does not converge.

**(b) True.** Both paths run from $1$ to $-1$. Their difference is the integral
around the positively oriented unit circle:
$$
\int_{\gamma_+}e^{1/z^2}\,dz-
\int_{\gamma_-}e^{1/z^2}\,dz
=\int_{\abs{z}=1}e^{1/z^2}\,dz.
$$
The Laurent expansion
$$
e^{1/z^2}=\sum_{n=0}^\infty\frac{z^{-2n}}{n!}
$$
has no $z^{-1}$ term, so the residue at $0$ is $0$. Therefore the circle
integral is $0$, and the two path integrals are equal.

**(c) True.** The hypothesis implies
$$
\abs{f(z)-\alpha}\ge r\qquad(z\in\CC).
$$
Hence $1/(f-\alpha)$ is bounded and entire, so it is constant by Liouville's
theorem. Thus $f$ is constant.

**(d) False.** If $F:\DD\setminus\{0\}\to\CC\setminus\{0\}$ were
a biholomorphism, its inverse
$$
G:\CC\setminus\{0\}\to\DD\setminus\{0\}
$$
would be bounded. The singularity of $G$ at $0$ is removable, so $G$ extends
to a bounded entire function on $\CC$. Liouville's theorem would make it
constant, contradicting bijectivity.

**(e) True.** On $\CC\setminus\{-i,i\}$ the holomorphic function
$z^2+1$ has no zeros. Locally it admits a holomorphic logarithm $L$, and
$$
u(z)=\log\abs{z^2+1}=\operatorname{Re}L(z).
$$
The real part of a holomorphic function is harmonic, so $u$ is harmonic on the
stated domain.
:::
