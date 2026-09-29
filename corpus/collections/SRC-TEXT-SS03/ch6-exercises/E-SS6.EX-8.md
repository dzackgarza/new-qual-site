---
schema: qual/card@1
id: E-SS6.EX-8
kind: problem
title: The power series of the Bessel function $J_\nu$
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
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
8. The Bessel functions arise in the study of spherical symmetries and the Fourier transform.
   See Chapter 6 in Book I. Prove that the following power series identity holds for Bessel functions of real order $\nu > - 1 / 2$

$$
J _ {\nu} (x) = \frac {(x / 2) ^ {\nu}}{\Gamma (\nu + 1 / 2) \sqrt {\pi}} \int_ {- 1} ^ {1} e ^ {i x t} (1 - t ^ {2}) ^ {\nu - (1 / 2)} d t = \left(\frac {x}{2}\right) ^ {\nu} \sum_ {m = 0} ^ {\infty} \frac {(- 1) ^ {m} \left(\frac {x ^ {2}}{4}\right) ^ {m}}{m ! \Gamma (\nu + m + 1)}
$$

whenever $x > 0$ . In particular, the Bessel function $J _ { \nu }$ satisfies the ordinary diferential equation

$$
\frac {d ^ {2} J _ {\nu}}{d x ^ {2}} + \frac {1}{x} \frac {d J _ {\nu}}{d x} + \left(1 - \frac {\nu^ {2}}{x ^ {2}}\right) J _ {\nu} = 0.
$$

[Hint: Expand the exponential $e ^ { i x t }$ in a power series, and express the remaining integrals in terms of the gamma function, using Exercise 7.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Expand $e^{ixt} = \sum_{m=0}^{\infty} \frac{(ixt)^m}{m!}$.

::: pf-proof

power series of the exponential.

:::

:::

::: {.pf-step #s2}

Then
$$\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \sum_{m=0}^{\infty} \frac{(ix)^m}{m!}\int_{-1}^{1} t^m (1 - t^2)^{\nu - 1/2}\,dt.$$

::: pf-proof

Step [](#s1){.pf-ref}, integrating term by term.

:::

:::

::: {.pf-step #s3}

For $m$ odd, $\int_{-1}^{1} t^m (1 - t^2)^{\nu - 1/2}\,dt = 0$ (the integrand is odd).

::: pf-proof

symmetry.

:::

:::

::: {.pf-step #s4}

For $m = 2k$ even, $\int_{-1}^{1} t^{2k}(1 - t^2)^{\nu - 1/2}\,dt = \frac{\Gamma(k + 1/2)\Gamma(\nu + 1/2)}{\Gamma(\nu + k + 1)}$.

::: pf-proof

beta function (substituting $u = t^2$).

:::

:::

::: {.pf-step #s5}

Hence
$$\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \sum_{k=0}^{\infty} \frac{(ix)^{2k}}{(2k)!} \cdot \frac{\Gamma(k + 1/2)\Gamma(\nu + 1/2)}{\Gamma(\nu + k + 1)}.$$

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Using $\Gamma(k + 1/2) = \frac{(2k)!}{4^k k!}\sqrt{\pi}$ and $(ix)^{2k} = (-1)^k x^{2k}$:
$$\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \Gamma(\nu + 1/2)\sqrt{\pi}\sum_{k=0}^{\infty} \frac{(-1)^k (x/2)^{2k}}{k!\,\Gamma(\nu + k + 1)}.$$

::: pf-proof

Step [](#s5){.pf-ref} and the identity for $\Gamma(k + 1/2)$.

:::

:::

::: {.pf-step #s7}

Multiplying by $\frac{(x/2)^\nu}{\Gamma(\nu + 1/2)\sqrt{\pi}}$:
$$J_\nu(x) = \frac{(x/2)^\nu}{\Gamma(\nu + 1/2)\sqrt{\pi}}\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \left(\frac{x}{2}\right)^\nu \sum_{k=0}^{\infty} \frac{(-1)^k (x/2)^{2k}}{k!\,\Gamma(\nu + k + 1)}.$$

::: pf-proof

Step [](#s6){.pf-ref}.

:::

:::

::: {.pf-step #s8}

This is the standard power series for $J_\nu(x)$.

::: pf-proof

Step [](#s7){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s8){.pf-ref}.

:::

:::

:::
