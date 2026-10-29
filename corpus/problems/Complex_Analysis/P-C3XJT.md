---
schema: qual/card@1
id: P-C3XJT
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx=\frac{\pi}{n\sin(a\pi/n)}$ for $0<a<n$
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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "$0 < a \leq n$". At a = n the integrand behaves like 1/x at infinity and the integral diverges; the statement now requires 0 < a < n.'
---

::: {.problem}
Show that
$$
\displaystyle \int_0^\infty \frac{x^{a-1}}{1+x^n} \dx
= \frac{\pi}{n\sin \frac{a\pi}{n}}
$$
using complex analysis, $0 < a < n$.
Here $n$ is a positive integer.
:::

::: {.solution}

Let $I$ denote the integral, which converges because $0<a<n$.
Let $z^{a-1}$ be the branch $\abs{z}^{a-1}e^{i(a-1)\arg z}$ with $0\le\arg z\le2\pi/n$, let $f(z)\coloneqq z^{a-1}/(1+z^n)$, and let $z_0\coloneqq e^{i\pi/n}$.
For $0<\varepsilon<1<R$ let $\Gamma$ be the boundary of the sector $\{\varepsilon<\abs{z}<R,\ 0<\arg z<2\pi/n\}$, oriented positively.

::: pf

::: {.pf-step #residue}
$z_0$ is the only pole of $f$ inside $\Gamma$, and $\Res_{z=z_0}f=-z_0^a/n=-e^{ia\pi/n}/n$.

::: pf-proof
The poles of $f$ are the roots $e^{i(2k+1)\pi/n}$ of $z^n=-1$, and only $k=0$ has argument in $(0,2\pi/n)$.
The pole is simple, and $\Res_{z=z_0}f=z_0^{a-1}/(nz_0^{n-1})=z_0^a/(nz_0^n)=-z_0^a/n$.
:::

:::

::: {.pf-step #contour}
$(1-e^{2\pi ia/n})\,I=2\pi i\Res_{z=z_0}f$.

::: pf-proof
On the ray $\arg z=2\pi/n$, $z=xe^{2\pi i/n}$ gives $z^{a-1}\,dz=e^{2\pi ia/n}x^{a-1}\,dx$ and $1+z^n=1+x^n$, so the two radial sides of $\Gamma$ contribute $(1-e^{2\pi ia/n})\int_\varepsilon^Rx^{a-1}/(1+x^n)\,dx$.
The outer arc contributes $O(R^{a}/R^n)\to0$ as $R\to\infty$ because $a<n$, and the inner arc contributes $O(\varepsilon^a)\to0$ as $\varepsilon\to0$ because $a>0$.
The residue theorem and step [](#residue){.pf-ref} give the claim in the limit.
:::

:::

::: pf-step
$I=\dfrac{\pi}{n\sin(a\pi/n)}$.

::: pf-proof
By steps [](#residue){.pf-ref} and [](#contour){.pf-ref},
$$
I=\frac{-2\pi ie^{ia\pi/n}}{n(1-e^{2\pi ia/n})}
=\frac{-2\pi i}{n(e^{-ia\pi/n}-e^{ia\pi/n})}
=\frac{-2\pi i}{-2in\sin(a\pi/n)}
=\frac{\pi}{n\sin(a\pi/n)}.
$$
:::

:::

:::

:::
