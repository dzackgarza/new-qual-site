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
> \[
> R\cong M_n(D)
> \]
> for some integer $n\ge1$ and some division ring $D$.

Here "simple" means that $R$ has no two-sided ideals other than $0$ and $R$, and "Artinian" means that descending chains of left ideals terminate.

The converse is direct. The matrix ring $M_n(D)$ is left and right Artinian because it is finite-dimensional over the division ring $D$, and every nonzero two-sided ideal contains a nonzero matrix. Multiplying by matrix units then produces every matrix unit, so the ideal is all of $M_n(D)$.

For the forward direction, the Artinian hypothesis gives a minimal nonzero left ideal $L$. Schur's lemma implies that
\[
D=\operatorname{End}_R(L)^{\mathrm{op}}
\]
is a division ring. The regular left module $R$ is a finite direct sum of minimal left ideals, and simplicity makes all of them isomorphic to $L$:
\[
{}_R R\cong L^{\oplus n}.
\]
Taking endomorphism rings gives
\[
R^{\mathrm{op}}\cong\operatorname{End}_R(R)
\cong M_n(\operatorname{End}_R(L)),
\]
and hence
\[
R\cong M_n(D).
\]
:::
