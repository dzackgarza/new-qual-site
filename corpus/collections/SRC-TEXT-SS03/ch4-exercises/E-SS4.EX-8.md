---
schema: qual/card@1
id: E-SS4.EX-8
kind: problem
title: "SS 4.8: Compact support of a Fourier transform and coefficient growth"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: exercise
8. Suppose $\hat { f }$ has compact support contained in $[ - M , M ]$ and let $\begin{array} { r } { f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n } } \end{array}$ Show that

$$
a _ {n} = \frac {(2 \pi i) ^ {n}}{n !} \int_ {- M} ^ {M} \hat {f} (\xi) \xi^ {n} d \xi ,
$$

and as a result

$$
\limsup _ {n \to \infty} (n! | a _ {n} |) ^ {1 / n} \leq 2 \pi M.
$$

In the converse direction, let f be any power series $\textstyle f ( z ) = \sum _ { n = 0 } ^ { \infty } a _ { n } z ^ { n }$ with lim $\begin{array} { r } { \operatorname* { s u p } _ { n \to \infty } ( n ! | a _ { n } | ) ^ { 1 / n } \leq 2 \pi M } \end{array}$ . Then, f is holomorphic in the complex plane, and for every $\epsilon > 0$ there exists $A _ { \epsilon } > 0$ such that

$$
| f (z) | \leq A _ {\epsilon} e ^ {2 \pi (M + \epsilon) | z |}.
$$
:::

::: solution
Assume $\operatorname{supp}\widehat f\subset[-M,M]$. Fourier inversion gives, for real $x$ and hence by analytic continuation for complex $z$,
\[
f(z)=\int_{-M}^{M}\widehat f(\xi)e^{2\pi i\xi z}\,d\xi.
\]
Because the interval is compact, differentiation under the integral sign is justified to every order. Thus
\[
f^{(n)}(0)=(2\pi i)^n\int_{-M}^{M}\widehat f(\xi)\xi^n\,d\xi.
\]
Since $a_n=f^{(n)}(0)/n!$,
\[
a_n=\frac{(2\pi i)^n}{n!}
\int_{-M}^{M}\widehat f(\xi)\xi^n\,d\xi.
\]
Hence
\[
n!|a_n|
\le (2\pi M)^n\|\widehat f\|_{L^1([-M,M])},
\]
and therefore
\[
\limsup_{n\to\infty}(n!|a_n|)^{1/n}\le2\pi M.
\]

Conversely, suppose
\[
L:=\limsup_{n\to\infty}(n!|a_n|)^{1/n}\le2\pi M.
\]
Fix $\varepsilon>0$ and put
\[
R=2\pi(M+\varepsilon).
\]
Since $R>L$, there is $N$ such that for $n\ge N$,
\[
n!|a_n|\le R^n.
\]
After enlarging a constant $C_\varepsilon$ to absorb the finitely many indices $n<N$, we have for every $n\ge0$
\[
|a_n|\le C_\varepsilon\frac{R^n}{n!}.
\]
Thus the power series converges absolutely for every $z\in\mathbb C$ and
\[
|f(z)|
\le C_\varepsilon\sum_{n=0}^{\infty}\frac{(R|z|)^n}{n!}
=C_\varepsilon e^{R|z|}
=C_\varepsilon e^{2\pi(M+\varepsilon)|z|}.
\]
So $f$ is entire and has the stated exponential-type bound.
:::
