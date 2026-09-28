---
schema: qual/card@1
id: P-TOPS06B
kind: problem
title: "No finite covering from a higher-genus surface to a lower-genus surface for n > 2"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
---

::: {.problem}
Let $\Sigma_n$ denote the Riemann surface of genus $n$.
Use the Euler characteristic to show that there is no finite covering map from $\Sigma_{n+1}$ to $\Sigma_n$ for $n > 2$.
:::

::: {.solution}
<1>1. If a finite covering
$$
p:\Sigma_{n+1}\to\Sigma_n
$$
has degree $d$, then
$$
\chi(\Sigma_{n+1})=d\,\chi(\Sigma_n).
$$
::: {.proof}
Euler characteristic multiplies by the number of sheets of a finite covering.
:::

<1>2. Since $\chi(\Sigma_g)=2-2g$, the equation becomes
$$
-2n=d\bigl(-2(n-1)\bigr).
$$
::: {.proof}
Substitute $g=n+1$ and $g=n$ into the surface Euler-characteristic formula.
:::

<1>3. Thus
$$
d=\frac{n}{n-1}=1+\frac1{n-1}.
$$
::: {.proof}
Cancel the common factor $-2$ and solve for $d$.
:::

<1>4. If $n>2$, this is not an integer, so no such finite covering exists.
::: {.proof}
For $n>2$, $n-1>1$ and therefore $n-1$ does not divide $1$. A covering degree must be a positive integer.
:::
:::
