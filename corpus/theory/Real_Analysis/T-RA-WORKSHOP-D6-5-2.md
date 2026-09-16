---
schema: qual/card@1
id: T-RA-WORKSHOP-D6-5-2
kind: theorem
title: Riemann--Stieltjes integration by parts
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $a<b$ and let $f,\alpha\colon[a,b]\to\RR$.
Write $f\in\mathcal R(\alpha)$ if there is $A\in\RR$ such that for every $\varepsilon>0$ there is a partition $P_\varepsilon$ of $[a,b]$ with
$$
\abs{\sum_{i=1}^k f(t_i)\qty{\alpha(x_i)-\alpha(x_{i-1})}-A}<\varepsilon
$$
for every partition $P=\theset{a=x_0<\cdots<x_k=b}$ refining $P_\varepsilon$ and every choice of $t_i\in[x_{i-1},x_i]$; then $\int_a^b f\,d\alpha\coloneqq A$.
If $f\in\mathcal R(\alpha)$ on $[a,b]$, then $\alpha\in\mathcal R(f)$ on $[a,b]$ and
$$
\int_a^b f\,d\alpha=f(b)\alpha(b)-f(a)\alpha(a)-\int_a^b\alpha\,df.
$$
:::
