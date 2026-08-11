---
schema: qual/card@1
id: P-MMAQ-QH4B3ZM42E
kind: problem
title: Let $E \subset \RR$ be measurable with $m(E) < \infty$.
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - measure-theory
  - l1
relations: []
review: draft
---

::: problem
Let $E \subset \RR$ be measurable with $m(E) < \infty$.
Define
$$
f(x)=m(E \cap(E+x)).
$$

Show that

1. $f\in L^1(\RR)$.

2. $f$ is uniformly continuous.

3. $\lim _{|x| \rightarrow \infty} f(x)=0$

> Hint:
> $$
> \chi_{E \cap(E+x)}(y)=\chi_{E}(y) \chi_{E}(y-x)
> $$
:::
