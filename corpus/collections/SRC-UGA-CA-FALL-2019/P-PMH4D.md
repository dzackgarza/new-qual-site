---
schema: qual/card@1
id: P-PMH4D
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx=\frac{\pi}{n\sin\frac{a\pi}{n}}$ for
  $0<a<n$
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
  date: 2026-08-25
---

::: problem
Show that
\[
\int_{0}^{\infty} \frac{x^{a-1}}{1+x^{n}} d x=\frac{\pi}{n \sin \frac{a \pi}{n}}
\]
using complex analysis, $0<a<n$.
Here $n$ is a positive integer.
:::

::: {.solution}
**Goal:** Show $\int_0^\infty \frac{x^{a-1}}{1+x^n}\, dx = \frac{\pi}{n\sin \frac{a\pi}{n}}$ for $0 < a < n$ by complex analysis.

<1>1. Set up the integrand and the contour: $f(z) = \frac{z^{a-1}}{1 + z^n}$ with $z^{a-1}$ the branch $\abs{z}^{a-1} e^{i(a-1)\arg z}$, $0 \leq \arg z \leq \frac{2\pi}{n}$; integrate over the sector $\Gamma_R$: the segment $[0, R]$, the arc $\abs{z} = R$ with $0 \leq \arg z \leq \frac{2\pi}{n}$, and the ray $\arg z = \frac{2\pi}{n}$ back to $0$.
Proof: On the sector the branch of $z^{a-1}$ is single-valued and holomorphic, and the only pole of $f$ inside is at $z = e^{i\pi/n}$ (where $z^n = -1$), since $0 < \pi/n < 2\pi/n$.

<1>2. The integral along the ray $\arg z = \frac{2\pi}{n}$ equals $-e^{2\pi i a/n} \int_0^R \frac{x^{a-1}}{1 + x^n}\, dx$.
Proof: On that ray $z = re^{2\pi i/n}$, $dz = e^{2\pi i/n} dr$, $z^{a-1} = r^{a-1} e^{2\pi i (a-1)/n}$, and $z^n = r^n e^{2\pi i} = r^n$; traversed from $R$ down to $0$, the integral is $-\int_0^R \frac{r^{a-1} e^{2\pi i(a-1)/n}}{1 + r^n} e^{2\pi i/n}\, dr = -e^{2\pi i a/n} \int_0^R \frac{r^{a-1}}{1+r^n}\, dr$.

<1>3. The arc integral tends to $0$ as $R \to \infty$.
Proof: On the arc, $\abs{f(z)} \leq \frac{R^{a-1}}{R^n - 1}$ (since $\abs{1 + z^n} \geq \abs{z}^n - 1$), and the arc has length $\frac{2\pi R}{n}$; hence the arc integral is bounded by $\frac{2\pi}{n}\frac{R^a}{R^n - 1} \to 0$ as $R \to \infty$ because $a < n$.

<1>4. The residue of $f$ at $z = e^{i\pi/n}$ is $\frac{1}{n} e^{i(a-n)\pi/n}$.
Proof: At a simple pole, $\Res_{z = \zeta} \frac{z^{a-1}}{1+z^n} = \frac{\zeta^{a-1}}{n\zeta^{n-1}} = \frac{1}{n} \zeta^{a-n} = \frac{1}{n} e^{i(a-n)\pi/n}$, using $\zeta = e^{i\pi/n}$.

<1>5. The sector integral equals $2\pi i$ times the residue.
Proof: By the residue theorem applied on $\Gamma_R$ (with the arc contribution handled in <1>3), $\qty(1 - e^{2\pi i a/n}) \int_0^R \frac{x^{a-1}}{1+x^n}\, dx + o(1) = 2\pi i \cdot \frac{1}{n} e^{i(a-n)\pi/n}$; here <1>1, <1>2 and <1>3 give the left-hand side, and <1>4 the right-hand side.

<1>6. Solve for the integral.
Proof: From <1>5, $\int_0^\infty \frac{x^{a-1}}{1+x^n}\, dx = \frac{2\pi i}{n} \frac{e^{i(a-n)\pi/n}}{1 - e^{2\pi i a/n}}$.
Since $1 - e^{2\pi i a/n} = -2i e^{\pi i a/n} \sin\frac{a\pi}{n}$ and $e^{i(a-n)\pi/n} e^{-i a\pi/n} = e^{-i\pi} = -1$, this simplifies to $\frac{2\pi i}{n} \cdot \frac{-e^{i a\pi/n}}{-2i e^{i a\pi/n} \sin\frac{a\pi}{n}} = \frac{\pi}{n \sin\frac{a\pi}{n}}$.

<1>7. Q.E.D. Proof: <1>6 establishes the claimed formula for all $0 < a < n$.
:::
