---
schema: qual/card@1
id: P-WXP5K
kind: problem
title: Subgroups of finitely generated free abelian groups and of free groups
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Free Groups
  - Abelian Groups
relations: []
review: draft
---

::: problem
Describe subgroups of finitely generated free abelian groups and subgroups of finitely generated free groups. Prove the assertions.
:::

::: solution
For free abelian groups, let
\[
H\le \ZZ^n.
\]
Since $\ZZ$ is a PID, every submodule of a free $\ZZ$-module is free. Hence
\[
H\cong\ZZ^r
\]
for some $0\le r\le n$.

One can see this inductively without invoking the full structure theorem. Project $H$ to the first coordinate. Its image is $d\ZZ$ for some $d\ge0$. The kernel lies in $\ZZ^{n-1}$ and is free by induction. If $d>0$, choose $h\in H$ projecting to $d$; then
\[
H=\ker(\pi|_H)\oplus\ZZ h.
\]
Thus every subgroup of a finitely generated free abelian group is again finitely generated free abelian.

For free groups, the Nielsen--Schreier theorem says that every subgroup of a free group is free. A geometric proof realizes
\[
F_r=\pi_1\left(\bigvee_{i=1}^r S^1\right).
\]
A subgroup $H\le F_r$ corresponds to a connected covering graph $X_H$ of the bouquet. Since the fundamental group of every connected graph is free,
\[
H\cong\pi_1(X_H)
\]
is free.

Unlike the abelian case, $H$ need not be finitely generated even when $F_r$ is. For example,
\[
[F_2,F_2]\le F_2
\]
is free of countably infinite rank. If $H$ has finite index $d$ in $F_r$, then the Schreier formula gives
\[
\operatorname{rank}H=1+d(r-1),
\]
so finite-index subgroups are finitely generated.
:::
