---
schema: qual/card@1
id: PR-TORSMAFF
kind: proposition
title: Smooth affine toric varieties and normality
slogan: 'Smooth cones give affine space times a torus, simplicial cones are finite diagonalizable quotients, and saturated semigroups make toric varieties normal.'
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
- What singularities can a toric variety with a simplicial fan have?
---

::: {.proposition title="Classification"}
If $\sigma$ is a smooth cone of dimension $k$ inside $N \cong \ZZ^n$, then
$$
U_\sigma \cong \AA^k \times \GG_m^{n-k} .
$$
Every smooth affine toric variety is of this form.
:::

::: {.proof}
Let $v_1,\ldots,v_k$ be the primitive ray generators of $\sigma$. Since $\sigma$ is smooth, they extend to a $\ZZ$-basis $v_1,\ldots,v_n$ of $N$.
For the dual basis $m_1,\ldots,m_n$ of $M$,
$$
S_\sigma=\sigma^\vee\cap M
=\NN m_1\oplus\cdots\oplus\NN m_k
\oplus\ZZ m_{k+1}\oplus\cdots\oplus\ZZ m_n.
$$
Hence
$$
k[S_\sigma]\cong k[x_1,\ldots,x_k,x_{k+1}^{\pm1},\ldots,x_n^{\pm1}].
$$
:::

::: {.proposition title="Simplicial cones"}
Let $\sigma$ be simplicial of dimension $k$ in a lattice $N\cong\ZZ^n$, with primitive ray generators $v_1,\ldots,v_k$. Choose $v_{k+1},\ldots,v_n\in N$ so that
$$
N'\coloneqq\ZZ v_1+\cdots+\ZZ v_n\subseteq N
$$
has finite index, and put $M'\coloneqq\Hom(N',\ZZ)$. The same cone in the lattice $N'$ is smooth, so its affine toric variety is $\AA^k\times\GG_m^{n-k}$. The finite diagonalizable group
$$
G\coloneqq\Hom(M'/M,\GG_m)
$$
acts on this smooth affine toric variety, and
$$
U_\sigma\cong(\AA^k\times\GG_m^{n-k})/G.
$$
Thus a toric variety with simplicial fan has finite diagonalizable quotient singularities.
[@Ful93]
:::

::: {.proposition title="Normality"}
$X_\Sigma$ is normal.
:::

::: {.remark}
For every cone $\sigma$, the semigroup $S_\sigma=\sigma^\vee\cap M$ is saturated: if $\ell m\in S_\sigma$ for an integer $\ell>0$, then $m\in S_\sigma$ because $\inner{\ell m}{u}\geq0$ implies $\inner{m}{u}\geq0$ for every $u\in\sigma$.
The semigroup algebra of a saturated affine semigroup is normal, so every affine chart $U_\sigma=\Spec k[S_\sigma]$ is normal and therefore $X_\Sigma$ is normal.

The nodal cubic has a dense $\GG_m$-orbit but is not normal, so it is not a toric variety under the normal definition used here.
:::
