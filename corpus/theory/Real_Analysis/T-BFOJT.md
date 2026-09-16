---
schema: qual/card@1
id: T-BFOJT
kind: theorem
title: Continuity of translation in $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Equicontinuity
relations: []
review: draft
---

::: {.theorem}
For $h\in\RR^n$ and $f\in L^1(\RR^n)$ let $(\tau_hf)(x)\coloneqq f(x-h)$.
For every $f\in L^1(\RR^n)$,
$$
\lim_{h\to 0}\norm{\tau_h f - f}_1 = 0 .
$$
:::

::: {.remark}
Each $\tau_h$ is a linear isometry of $L^1(\RR^n)$, so the family $\theset{\tau_h\suchthat h\in\RR^n}$ is equicontinuous as a family of maps $L^1(\RR^n)\to L^1(\RR^n)$.
Together with the pointwise convergence $\tau_hf\to f$ of the theorem, this makes the convergence uniform on compact subsets $K\subseteq L^1(\RR^n)$:
$$
\lim_{h\to0}\sup_{f\in K}\norm{\tau_hf-f}_1=0 .
$$
:::
