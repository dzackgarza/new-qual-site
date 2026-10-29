---
schema: qual/card@1
id: P-ZJXP5
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
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that
$$
\int_0^\infty \frac{x^{a-1}} {1+x^n} \dx=\frac{\pi}{n\sin \frac{a\pi}{n}}
$$
using complex analysis, $0< a < n$. Here $n$ is a positive integer.
:::

::: {.solution}
Let $I$ be the integral; it converges because the integrand is $O(x^{a-1})$ at $0$ and $O(x^{a-1-n})$ at $\infty$.
Let $f(z)=z^{a-1}/(1+z^n)$, where $z^{a-1}=\abs{z}^{a-1}e^{i(a-1)\arg z}$ with $\arg z$ taken continuously in $[0,2\pi/n]$ on the closed sector $S=\theset{0\le\arg z\le2\pi/n}$; for $n=1$ the ray $\arg z=2\pi$ is the lower side of the cut along $[0,\infty)$.
For $0<\varepsilon<1<R$, let $\Gamma$ be the positively oriented boundary of $S\cap\theset{\varepsilon\le\abs{z}\le R}$: the segment $[\varepsilon,R]$, the arc $\Gamma_R$ of $\abs{z}=R$, the ray segment from $Re^{2\pi i/n}$ to $\varepsilon e^{2\pi i/n}$, and the arc $\Gamma_\varepsilon$ of $\abs{z}=\varepsilon$ traversed clockwise.

::: pf

::: {.pf-step #residue}
$\displaystyle\int_\Gamma f(z)\,dz=-\frac{2\pi i}{n}e^{ia\pi/n}$.

::: pf-proof
The poles of $f$ are the roots of $z^n=-1$, with arguments $(2k+1)\pi/n$. Only $z_0=e^{i\pi/n}$ lies inside $\Gamma$, since the next root has argument $3\pi/n>2\pi/n$. It is simple, and
$$
\Res(f,z_0)=\frac{z_0^{a-1}}{nz_0^{n-1}}=\frac{z_0^a}{nz_0^n}=-\frac1ne^{ia\pi/n}.
$$
The residue theorem gives the claim.
:::

:::

::: {.pf-step #arcs}
$\int_{\Gamma_R}f\,dz\to0$ as $R\to\infty$ and $\int_{\Gamma_\varepsilon}f\,dz\to0$ as $\varepsilon\to0$.

::: pf-proof
On $\Gamma_R$, $\abs{1+z^n}\ge R^n-1$, so the integral is at most $\frac{2\pi R}{n}\cdot\frac{R^{a-1}}{R^n-1}\to0$ since $a<n$.
On $\Gamma_\varepsilon$, $\abs{1+z^n}\ge1-\varepsilon^n$, so the integral is at most $\frac{2\pi\varepsilon}{n}\cdot\frac{\varepsilon^{a-1}}{1-\varepsilon^n}\to0$ since $a>0$.
:::

:::

::: {.pf-step #rays}
The two straight pieces contribute $(1-e^{2\pi ia/n})\int_\varepsilon^R\frac{x^{a-1}}{1+x^n}\,dx$.

::: pf-proof
On $[\varepsilon,R]$, $f(x)=x^{a-1}/(1+x^n)$. On the ray $z=re^{2\pi i/n}$, $z^n=r^n$ and $z^{a-1}\,dz=r^{a-1}e^{2\pi i(a-1)/n}e^{2\pi i/n}\,dr=e^{2\pi ia/n}r^{a-1}\,dr$, and the ray is traversed inward.
:::

:::

::: pf-step
$I=\dfrac{\pi}{n\sin(a\pi/n)}$.

::: pf-proof
Letting $\varepsilon\to0$ and $R\to\infty$ in steps [](#residue){.pf-ref}, [](#arcs){.pf-ref} and [](#rays){.pf-ref} gives $(1-e^{2\pi ia/n})I=-\frac{2\pi i}{n}e^{ia\pi/n}$, so
$$
I=\frac{2\pi i}{n\qty(e^{ia\pi/n}-e^{-ia\pi/n})}=\frac{\pi}{n\sin(a\pi/n)}.
$$
:::

:::

:::

:::
