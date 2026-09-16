---
schema: qual/card@1
id: P-Q5PQ6
kind: problem
title: Intermediate fields of $\QQ(2^{1/4},\zeta_8)$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Roots of Unity
relations: []
review: draft
---

::: {.problem}
Compute all intermediate fields of
\[
L=\QQ(2^{1/4},\zeta_8)/\QQ.
\]
:::

::: {.solution}
Let
\[
\alpha=2^{1/4}.
\]
Since $\alpha^2=\sqrt2$ and $\zeta_8=(1+i)/\sqrt2$, we have
\[
L=\QQ(\alpha,i),
\]
the splitting field of $x^4-2$. Hence
\[
[L:\QQ]=8
\]
and
\[
G=\operatorname{Gal}(L/\QQ)\cong D_4.
\]
Take generators
\[
r(\alpha)=i\alpha,\quad r(i)=i,
\qquad
s(\alpha)=\alpha,\quad s(i)=-i,
\]
so
\[
r^4=s^2=1,
\qquad
srs=r^{-1}.
\]

By Galois correspondence, the three subgroups of order $4$ give the three quadratic intermediate fields:
\[
\begin{array}{c|c}
\text{subgroup} & \text{fixed field}\\ \hline
\langle r\rangle & \QQ(i)\\
\langle r^2,s\rangle & \QQ(\sqrt2)\\
\langle r^2,rs\rangle & \QQ(\sqrt{-2}).
\end{array}
\]

The five subgroups of order $2$ give the five quartic intermediate fields:
\[
\begin{array}{c|c}
\text{subgroup} & \text{fixed field}\\ \hline
\langle r^2\rangle & \QQ(\sqrt2,i)=\QQ(\zeta_8)\\
\langle s\rangle & \QQ(\alpha)\\
\langle r^2s\rangle & \QQ(i\alpha)\\
\langle rs\rangle & \QQ((1+i)\alpha)\\
\langle r^3s\rangle & \QQ((1-i)\alpha).
\end{array}
\]

Together with the endpoints $\QQ$ and $L$, these are all intermediate fields, because the displayed subgroups exhaust the subgroup lattice of $D_4$.
:::
