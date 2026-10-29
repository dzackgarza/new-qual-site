---
schema: qual/card@1
id: P-YWMCT
kind: problem
title: $\int_0^\infty\frac{x^{-s}}{x+1}\,dx=\frac{\pi}{\sin(\pi s)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The card printed the integral without dx and without a range for s; the integral converges exactly for 0 < s < 1, so that hypothesis and dx were added.'
---

::: {.problem}
Show that for $0<s<1$,
$$
\int_{\RR_{\geq 0}}\frac{x^{-s}}{x+1}\,dx = \frac{\pi}{\sin(\pi s)}.
$$
:::

::: {.solution}
Let $I$ be the integral, which converges because the integrand is $O(x^{-s})$ near $0$ and $O(x^{-1-s})$ at $\infty$.
Let $z^{-s}=e^{-s\log z}$ with the branch of $\log$ on $\CC\setminus[0,\infty)$ for which $0<\arg z<2\pi$, and let $f(z)=z^{-s}/(z+1)$.
For $0<r<1<R$, let $\gamma_{r,R}$ be the keyhole contour: the segment $[r,R]$ on the upper side of the cut, the circle $\abs{z}=R$ counterclockwise, the segment from $R$ to $r$ on the lower side of the cut, and the circle $\abs{z}=r$ clockwise.

::: pf

::: {.pf-step #residue}
$\displaystyle\int_{\gamma_{r,R}}f(z)\,dz=2\pi i\,e^{-i\pi s}$.

::: pf-proof
The only pole of $f$ inside $\gamma_{r,R}$ is the simple pole at $-1=e^{i\pi}$, with residue $(e^{i\pi})^{-s}=e^{-i\pi s}$.
:::

:::

::: {.pf-step #circles}
The integrals over $\abs{z}=R$ and $\abs{z}=r$ tend to $0$ as $R\to\infty$ and $r\to0$.

::: pf-proof
On $\abs{z}=R$, $\abs{f}\le R^{-s}/(R-1)$, so the integral is at most $2\pi R^{1-s}/(R-1)\to0$ since $s>0$.
On $\abs{z}=r$, $\abs{f}\le r^{-s}/(1-r)$, so the integral is at most $2\pi r^{1-s}/(1-r)\to0$ since $s<1$.
:::

:::

::: {.pf-step #edges}
The two segments contribute $(1-e^{-2\pi is})\int_r^R\frac{x^{-s}}{x+1}\,dx$.

::: pf-proof
On the upper side $z^{-s}=x^{-s}$; on the lower side $\arg z=2\pi$, so $z^{-s}=x^{-s}e^{-2\pi is}$, and that segment is traversed from $R$ to $r$.
:::

:::

::: pf-step
$I=\dfrac{\pi}{\sin(\pi s)}$.

::: pf-proof
Letting $r\to0$ and $R\to\infty$ in steps [](#residue){.pf-ref}, [](#circles){.pf-ref} and [](#edges){.pf-ref} gives $(1-e^{-2\pi is})I=2\pi ie^{-i\pi s}$, so
$$
I=\frac{2\pi i}{e^{i\pi s}-e^{-i\pi s}}=\frac{2\pi i}{2i\sin(\pi s)}=\frac{\pi}{\sin(\pi s)}.
$$
:::

:::

:::

:::
