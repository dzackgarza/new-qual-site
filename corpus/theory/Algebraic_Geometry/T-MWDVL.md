---
schema: qual/card@1
id: T-MWDVL
kind: theorem
title: Riemann--Roch and Serre duality on a curve
slogan: 'On a smooth projective curve, $\chi(\OO(D))=\deg D+1-g$, and Serre duality turns the correction term into sections of $K-D$.'
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
---

::: {.theorem title="Riemann--Roch"}
Let $X$ be a smooth projective geometrically connected curve of genus $g$ over a field $k$. For every divisor $D$ on $X$,
$$
\ell(D) - \ell(K - D) = \deg D + 1 - g ,
$$
where $\ell(D) \coloneqq \dim_k H^0(X, \OO_X(D))$ and $K$ is a canonical divisor [@Har77, Theorem IV.1.3].
:::

::: {.theorem title="Serre duality"}
$H^1(X, \OO_X(D)) \cong \dualof{H^0(X, \OO_X(K-D))}$, so $\ell(K-D) = h^1(X,\OO_X(D))$ and Riemann--Roch gives
$$
\chi(\OO_X(D)) = \deg D + 1 - g .
$$
:::

::: {.example title="Hyperplane sections"}
If $X \subseteq \PP^n_k$ is a smooth projective geometrically connected curve of degree $d$ and $D = X \cap H$ is a hyperplane section, then $\OO_X(D) \cong \OO_X(1)$, $\deg D = d$, and Riemann--Roch gives
$$
\chi(\OO_X(D)) = d + 1 - g .
$$
:::

::: {.remark}
For a closed point $P\in X$, adding $P$ to a divisor raises the degree and Euler characteristic by
$$
\deg P=[\kappa(P):k].
$$
Thus $\chi(\OO_X(D))=\deg D+\chi(\OO_X)$ with $\deg D=\sum_P n_P\deg P$ ([[D-CRVDEGREES]]).
:::

::: {.remark}
Taking $D=0$ gives $\ell(K)=g$, equivalently
$$
\dim_k H^0(X,\omega_X)=g.
$$
Taking $D=K$ gives $\deg K=2g-2$.

If $\deg D>2g-2$, then $\deg(K-D)<0$, hence $\ell(K-D)=0$ and
$$
\ell(D)=\deg D+1-g.
$$
:::
