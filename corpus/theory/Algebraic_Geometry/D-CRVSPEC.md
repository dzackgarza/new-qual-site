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
The **index of speciality** of $D$ is $\ell(K-D) = h^1(\OO_C(D))$.
$D$ is **special** if this is positive, and **nonspecial** if it vanishes.
:::

::: {.proposition}
If $\deg D > 2g-2$ then $D$ is nonspecial, and then Riemann--Roch reads
\[
\ell(D) = \deg D + 1 - g .
\]
:::

::: {.remark}
Riemann--Roch expresses $\ell(D)$ as $\deg D+1-g+\ell(K-D)$.
Once $\deg D$ exceeds $\deg K = 2g-2$, the divisor $K-D$ has negative degree, so $\ell(K-D)=0$.

Riemann--Roch gives $\ell(D) \geq \deg D + 1 - g$ for every divisor $D$. Examples of special divisors include $K$ itself and every divisor cut out by the $g^1_2$ on a hyperelliptic curve.
For a special divisor with $\ell(D)>0$, Clifford's theorem also gives $\ell(D)\leq \deg D/2+1$.
:::
