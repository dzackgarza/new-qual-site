---
schema: qual/card@1
id: D-CRVSPEC
kind: definition
title: Special divisors and the index of speciality
classification:
  areas:
  - algebraic-geometry
  topics:
  - Special Divisors
  - Riemann-Roch
  - Curves
relations:
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- What is a special divisor?
- Give an example of a nonspecial divisor.
- When does Riemann--Roch compute $\ell(D)$ outright?
---

::: {.definition}
Let $D$ be a divisor on a smooth projective curve $C$ of genus $g$.
The \dfn{index of speciality} of $D$ is $\ell(K-D) = h^1(\OO_C(D))$.
$D$ is \dfn{special} if this number is positive and \dfn{nonspecial} if it is zero.
:::

::: {.proposition}
If $\deg D > 2g-2$ then $D$ is nonspecial, and then Riemann--Roch reads
$$
\ell(D) = \deg D + 1 - g .
$$
:::

::: {.remark}
Riemann--Roch expresses $\ell(D)$ as $\deg D+1-g+\ell(K-D)$.
Once $\deg D$ exceeds $\deg K = 2g-2$, the divisor $K-D$ has negative degree, so $\ell(K-D)=0$.

Thus when $\deg D>2g-2$, Riemann--Roch gives $\ell(D)=\deg D+1-g$.
For arbitrary $D$, Riemann--Roch gives
$$
\ell(D)=\deg D+1-g+\ell(K-D)\geq\deg D+1-g.
$$
The canonical divisor is special for $g\geq1$. On a hyperelliptic curve, a divisor in the $g^1_2$ is special for $g\geq2$. Clifford's theorem bounds $\ell(D)$ for effective special divisors.
:::
