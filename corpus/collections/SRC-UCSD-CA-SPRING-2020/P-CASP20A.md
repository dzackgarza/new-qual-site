---
schema: qual/card@1
id: P-CASP20A
kind: problem
title: 'Roots of $\pi^2z^5e^{-2z}-1$ in the unit disc'
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomial Roots
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
Let $f(z) = \pi^2 z^5 e^{-2z} - 1$.
How many roots does $f$ have in $\DD$?
How many simple roots does $f$ have in $\DD$?

Hint: $e < \pi$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own application of Rouché's theorem follows, with the estimate on the circle, the count, and the simplicity test as separate steps.

Let $f(z)=\pi^{2}z^{5}e^{-2z}-1$ and $g(z)=\pi^{2}z^{5}e^{-2z}$.

::: pf

::: {.pf-step #estimate}
On $\abs{z}=1$ one has $\abs{g(z)}>1=\abs{-1}$, hence $\abs{f-g}<\abs{g}$ there.

::: pf-proof
On $\abs{z}=1$, $\abs{g(z)}=\pi^{2}\abs{z}^{5}e^{-2\operatorname{Re}z}=\pi^{2}e^{-2\operatorname{Re}z}\ge\pi^{2}e^{-2}>1$, using $\operatorname{Re}z\le1$ and $\pi>e$, so that $\pi^{2}/e^{2}>1$. Since $f-g=-1$ has modulus $1$, the strict inequality holds.
:::

:::

::: {.pf-step #count}
$f$ has exactly $5$ zeros in $\DD$, counted with multiplicity.

::: pf-proof
$f$ and $g$ are entire and $\abs{f-g}<\abs{g}$ on the circle $\abs{z}=1$ by step [](#estimate){.pf-ref}, so Rouché's theorem gives that they have equally many zeros in $\DD$. Now $g(z)=\pi^{2}z^{5}e^{-2z}$ vanishes exactly at $z=0$, and $e^{-2z}$ never vanishes, so $z=0$ is a zero of order $5$.
:::

:::

::: {.pf-step #simple}
Every zero of $f$ in $\DD$ is simple.

::: pf-proof
$f'(z)=\pi^{2}\big(5z^{4}e^{-2z}-2z^{5}e^{-2z}\big)=\pi^{2}e^{-2z}z^{4}(5-2z)$. A multiple zero $z_{0}$ satisfies $f(z_{0})=f'(z_{0})=0$; from $f'$ either $z_{0}=0$ or $z_{0}=5/2$. But $f(0)=-1\ne0$, and $\abs{5/2}>1$ so $5/2\notin\DD$. Hence no zero in $\DD$ is multiple.
:::

:::

::: {.pf-qed}
$f$ has $5$ roots in $\DD$ by step [](#count){.pf-ref}, and all of them are simple by step [](#simple){.pf-ref}.
:::

:::

:::
