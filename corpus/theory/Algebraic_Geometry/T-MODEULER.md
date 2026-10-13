---
schema: qual/card@1
id: T-MODEULER
kind: theorem
title: The Euler sequence on projective space
slogan: 'The Euler sequence is the cotangent sequence of projective space; taking determinants gives $\omega_{\PP^n}\cong\OO(-n-1)$.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Differentials
  - Twisting Sheaves
  - Canonical Sheaf
relations:
- kind: uses
  target: D-4GCH6
- kind: uses
  target: D-CB9XS
review: draft
prompts:
- What is the Euler sequence?
- How do you compute $\omega_{\PP^n}$?
- Why is $\Omega_{\PP^n}$ not a sum of line bundles?
- On $\PP^1$, what is the cokernel of $\OO \to \OO(1)^{\oplus 2}$?
---

::: {.theorem title="Euler sequence"}
For $X = \PP^n_A$ there is a short exact sequence of $\OO_X$-modules
$$
0 \to \Omega_{X/A} \to \OO_X(-1)\sumpower{n+1} \to \OO_X \to 0 .
$$
:::

::: {.remark}
The sequence is the sheaf-level record of $\PP^n = (\AA^{n+1} \setminus 0)/\GG_m$: the middle term is the pullback of the cotangent bundle of the affine space, twisted, and the surjection onto $\OO_X$ is contraction with the Euler vector field, whose kernel is the forms that descend.
Dually, $0 \to \OO_X \to \OO_X(1)\sumpower{n+1} \to T_X \to 0$, and the $\OO_X$ is the Euler field itself.

Its determinant computes the canonical bundle.
Taking top exterior powers in a short exact sequence multiplies them, so
$$
\omega_{\PP^n_A/A}
=\Wedgepower^n\Omega_{\PP^n_A/A}
\cong\OO_{\PP^n_A}(-n-1).
$$

Over a field, $\Omega_{\PP^n}$ is not a direct sum of line bundles for $n\geq2$. If
$$
\Omega_{\PP^n}\cong\bigoplus_{i=1}^n\OO(a_i),
$$
then the Euler sequence gives
$$
c(\Omega_{\PP^n})=(1-H)^{n+1}.
$$
Comparing $c_1$ and $c_2$ yields
$$
\sum_i a_i=-(n+1),
\qquad
\sum_{i<j}a_ia_j=\binom{n+1}{2}.
$$
Hence $\sum_i a_i^2=n+1$. But Cauchy--Schwarz gives
$$
\sum_i a_i^2\geq\frac{(n+1)^2}{n}>n+1,
$$
a contradiction.
:::

::: {.example}
On $\PP^1$ with coordinates $x, y$, the dual Euler sequence is $0 \to \OO \xrightarrow{(x,\,y)} \OO(1)^{\oplus 2} \to T_{\PP^1} \to 0$.
So the cokernel of $(x, y) \colon \OO \to \OO(1)^{\oplus 2}$ is $T_{\PP^1} \cong \OO(2)$, the determinant of $\OO(1)^{\oplus 2}$; explicitly $(s, t) \mapsto y s - x t$ identifies it with $\OO(2)$.
:::
