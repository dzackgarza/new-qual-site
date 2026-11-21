---
schema: qual/card@1
id: E-SS6.EX-9
kind: problem
title: An integral representation of the hypergeometric series
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with six steps, each carrying a `pf-proof`; the statement, the identity and the continuation
    claim are unchanged. Cited by number only: the definition of the hypergeometric series in
    Exercise 16 of Chapter 1, the Weierstrass $M$-test, the beta-gamma identity
    $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$ and $\Gamma(x+1)=x\Gamma(x)$. Checked: that the ratio
    of consecutive coefficients tends to $1$, that the binomial series converges uniformly on
    $\abs z\le\rho<1$ times $[0,1]$, that the beta integral is the one produced by termwise
    integration, and that $1-zt$ avoids the nonpositive real axis exactly when
    $z\notin[1,\infty)$.
---

::: {.exercise}
The hypergeometric series $F(\alpha, \beta, \gamma; z)$ was defined in Exercise 16 of Chapter 1. Show that
$$
F(\alpha, \beta, \gamma; z) = \frac{\Gamma(\gamma)}{\Gamma(\beta)\Gamma(\gamma - \beta)} \int_0^1 t^{\beta - 1} (1 - t)^{\gamma - \beta - 1} (1 - zt)^{-\alpha}\, dt.
$$
Here $\alpha > 0$, $\beta > 0$, $\gamma > \beta$, and $\abs{z} < 1$.

Show as a result that the hypergeometric function, initially defined by a power series convergent in the unit disc, can be continued analytically to the complex plane slit along the half-line $[1, \infty)$.

Note that
$$
\log(1 - z) = -zF(1, 1, 2; z),
$$
$$
e^z = \lim_{\beta \to \infty} F(1, \beta, 1; z/\beta),
$$
$$
(1 - z)^{-\alpha} = F(\alpha, 1, 1; z).
$$
[Hint: To prove the integral identity, expand $(1 - zt)^{-\alpha}$ as a power series.]
:::

::: {.solution}

::: pf

::: pf-step

By definition
$$
F(\alpha,\beta,\gamma;z)=\sum_{n=0}^\infty\frac{(\alpha)_n(\beta)_n}{(\gamma)_n\,n!}z^n,
$$
a power series convergent on $\abs{z}<1$.

::: pf-proof

This is the definition given in Exercise 16 of Chapter 1, with $(a)_n=a(a+1)\cdots(a+n-1)$ the Pochhammer symbol. The ratio of consecutive coefficients is $\frac{(\alpha+n)(\beta+n)}{(\gamma+n)(n+1)}$, which tends to $1$, so the radius of convergence is $1$ by the ratio test; the series therefore converges normally on every disc $\abs z\le\rho<1$.

:::

:::

::: pf-step

For $\abs z\le\rho<1$ and $0\le t\le1$,
$$
(1-zt)^{-\alpha}=\sum_{n=0}^\infty\frac{(\alpha)_n}{n!}(zt)^n,
$$
the convergence being uniform in $(z,t)$.

::: pf-proof

The binomial series $(1-w)^{-\alpha}=\sum_n\frac{(\alpha)_n}{n!}w^n$ converges for $\abs w<1$. Here $w=zt$ with $\abs w\le\abs z\le\rho<1$, so the series converges; the $n$-th term is bounded by $\frac{\abs{(\alpha)_n}}{n!}\rho^n$, whose sum converges because $\rho<1$, so by the Weierstrass $M$-test the convergence is uniform on the whole set $\abs z\le\rho$, $0\le t\le1$.

:::

:::

::: pf-step

Hence termwise integration gives
$$
\int_0^1 t^{\beta-1}(1-t)^{\gamma-\beta-1}(1-zt)^{-\alpha}\,dt
=\sum_{n=0}^\infty\frac{(\alpha)_n z^n}{n!}B(\beta+n,\gamma-\beta).
$$

::: pf-proof

The factor $t^{\beta-1}(1-t)^{\gamma-\beta-1}$ is continuous on $(0,1)$ and integrable there when $\beta>0$ and $\gamma-\beta>0$, and it does not depend on $z$; multiplying by a uniformly convergent series of continuous functions and integrating term by term is legitimate (uniform convergence permits the interchange of sum and integral). The $n$-th integral is $\int_0^1t^{\beta+n-1}(1-t)^{\gamma-\beta-1}dt=B(\beta+n,\gamma-\beta)$ by the definition of the beta function as that integral for positive parameters.

:::

:::

::: pf-step

Using the beta-gamma identity,
$$
B(\beta+n,\gamma-\beta)=\frac{\Gamma(\beta+n)\Gamma(\gamma-\beta)}{\Gamma(\gamma+n)}
=\frac{\Gamma(\beta)\Gamma(\gamma-\beta)}{\Gamma(\gamma)}\cdot\frac{(\beta)_n}{(\gamma)_n}.
$$

::: pf-proof

$B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$ gives the first equality with $p=\beta+n$, $q=\gamma-\beta$, so $p+q=\gamma+n$. For the second, $\Gamma(\beta+n)=\Gamma(\beta)(\beta)_n$ and $\Gamma(\gamma+n)=\Gamma(\gamma)(\gamma)_n$ by iterating $\Gamma(x+1)=x\Gamma(x)$.

:::

:::

::: pf-step

Multiplying by the prefactor yields exactly the hypergeometric series, which is the integral formula of the exercise.

::: pf-proof

Substituting step 4 into step 3 gives $\frac{\Gamma(\beta)\Gamma(\gamma-\beta)}{\Gamma(\gamma)}\sum_n\frac{(\alpha)_n(\beta)_n}{(\gamma)_n n!}z^n$; multiplying by $\Gamma(\gamma)/(\Gamma(\beta)\Gamma(\gamma-\beta))$ gives $F(\alpha,\beta,\gamma;z)$ by step 1.

:::

:::

::: pf-step

Now let $\Omega=\CC\setminus[1,\infty)$. For $z\in\Omega$ and $0\le t\le1$ the number $1-zt$ never lies on the nonpositive real axis, and the integral defines a holomorphic function on $\Omega$, which agrees with the series on $\abs z<1$; it is therefore the analytic continuation of $F$ to $\Omega$.

::: pf-proof

If $1-zt$ were real and $\le0$ with $t\in(0,1]$, then $z=(1-s)/t\ge1$ for some $s\ge0$, so $z\in[1,\infty)$, excluded; and $t=0$ gives $1$. So the principal branch of the logarithm, hence $(1-zt)^{-\alpha}=e^{-\alpha\log(1-zt)}$, is defined and holomorphic in $z$ on a neighbourhood of each $z\in\Omega$, uniformly for $t\in[0,1]$. For a compact $K\subset\Omega$ the quantity $\abs{1-zt}$ is bounded below by a positive constant, so the integrand is bounded by a constant times $t^{\beta-1}(1-t)^{\gamma-\beta-1}$, which is integrable; the standard theorem on differentiation under the integral sign (a holomorphic integrand, locally uniformly dominated by an integrable function of $t$) then gives that the integral is holomorphic on $\Omega$ and may be differentiated under the sign. It agrees with the power series on the unit disc by step 5, and two holomorphic functions agreeing on a nonempty open set agree on the connected component containing it, so the integral is the analytic continuation of $F$ to $\Omega$.

:::

:::

:::
:::
