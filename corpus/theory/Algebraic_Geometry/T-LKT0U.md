---
schema: qual/card@1
id: T-LKT0U
kind: theorem
title: Riemann--Hurwitz
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Differentials
  - Curves
relations:
- kind: uses
  target: D-4GCH6
- kind: uses
  target: T-MWDVL
review: draft
prompts:
- State Riemann--Hurwitz.
- Prove the weak form.
- How do you use it to compute a genus?
---

::: {.theorem}
Let $f : X \to Y$ be a finite separable morphism of smooth projective curves of degree $n$.
Then
\[
2g_X - 2 = n(2g_Y - 2) + \deg R ,
\]
where $R = \sum_{p} \operatorname{length}(\Omega_{X/Y})_p$ is the ramification divisor.
When every ramification is tame, $\deg R = \sum_p (e_p - 1)$.
:::

::: {.remark title="The proof, in the order it is asked"}
The relative cotangent sequence for $X \to Y \to \Spec k$ is
\[
f^* \Omega_{Y} \to \Omega_{X} \to \Omega_{X/Y} \to 0 .
\]
For a nonconstant separable map of smooth curves the left map is injective, so the sequence is short exact, and $\Omega_{X/Y}$ is a torsion sheaf supported at the ramification points.
Taking degrees gives $\deg \Omega_X = n \deg \Omega_Y + \deg R$, and $\deg \Omega_C = 2g_C - 2$ from Riemann--Roch.

That is the whole proof, and it explains why the examiner's first two questions are about the map on differentials and whether the sequence is short exact: those *are* the theorem.
Separability is what makes the left map injective, and in characteristic $p$ the Frobenius $\PP^1 \to \PP^1$ shows the statement fails without it — the map on differentials is zero.
:::

::: {.remark title="Using it"}
The formula is used in both directions.
Forward, with $Y = \PP^1$: a degree-$2$ cover of $\PP^1$ branched at $2g+2$ points has genus $g$, which is every hyperelliptic curve.
Backward: a curve admitting a map of known degree to a known curve has its genus pinned, and since $\deg R \geq 0$, a nonconstant map $X \to Y$ forces $g_X \geq g_Y$ — no curve maps onto one of larger genus.
:::
