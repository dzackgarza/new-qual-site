---
schema: qual/card@1
id: T-U5QSY
kind: definition
title: The Jacobian, Abel's theorem, and the Abel--Jacobi map
slogan: 'The Jacobian geometrizes degree-zero divisors: Abel kills exactly the principal ones, and Jacobi inversion reaches every divisor class.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Jacobians
  - Abel-Jacobi Map
  - Elliptic Curves
relations:
- kind: uses
  target: PR-Y5S7V
- kind: uses
  target: T-MWDVL
- kind: uses
  target: T-CRVJACFUN
review: draft
prompts:
- State Abel's theorem.
- What is the significance of the Jacobian?
- What kind of map is the Abel--Jacobi map, and what is it in genus $1$?
---

::: {.definition}
Let $X$ be a smooth projective connected curve over $\CC$. Under the analytic identification from [[T-CRVJACFUN]],
$$
\Jac(X)(\CC)
\cong
H^0(X,\Omega_X^1)^\vee/H_1(X,\ZZ),
$$
where a homology class acts on a holomorphic differential by integration.

The \dfn{Abel--Jacobi map} is the homomorphism
$$
\operatorname{AJ}\colon\Div^0(X)\longrightarrow\Jac(X)(\CC)
$$
defined by
$$
\operatorname{AJ}\!\left(\sum_i(p_i-q_i)\right)
=
\left[\omega\longmapsto\sum_i\int_{q_i}^{p_i}\omega\right],
$$
where changing the integration paths changes the functional by a period and hence does not change its class in the quotient.
:::

::: {.theorem title="Abel"}
A divisor of degree zero is principal exactly when its image under the Abel--Jacobi map is zero.
Hence
$$
\Pic^0(X)\xrightarrow{\sim}\Jac(X)(\CC).
$$
:::

::: {.theorem title="Jacobi inversion"}
The Abel--Jacobi map is surjective. Equivalently, every point of $\Jac(X)(\CC)$ is represented by a degree-zero divisor class on $X$.
:::

::: {.remark}
Abel's theorem identifies the kernel of the integration map with principal divisors, and Jacobi inversion identifies its image with the whole Jacobian. Thus the analytic quotient and the algebraic group of degree-zero line bundles agree.

Fixing a base point $p_0$ gives $X \to \Jac(X)$, $p \mapsto [p - p_0]$, which is an embedding for $g \geq 1$.
In genus $1$ it is an isomorphism: an elliptic curve is its own Jacobian, and the group law on $E$ is the statement that $[p]+[q]=[r]+[0]$ exactly when $p+q=r$.
:::
