---
schema: qual/card@1
id: P-GWHUX
kind: problem
title: Elementary divisors and invariant factors of $\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9$;
  abelian groups of order $2700$
classification:
  areas:
  - prelim
  topics:
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
---

:::{.problem}
a. Determine the elementary divisors and invariant factors of the Abelian group $\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9$ of order 2700.
b. Determine the number of nonisomorphic Abelian groups of order 2700.
:::

::: {.solution}
**a.** $G=\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9$.
If $\gcd(a,b)=1$, then $\mathbf{Z}_a\times\mathbf{Z}_b\cong\mathbf{Z}_{ab}$, therefore we may conclude that $$\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9\cong\mathbf{Z}_{15}\times\mathbf{Z}_{180}$$ However, two groups are isomorphic just in case they have the same rank and list of invariant factors, so we may conclude that the invariant factors of $G$ are 15 and 180. In addition, we know $$\mathbf{Z}_{180}\cong\mathbf{Z}_{3^2}\times\mathbf{Z}_{2^2}\times\mathbf{Z}_5,\qquad \mathbf{Z}_{15}\cong\mathbf{Z}_3\times\mathbf{Z}_5$$ Therefore the elementary divisors of $G$ are $3,5,3^2,2^2,5$.

**b.** Too long to write out.
Just think about it.
:::
