---
schema: qual/card@1
id: P-VLZN2
kind: problem
title: 'Fourier transforms of $L^1$ functions: boundedness, uniqueness, the multiplication
  formula, and Fourier series of $C^1$ functions'
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - L¹
  - Uniform Continuity
  - Counterexamples
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source did not name the domain, said that f with f, f-hat in L^1 is itself bounded and uniformly continuous, and asked whether a C^1 function equals its Fourier series without periodicity; the statement now works on R, says f agrees a.e. with such a function, and takes f to be 1-periodic for the Fourier series part.'
---

::: {.problem}

All functions below are complex-valued functions on $\RR$, and $\hat f(\xi) = \int_\RR f(x)e^{-2\pi i x\xi}\dx$.

(a) Show that if $f\in L^1$ then $\hat f$ is bounded and uniformly continuous.

(b) Is it the case that $f\in L^1$ implies $\hat f\in L^1$?

(c) Show that if $f, \hat f \in L^1$ then $f$ agrees almost everywhere with a function that is bounded, uniformly continuous, and vanishes at infinity. Show that this is not true for arbitrary $L^1$ functions.

(d) Show that if $f\in L^1$ and $\hat f = 0$ almost everywhere then $f = 0$ almost everywhere. Prove that $\hat f = \hat g$ implies that $f=g$ a.e.

(e) Show that if $f, g \in L^1$ then
$$
\int \hat f g = \int f\hat g.
$$
Give an example showing that this fails if $g$ is not bounded.

(f) Show that if $f$ is $1$-periodic and $C^1$ then $f$ is equal to its Fourier *series*.

:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) $\hat f$ is bounded and uniformly continuous.

::: pf-proof

Boundedness: $\abs{\hat f(\xi)} \le \int\abs{f} = \norm{f}_1$.

Uniform continuity: for $h \in \RR$,
$$
\abs{\hat f(\xi+h) - \hat f(\xi)} \le \int \abs{f(x)}\,\abs{e^{-2\pi i xh} - 1}\dx,
$$
and the right side does not depend on $\xi$. Its integrand is dominated by $2\abs{f} \in L^1$ and tends to $0$ pointwise as $h \to 0$, so the dominated convergence theorem gives $\sup_\xi \abs{\hat f(\xi+h) - \hat f(\xi)} \to 0$.

:::

:::

::: pf-step

(b) No: $f \in L^1$ does not imply $\hat f \in L^1$.

::: pf-proof

$f = \chi_{[-1,1]}$ has $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi}$, which is not integrable: $\int_{k/2}^{(k+1)/2} \abs{\sin 2\pi\xi}\,d\xi = 1/\pi$ for every integer $k$, so $\int_{1/2}^\infty \abs{\hat f} \ge \sum_{k\ge1} \frac{2}{\pi^2 (k+1)} = \infty$.

:::

:::

