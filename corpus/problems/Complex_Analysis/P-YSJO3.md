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
\[
h(z) \definedas z^5 + 3z + 1
.\]

:::

::: {.hint}
Compare $h$ with $z^5$ on $\abs{z} = 2$ and apply Rouché's theorem.
:::

::: {.solution}

- Big: $F(z) \definedas z^5$ so $\abs{F(z)} = 2^5 = 32$ on $\abs{z} = 2$
- Small: $g(z) \definedas p(z) - F(z) = 3z+1$, so $\abs{g(z)} \leq 3\abs{z}+ 1 = 7$ on $\abs{z} = 2$.

Then $\abs{g}\leq \abs{F}$ on $\abs{z} = 2$, $Z_{p} = Z_F = 5$.
:::
