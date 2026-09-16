---
schema: qual/card@1
id: P-CASP13D
kind: problem
title: "Counting zeros of a degree-7 polynomial in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
How many zeroes (counted with multiplicity) does the polynomial $$f(z) = z^7 - 2z^5 + 6z^3 - z + 1$$ have in the unit disk $\mathbb{D}$?
:::

::: {.solution}
On $|z|=1$ write
\[
f(z)=6z^3+\bigl(z^7-2z^5-z+1\bigr).
\]
The remainder satisfies
\[
|z^7-2z^5-z+1|\le 1+2+1+1=5<6=|6z^3|.
\]
Thus Rouché's theorem shows that $f$ and $6z^3$ have the same number of
zeros in $\mathbb D$, counted with multiplicity. Therefore
\[
\boxed{f\text{ has exactly }3\text{ zeros in }\mathbb D.}
\]
:::
