---
schema: qual/card@1
id: P-NBSTW
kind: problem
title: Power series of $\tan z$ via geometric-series inversion
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Trigonometry
  - Laurent Series
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source says "Laurent expand tan(z) at 0 using this method", referring to an earlier geometric-series inversion; the statement now names that method and the order z^5 the solution computes.'
---

::: {.exercise}
Expand $\tan z$ in a power series at $0$ through the term in $z^5$: compute $1/\cos z$ by writing $\cos z=1-u$ and expanding $\frac{1}{1-u}$ as a geometric series, then take the product $\sin z\cdot\frac{1}{\cos z}$.
:::

::: {.solution}
Write $\mathcal{O}(z^m)$ for a power series whose terms have degree at least $m$.

::: pf

::: {.pf-step #secant}
$\frac{1}{\cos z}=1+\frac{1}{2}z^2+\frac{5}{24}z^4+\mathcal{O}(z^6)$.

::: pf-proof
$\cos z=1-u$ with $u=\frac{z^2}{2}-\frac{z^4}{24}+\mathcal{O}(z^6)$, and $u=\mathcal{O}(z^2)$, so
$$
\frac{1}{\cos z}=1+u+u^2+\mathcal{O}(z^6)=1+\frac{z^2}{2}-\frac{z^4}{24}+\frac{z^4}{4}+\mathcal{O}(z^6).
$$
:::

:::

::: pf-step
$\tan z=\boxed{z+\frac{1}{3}z^3+\frac{2}{15}z^5+\mathcal{O}(z^7)}$.

::: pf-proof
By step [](#secant){.pf-ref},
$$
\tan z=\Bigl(z-\frac{z^3}{6}+\frac{z^5}{120}+\mathcal{O}(z^7)\Bigr)\Bigl(1+\frac{z^2}{2}+\frac{5z^4}{24}+\mathcal{O}(z^6)\Bigr).
$$
The coefficient of $z^3$ is $\frac12-\frac16=\frac13$ and that of $z^5$ is $\frac{5}{24}-\frac{1}{12}+\frac{1}{120}=\frac{2}{15}$. Since $\tan z$ is odd, no even powers occur, so the error term is $\mathcal{O}(z^7)$.
:::

:::

:::
:::
