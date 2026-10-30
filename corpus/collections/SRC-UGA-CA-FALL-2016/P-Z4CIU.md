---
schema: qual/card@1
id: P-Z4CIU
kind: problem
title: All roots of $z^7-5z^3+12$ lie between $\abs{z}=1$ and $\abs{z}=2$
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

::: {.problem}
Prove that all the roots of the complex polynomial
$$f(z) = z^7 - 5 z^3 +12 =0$$ lie between the circles $\abs{z}=1$ and $\abs{z}=2$.
:::

::: {.solution}

::: pf

::: {.pf-step #inner}

$f$ has no zeros in $\abs{z}\le1$.

::: pf-proof

For $\abs{z}\le1$, $\abs{z^7-5z^3}\le1+5=6<12$, so $\abs{f(z)}\ge12-6>0$.

:::

:::

::: {.pf-step #outer}

$f$ has all seven of its zeros in $\abs{z}<2$.

::: pf-proof

On $\abs{z}=2$, $\abs{-5z^3+12}\le5\cdot8+12=52<128=\abs{z^7}$. By Rouché's theorem, $f=z^7+(-5z^3+12)$ and $z^7$ have the same number of zeros in $\abs{z}<2$, namely seven counted with multiplicity. Since $f$ has degree seven, these are all of its zeros.

:::

:::

::: pf-qed

By Steps [](#inner){.pf-ref} and [](#outer){.pf-ref}, every zero $z$ of $f$ satisfies $1<\abs{z}<2$.

:::

:::

:::
