---
schema: qual/card@1
id: T-CRVCLIFF
kind: theorem
title: Clifford's theorem
slogan: 'Special divisors satisfy $\ell(D)\leq \deg D/2+1$; equality beyond $0$ and $K$ is the signature of a hyperelliptic $g^1_2$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Special Divisors
  - Linear Systems
  - Hyperelliptic Curves
relations:
- kind: uses
  target: D-CRVSPEC
- kind: uses
  target: D-CRVHYP
review: draft
prompts:
- State Clifford's theorem.
- When does equality hold in Clifford's theorem?
- How do you bound $\ell(D)$ for a special divisor?
---

::: {.theorem}
Let $C$ be a smooth projective curve of genus $g\geq2$ over an algebraically closed field, and let $D$ be an effective special divisor on $C$.
Then
$$
\ell(D) \leq \tfrac{1}{2}\deg D + 1 ,
$$
equivalently $\dim \abs{D} \leq \tfrac{1}{2}\deg D$.
Equality holds exactly when $D = 0$, or $D = K$, or $C$ is hyperelliptic and $D$ is a multiple of its unique $g^1_2$.
[@Har77, Theorem IV.5.4]
:::

::: {.remark}
If $\deg D>2g-2$, then $D$ is nonspecial and Riemann--Roch gives
$$
\ell(D)=\deg D+1-g.
$$
Clifford's theorem controls the complementary special range. For an effective special divisor with $0<\deg D<2g-2$, equality can occur only on a hyperelliptic curve, and then only for multiples of the hyperelliptic pencil.
:::
