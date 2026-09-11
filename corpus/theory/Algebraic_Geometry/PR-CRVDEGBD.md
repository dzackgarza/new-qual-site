---
schema: qual/card@1
id: PR-CRVDEGBD
kind: proposition
title: The degree thresholds $2g$ and $2g+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Very Ample Divisors
  - Ample Divisors
  - Linear Systems
relations:
- kind: uses
  target: T-MWDVL
- kind: uses
  target: D-CRVSPEC
review: draft
prompts:
- When is a divisor on a curve ample?
- When is a divisor on a curve base-point free?
- What degree guarantees a divisor on a curve is very ample?
---

::: {.proposition}
Let $D$ be a divisor on a smooth projective curve $C$ of genus $g$.

- $D$ is ample if and only if $\deg D > 0$.

- $\abs{D}$ is base-point free if $\deg D \geq 2g$.

- $D$ is very ample if $\deg D \geq 2g+1$.

The last two are sufficient, not necessary.
:::

::: {.remark}
All three come from running Riemann--Roch twice and watching the speciality term vanish.
For base-point freeness one needs $\ell(D-p) = \ell(D)-1$; with $\deg D \geq 2g$ both $D$ and $D-p$ have degree $> 2g-2$, both are nonspecial, and subtracting the two formulas gives the drop of exactly one.
For very ampleness one needs the drop by two at every pair, and $\deg D \geq 2g+1$ keeps $D-p-q$ nonspecial as well.
Ampleness follows because $\deg nD > 0$ eventually exceeds $2g+1$.

The thresholds are not sharp, and the standard counterexample is the canonical divisor on a smooth plane quartic: $g=3$, $\deg K = 4 < 2g+1 = 7$, and $K$ is very ample.
The specialisations worth having ready: on $\PP^1$ ample, very ample and $\deg \geq 1$ all coincide; on an elliptic curve $D$ is very ample exactly when $\deg D \geq 3$, which is the plane cubic model; on a genus-$2$ curve $\deg D = 5$ gives the quintic model in $\PP^3$.
If $D$ is very ample and $\varphi$ is the resulting embedding, then $\deg \varphi(C) = \deg D$.
:::
