---
schema: qual/card@1
id: D-SURFCH
kind: fact
title: Euler characteristics of the standard surfaces
classification:
  areas:
  - topology
  topics:
  - Surfaces
  - Euler Characteristic
relations: []
review: draft
---

::: {.fact}
For the standard closed surfaces,
$$
\chi(S^2)=2,\qquad \chi(T^2)=0,\qquad \chi(\Sigma_g)=2-2g,\qquad \chi(\RP^2)=1,\qquad \chi(\KK)=0,\qquad \chi(N_k)=2-k,
$$
where $\Sigma_g$ is the closed orientable surface of genus $g$ and $N_k$ is the connected sum of $k$ projective planes.
Each value is the alternating sum $\sum_n(-1)^n\operatorname{rank}H_n$ of the homology computed from the cell structure [@Hat02, Theorem 2.44].
By [[T-NBARV|the classification of compact surfaces]], whose closed members are the sphere $S^2$, the tori $T_g$ and the connected sums $N_k$ of projective planes [@Mun00, Theorem 77.5], the closed surfaces with a given Euler characteristic are:

| Orientable | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Yes | $\Sigma_3$ | none | $\Sigma_2$ | none | $T^2$ | none | $S^2$ |
| No | $N_6$ | $N_5$ | $N_4$ | $N_3$ | $\KK$ | $\RP^2$ | none |

With boundary, the formula of [[T-NBARV]] admits $\chi=0$ for the annulus $S^1\cross I$ and the Möbius band, and $\chi=1$ for the disc $D^2$.
:::
