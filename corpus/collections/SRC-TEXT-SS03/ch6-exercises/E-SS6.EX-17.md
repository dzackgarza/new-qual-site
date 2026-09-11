---
schema: qual/card@1
id: E-SS6.EX-17
kind: problem
title: "The Mellin transform of a Schwartz function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Repaired the derivative-index transcription defect using the supplied integration-by-parts identity.
---

::: exercise
17. Let f be an indefinitely diferentiable function on R that has compact support, or more generally, let $f$ belong to the Schwartz space.<sup>4</sup> Consider

$$
I (s) = \frac {1}{\Gamma (s)} \int_ {0} ^ {\infty} f (x) x ^ {- 1 + s} d x.
$$

(a) Observe that $I ( s )$ is holomorphic for $\operatorname { R e } ( s ) > 0$ . Prove that I has an analytic continuation as an entire function in the complex plane.

(b) Prove that $I(0)=f(0)$, and more generally

$$
I(-n)=(-1)^n f^{(n)}(0) \quad \text{for all } n\ge0.
$$

[Hint: To prove the analytic continuation, as well as the formulas in the second part, integrate by parts to show that $\begin{array} { r } { I ( s ) = \frac { ( - 1 ) ^ { k } } { \Gamma ( s + k ) } \int _ { 0 } ^ { \infty } f ^ { ( k ) } ( x ) x ^ { s + k - 1 } d x . } \end{array}$
:::

::: solution
For $\Re s>0$,
\[
I(s)=\frac1{\Gamma(s)}\int_0^\infty f(x)x^{s-1}\,dx
\]
is holomorphic by dominated convergence on compact vertical strips.

Integrating by parts once gives
\[
\int_0^\infty f(x)x^{s-1}\,dx
=-\frac1s\int_0^\infty f'(x)x^s\,dx,
\]
because the boundary terms vanish when $\Re s>0$. Using $\Gamma(s+1)=s\Gamma(s)$,
\[
I(s)=-\frac1{\Gamma(s+1)}\int_0^\infty f'(x)x^s\,dx.
\]
Iterating $k$ times yields
\[
I(s)=\frac{(-1)^k}{\Gamma(s+k)}
\int_0^\infty f^{(k)}(x)x^{s+k-1}\,dx,
\tag{1}
\]
initially for $\Re s>0$.

For fixed $k$, the right-hand side is holomorphic for $\Re s>-k$: the integral is holomorphic there, and $1/\Gamma$ is entire. On overlaps these expressions agree by (1), so they analytically continue one another. Since $k$ is arbitrary, $I$ extends to an entire function.

Now fix $n\ge0$ and take $k=n+1$ in (1). At $s=-n$,
\[
I(-n)=(-1)^{n+1}\int_0^\infty f^{(n+1)}(x)\,dx,
\]
because $\Gamma(1)=1$. Since $f^{(n)}(x)\to0$ as $x\to\infty$ for a Schwartz function (and likewise for compact support),
\[
\int_0^\infty f^{(n+1)}(x)\,dx
=-f^{(n)}(0).
\]
Therefore
\[
\boxed{I(-n)=(-1)^n f^{(n)}(0)}.
\]
In particular, $I(0)=f(0)$.
:::
