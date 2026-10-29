---
schema: qual/card@1
id: P-WTIIM
kind: problem
title: Structure theorem for simple rings
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Rings
  - Structure Theorem
relations: []
review: draft
---

::: {.problem}
State the structure theorem for simple Artinian rings.
:::

::: {.solution}
The simple case of the Artin--Wedderburn theorem says:

> A ring $R$ is simple Artinian if and only if
> $$
> R\cong M_n(D)
> $$
> for some integer $n\ge1$ and some division ring $D$.

Here "simple" means that $R$ has no two-sided ideals other than $0$ and $R$, and "Artinian" means that descending chains of left ideals terminate.

The matrix ring $M_n(D)$ is simple Artinian. It is left and right Artinian because its left and right ideals are $D$-subspaces of the finite-dimensional $D$-vector space $M_n(D)$. A nonzero two-sided ideal contains a matrix $A$ with some entry $a_{kl}\ne0$, and then $E_{ij}=a_{kl}^{-1}E_{ik}AE_{lj}$ lies in the ideal for all $i,j$, so the ideal is all of $M_n(D)$.

For the forward direction, the Artinian hypothesis gives a minimal nonzero left ideal $L$. Schur's lemma implies that
$$
D=\Endo_R(L)^{\mathrm{op}}
$$
is a division ring. The sum $LR=\sum_{a\in R}La$ is a nonzero two-sided ideal, so $LR=R$ by simplicity. Each $La$ is the image of $L$ under $x\mapsto xa$, so it is $0$ or isomorphic to $L$. Hence the regular left module $R$ is a sum of simple submodules isomorphic to $L$, and therefore a direct sum of some of them; since $1$ lies in a finite subsum, finitely many suffice:
$$
{}_R R\cong L^{\oplus n}.
$$
Taking endomorphism rings gives
$$
R^{\mathrm{op}}\cong\Endo_R(R)
\cong M_n(\Endo_R(L)),
$$
and transposing gives
$$
R\cong M_n(D).
$$
:::
