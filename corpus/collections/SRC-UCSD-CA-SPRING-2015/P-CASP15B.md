---
schema: qual/card@1
id: P-CASP15B
kind: problem
title: "True or false: five statements in complex analysis"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Holomorphic Functions
  - Uniform Convergence
  - Liouville's Theorem
  - Sheaf of Germs
relations: []
review: draft
---

::: {.problem}
Are the following statements true or false?
If true, give a brief proof.
If false, give a counterexample.

(i) If $u$ and $v$ are two harmonic functions on a region $U$ and the set of points where $u$ and $v$ are equal contains an accumulation belonging to $U$ then $u = v$.

(ii) There is a nonconstant holomorphic function $f(z)$ on the region $U = \mathbb{C} \setminus \{z \in \mathbb{C} \mid \operatorname{Im} z = 0, \operatorname{Re} z < 0\}$ such that $|f(z)| \leq 1$.

(iii) There are polynomials $p_1, p_2, \ldots$ such that $\frac{1}{z(z-3)} - p_n(z)$ converges uniformly to zero on the annulus $U = \{z \in \mathbb{C} \mid 1 < |z| < 2\}$ as $n$ tends to infinity.

(iv) If $f(z)$ is an entire function then either the image of $f$ is dense in $\mathbb{C}$ or $f(z)$ is constant.

(v) Let $\pi : \mathcal{O} \to \mathbb{C}$ be the sheaf of germs of holomorphic functions over $\mathbb{C}$.
Assume that there are germs $\zeta, \zeta_n \in \mathcal{O}$ such that $\lim_{n \to \infty} \zeta_n = \zeta$.
Then there is a function element $(f, D)$ such that $\zeta_n = (f)_{\pi(\zeta_n)}$ for $n$ sufficiently large.
:::

::: {.solution}
**(i) False.** Take $u(z)=\operatorname{Re}z$ and $v(z)=0$ on
$U=\mathbb C$. They agree on the imaginary axis, which has accumulation
points in $U$, but $u\ne v$.

**(ii) True.** The slit plane
\[
U=\mathbb C\setminus(-\infty,0]
\]
is simply connected and proper, so by the Riemann mapping theorem there is a
nonconstant biholomorphism $F:U\to\mathbb D$. In particular $|F|<1$.

**(iii) False.** If polynomials $p_n$ converged uniformly on
$1<|z|<2$ to $1/[z(z-3)]$, then they would converge uniformly on the circle
$|z|=3/2$. Hence
\[
0=\int_{|z|=3/2}p_n(z)\,dz
\longrightarrow
\int_{|z|=3/2}\frac{dz}{z(z-3)}.
\]
The latter integral equals
$2\pi i\operatorname{Res}_{z=0}(1/[z(z-3)])=-2\pi i/3\ne0$, a
contradiction.

**(iv) True.** If a nonconstant entire function is a polynomial, it is
surjective onto $\mathbb C$ by the fundamental theorem of algebra applied to
$f-w$. If it is transcendental entire, Great Picard at $\infty$ says that it
takes every complex value, with at most one exception, infinitely often.
Either way its image is dense in $\mathbb C$.

**(v) True.** The sheaf space $\mathcal O$ is equipped with the étalé-space
topology. A basic neighborhood of the germ $\zeta=(f)_a$ is
\[
\{(f)_z:z\in D\},
\]
where $(f,D)$ is a function element representing $\zeta$. Convergence
$\zeta_n\to\zeta$ therefore implies that all sufficiently large $\zeta_n$
belong to such a basic neighborhood. Thus
\[
\zeta_n=(f)_{\pi(\zeta_n)}
\]
for all sufficiently large $n$.
:::
