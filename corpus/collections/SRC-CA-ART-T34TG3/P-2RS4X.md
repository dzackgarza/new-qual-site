---
schema: qual/card@1
id: P-2RS4X
kind: problem
title: The integral of $1/(1+x^4)$ over $\RR$ and the poles of $1/(1+z^4)$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Poles
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Evaluate the integral
\[
\int_\RR {dx \over 1 + x^4}
.\]

What are the poles of ${1\over 1 + z^4}$ ?
:::

::: {.solution}
Let $f(z) = 1/(1 + z^4)$. For $R>1$, let $\Gamma_R$ be the closed contour consisting of the segment $[-R, R]$ and the arc $C_R$: $z = Re^{it}$, $t \in [0, \pi]$.

::: pf

::: {.pf-step #s1}

The poles of $f$ are the simple poles $z_k = e^{i\pi(1 + 2k)/4}$, $k = 0, 1, 2, 3$.

::: pf-proof

$1 + z^4 = 0$ if and only if $z^4 = -1 = e^{i\pi}$, so the zeros of $1+z^4$ are $z_0 = e^{i\pi/4}$, $z_1 = e^{3i\pi/4}$, $z_2 = e^{5i\pi/4}$, $z_3 = e^{7i\pi/4}$. Each is simple, since the derivative $4z^3$ does not vanish at any of them.

:::

:::

::: {.pf-step #s2}

The poles inside $\Gamma_R$ are $z_0 = e^{i\pi/4}$ and $z_1 = e^{3i\pi/4}$.

::: pf-proof

By step [](#s1){.pf-ref}, $z_0$ and $z_1$ have positive imaginary part and modulus $1<R$; $z_2$ and $z_3$ have negative imaginary part.

:::

:::

::: {.pf-step #s3}

$\Res_{z_0} f + \Res_{z_1} f = -\dfrac{i\sqrt2}{4}$.

::: pf-proof

At a simple zero $z_k$ of $1+z^4$, $\Res_{z_k} f = 1/(4 z_k^3)$. Since $z_0^3 = e^{3i\pi/4}$ and $z_1^3 = e^{9i\pi/4} = e^{i\pi/4}$,
$$\Res_{z_0} f + \Res_{z_1} f = \frac14\left(e^{-3i\pi/4} + e^{-i\pi/4}\right) = \frac14\left(-\frac{\sqrt2}{2} - i\frac{\sqrt2}{2} + \frac{\sqrt2}{2} - i\frac{\sqrt2}{2}\right) = -\frac{i\sqrt2}{4}.$$

:::

:::

::: {.pf-step #s4}

$\displaystyle\int_{C_R} f(z)\,dz \to 0$ as $R \to \infty$.

::: pf-proof

On $C_R$, $\abs{1 + z^4} \ge \abs{z}^4 - 1 = R^4 - 1$, so $\abs{f(z)} \le 1/(R^4 - 1)$. The arc has length $\pi R$, so the integral is bounded by $\pi R /(R^4 - 1) \to 0$.

:::

:::

::: {.pf-step #s5}

$\displaystyle\int_\RR \frac{dx}{1+x^4} = \boxed{\frac{\pi}{\sqrt2}}$.

::: pf-proof

By step [](#s2){.pf-ref} and the residue theorem, $\int_{\Gamma_R} f = 2\pi i \left(\Res_{z_0} f + \Res_{z_1} f\right)$ for $R>1$, which is $2\pi i\cdot(-i\sqrt2/4) = \pi\sqrt2/2$ by step [](#s3){.pf-ref}. Letting $R\to\infty$ and using step [](#s4){.pf-ref}, the integral over $[-R,R]$ converges to the same value.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} evaluates the integral, and step [](#s1){.pf-ref} lists the poles.

:::

:::

:::
