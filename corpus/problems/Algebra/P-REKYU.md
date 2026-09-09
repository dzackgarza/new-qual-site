---
schema: qual/card@1
id: P-REKYU
kind: problem
title: Quotients of dihedral groups are cyclic or dihedral
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Groups
  - Classification
relations: []
review: draft
---

::: problem
Let $N\normal D_n$, where
\[
D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle.
\]
Show that $D_n/N$ is cyclic or dihedral.
:::

::: solution
Let $\bar r=rN$ and $\bar s=sN$. Since $r,s$ generate $D_n$, the elements $\bar r,\bar s$ generate $D_n/N$, and they satisfy
\[
\bar s^2=1,\qquad \bar s\bar r\bar s=\bar r^{-1}.
\]
Let $m=|\langle\bar r\rangle|$, so $m\mid n$.

If $\bar s\in\langle\bar r\rangle$, then $D_n/N=\langle\bar r\rangle$ is cyclic.

Otherwise $\langle\bar r\rangle$ has index $2$: every element of the quotient is of the form $\bar r^i$ or $\bar s\bar r^i$, and the two sets are disjoint. Hence
\[
D_n/N\cong D_m.
\]
Thus every quotient of a dihedral group is cyclic or dihedral. In particular, quotienting by the full rotation subgroup gives the cyclic quotient $C_2$.
:::
