---
schema: qual/card@1
id: T-CRVCLIFF
kind: theorem
title: Clifford's theorem
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
Let $D$ be an effective special divisor on a smooth projective curve $C$.
Then
\[
\ell(D) \leq \tfrac{1}{2}\deg D + 1 ,
\]
equivalently $\dim \abs{D} \leq \tfrac{1}{2}\deg D$.
Equality holds exactly when $D = 0$, or $D = K$, or $C$ is hyperelliptic and $D$ is a multiple of its unique $g^1_2$.
:::

::: {.remark}
Clifford is the tool for the range Riemann--Roch cannot reach.
For $\deg D > 2g-2$ the divisor is nonspecial and $\ell(D)$ is known exactly; for $0 \leq \deg D \leq 2g-2$ Riemann--Roch gives only a lower bound, and Clifford supplies the upper one.

The proof is the superadditivity $\ell(D) + \ell(E) \leq \ell(D+E)$ for effective $D, E$, applied to $D$ and $K - D$: it gives $\ell(D) + \ell(K-D) \leq \ell(K) = g$, and Riemann--Roch turns that into the stated bound.

The equality cases are the content.
They say that the only curves carrying unusually large special systems are the hyperelliptic ones, which is why Clifford is the standard first step in proving anything about non-hyperelliptic curves.
:::
