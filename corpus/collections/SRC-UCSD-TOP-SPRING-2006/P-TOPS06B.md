---
schema: qual/card@1
id: P-TOPS06B
kind: problem
title: No finite covering $\Sigma_{n+1} \to \Sigma_n$ for $n > 2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. A degree-d covering has chi(total) = d chi(base), so
    2 - 2(n+1) = d(2 - 2n), giving d = n/(n-1); for n > 2 this lies strictly between 1 and 3/2 and so
    is not an integer, and no finite covering exists. Checked the Euler characteristic of a genus-g
    surface is 2 - 2g and that multiplicativity under finite coverings is the one input, and that
    n = 2 is genuinely excluded (d = 2 there, and a double cover does exist).
---

::: {.problem}
Let $\Sigma_n$ denote the Riemann surface of genus $n$.
Use the Euler characteristic to show that there is no finite covering map from $\Sigma_{n+1}$ to $\Sigma_n$ for $n > 2$.
:::

::: {.solution}

::: pf

::: pf-step

If a finite covering
$$
p:\Sigma_{n+1}\to\Sigma_n
$$
has degree $d$, then
$$
\chi(\Sigma_{n+1})=d\,\chi(\Sigma_n).
$$

::: pf-proof

Euler characteristic multiplies by the number of sheets of a finite covering.

:::

:::

::: pf-step

Since $\chi(\Sigma_g)=2-2g$, the equation becomes
$$
-2n=d\bigl(-2(n-1)\bigr).
$$

::: pf-proof

Substitute $g=n+1$ and $g=n$ into the surface Euler-characteristic formula.

:::

:::

::: pf-step

Thus
$$
d=\frac{n}{n-1}=1+\frac1{n-1}.
$$

::: pf-proof

Cancel the common factor $-2$ and solve for $d$.

:::

:::

::: pf-step

If $n>2$, this is not an integer, so no such finite covering exists.

::: pf-proof

For $n>2$, $n-1>1$ and therefore $n-1$ does not divide $1$. A covering degree must be a positive integer.

:::

:::

:::

:::
