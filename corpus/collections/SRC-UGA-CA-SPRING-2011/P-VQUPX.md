---
schema: qual/card@1
id: P-VQUPX
kind: problem
title: Taylor coefficients of an entire function as contour integrals, uniform convergence
  on bounded sets, and uniform convergence on $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Cauchy Integral Formula
  - Uniform Convergence
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Suppose $f$ is entire and has Taylor series $\sum a_n z^n$ about 0.

(a) Express $a_n$ as a contour integral along the circle $\abs{z} = R$.

(b) Apply (a) to show that the above Taylor series converges uniformly on every bounded subset of $\CC$.

(c) Determine those functions $f$ for which the above Taylor series converges uniformly on all of $\CC$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $R>0$ and every $n\ge0$,
$$
\boxed{
a_n=\frac{1}{2\pi i}
\int_{\abs{\zeta}=R}
\frac{f(\zeta)}{\zeta^{n+1}}\,d\zeta}.
$$


::: pf-proof

Because $f$ is entire, it is holomorphic on a neighborhood of the closed
disk $\abs{z}\le R$. Cauchy's formula for derivatives gives
$$
f^{(n)}(0)
=\frac{n!}{2\pi i}
\int_{\abs{\zeta}=R}
\frac{f(\zeta)}{\zeta^{n+1}}\,d\zeta.
$$
Since $a_n=f^{(n)}(0)/n!$, the displayed coefficient formula follows.

:::

:::

::: {.pf-step #s1-2}

For every $R>0$,
$$
\abs{a_n}\le \frac{M_R}{R^n},
\qquad
M_R=\max_{\abs{\zeta}=R}\abs{f(\zeta)}.
$$


::: pf-proof

Apply the ML estimate to the integral in step [](#s1-1){.pf-ref}:
$$
\abs{a_n}
\le
\frac1{2\pi}
(2\pi R)
\frac{M_R}{R^{n+1}}
=\frac{M_R}{R^n}.
$$

:::

:::

::: {.pf-step #s1-3}

The Taylor series of $f$ converges uniformly on every bounded
subset of $\CC$.


::: pf-proof

Let $E\subset\CC$ be bounded. Choose $r>0$ with
$$
E\subseteq\{z:\abs{z}\le r\},
$$
and then choose $R>r$. For $z\in E$, step [](#s1-2){.pf-ref} gives
$$
\abs{a_nz^n}
\le M_R\left(\frac rR\right)^n.
$$
The geometric series
$$
\sum_{n=0}^\infty
M_R\left(\frac rR\right)^n
$$
converges because $r/R<1$. Hence the Weierstrass $M$-test shows that
$\sum a_nz^n$ converges uniformly on $E$.

:::

:::

::: {.pf-step #s1-4}

If the Taylor series converges uniformly on all of $\CC$, then
$f$ is a polynomial.


::: pf-proof

Uniform convergence of the series implies that its terms converge
uniformly to zero. Therefore there is $N$ such that, for every $n\ge N$,
$$
\sup_{z\in\CC}\abs{a_nz^n}<1.
$$
If $n\ge N$ and $a_n\ne0$, then
$$
\abs{a_nz^n}\longrightarrow\infty
\qquad(\abs{z}\to\infty),
$$
contradicting the displayed uniform bound. Hence $a_n=0$ for all
$n\ge N$, so the Taylor series is finite and $f$ is a polynomial.

:::

:::

::: {.pf-step #s1-5}

Conversely, the Taylor series of every polynomial converges
uniformly on all of $\CC$.


::: pf-proof

If $f$ is a polynomial of degree $d$, then $a_n=0$ for $n>d$.
Consequently every partial sum of order at least $d$ is exactly $f$.
Thus the partial sums converge uniformly, indeed eventually identically,
on all of $\CC$.

:::

:::

::: {.pf-step #s1-6}

Therefore the answer to part (c) is
$$
\boxed{\text{exactly the polynomials}}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} proves necessity, and step [](#s1-5){.pf-ref} proves sufficiency.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), step [](#s1-3){.pf-ref} proves part (b), and step [](#s1-6){.pf-ref}
answers part (c).

:::

:::

:::
