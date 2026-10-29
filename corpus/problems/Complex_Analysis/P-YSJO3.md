---
schema: qual/card@1
id: P-YSJO3
kind: problem
title: Zeros of $z^5+3z+1$ in $\abs{z}<2$ by Rouché's theorem
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
Find the number of zeros in $\abs{z} < 2$ of
$$
h(z) \coloneqq z^5 + 3z + 1.
$$

:::

::: {.hint}
Compare $h$ with $z^5$ on $\abs{z} = 2$ and apply Rouché's theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #compare}
$\abs{3z+1}<\abs{z^5}$ on $\abs{z}=2$.

::: pf-proof
On $\abs{z}=2$, $\abs{z^5}=32$ and $\abs{3z+1}\le3\abs{z}+1=7$.
:::

:::

::: pf-step
$h$ has $\boxed{5}$ zeros in $\abs{z}<2$, counted with multiplicity.

::: pf-proof
By step [](#compare){.pf-ref} and Rouché's theorem, $h=z^5+(3z+1)$ has as many zeros in $\abs{z}<2$ as $z^5$, which has a zero of order $5$ at $0$.
:::

:::

:::

:::
