---
schema: qual/card@1
id: T-WFXQP
kind: theorem
title: Residue at infinity
slogan: 'Residue at infinity is the ordinary residue after inversion, with the sign supplied by $dz=-w^{-2}dw$.'
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Singularities
relations: []
review: draft
---

::: {.theorem}
Let $R>0$ and let $f$ be [[D-E7A5W|holomorphic]] on $\{z : \abs{z}>R\}$, with [[D-Q8XRV|residue at infinity]] as defined there.
Then for every $\rho>R$, the circle $\abs{z}=\rho$ being oriented counterclockwise,
$$
\Res_{z=\infty}f=-\frac{1}{2\pi i}\int_{\abs{z}=\rho}f(z)\dz.
$$
Equivalently, if $f(z) = \sum_{k\in\ZZ}a_kz^k$ is the Laurent expansion on $\abs z>R$, then $\Res_{z=\infty}f = -a_{-1}$, the coefficient of $z^{-1}$ with the sign that the orientation of the circle gives.
:::

::: {.corollary}
Let $f$ be [[D-E7A5W|holomorphic]] on $\CC$ except for finitely many isolated singularities $z_1,\ldots,z_N$, and let $\Res_{z=\infty}f$ be its residue at infinity.
Then
$$
\sum_{j=1}^N \Res_{z=z_j} f + \Res_{z=\infty} f = 0.
$$
:::

::: {.remark}
This is the two displays above read at a circle $\abs z=\rho$ enclosing every $z_j$: the [[T-HRPNO|residue theorem]] gives $2\pi i\sum_j\Res_{z=z_j}f$ for the integral, and the residue at infinity gives $-2\pi i\Res_{z=\infty}f$ for the same integral.
:::

::: {.corollary}
Let $f$ be holomorphic on $\{z : \abs z>R\}$ and suppose $f(z)\to0$ as $\abs z\to\infty$.
Then $\lim_{\abs z\to\infty} zf(z)$ exists and
$$
\Res_{z=\infty}f = -\lim_{\abs z\to\infty} zf(z).
$$
:::

::: {.remark}
Vanishing at infinity removes the nonnegative powers from the Laurent expansion on $\abs z>R$, so $zf(z)=a_{-1}+O(1/z)$ there and the limit is $a_{-1}$; the sign is the one the theorem above gives.
:::
