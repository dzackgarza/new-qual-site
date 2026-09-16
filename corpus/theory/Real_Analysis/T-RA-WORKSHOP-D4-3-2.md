---
schema: qual/card@1
id: T-RA-WORKSHOP-D4-3-2
kind: theorem
title: Continuous images of compact sets and the extreme value theorem
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Compactness
relations: []
review: draft
---

::: {.theorem}
Let $K\subseteq\RR^n$ be [[D-EILKJ|compact]] and let $f\colon K\to\RR^m$ be continuous.
Then $f(K)$ is compact.
In particular, if $a<b$ and $f\colon[a,b]\to\RR$ is continuous, then there exist $p,q\in[a,b]$ such that
$$
f(p)=\sup_{x\in[a,b]}f(x)\qquad\text{and}\qquad f(q)=\inf_{x\in[a,b]}f(x).
$$
[@Rud76].
:::
