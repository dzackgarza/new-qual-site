---
schema: qual/card@1
id: E-SS4.EX-6
kind: problem
title: $\frac1\pi\sum_n\frac{a}{a^2+n^2}=\coth\pi a$ by Poisson summation
classification:
  areas:
  - complex-analysis
  topics:
  - Poisson Summation
  - Series of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
Prove that

$$
\frac {1}{\pi} \sum_ {n = - \infty} ^ {\infty} \frac {a}{a ^ {2} + n ^ {2}} = \sum_ {n = - \infty} ^ {\infty} e ^ {- 2 \pi a \abs{ n }}
$$

whenever $a > 0$. Hence show that the sum equals $\coth \pi a$.
:::

::: {.solution}

The argument is the card's own: Poisson summation turns the sum of the Poisson kernel into the sum of its transform, and that sum is geometric.

::: pf

::: {.pf-step #transform}

For $f(x)=\frac1\pi\frac{a}{a^{2}+x^{2}}$ with $a>0$, $\widehat f(\xi)=e^{-2\pi a\abs{\xi}}$.

::: pf-proof

This is the computation of Exercise 3 of this section: the Fourier transform of the Poisson kernel $\frac{1}{\pi}\frac{a}{a^{2}+x^{2}}$ is $e^{-2\pi a\abs{\xi}}$ under the convention $\widehat f(\xi)=\int_{\RR}f(x)e^{-2\pi ix\xi}\,dx$.

:::

:::

::: {.pf-step #poisson}

$f$ and $\widehat f$ are of moderate decrease, so $\sum_{n\in\ZZ}f(n)=\sum_{n\in\ZZ}\widehat f(n)$.

::: pf-proof

$\abs{f(x)}=\frac{1}{\pi}\frac{a}{a^{2}+x^{2}}=O\bigl((1+x^{2})^{-1}\bigr)$ and $\abs{\widehat f(\xi)}=e^{-2\pi a\abs{\xi}}\le1$, so both are bounded by $C(1+x^{2})^{-1}$ and are therefore of moderate decrease; both series converge absolutely. The Poisson summation formula applies to a function and its transform when both are of moderate decrease and gives the displayed identity.

:::

:::

::: {.pf-step #main}

$\displaystyle\frac1\pi\sum_{n=-\infty}^{\infty}\frac{a}{a^{2}+n^{2}}=\sum_{n=-\infty}^{\infty}e^{-2\pi a\abs{n}}$.

::: pf-proof

Evaluating $f$ and $\widehat f$ at the integers in step [](#transform){.pf-ref} and applying step [](#poisson){.pf-ref} gives exactly this identity.

:::

:::

::: {.pf-step #geometric}

$\displaystyle\sum_{n=-\infty}^{\infty}e^{-2\pi a\abs{n}}=\coth(\pi a)$.

::: pf-proof

Pairing $n$ with $-n$ and using $\abs{-n}=\abs{n}$,
$$
\sum_{n\in\ZZ}e^{-2\pi a\abs{n}}=1+2\sum_{n=1}^{\infty}\bigl(e^{-2\pi a}\bigr)^{n}=1+\frac{2e^{-2\pi a}}{1-e^{-2\pi a}},
$$
the geometric series converging because $0<e^{-2\pi a}<1$ for $a>0$. Writing $q=e^{-2\pi a}$, the sum is $\frac{1-q+2q}{1-q}=\frac{1+q}{1-q}$; multiplying numerator and denominator by $e^{\pi a}$ gives $\frac{e^{\pi a}+e^{-\pi a}}{e^{\pi a}-e^{-\pi a}}=\coth(\pi a)$.

:::

:::

::: {.pf-step #conclusion}

Both displayed sums equal $\coth(\pi a)$.

::: pf-proof

Steps [](#main){.pf-ref} and [](#geometric){.pf-ref} give
$$
\boxed{\frac{1}{\pi}\sum_{n=-\infty}^{\infty}\frac{a}{a^{2}+n^{2}}=\sum_{n=-\infty}^{\infty}e^{-2\pi a\abs{n}}=\coth(\pi a),\qquad a>0.}
$$

:::

:::

:::

:::
