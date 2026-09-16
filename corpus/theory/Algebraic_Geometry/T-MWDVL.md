---
schema: qual/card@1
id: T-MWDVL
kind: theorem
title: Riemann--Roch and Serre duality on a curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Serre Duality
  - Curves
relations:
- kind: uses
  target: PR-Y5S7V
- kind: uses
  target: T-IJW1K
review: draft
prompts:
- State Riemann--Roch.
- State Serre duality for a curve.
- What is the dimension of the space of holomorphic differentials on a curve of genus $g$?
- Prove Riemann--Roch for curves by induction on the divisor.
---

::: {.theorem title="Riemann--Roch"}
For $D$ a divisor on a smooth projective curve $X$ of genus $g$ over $k = \bar{k}$,
\[
\ell(D) - \ell(K - D) = \deg D + 1 - g ,
\]
where $\ell(D) = h^0(X, \OO(D))$ and $K$ is a canonical divisor.
:::

::: {.theorem title="Serre duality"}
$H^1(X, \OO(D)) \cong H^0(X, \OO(K-D))\dual$, so $\ell(K-D) = h^1(D)$ and Riemann--Roch reads
\[
\chi(\OO(D)) = \deg D + 1 - g .
\]
:::

<1>1. For every divisor $D$ and closed point $P$, $\chi(\OO(D + P)) = \chi(\OO(D)) + 1$.

::: {.proof}
Tensor $0 \to \OO_X(-P) \to \OO_X \to \OO_P \to 0$ with the invertible sheaf $\OO_X(D+P)$: this gives $0 \to \OO_X(D) \to \OO_X(D+P) \to \OO_P \otimes \OO_X(D+P) \to 0$, and $\OO_P \otimes \OO_X(D+P) \cong \OO_P$ because $\OO_X(D+P)$ is locally free of rank one. Additivity of $\chi$ on short exact sequences and $h^0(\OO_P) = [\kappa(P) : k] = 1$, since $k$ is algebraically closed, give the claim.
:::

<1>2. $\chi(\OO(D)) = \deg D + 1 - g$ for every $D$.

::: {.proof}
For $D = 0$, $\chi(\OO_X) = h^0(\OO_X) - h^1(\OO_X) = 1 - g$, since $X$ is projective and connected and $g = h^1(\OO_X)$. Every divisor is obtained from $0$ by adding and subtracting points one at a time, and by step <1>1 both sides change by $\pm 1$ at each step, so the formula holds for $D + P$ exactly when it holds for $D$.
:::

<1>3. Q.E.D.

::: {.proof}
By Serre duality $h^1(\OO(D)) = \ell(K - D)$, so step <1>2 is the stated formula.
:::

::: {.remark}
Over a field $k$ that is not algebraically closed, step <1>1 adds $\deg P = [\kappa(P) : k]$ instead of $1$, and the formula reads $\chi(\OO(D)) = \deg D + \chi(\OO_X)$ with $\deg D = \sum n_P \deg P$ ([[D-CRVDEGREES]]).
:::

::: {.remark}
The second form is the one to state first when asked, because it says what the theorem is: the Euler characteristic is linear in the divisor, and the genus is the constant of integration.
Duality is what converts the unknown $h^1$ into a countable $h^0$.

Two immediate consequences, both asked:

- $D = 0$ gives $\ell(K) = g$: the space of global regular differentials on a curve of genus $g$ has dimension exactly $g$.
  This is the answer to the question about holomorphic differentials on a Riemann surface, and it is also how $g$ can be *defined* so that Riemann--Roch becomes a statement rather than a tautology.

- $D = K$ gives $\deg K = 2g-2$, which is the input to Riemann--Hurwitz and to every genus computation.

For $\deg D > 2g - 2$ the correction term vanishes and $\ell(D) = \deg D + 1 - g$ exactly; this is the range in which everything is computable and where "very ample" questions are settled.
:::
