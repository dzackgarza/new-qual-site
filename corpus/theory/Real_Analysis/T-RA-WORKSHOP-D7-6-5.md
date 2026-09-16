---
schema: qual/card@1
id: T-RA-WORKSHOP-D7-6-5
kind: theorem
title: Arzelà--Ascoli theorem for $C(K,\RR^m)$
classification:
  areas:
  - real-analysis
  topics:
  - Arzelà-Ascoli
  - Compactness
  - Function Spaces
  - Equicontinuity
relations: []
review: draft
---

::: {.theorem}
Let $n,m\geq1$, let $K\subseteq\RR^n$ be [[D-EILKJ|compact]], and equip $C(K,\RR^m)$ with the metric $d(f,g)\coloneqq\sup_{x\in K}\norm{f(x)-g(x)}$.
A subset $\mathcal F\subseteq C(K,\RR^m)$ is [[D-EILKJ|compact]] if and only if $\mathcal F$ is closed, [[D-2GCTV|bounded]], and equicontinuous at every point of $K$, that is,
$$
\forall x\in K\quad\forall\varepsilon>0\quad\exists\delta>0\quad\forall y\in K\quad\forall f\in\mathcal F:\quad\norm{x-y}<\delta\implies\norm{f(x)-f(y)}<\varepsilon.
$$
:::
