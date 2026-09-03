---
schema: qual/card@1
id: E-SS6.EX-8
kind: problem
title: "The Bessel functions arise in the study of spherical symmetries and the Fourier "
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
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
<1>1. Expand $e^{ixt} = \sum_{m=0}^{\infty} \frac{(ixt)^m}{m!}$.
::: {.proof}
power series of the exponential.
:::

<1>2. Then
$$\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \sum_{m=0}^{\infty} \frac{(ix)^m}{m!}\int_{-1}^{1} t^m (1 - t^2)^{\nu - 1/2}\,dt.$$
::: {.proof}
<1>1, integrating term by term.
:::

<1>3. For $m$ odd, $\int_{-1}^{1} t^m (1 - t^2)^{\nu - 1/2}\,dt = 0$ (the integrand is odd).
::: {.proof}
symmetry.
:::

<1>4. For $m = 2k$ even, $\int_{-1}^{1} t^{2k}(1 - t^2)^{\nu - 1/2}\,dt = \frac{\Gamma(k + 1/2)\Gamma(\nu + 1/2)}{\Gamma(\nu + k + 1)}$.
::: {.proof}
beta function (substituting $u = t^2$).
:::

<1>5. Hence
$$\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \sum_{k=0}^{\infty} \frac{(ix)^{2k}}{(2k)!} \cdot \frac{\Gamma(k + 1/2)\Gamma(\nu + 1/2)}{\Gamma(\nu + k + 1)}.$$
::: {.proof}
<1>2–<1>4.
:::

<1>6. Using $\Gamma(k + 1/2) = \frac{(2k)!}{4^k k!}\sqrt{\pi}$ and $(ix)^{2k} = (-1)^k x^{2k}$:
$$\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \Gamma(\nu + 1/2)\sqrt{\pi}\sum_{k=0}^{\infty} \frac{(-1)^k (x/2)^{2k}}{k!\,\Gamma(\nu + k + 1)}.$$
::: {.proof}
<1>5 and the identity for $\Gamma(k + 1/2)$.
:::

<1>7. Multiplying by $\frac{(x/2)^\nu}{\Gamma(\nu + 1/2)\sqrt{\pi}}$:
$$J_\nu(x) = \frac{(x/2)^\nu}{\Gamma(\nu + 1/2)\sqrt{\pi}}\int_{-1}^{1} e^{ixt}(1 - t^2)^{\nu - 1/2}\,dt = \left(\frac{x}{2}\right)^\nu \sum_{k=0}^{\infty} \frac{(-1)^k (x/2)^{2k}}{k!\,\Gamma(\nu + k + 1)}.$$
::: {.proof}
<1>6.
:::

<1>8. This is the standard power series for $J_\nu(x)$.
::: {.proof}
<1>7.
:::

<1>9. Q.E.D.
::: {.proof}
<1>8.
:::
:::
