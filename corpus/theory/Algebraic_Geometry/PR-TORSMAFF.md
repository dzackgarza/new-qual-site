---
schema: qual/card@1
id: PR-TORSMAFF
kind: proposition
title: Smooth affine toric varieties and why toric varieties are normal
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Normal Varieties
  - Smoothness
relations:
- kind: uses
  target: D-Q7Q2N
review: draft
prompts:
- Classify the smooth affine toric varieties.
- Why is every toric variety built from a fan normal?
---

::: {.proposition title="Classification"}
If $\sigma$ is a smooth cone of dimension $k$ inside $N \cong \ZZ^n$, then
\[
U_\sigma \cong \AA^k \times \GG_m^{n-k} .
\]
Every smooth affine toric variety is of this form.
:::

::: {.proof}
Extend the minimal generators of $\sigma$ to a $\ZZ$-basis of $N$, which is possible exactly because $\sigma$ is smooth.
In the dual basis $\sigma\dual$ is the cone spanned by $e_1, \ldots, e_k$ and $\pm e_{k+1}, \ldots, \pm e_n$, so
\[
S_\sigma = \NN^k \oplus \ZZ^{n-k}, \qquad k[S_\sigma] = k[x_1, \ldots, x_k, x_{k+1}^{\pm 1}, \ldots, x_n^{\pm 1}] .
\]
:::

::: {.proposition title="Normality"}
$X_\Sigma$ is normal.
:::

::: {.remark}
The reason is that $S_\sigma$ is a *saturated* semigroup: if $\ell m \in S_\sigma$ for some $\ell > 0$ then $m \in S_\sigma$, since the defining inequalities $\inp{m}{u} \geq 0$ are homogeneous.
Concretely, $k[S_\sigma]$ is the intersection of the rings $k[S_\tau]$ over the rays $\tau \leq \sigma$, each of which is a Laurent polynomial ring $k[x_1, x_2^{\pm 1}, \ldots, x_n^{\pm 1}]$ and so integrally closed, and an intersection of integrally closed domains with the same fraction field is integrally closed.

This is the standing caveat on the whole dictionary: fans produce *normal* toric varieties only.
The nodal cubic has a torus acting with a dense orbit and is not on the list.
:::
