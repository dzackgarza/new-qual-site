---
schema: qual/card@1
id: PR-LCV2V
kind: proposition
title: Pointwise limits do not preserve boundedness or sup norms
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Counterexamples
relations: []
review: draft
---

::: {.proposition}
(a) For $n\geq1$, the functions $f_n\colon(0,1)\to\RR$, $f_n(x)\coloneqq\min(n,1/x)$, are bounded and converge pointwise to the unbounded function $x\mapsto1/x$.

(b) For $n\geq1$, the functions $g_n\coloneqq\chi_{[n,n+1]}\colon\RR\to\RR$ converge pointwise to $0$, while
$$
\lim_{n\to\infty}\sup_{x\in\RR}\abs{g_n(x)}=1\neq0=\sup_{x\in\RR}\abs{\lim_{n\to\infty}g_n(x)} .
$$
:::
