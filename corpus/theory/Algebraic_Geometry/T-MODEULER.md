---
schema: qual/card@1
id: T-MODEULER
kind: theorem
title: The Euler sequence on projective space
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
\[
0 \to \Omega_{X/A} \to \OO_X(-1)\sumpower{n+1} \to \OO_X \to 0 .
\]
:::

::: {.remark}
The sequence is the sheaf-level record of $\PP^n = (\AA^{n+1} \setminus 0)/\GG_m$: the middle term is the pullback of the cotangent bundle of the affine space, twisted, and the surjection onto $\OO_X$ is contraction with the Euler vector field, whose kernel is the forms that descend.
Dually, $0 \to \OO_X \to \OO_X(1)\sumpower{n+1} \to T_X \to 0$, and the $\OO_X$ is the Euler field itself.

The reason to memorise it is the determinant.
Taking top exterior powers in a short exact sequence multiplies them, so
\[
\omega_{\PP^n} = \Extpower^n \Omega = \Extpower^{n+1}\qty{\OO(-1)\sumpower{n+1}} \tensor \OO\dual = \OO(-n-1) ,
\]
which is the one computation that the genus formulas, the Fano property of $\PP^n$, and every application of adjunction in projective space come out of.

The sequence does not split for $n \geq 1$, and for $n \geq 2$ the sheaf $\Omega_{\PP^n}$ is locally free but not a direct sum of line bundles: the Euler sequence is the standard witness that locally free does not mean split.
:::

::: {.example}
On $\PP^1$ with coordinates $x, y$, the dual Euler sequence is $0 \to \OO \xrightarrow{(x,\,y)} \OO(1)^{\oplus 2} \to T_{\PP^1} \to 0$.
So the cokernel of $(x, y) \colon \OO \to \OO(1)^{\oplus 2}$ is $T_{\PP^1} \cong \OO(2)$, the determinant of $\OO(1)^{\oplus 2}$; explicitly $(s, t) \mapsto y s - x t$ identifies it with $\OO(2)$.
:::

