---
schema: qual/card@1
id: E-SS6.EX-4
kind: problem
title: Taylor coefficients of $(1-z)^{-\alpha}$ via $\Gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Added the necessary exclusion of nonpositive integral alpha and handled that exceptional polynomial case separately.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there, with the two inputs
    that the prose named made precise: the Taylor coefficients of (1-z)^{-alpha} are
    computed from the n-th derivative at 0 rather than quoted from the binomial
    theorem, the identification of the Pochhammer symbol with the gamma ratio is
    derived by iterating Gamma(w+1) = w Gamma(w), and the gamma-ratio asymptotic is
    derived from Stirling's formula with the expansion written out to the order
    needed. The excluded alphas are handled as their own step, where the
    asymptotic relation has no meaning because a_n vanishes for large n. Not
    checked: the book's own text of the exercise and its form of Stirling's formula,
    since no copy of Stein and Shakarchi is retained in this checkout; the statement
    is as transcribed on the card. No retained solution set covers the exercise (the
    collection's provenance is a Google Books record), so the argument is the card's
    own. No statement repair.
---

::: {.exercise}
Prove that if we take
$$
f(z) = \frac{1}{(1 - z)^\alpha}, \quad \text{for } \abs{z} < 1
$$
(defined in terms of the principal branch of the logarithm), where $\alpha$ is a fixed complex number not in $\{0, -1, -2, \ldots\}$, then
$$
f(z) = \sum_{n=0}^{\infty} a_n(\alpha) z^n
$$
with
$$
a_n(\alpha) \sim \frac{1}{\Gamma(\alpha)} n^{\alpha - 1} \quad \text{as } n \to \infty.
$$
:::

::: {.remark}
The source allows every complex $\alpha$. For $\alpha \in \{0, -1, -2, \ldots\}$, $1/\Gamma(\alpha) = 0$ and $f$ is a polynomial, so $a_n(\alpha) = 0$ for large $n$ and the relation $\sim$ has no meaning; the statement excludes these $\alpha$.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Fix $\alpha\in\CC\setminus\{0,-1,-2,\dots\}$ and define $f(z)=(1-z)^{-\alpha}$ on the disc $\abs{z}<1$ by the principal branch of the logarithm, that is $f(z)=\exp\bigl(-\alpha\operatorname{Log}(1-z)\bigr)$ with $\operatorname{Log}$ the principal logarithm, whose argument lies in $(-\pi,\pi)$ because $\abs{z}<1$ keeps $1-z$ in the right half-plane. Write $(\alpha)_n=\alpha(\alpha+1)\cdots(\alpha+n-1)$ and $(\alpha)_0=1$.

::: pf

::: {.pf-step #coefficients}
$f$ is holomorphic on the disc and $f^{(n)}(0)=(\alpha)_n$; hence $f(z)=\sum_{n\ge0}a_n(\alpha)z^n$ with $a_n(\alpha)=\frac{(\alpha)_n}{n!}$ for $\abs{z}<1$.

::: pf-proof
$1-z$ stays in the right half-plane for $\abs{z}<1$, so $\operatorname{Log}(1-z)$ is holomorphic there and $f$ is holomorphic on the disc. Its derivatives are $f'(z)=\alpha(1-z)^{-\alpha-1}$ and, by induction, $f^{(n)}(z)=(\alpha)_n(1-z)^{-\alpha-n}$: the induction step uses $\frac{d}{dz}(1-z)^{-k}=k(1-z)^{-k-1}$ with $k=\alpha+n$, whose left side is $-k(1-z)^{-k-1}\cdot(-1)$ by the chain rule with inner derivative $-1$, and $(\alpha)_{n+1}=(\alpha)_n(\alpha+n)$. At $z=0$ this gives $f^{(n)}(0)=(\alpha)_n$. The Taylor series of a function holomorphic on the disc converges to it on the disc, and its coefficients are $f^{(n)}(0)/n!$, which is the display.
:::

:::

::: {.pf-step #gamma}
$(\alpha)_n=\Gamma(n+\alpha)/\Gamma(\alpha)$, so $a_n(\alpha)=\dfrac{\Gamma(n+\alpha)}{\Gamma(\alpha)\Gamma(n+1)}$.

::: pf-proof
Iterating $\Gamma(w+1)=w\Gamma(w)$, valid for $w\in\CC$ away from the non-positive integers, gives $\Gamma(n+\alpha)=\Gamma(\alpha)\prod_{j=0}^{n-1}(\alpha+j)=\Gamma(\alpha)(\alpha)_n$; the hypothesis $\alpha\notin\{0,-1,-2,\dots\}$ is what makes $\Gamma(\alpha)$ finite and nonzero, so the division is legitimate. Also $n!=n\Gamma(n)=\Gamma(n+1)$ for $n\ge1$, and $a_0=1=\Gamma(\alpha)/\Gamma(\alpha)\Gamma(1)$. Combining with step [](#coefficients){.pf-ref} gives the displayed coefficient.
:::

:::

::: {.pf-step #stirling}
$\dfrac{\Gamma(n+\alpha)}{\Gamma(n+1)}\sim n^{\alpha-1}$ as $n\to\infty$, for fixed $\alpha$.

::: pf-proof
Stirling's formula in the form $\log\Gamma(w)=\bigl(w-\tfrac12\bigr)\log w-w+\tfrac12\log2\pi+O(1/w)$, valid for $\abs{\arg w}<\pi$, applies to both $w=n+\alpha$ and $w=n+1$ once $n$ is large, since those points stay in a fixed half-plane. Subtracting,
$$
\log\frac{\Gamma(n+\alpha)}{\Gamma(n+1)}=\Bigl(n+\alpha-\tfrac12\Bigr)\log(n+\alpha)-\Bigl(n+\tfrac12\Bigr)\log(n+1)-\alpha+O\Bigl(\frac1n\Bigr).
$$
Now $\log(n+\alpha)=\log n+\frac{\alpha}{n}+O(n^{-2})$ and $\log(n+1)=\log n+\frac1n+O(n^{-2})$, so the logarithmic terms contribute $\bigl(\alpha-\tfrac12-\tfrac12\bigr)\log n+\alpha-\tfrac12+O(1/n)=(\alpha-1)\log n+\alpha-\tfrac12+O(1/n)$, and the linear terms contribute $1-\alpha+\tfrac12$. Adding, the sum is $(\alpha-1)\log n+O(1/n)$. Exponentiating, the ratio equals $n^{\alpha-1}e^{O(1/n)}$, and $e^{O(1/n)}\to1$, so the ratio is asymptotic to $n^{\alpha-1}$.
:::

:::

::: {.pf-step #conclusion}
$a_n(\alpha)\sim\dfrac{1}{\Gamma(\alpha)}n^{\alpha-1}$ as $n\to\infty$.

::: pf-proof
Divide the display of step [](#gamma){.pf-ref} by $n^{\alpha-1}$: $a_n(\alpha)/n^{\alpha-1}=\bigl(\Gamma(n+\alpha)/\Gamma(n+1)\bigr)/\Gamma(\alpha)\cdot$ the reciprocal factor, which is to say $a_n(\alpha)\sim n^{\alpha-1}/\Gamma(\alpha)$ by step [](#stirling){.pf-ref}. The constant $\Gamma(\alpha)$ is finite and nonzero by the hypothesis, so the relation is a genuine asymptotic equivalence with a nonzero limit of $a_n/n^{\alpha-1}$.
:::

:::

::: {.pf-step #excluded}
If $\alpha=-m$ with $m\in\ZZ_{\ge0}$ then $f$ is the polynomial $(1-z)^{m}$ of degree $m$, so $a_n(-m)=0$ for $n>m$ and no asymptotic relation of the displayed form can hold.

::: pf-proof
With $\alpha=-m$ the exponent $-\alpha=m$ is a non-negative integer, so $(1-z)^{-\alpha}=(1-z)^{m}$ is a polynomial of degree $m$: its Taylor series terminates. Then $a_n(-m)=0$ for all $n>m$, whereas $n^{\alpha-1}/\Gamma(\alpha)$ is not eventually zero, and in fact $1/\Gamma(-m)=0$ because $\Gamma$ has a pole at each non-positive integer. So for these $\alpha$ the coefficient formula still makes sense but the asymptotic statement has no meaning, which is why the exercise excludes them.
:::

:::

::: {.pf-step}
The statement of the exercise holds for every $\alpha\notin\{0,-1,-2,\dots\}$, and those are exactly the $\alpha$ for which it has content.

::: pf-proof
Steps [](#coefficients){.pf-ref}, [](#gamma){.pf-ref}, [](#stirling){.pf-ref} and [](#conclusion){.pf-ref} give the expansion and the asymptotic relation for every $\alpha$ that is not a non-positive integer, which is the assertion of the exercise. Step [](#excluded){.pf-ref} shows what fails without that hypothesis: the function becomes a polynomial, the coefficients vanish beyond its degree, and the relation cannot hold. The two together are the complete answer.
:::

:::


:::

:::
