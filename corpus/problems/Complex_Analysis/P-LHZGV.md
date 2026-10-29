---
schema: qual/card@1
id: P-LHZGV
kind: problem
title: Log properties can fail
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Counterexamples
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source prints log(zw) != log(z)log(w) with no branch named; the statement names the principal branch and the intended identity Log(zw) = Log z + Log w.'
---

::: {.exercise}
Let $\Log$ denote the principal branch of the logarithm on $\CC\setminus\theset{0}$, with $\Arg$ taking values in $(-\pi,\pi]$. Show that, in general,

- $\Log(zw)\neq \Log(z)+\Log(w)$, and
- $\Log(\exp(z))\neq z$.

:::

::: {.solution}
::: pf

::: pf-step
For $z=w=-1$, $\Log(zw)\neq\Log(z)+\Log(w)$.

::: pf-proof
Since $\Arg(-1)=\pi$, $\Log(-1)=i\pi$, so $\Log(z)+\Log(w)=2\pi i$. But $zw=1$ and $\Log(1)=0\neq 2\pi i$.
:::

:::

::: pf-step
For $z=2\pi i$, $\Log(\exp(z))\neq z$.

::: pf-proof
We have $\exp(2\pi i)=1$ and $\Log(1)=0\neq 2\pi i$. More generally, for $z=x+iy$ we have $\Log(\exp z)=x+i\theta$, where $\theta$ is the unique element of $(-\pi,\pi]$ with $\theta\equiv y \pmod{2\pi}$, so $\Log(\exp z)=z$ exactly when $-\pi<\Im z\leq\pi$.
:::

:::

:::
:::
