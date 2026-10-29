---
schema: qual/card@1
id: E-FRWVZ
kind: problem
title: $\int_0^{\infty}\frac{\cos x}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{2b}$
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
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source states the identity with no request and no hypothesis on $b$; the identity fails for $b<0$ and is undefined for $b=0$. The statement now takes $b>0$ and asks to show the identity.'
---

::: {.exercise}
Let $b>0$. Show that
$$
\int_{0}^{\infty} \frac{\cos (x)}{x^{2}+b^{2}}\, dx=\frac{\pi e^{-b}}{2 b}.
$$
:::

::: {.solution}
Let $f(z)=\frac{e^{iz}}{z^2+b^2}$, and integrate over the boundary of the upper half-disk of radius $R>b$, oriented counterclockwise.

![](../../assets/figures/2021-07-29_18-42-38.png)

::: pf

::: {.pf-step #arc}
The arc contributes $0$ as $R\to\infty$.

::: pf-proof
On the arc $\abs{e^{iz}}=e^{-\Im z}\le1$ and $\abs{z^2+b^2}\ge R^2-b^2$, so the arc integral is at most $\pi R/(R^2-b^2)\to0$.
:::

:::

::: {.pf-step #residue}
$\int_\RR\frac{e^{ix}}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{b}$.

::: pf-proof
The only pole of $f$ in the upper half-plane is the simple pole $ib$, with $\Res_{z=ib}f=\frac{e^{-b}}{2ib}$. The residue theorem and step [](#arc){.pf-ref} give $2\pi i\cdot\frac{e^{-b}}{2ib}=\frac{\pi e^{-b}}{b}$.
:::

:::

::: pf-step
$\int_0^\infty\frac{\cos x}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{2b}$.

::: pf-proof
Taking real parts in step [](#residue){.pf-ref} gives $\int_\RR\frac{\cos x}{x^2+b^2}\,dx=\frac{\pi e^{-b}}{b}$. The integrand is even, so the integral over $[0,\infty)$ is half of this.
:::

:::

:::

:::
