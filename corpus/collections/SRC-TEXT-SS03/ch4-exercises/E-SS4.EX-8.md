---
schema: qual/card@1
id: E-SS4.EX-8
kind: problem
title: Taylor coefficients of a function whose Fourier transform has compact support
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
    card's own and the card says so. Each step re-read: Fourier inversion plus analytic continuation
    gives the integral representation on the whole plane; differentiating n times under the
    integral gives the coefficient formula; the elementary bound by (2 pi M)^n times the L^1 norm
    of the transform gives the limsup statement after taking n-th roots; and the converse turns
    limsup < R into the coefficient bound a_n <= C R^n / n!, which sums to C e^{R|z|}. The two
    directions are kept in the order printed. Not claimed: the sharper Paley-Wiener statement, or
    any converse with the same constant when the limsup equals 2 pi M.
---

::: {.exercise}
Suppose $\hat{f}$ has compact support contained in $[-M, M]$ and let $f(z) = \sum_{n=0}^{\infty} a_n z^n$. Show that
$$
a_n = \frac{(2\pi i)^n}{n!} \int_{-M}^{M} \hat{f}(\xi)\, \xi^n\, d\xi,
$$
and as a result
$$
\limsup_{n \to \infty} (n!\abs{a_n})^{1/n} \leq 2\pi M.
$$
In the converse direction, let $f$ be any power series $f(z) = \sum_{n=0}^{\infty} a_n z^n$ with $\limsup_{n \to \infty} (n!\abs{a_n})^{1/n} \leq 2\pi M$. Then, $f$ is holomorphic in the complex plane, and for every $\epsilon > 0$ there exists $A_\epsilon > 0$ such that
$$
\abs{f(z)} \leq A_\epsilon e^{2\pi(M + \epsilon)\abs{z}}.
$$
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 4 Exercise 8.

::: pf

::: {.pf-step #inversion}
If $\operatorname{supp}\widehat f\subseteq[-M,M]$ then $f(z)=\int_{-M}^{M}\widehat f(\xi)e^{2\pi i\xi z}\,d\xi$ for every complex $z$.

::: pf-proof
Fourier inversion gives the identity for real $z$. The integral defines an entire function of $z$, since on the compact interval $\abs{\widehat f(\xi)e^{2\pi i\xi z}}\le\abs{\widehat f(\xi)}e^{2\pi M\abs{z}}$ with the right side integrable, so differentiation under the integral sign is justified to every order and the result is holomorphic. Two entire functions agreeing on $\RR$ agree everywhere, by the identity theorem.
:::

:::

::: {.pf-step #derivatives}
$f^{(n)}(0)=(2\pi i)^{n}\int_{-M}^{M}\widehat f(\xi)\xi^{n}\,d\xi$.

::: pf-proof
Differentiating the integral of step [](#inversion){.pf-ref} $n$ times under the integral sign brings down $(2\pi i\xi)^{n}$ at each step; the justification is the same uniform domination, with $\xi$ bounded by $M$ on the interval. Setting $z=0$ leaves $e^{0}=1$.
:::

:::

::: {.pf-step #coefficients}
$a_{n}=\dfrac{(2\pi i)^{n}}{n!}\displaystyle\int_{-M}^{M}\widehat f(\xi)\xi^{n}\,d\xi$.

::: pf-proof
$a_{n}=f^{(n)}(0)/n!$ for the Taylor expansion at $0$, and step [](#derivatives){.pf-ref} gives $f^{(n)}(0)$.
:::

:::

::: {.pf-step #growth}
$n!\abs{a_{n}}\le(2\pi M)^{n}\norm{\widehat f}_{L^{1}([-M,M])}$.

::: pf-proof
$\abs{n!a_{n}}=(2\pi)^{n}\abs{\int\widehat f\xi^{n}}\le(2\pi)^{n}\int\abs{\widehat f}\abs{\xi}^{n}d\xi\le(2\pi M)^{n}\int\abs{\widehat f}$, using $\abs{\xi}\le M$ on the interval of integration.
:::

:::

::: {.pf-step #limsup}
$\limsup_{n}(n!\abs{a_{n}})^{1/n}\le2\pi M$.

::: pf-proof
Taking $n$-th roots in step [](#growth){.pf-ref} gives $(n!\abs{a_{n}})^{1/n}\le2\pi M\norm{\widehat f}_{L^{1}}^{1/n}$, and $\norm{\widehat f}_{L^{1}}^{1/n}\to1$ for a positive constant, so the limsup is at most $2\pi M$.
:::

:::

::: {.pf-step #converse}
Conversely, if $\limsup_{n}(n!\abs{a_{n}})^{1/n}\le2\pi M$ then $f$ is entire and $\abs{f(z)}\le A_{\varepsilon}e^{2\pi(M+\varepsilon)\abs{z}}$ for every $\varepsilon>0$.

:::: pf-proof

::: {.pf-step #boundcoeffs}
For each $\varepsilon>0$ there is $C_{\varepsilon}$ with $\abs{a_{n}}\le C_{\varepsilon}R^{n}/n!$ for all $n\ge0$, where $R=2\pi(M+\varepsilon)$.

::: pf-proof
Let $L=\limsup_{n}(n!\abs{a_{n}})^{1/n}\le2\pi M<R$. By the definition of limsup there is $N$ with $(n!\abs{a_{n}})^{1/n}\le R$ for $n\ge N$, that is $n!\abs{a_{n}}\le R^{n}$, i.e. $\abs{a_{n}}\le R^{n}/n!$. The finitely many indices $n<N$ are absorbed by enlarging the constant: take $C_{\varepsilon}=\max\{1,\max_{n<N}n!\abs{a_{n}}/R^{n}\}$.
:::

:::

::: {.pf-step #entire}
The series converges absolutely for every $z$ and $\abs{f(z)}\le C_{\varepsilon}e^{R\abs{z}}$.

::: pf-proof
$\sum_{n}\abs{a_{n}}\abs{z}^{n}\le C_{\varepsilon}\sum_{n}(R\abs{z})^{n}/n!=C_{\varepsilon}e^{R\abs{z}}<\infty$ by step [](#boundcoeffs){.pf-ref}. Absolute convergence everywhere makes $f$ entire, and the displayed estimate gives the stated bound with $R=2\pi(M+\varepsilon)$.
:::

:::

:::

:::

::: {.pf-step}
The two directions of the exercise hold.

::: pf-proof
Steps [](#coefficients){.pf-ref}, [](#limsup){.pf-ref} and [](#converse){.pf-ref} give the formula for $a_{n}$, the limsup bound, and the converse:
$$
\boxed{a_{n}=\frac{(2\pi i)^{n}}{n!}\int_{-M}^{M}\widehat f(\xi)\xi^{n}d\xi;\quad \limsup_{n}(n!\abs{a_{n}})^{1/n}\le 2\pi M;\quad \text{and the converse with }A_{\varepsilon}=C_{\varepsilon}.}
$$
The number $2\pi M$ is the exponential type of $f$, and the exercise shows it is exactly the exponential type of the Fourier transform's support.
:::

:::

:::
:::
