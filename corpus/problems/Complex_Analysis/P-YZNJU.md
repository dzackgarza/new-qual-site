---
schema: qual/card@1
id: P-YZNJU
kind: problem
title: The sum $\sum_{k=1}^n\sin kx$ via de Moivre's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Series of Numbers
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The card printed "(e^{i theta})^n == cos n theta + i sin n theta" with a doubled equals sign and a misplaced \left. delimiter; corrected to a single equals sign and balanced parentheses.'
---

::: {.problem}
Use de Moivre's theorem (i.e. $\qty(e^{i \theta})^{n}=\cos n \theta+i \sin n \theta$, or $(\cos \theta+i \sin \theta)^{n}=\cos n \theta+i \sin n \theta$) to find the sum

$$
\sin x+\sin 2 x+\cdots+\sin n x
$$
:::

::: {.solution}

::: pf

::: {.pf-step #geom}
For $x\notin2\pi\ZZ$, $\displaystyle\sum_{k=1}^n e^{ikx}=e^{i(n+1)x/2}\frac{\sin(nx/2)}{\sin(x/2)}$.

::: pf-proof
By de Moivre's theorem $e^{ikx}=(e^{ix})^k$, and since $e^{ix}\ne1$ the geometric-series identity gives
$$
\sum_{k=1}^n e^{ikx}=e^{ix}\frac{1-e^{inx}}{1-e^{ix}}.
$$
Substituting $1-e^{it}=-2ie^{it/2}\sin(t/2)$ with $t=nx$ and $t=x$ gives the claim.
:::

:::

::: pf-step
$$
\sin x+\cdots+\sin nx=
\boxed{\begin{cases}
\dfrac{\sin(nx/2)\sin((n+1)x/2)}{\sin(x/2)}, & x\notin2\pi\ZZ,\\[1ex]
0, & x\in2\pi\ZZ.
\end{cases}}
$$

::: pf-proof
For $x\notin2\pi\ZZ$, take imaginary parts in step [](#geom){.pf-ref}, using $\Im e^{ikx}=\sin kx$. For $x\in2\pi\ZZ$ every summand is $0$.
:::

:::

:::

:::
