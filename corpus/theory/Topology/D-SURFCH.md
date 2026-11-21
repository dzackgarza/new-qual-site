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
\chi(S^2)=2,\qquad \chi(\Sigma_g)=2-2g,\qquad \chi(\RP^2)=1,\qquad \chi(\KK)=0,\qquad \chi(N_k)=2-k,
$$
where $\Sigma_g$ is the closed orientable surface of genus $g$ and $N_k$ is the connected sum of $k$ copies of $\RP^2$, so that $\RP^2=N_1$ and $\KK=N_2$.
Each value is the alternating sum $\sum_n(-1)^n\operatorname{rank}H_n$ of the homology computed from the cell structure [@Hat02, Theorem 2.44; §2.2].
By [[T-NBARV|the classification of compact surfaces]], whose closed members are the surfaces $\Sigma_g$ for $g\geq 0$ and $N_k$ for $k\geq 1$ [@Mun00, Theorem 77.5 and Theorem 78.2], the closed surfaces with a given Euler characteristic are:

| Orientable | $-4$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Yes | $\Sigma_3$ | none | $\Sigma_2$ | none | $\Sigma_1$ | none | $\Sigma_0$ |
| No | $N_6$ | $N_5$ | $N_4$ | $N_3$ | $N_2$ | $N_1$ | none |

For compact surfaces with boundary the same computation gives $\chi(S^1\cross I)=\chi(\mobiusband)=0$ and $\chi(D^2)=1$, in agreement with $\chi=2-2g-b$ and $\chi=2-k-b$ for $b$ boundary components.
:::
