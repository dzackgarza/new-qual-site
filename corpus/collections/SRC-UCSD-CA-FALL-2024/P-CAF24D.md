---
schema: qual/card@1
id: P-CAF24D
kind: problem
title: 'Entire function real on $\RR$ and imaginary on $\operatorname{Re}z=\operatorname{Im}z$ is real on $i\RR$'
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: reality on the
    real axis makes the Taylor coefficients at 0 real, the line Re z = Im z is the ray
    e^{i pi/4} t, the vanishing real part gives a_n cos(n pi/4) = 0, the cosine vanishes
    exactly at n = 2 mod 4, and i^n = -1 there, so f(it) is real. The dependence of the
    argument on the reality of the coefficients is now a step with its justification.
    The collection's provenance is the examination paper only, so no retained solution set
    covers the exercise and the argument is the card's own.
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire function.
Assume that

(i) $f$ takes real values on the real axis,

(ii) $f$ takes purely imaginary values on the line $\operatorname{Re} z = \operatorname{Im} z$.

Prove that $f$ takes real values on the imaginary axis.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #real-coefficients}
$f$ has a Taylor expansion $f(z)=\sum_{n\ge0}a_nz^n$ about $0$ that converges on all of $\CC$, with $a_n\in\RR$ for every $n$.

::: pf-proof
$f$ is entire, so its Taylor series about $0$ converges on all of $\CC$, with coefficients $a_n=\frac{f^{(n)}(0)}{n!}$. Hypothesis (i) says the function $t\mapsto f(t)$ of a real variable is real-valued; each derivative $f^{(n)}$ is again real-valued on $\RR$, because a derivative at a real point is the limit of the real difference quotients $\frac{f^{(n-1)}(t+h)-f^{(n-1)}(t)}{h}$ for real $h\ne0$. Hence every $f^{(n)}(0)$ is a real number, and so is $a_n$.
:::

:::

::: {.pf-step #line}
For every real $t$ the point $e^{i\pi/4}t$ lies on the line $\operatorname{Re}z=\operatorname{Im}z$.

::: pf-proof
$e^{i\pi/4}t=\frac{t}{\sqrt2}+i\frac{t}{\sqrt2}$, whose real and imaginary parts are equal.
:::

:::

::: {.pf-step #zero-real-parts}
For every real $t$,
$$
\sum_{n=0}^{\infty}a_n\cos\left(\frac{n\pi}{4}\right)t^n=0 .
$$

::: pf-proof
By step [](#line){.pf-ref} the hypothesis (ii) makes $f(e^{i\pi/4}t)$ purely imaginary, so its real part vanishes. Since
$$
f(e^{i\pi/4}t)=\sum_{n=0}^{\infty}a_n\left(e^{i\pi/4}\right)^nt^n
=\sum_{n=0}^{\infty}a_ne^{in\pi/4}t^n,
$$
and each $a_n$ is real by step [](#real-coefficients){.pf-ref}, the real part of that series is $\sum_na_n\cos\left(\frac{n\pi}{4}\right)t^n$, convergence being absolute for every $t$ because $f$ is entire.
:::

:::

::: {.pf-step #vanishing-coefficients}
$a_n\cos\left(\frac{n\pi}{4}\right)=0$ for every $n\ge0$.

::: pf-proof
The real coefficients of a power series in $t$ that converges to $0$ for every real $t$ all vanish: the $n$-th coefficient is $\frac1{n!}$ times the $n$-th derivative at $t=0$ of the sum, which is $0$.
:::

:::

::: {.pf-step #support}
$a_n=0$ whenever $n\not\equiv2\pmod4$.

::: pf-proof
$\cos\left(\frac{n\pi}{4}\right)=0$ exactly for the integers $n$ with $\frac{n\pi}{4}=\frac\pi2+k\pi$, that is $n=2+4k$; for those and only those $n$ the vanishing of step [](#vanishing-coefficients){.pf-ref} carries no information about $a_n$. Since all other $n$ give $\cos\left(\frac{n\pi}{4}\right)\ne0$, the corresponding $a_n$ vanish.
:::

:::

::: {.pf-step #power-of-i}
$i^n=-1$ for every $n\equiv2\pmod4$.

::: pf-proof
Write $n=2+4k$. Then $i^n=i^2\left(i^4\right)^k=(-1)\cdot1^k=-1$.
:::

:::

::: {.pf-step}
$f$ takes real values on the imaginary axis.

::: pf-proof
For real $t$, using the absolute convergence of the Taylor series and the vanishing of step [](#support){.pf-ref},
$$
f(it)=\sum_{n=0}^{\infty}a_n(it)^n=\sum_{n\equiv2\ (4)}a_ni^nt^n=-\sum_{n\equiv2\ (4)}a_nt^n,
$$
where the last equality is step [](#power-of-i){.pf-ref}. The coefficients $a_n$ are real by step [](#real-coefficients){.pf-ref} and $t$ is real, so this value is a real number.
:::

:::

:::
:::
