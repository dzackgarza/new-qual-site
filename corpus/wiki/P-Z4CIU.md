---
schema: qual/card@1
id: P-Z4CIU
kind: problem
title: "Prove that all the roots of the complex polynomial"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Prove that all the roots of the complex polynomial
$$f(z) = z^7 - 5 z^3 +12 =0$$ lie between the circles $|z|=1$ and $|z|=2$.
:::

:::{.solution}
On $\abs{z} \leq 1$:

- Big: $M(z) = 12$
- Small: $m(z) = z^6 - 5z^3$

For $\abs{z} = 1$,
\[
\abs{m(z)} \da \abs{z^7-5z^3}\leq \abs{z}^7 + 5\abs{z}^3 = 6 < 12 \da \abs{M(z)}
,\]
so $0 = Z_M = Z_{f}$.

On $\abs{z} \leq 2$,

- Big: $M(z) = z^7$
- Small: $m(z) = -5z^3 + 12$

On $\abs{z} = 2$,
\[
\abs{m(z)} \da \abs{-5z^3 + 12} \leq 5\abs{z}^2 + 12 = 32 < 128 = 2^7 \da \abs{M(z)}
,\]
so $7 = Z_M = Z_{f}$.

So $f$ has 7 zeros in $1 \leq \abs{z} \leq 2$.
:::

