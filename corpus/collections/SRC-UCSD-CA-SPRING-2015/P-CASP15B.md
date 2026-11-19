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
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: Read against the UCSD Complex Analysis Qualifying Exam, Spring 2015; all five items match.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    No retained solution set covers this examination. Structured the card's own answers:
    the real-part counterexample, the slit-plane Riemann map, the residue obstruction,
    the polynomial/transcendental cases for density, and the etale sheaf neighborhood.
---

::: {.problem}
Are the following statements true or false?
If true, give a brief proof.
If false, give a counterexample.

(i) If $u$ and $v$ are two harmonic functions on a region $U$ and the set of points where $u$ and $v$ are equal contains an accumulation belonging to $U$ then $u = v$.

(ii) There is a nonconstant holomorphic function $f(z)$ on the region $U = \CC \setminus \{z \in \CC \mid \operatorname{Im} z = 0, \operatorname{Re} z < 0\}$ such that $\abs{f(z)} \leq 1$.

(iii) There are polynomials $p_1, p_2, \ldots$ such that $\frac{1}{z(z-3)} - p_n(z)$ converges uniformly to zero on the annulus $U = \{z \in \CC \mid 1 < \abs{z} < 2\}$ as $n$ tends to infinity.

(iv) If $f(z)$ is an entire function then either the image of $f$ is dense in $\CC$ or $f(z)$ is constant.

(v) Let $\pi : \mathcal{O} \to \CC$ be the sheaf of germs of holomorphic functions over $\CC$.
Assume that there are germs $\zeta, \zeta_n \in \mathcal{O}$ such that $\lim_{n \to \infty} \zeta_n = \zeta$.
Then there is a function element $(f, D)$ such that $\zeta_n = (f)_{\pi(\zeta_n)}$ for $n$ sufficiently large.
:::

::: {.solution}

No retained solution set covers this examination; the argument below is the card's own.

::: pf

::: {.pf-step #i-false}
Statement (i) is false.

::: pf-proof
On $U=\CC$, take $u(z)=\operatorname{Re}z$ and $v(z)=0$. Both are harmonic, and they agree on the imaginary axis, every point of which is an accumulation point in $U$; but $u\ne v$.
:::
:::

::: {.pf-step #ii-true}
Statement (ii) is true.

::: pf-proof
The slit plane $U=\CC\setminus(-\infty,0]$ is a proper simply connected domain. The Riemann mapping theorem gives a nonconstant biholomorphism $F:U\to\DD$, and then $\abs{F(z)}<1$ for all $z\in U$.
:::
:::

::: {.pf-step #iii-false}
Statement (iii) is false.

::: pf-proof
Uniform polynomial convergence on the annulus would give convergence on the circle $\abs z=3/2$. Each polynomial has zero integral there, so
$$
0=\int_{\abs z=3/2}p_n(z)\,dz\longrightarrow \int_{\abs z=3/2}\frac{dz}{z(z-3)}
=2\pi i\operatorname{Res}_{z=0}\frac1{z(z-3)}=-\frac{2\pi i}{3}\ne0,
$$
a contradiction.
:::
:::

::: {.pf-step #iv-true}
Statement (iv) is true.

::: pf-proof
A nonconstant polynomial is surjective onto $\CC$ by the fundamental theorem of algebra applied to $f(z)-w$. A transcendental entire function has an essential singularity at infinity, so Casorati--Weierstrass says its image is dense in $\CC$. Thus every nonconstant entire function has dense image; a constant function need not.
:::
:::

::: {.pf-step #v-true}
Statement (v) is true.

::: pf-proof
In the etale topology on $\mathcal O$, a basic neighborhood of the germ $\zeta$ represented by $(f,D)$ is $\{(f)_z:z\in D\}$. By definition of convergence, all sufficiently large $\zeta_n$ lie in this neighborhood, hence are germs of the same function element: $\zeta_n=(f)_{\pi(\zeta_n)}$ for all large $n$.
:::
:::

:::
:::
