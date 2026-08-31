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
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
- Show that if $f\in L^1$ then $\hat f$ is bounded and uniformly continuous.

- Is it the case that $f\in L^1$ implies $\hat f\in L^1$?

- Show that if $f, \hat f \in L^1$ then $f$ is bounded, uniformly continuous, and vanishes at infinity.

  - Show that this is not true for arbitrary $L^1$ functions.

- Show that if $f\in L^1$ and $\hat f = 0$ almost everywhere then $f = 0$ almost everywhere.

  - Prove that $\hat f = \hat g$ implies that $f=g$ a.e.

- Show that if $f, g \in L^1$ then $$\int \hat f g = \int f\hat g.$$

  - Give an example showing that this fails if $g$ is not bounded.

- Show that if $f\in C^1$ then $f$ is equal to its Fourier *series*.
:::
::: {.solution}
*Setup note.* This is the parent problem of E-TF33D; the Fourier transform is normalized as $\hat f(\xi) = \int f(x)e^{-2\pi i x\xi}\,dx$, and the parts below are proved in the companion cards E-WURI3, E-FZXFR, E-O742O, E-TF33D; we give the consolidated argument.

<1>1. $\hat f$ is bounded and uniformly continuous.
::: {.proof}
boundedness: $|\hat f(\xi)| \le \int|f| = \norm{f}_1$.
:::
Uniform continuity: for $h \to 0$, \[ \hat f(\xi+h) - \hat f(\xi) = \int f(x) e^{-2\pi i x\xi}\big(e^{-2\pi i xh} - 1\big)\,dx, \] and the integrand is dominated by $2|f(x)| \in L^1$, so the dominated convergence theorem gives $\hat f(\xi+h) - \hat f(\xi) \to 0$ uniformly in $\xi$ (the domination is independent of $\xi$). <1>2. $f \in L^1$ does not imply $\hat f \in L^1$.
::: {.proof}
$f = \chi_{[-1,1]}$ has $\hat f(\xi) = \frac{\sin 2\pi\xi}{\pi\xi}$, which is not integrable (its absolute value integrates like $1/|\xi|$ at infinity).
:::
So the answer to the question is no. <1>3. If $f, \hat f \in L^1$, then $f$ is bounded, uniformly continuous, and vanishes at infinity.
::: {.proof}
the Fourier inversion formula $f(x) = \int \hat f(\xi) e^{2\pi i x\xi}\,d\xi$ holds (valid a.e., and here the right side is a continuous function, so $f$ has a continuous representative).
:::
Boundedness: $|f(x)| \le \int|\hat f|$.
Uniform continuity: same argument as <1>1 with $f$ and $\hat f$ interchanged.
Vanishing at infinity: $\hat f \in L^1$ and the Riemann--Lebesgue lemma applied to $\hat f$ give $f(x) \to 0$ as $|x| \to \infty$.
<1>4. This fails for arbitrary $L^1$ functions.
::: {.proof}
$\chi_{[-1,1]}$ is bounded and uniformly continuous but does not vanish at infinity.
:::
(A function that is merely in $L^1$ need not even be bounded: $f(x) = x^{-1/2}\chi_{(0,1)}$.)
<1>5. $\hat f = 0$ a.e. implies $f = 0$ a.e.; hence $\hat f = \hat g$ implies $f = g$ a.e.
::: {.proof}
apply <1>3 to the case $\hat f = 0 \in L^1$: then $f$ equals the inverse transform of $0$, i.e. $f = 0$ everywhere (a.e.). For the second part, apply the first to $f - g$: $\widehat{f-g} = \hat f - \hat g = 0$ a.e., so $f - g = 0$ a.e. <1>6. $\int \hat f\,g = \int f\,\hat g$ for $f, g \in L^1$.
:::
::: {.proof}
by Tonelli--Fubini, \[ \int \hat f(\xi) g(\xi)\,d\xi = \int\!\!\int f(x) g(\xi) e^{-2\pi i x\xi}\,dx\,d\xi = \int f(x) \Big(\int g(\xi) e^{-2\pi i x\xi}\,d\xi\Big)\,dx = \int f\,\hat g, \] since $|f(x)g(\xi)|$ is integrable on the product space.
:::
<1>7. The identity fails if $g$ is not bounded.
::: {.proof}
take $f(x) = e^{-|x|}$, so $\hat f(\xi) = \frac{2}{1 + (2\pi\xi)^2}$, and $g(\xi) = 1 + (2\pi\xi)^2$, unbounded and not in $L^1$.
:::
Then $\int \hat f\,g = \int 2\,d\xi = \infty$ while $\hat g$ is not defined (as $g \notin L^1$), so the identity has no meaning.
(See E-TF33D for the full treatment.)
<1>8. If $f \in C^1$, then $f$ equals its Fourier series.
::: {.proof}
for $f \in C^1$, $\widehat{f'}(n) = 2\pi i n \hat f(n)$, so $\hat f(n) = \widehat{f'}(n)/(2\pi i n)$ for $n \neq 0$; by Parseval and Cauchy--Schwarz, \[ \sum_{n \neq 0}|\hat f(n)| \le \Big(\sum_{n\neq 0}\frac{1}{(2\pi n)^2}\Big)^{1/2}\Big(\sum_n|\widehat{f'}(n)|^2\Big)^{1/2} < \infty, \] so the Fourier series converges absolutely, hence uniformly, to $f$ (Fejér's theorem gives the pointwise/uniform limit $f$ since the series converges).
:::
(See E-TF33D for details.)
<1>9. Q.E.D.
:::
