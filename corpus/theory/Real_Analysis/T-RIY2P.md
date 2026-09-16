---
schema: qual/card@1
id: T-RIY2P
kind: theorem
title: Small tails of $L^1(\RR^d)$ functions
classification:
  areas:
  - real-analysis
  topics:
  - Small Tails
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $d\geq1$, let $m$ be Lebesgue measure on $\RR^d$, and let $f\colon\RR^d\to\CC$ be [[D-R5DL3|integrable]] with respect to $m$.
For $r>0$, let $B_r(0)\coloneqq\theset{x\in\RR^d\suchthat\abs{x}<r}$.
Then
$$
\lim_{r\to\infty}\int_{\RR^d\setminus B_r(0)}\abs{f}\,dm=0.
$$
Equivalently, for every $\varepsilon>0$ there exists $r>0$ such that
$$
\int_{\RR^d\setminus B_r(0)}\abs{f}\,dm<\varepsilon.
$$
:::
