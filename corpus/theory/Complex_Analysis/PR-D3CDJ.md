---
schema: qual/card@1
id: PR-D3CDJ
kind: proposition
title: Residue at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Singularities
relations: []
review: draft
---

::: {.proposition}
Let $R\ge0$, let $f$ be [[D-E7A5W|holomorphic]] on $\theset{z : \abs{z}>R}$ with Laurent expansion $f(z)=\sum_{k\in\ZZ}a_kz^k$ there, and let
$$
\Res_{z=\infty}f(z) \coloneqq -\frac{1}{2\pi i}\int_{\abs{z}=r}f(z)\dz = -a_{-1}
$$
for any $r>R$, with the circle oriented counterclockwise.
Then, with $g(z) \coloneqq -{1 \over z^2}f\qty{1\over z}$ for $0<\abs{z}<1/R$,
$$
\Res_{z=\infty}f(z) = \Res_{z=0} g(z).
$$
:::

::: {.proof}
For $0<\abs{w}<1/R$, $g(w)=-w^{-2}\sum_{k\in\ZZ}a_kw^{-k}=-\sum_{k\in\ZZ}a_kw^{-k-2}$.
The coefficient of $w^{-1}$ comes from $k=-1$ and equals $-a_{-1}$, so $\Res_{w=0}g(w)=-a_{-1}=\Res_{z=\infty}f(z)$.
:::