::: {.pf-step #s3}

(c) If $f, \hat f \in L^1$, then $f$ agrees a.e. with a bounded, uniformly continuous function that vanishes at infinity; this fails for arbitrary $f \in L^1$.

::: pf-proof

By the Fourier inversion theorem, $f(x) = \int \hat f(\xi) e^{2\pi i x\xi}\,d\xi$ for almost every $x$. The right side is the Fourier transform of $\hat f \in L^1$ evaluated at $-x$, so it is bounded and uniformly continuous by step [](#s1){.pf-ref}, and it tends to $0$ as $\abs{x} \to \infty$ by the Riemann--Lebesgue lemma.

For arbitrary $f \in L^1$ this fails: $f(x) = x^{-1/2}\chi_{(0,1)}(x)$ lies in $L^1$, but every function equal to it a.e. is unbounded near $0$.

:::

:::

::: pf-step

(d) $\hat f = 0$ a.e. implies $f = 0$ a.e.; hence $\hat f = \hat g$ implies $f = g$ a.e.

::: pf-proof

$\hat f$ is continuous by step [](#s1){.pf-ref}, so $\hat f = 0$ a.e. gives $\hat f = 0$ everywhere, and $\hat f \in L^1$. Step [](#s3){.pf-ref} gives $f(x) = \int 0 \, d\xi = 0$ for almost every $x$. For the second part, $\widehat{f-g} = \hat f - \hat g = 0$, so $f - g = 0$ a.e.

:::

:::

::: pf-step

(e) $\int \hat f\,g = \int f\,\hat g$ for $f, g \in L^1$.

::: pf-proof

The function $(x,\xi) \mapsto f(x) g(\xi) e^{-2\pi i x\xi}$ has absolute value $\abs{f(x)}\abs{g(\xi)}$, which is integrable on $\RR^2$ with integral $\norm{f}_1\norm{g}_1$. Fubini's theorem gives
$$
\int \hat f(\xi) g(\xi)\,d\xi = \iint f(x) g(\xi) e^{-2\pi i x\xi}\dx\,d\xi = \int f(x) \Big(\int g(\xi) e^{-2\pi i x\xi}\,d\xi\Big)\dx = \int f\,\hat g.
$$

:::

:::

::: pf-step

(e) For an unbounded $g$ the identity can fail.

::: pf-proof

Take $f(x) = e^{-\abs{x}}$, so $\hat f(\xi) = \frac{2}{1 + (2\pi\xi)^2}$, and the unbounded function $g(\xi) = 1 + (2\pi\xi)^2$, which is not in $L^1$. Then $\int \hat f\,g = \int 2\,d\xi = \infty$, while $\hat g$ is not defined as a Lebesgue integral, so the right side has no meaning.

:::

:::

::: pf-step

(f) If $f$ is $1$-periodic and $C^1$, then $f(x) = \sum_{n\in\ZZ} \hat f(n) e^{2\pi i n x}$ for every $x$, where $\hat f(n) = \int_0^1 f(x)e^{-2\pi i n x}\dx$.

::: pf-proof

Integration by parts, with periodicity cancelling the boundary terms, gives $\widehat{f'}(n) = 2\pi i n \hat f(n)$, so $\hat f(n) = \widehat{f'}(n)/(2\pi i n)$ for $n \neq 0$. By the Cauchy--Schwarz inequality and Bessel's inequality,
$$
\sum_{n \neq 0}\abs{\hat f(n)} \le \Big(\sum_{n\neq 0}\frac{1}{(2\pi n)^2}\Big)^{1/2}\Big(\sum_n\abs{\widehat{f'}(n)}^2\Big)^{1/2} \le \Big(\sum_{n\neq 0}\frac{1}{(2\pi n)^2}\Big)^{1/2}\norm{f'}_{L^2[0,1]} < \infty.
$$
So the Fourier series converges absolutely and uniformly to a continuous $1$-periodic function $g$. Uniform convergence allows term-by-term integration, so $\hat g(n) = \hat f(n)$ for all $n$. The continuous function $f - g$ has all Fourier coefficients $0$; its Fejér means are then $0$ and converge uniformly to $f - g$ by Fejér's theorem, so $f = g$.

:::

:::

:::

:::

::: {.remark title="Variations"}
The parts are also posed with the convention $\hat f(\xi)=\int f(x)e^{-ix\xi}\,dx$. Then the inversion formula in (c) reads $f(x)=\frac1{2\pi}\int\hat f(\xi)e^{ix\xi}\,d\xi$, and the proofs apply unchanged.

Parts (d) and (e) are also posed for $f,g\in L^1(\RR^n)$. The proofs apply unchanged, with Fourier inversion on $\RR^n$ in (d) and Fubini's theorem on $\RR^{2n}$ in (e).

Part (f) is also posed for $2\pi$-periodic $f$. Apply (f) to the $1$-periodic function $x\mapsto f(2\pi x)$.
:::

::: {.remark}
Uniqueness in (d) can also be proved without the inversion theorem. Put $h=f-g$ and let $u_\eps=h\ast\phi_\eps$ for an approximate identity $\phi_\eps$ built from a continuous compactly supported $\phi\ge0$ with $\int\phi=1$. Then $u_\eps\to h$ in $L^1$, and $\widehat{u_\eps}=\hat h\,\hat\phi(\eps\,\cdot)=0$. Each $u_\eps$ is continuous and lies in $L^1\cap L^\infty\subseteq L^2$, so Plancherel's theorem gives $u_\eps=0$. Hence $h=0$ a.e.
:::
