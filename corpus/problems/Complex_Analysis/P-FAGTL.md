---
schema: qual/card@1
id: P-FAGTL
kind: problem
title: Zeros of $z^6+9z^4+z^3+2z+4$ in $\abs{z}<1$ by Rouché's theorem
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
Find the number of zeros in $\abs{z} < 1$ of
\[
p(z) \definedas z^6 + 9z^4 + z^3 + 2z + 4
.\]

:::

::: {.hint}
Compare $p$ with its dominant term $9z^4$ on $\abs{z}=1$ and apply Rouché's theorem.
:::

::: {.solution}
Find the big and small term:

- Big: $F(z) = 9z^4$, so $\abs{F(z)} = 9$ on the boundary
- Small: $g(z) = p(z) - F(z) = z^6 + z^3 + 2z + 4$, so $\abs{g(z)}\leq 1+1+2+4=8$ on the boundary.

So $\abs{p-F} \leq \abs{F}$ on $\abs{z} = 1$, meaning $Z_{p} = Z_F = 4$.

:::
