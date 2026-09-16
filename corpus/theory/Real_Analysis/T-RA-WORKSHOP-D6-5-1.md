---
schema: qual/card@1
id: T-RA-WORKSHOP-D6-5-1
kind: theorem
title: Riemann's condition for Riemann--Stieltjes integrability
classification:
  areas:
  - real-analysis
  topics:
  - Riemann Integrability
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $a<b$, let $\alpha\colon[a,b]\to\RR$ be monotonically increasing, and let $f\colon[a,b]\to\RR$ be bounded.
For a partition $P=\theset{a=x_0<x_1<\cdots<x_k=b}$ of $[a,b]$, put $\Delta\alpha_i\coloneqq\alpha(x_i)-\alpha(x_{i-1})$ and
$$
U(P,f,\alpha)\coloneqq\sum_{i=1}^k\qty{\sup_{[x_{i-1},x_i]}f}\Delta\alpha_i,\qquad
L(P,f,\alpha)\coloneqq\sum_{i=1}^k\qty{\inf_{[x_{i-1},x_i]}f}\Delta\alpha_i .
$$
Then $f\in\mathcal R(\alpha)$, that is, $f$ is Riemann--Stieltjes integrable with respect to $\alpha$ on $[a,b]$, if and only if for every $\varepsilon>0$ there exists a partition $P$ of $[a,b]$ such that
$$
U(P,f,\alpha)-L(P,f,\alpha)<\varepsilon.
$$
[@Rud76].
:::
