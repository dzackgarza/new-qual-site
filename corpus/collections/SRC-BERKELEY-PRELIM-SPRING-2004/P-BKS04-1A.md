---
schema: qual/card@1
id: P-BKS04-1A
kind: problem
title: UC Berkeley Spring 2004 prelim 1A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Consider a sequence of functions $f_n\colon[a,b]\to\RR$ with the property that for each $x\in[a,b]$ there is an open interval $I_x$ containing $x$ such that $(f_n)_{n\geq1}$ converges uniformly in $I_x\cap[a,b]$. Show that $(f_n)_{n\geq1}$ converges uniformly in $[a,b]$.
:::

::: {.solution}
For each $x\in[a,b]$, the sequence $(f_n)$ converges uniformly on $I_x$, and in particular converges pointwise at $x$. Let $f\colon[a,b]\to\RR$ be the pointwise limit of $(f_n)$. The compact set $[a,b]$ is covered by the collection of open intervals $I_x$, so there is a finite subcovering, say $[a,b]\subset\bigcup_{k=1}^mI_{x_k}$. Given $\varepsilon>0$, there exists $N_k$ such that for $n\geq N_k$, the difference $\abs{f_n-f}$ is bounded by $\varepsilon$ on $I_{x_k}$. Let $N\coloneqq\max(N_1,\ldots,N_m)$. Then for $n\geq N$, the difference $\abs{f_n-f}$ is bounded by $\varepsilon$ on all of $[a,b]$. Hence by definition, $(f_n)$ converges to $f$ uniformly.
:::
