---
schema: qual/card@1
id: T-5JNUU
kind: theorem
title: Rouché's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Winding Number
relations: []
review: draft
---

::: {.theorem ref="Rouche"}
Let $\Omega\subseteq\CC$ be open, let $f,g$ be [[D-7DFVJ|meromorphic]] on $\Omega$, and let $\gamma$ be a positively oriented [[D-YKB3V|toy contour]] such that $\gamma$ and its interior lie in $\Omega$.
Suppose that $f$ and $f+g$ have no zeros or poles on $\gamma$, and that
$$
\abs{g(z)}<\abs{f(z)}\qquad\text{for all }z\in\gamma.
$$
Let $Z_h$ and $P_h$ be the numbers of zeros and poles of $h$ inside $\gamma$, counted with multiplicity.
Then $\Index_{w=0}(f\circ\gamma)=\Index_{w=0}\big((f+g)\circ\gamma\big)$, and hence
$$
Z_f-P_f=Z_{f+g}-P_{f+g}.
$$
In particular, if $f$ and $g$ are [[D-E7A5W|holomorphic]] on $\Omega$, then $f$ and $f+g$ have the same number of zeros inside $\gamma$.
:::

::: {.proof}
On $\gamma$, $\frac{f+g}{f}=1+\frac gf$ takes values in the disc $\ts{\abs{w-1}<1}$, which does not contain $0$, so the closed curve $\frac{f+g}{f}\circ\gamma$ has [[D-PJ7JM|winding number]] $0$ about $0$.
The logarithmic derivative of a product is the sum of the logarithmic derivatives, so by [[T-52HK6]]
$$
\Index_{w=0}\big((f+g)\circ\gamma\big)=\Index_{w=0}(f\circ\gamma)+\Index_{w=0}\Big(\frac{f+g}{f}\circ\gamma\Big)=\Index_{w=0}(f\circ\gamma).
$$
By the argument principle, $\Index_{w=0}(h\circ\gamma)=Z_h-P_h$ for $h=f$ and $h=f+g$.
:::
