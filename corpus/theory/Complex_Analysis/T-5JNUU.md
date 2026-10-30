---
schema: qual/card@1
id: T-5JNUU
kind: theorem
title: Rouché's theorem
slogan: 'If $\abs{g}<\abs{f}$ on $\gamma$, then $f\circ\gamma$ and $(f+g)\circ\gamma$ have the same winding number about $0$, so $f$ and $f+g$ have the same number of zeros minus poles inside $\gamma$.'
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
