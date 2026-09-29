---
schema: qual/card@1
id: P-C3XJT
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx=\frac{\pi}{n\sin(a\pi/n)}$ for $0<a\le
  n$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Show that
\[
\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n} \dx 
= \frac{\pi}{n\sin \frac{a\pi}{n}}
\]
using complex analysis, $0 < a \leq n$.
Here $n$ is a positive integer.
:::

::: {.solution}
**Goal.** Show $\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx = \frac{\pi}{n\sin(a\pi/n)}$ for $0 < a \le n$.

::: pf

::: pf-step
Use the keyhole contour (or a sector contour) around the branch cut of $z^{a-1}$.

::: pf-proof
the integrand $z^{a-1}/(1+z^n)$ has a branch point at $0$ and poles at the $n$-th roots of $-1$.
:::

:::

::: pf-step
The poles of $1/(1+z^n)$ are at $z = e^{i(2k+1)\pi/n}$, $k = 0, \dots, n-1$.

::: pf-proof
$z^n = -1$ at these points.
:::

:::

::: {.pf-step #residue-at-z0}
The residue at $z_0 = e^{i\pi/n}$ (the pole in the upper half-plane nearest the positive real axis) is $\frac{z_0^{a-1}}{n z_0^{n-1}} = \frac{z_0^a}{n z_0^n} = -\frac{z_0^a}{n}$.

::: pf-proof
$\operatorname{Res}(z^{a-1}/(1+z^n), z_0) = z_0^{a-1}/(n z_0^{n-1}) = z_0^a/(n z_0^n) = -z_0^a/n$ (since $z_0^n = -1$).
:::

:::

::: pf-step
Sum the residues over the poles in the upper half-plane and apply the residue theorem to the sector contour.

::: pf-proof

::: pf-step
The sector contour (angle $2\pi/n$) encloses exactly one pole, $z_0 = e^{i\pi/n}$.

::: pf-proof
the sector $0 \le \arg z \le 2\pi/n$ contains the single pole $e^{i\pi/n}$.
:::

:::

::: pf-step
The integral over the sector gives $(1 - e^{2\pi i a/n})\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx = 2\pi i \operatorname{Res}(f, z_0)$.

::: pf-proof
the two radial segments differ by the factor $e^{2\pi i a/n}$ (from the branch of $z^{a-1}$), and the arc contribution vanishes as the radius $\to \infty$.
:::

:::

::: pf-step
Hence $\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx = \frac{2\pi i \operatorname{Res}(f, z_0)}{1 - e^{2\pi i a/n}}$.

::: pf-proof
solve for the integral.
:::

:::

:::

:::

::: pf-step
Evaluate.

::: pf-proof

::: pf-step
$\operatorname{Res}(f, z_0) = -\frac{e^{i a\pi/n}}{n}$.

::: pf-proof
Step [](#residue-at-z0){.pf-ref} with $z_0 = e^{i\pi/n}$.
:::

:::

::: pf-step
$\frac{2\pi i \cdot (-e^{ia\pi/n}/n)}{1 - e^{2\pi i a/n}} = \frac{-2\pi i e^{ia\pi/n}}{n(1 - e^{2\pi i a/n})}$.

::: pf-proof
substitute.
:::

:::

::: {.pf-step #final-value}
$= \frac{\pi}{n \sin(a\pi/n)}$.

::: pf-proof
$\frac{-2\pi i e^{ia\pi/n}}{1 - e^{2\pi i a/n}} = \frac{-2\pi i}{e^{-ia\pi/n} - e^{ia\pi/n}} = \frac{-2\pi i}{-2i\sin(a\pi/n)} = \frac{\pi}{\sin(a\pi/n)}$.
:::

:::

:::

:::

::: pf-qed
Step [](#final-value){.pf-ref} gives the result.
:::

:::
