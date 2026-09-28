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
$D$ is \dfn{special} if this is positive, and \dfn{nonspecial} if it vanishes.
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
For every $D$, Riemann--Roch gives the inequality $\ell(D) \geq \deg D + 1 - g$.

The canonical divisor $K$ is special, since $\ell(K-K)=1$, and on a hyperelliptic curve of genus $g\ge2$ every divisor of the $g^1_2$ is special.
For a special effective divisor $D$, Clifford's theorem gives $\ell(D)-1\le\frac12\deg D$, with equality if and only if $D=0$, $D\sim K$, or $C$ is hyperelliptic and $D$ is a multiple of the $g^1_2$ [@Har10a, Theorem IV.5.4].
:::
