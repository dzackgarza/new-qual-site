---
schema: qual/card@1
id: P-ER23C
kind: problem
title: $z^4+6z+3$ has three zeros in $1\le\abs{z}\le 2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Show that $P(z) \coloneqq z^4 + 6z + 3$ has 3 zeros in $\theset{1\leq \abs{z} \leq 2}$.
:::

::: {.solution}
Zeros are counted with multiplicity.

::: pf

::: {.pf-step #outer}
$P$ has no zeros on $\abs z = 2$ and exactly $4$ zeros in $\abs z<2$.

::: pf-proof
Put $f(z) = z^4$ and $g(z) = 6z+3$.
On $\abs z = 2$, $\abs{g(z)}\leq 6\abs z + 3 = 15 < 16 = \abs{f(z)}$.
Hence $\abs{P(z)}\geq \abs{f(z)} - \abs{g(z)} > 0$ there, and by Rouché's theorem $P = f+g$ has as many zeros in $\abs z<2$ as $f$, which is $4$.
:::

:::

::: {.pf-step #inner}
$P$ has no zeros on $\abs z = 1$ and exactly $1$ zero in $\abs z<1$.

::: pf-proof
Put $f(z) = 6z$ and $g(z) = z^4+3$.
On $\abs z = 1$, $\abs{g(z)}\leq \abs z^4 + 3 = 4 < 6 = \abs{f(z)}$.
Hence $P$ does not vanish there, and by Rouché's theorem $P$ has as many zeros in $\abs z<1$ as $6z$, which is $1$.
:::

:::

::: pf-step
$P$ has exactly $\boxed{3}$ zeros in $\theset{1\leq\abs z\leq 2}$.

::: pf-proof
By steps [](#outer){.pf-ref} and [](#inner){.pf-ref}, no zero lies on either boundary circle, so the zeros in the closed annulus are the zeros in $\abs z<2$ that are not in $\abs z<1$, and there are $4-1 = 3$ of them.
:::

:::

:::

:::
